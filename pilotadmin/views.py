from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from core.decorators import permission_required

from .forms import PilotadminModelForm
from .models import Pilotadmin


def get_all_pilotadmin_queryset(request):
    """
    The queryset of model `Archive` with filter depending on user's role/identity/group.
    The views below will use this as a basic queryset. This ensures that users won't
    accidentally see or touch those they shouldn't.
    """
    model = Pilotadmin
    queryset = model.objects.all()
    return queryset


@login_required
@permission_required('archive.view_archive', raise_exception=True, exception=Http404)
def pilotadmin_list(request):
    model = Pilotadmin
    queryset = get_all_pilotadmin_queryset(request)
    if request.method == "POST":
        customername = request.POST['customer_name']
        queryset = model.objects.filter(customer_name__contains=customername)
    paginate_by = 10
    template_name = 'pilotadmin/pilotadmin_list.html'
    page_number = request.GET.get('page', '')
    paginator = Paginator(queryset, paginate_by)
    page_obj = paginator.get_page(page_number)
    is_paginated = page_number.lower() != 'all' and page_obj.has_other_pages()

    context = {
        'model': model,
        'page_obj': page_obj,
        'object_list': page_obj if is_paginated else queryset,
        'is_paginated': is_paginated,
    }
    return render(request, template_name, context)
