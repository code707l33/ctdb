from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from core.decorators import permission_required

from .forms import PilotadminModelForm
from .models import Pilotadmin

from log.models import Log


def get_all_pilotadmin_queryset(request):
    """
    The queryset of model `Archive` with filter depending on user's role/identity/group.
    The views below will use this as a basic queryset. This ensures that users won't
    accidentally see or touch those they shouldn't.
    """
    model = Pilotadmin
    queryset = model.objects.all()
    return queryset

def pilot_log_record(action, data):
    processmodel = Pilotadmin
    model = Log
    instance = model()
    instance.action = action
    instance.app_label = processmodel._meta.app_label
    instance.model_name = processmodel._meta.model_name
    instance.data = data
    instance.created_by=None
    instance.save()

@login_required
@permission_required('pilotadmin.view_pilotadmin', raise_exception=True, exception=Http404)
def pilotadmin_list(request):
    model = Pilotadmin
    queryset = None
    if request.method == "POST":
        customername = request.POST['customer_name']
        bg_name = request.POST['bg_name']
        direct_number = request.POST['direct_number']
        queryset = model.objects.filter(customer_name__contains=customername, bg_name__contains=bg_name, direct_number__contains=direct_number)

    template_name = 'pilotadmin/pilotadmin_list.html'

    context = {
        'model': model,
        'object_list': queryset,
    }
    return render(request, template_name, context)


@login_required
@permission_required('pilotadmin.view_pilotadmin', raise_exception=True, exception=Http404)
def pilotadmin_content(request, pk):
    model = Pilotadmin
    queryset = model.objects.get(pk=pk)
    template_name = 'pilotadmin/pilotadmin_content.html'

    action = "READ"
    log_data = f"{request.user} view customer info:{queryset.customer_name}, {queryset.direct_number}"
    pilot_log_record(action=action, data=log_data)

    context = {
        'model': model,
        'object': queryset,
    }
    return render(request, template_name, context)


@login_required
@permission_required('pilotadmin.add_pilotadmin', raise_exception=True, exception=Http404)
def pilotadmin_create(request):
    model = Pilotadmin
    instance = model(updated_by=request.user)
    form_class = PilotadminModelForm
    success_url = reverse('pilotadmin:pilotadmin_list')
    form_buttons = ['create']
    template_name = 'pilotadmin/pilotadmin_form.html'
    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
        context = {'model': model, 'form': form, 'form_buttons': form_buttons}
        return render(request, template_name, context)
    form = form_class()
    context = {'model': model, 'form': form, 'form_buttons': form_buttons}
    return render(request, template_name, context)


@login_required
@permission_required('pilotadmin.change_pilotadmin', raise_exception=True, exception=Http404)
def pilotadmin_update(request, pk):
    model = Pilotadmin
    queryset = get_all_pilotadmin_queryset(request)
    instance = get_object_or_404(klass=queryset, pk=pk)
    form_class = PilotadminModelForm
    success_url = reverse('pilotadmin:pilotadmin_list')
    form_buttons = ['update']
    template_name = 'pilotadmin/pilotadmin_form.html'
    if request.method == 'POST':
        instance.updated_by = request.user
        form = form_class(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
        context = {'model': model, 'form': form, 'form_buttons': form_buttons}
        return render(request, template_name, context)
    form = form_class(instance=instance)
    context = {'model': model, 'form': form, 'form_buttons': form_buttons}
    return render(request, template_name, context)


@login_required
@permission_required('pilotadmin.delete_pilotadmin', raise_exception=True, exception=Http404)
def pilotadmin_delete(request, pk):
    model = Pilotadmin
    queryset = get_all_pilotadmin_queryset(request)
    instance = get_object_or_404(klass=queryset, pk=pk)
    success_url = reverse('pilotadmin:pilotadmin_list')
    template_name = 'pilotadmin/pilotadmin_confirm_delete.html'
    if request.method == 'POST':
        instance.updated_by = request.user
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)
