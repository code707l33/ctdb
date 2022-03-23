from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http.response import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from core.decorators import permission_required
from core.utils import today

from .forms import CommentModelForm, CommentMessageModelForm
from .models import Comment, CommentMessage

# Create your views here.

@login_required
@permission_required('comment.view_comment', raise_exception=True, exception=Http404)
def comment_list(request):
    model = Comment
    queryset = model.objects.all()
    paginate_by = 20
    template_name = 'comment/comment_list.html'
    page_number = request.GET.get('page', '')
    paginator = Paginator(queryset, paginate_by)
    page_obj = paginator.get_page(page_number)
    is_paginated = page_number.lower() != 'all' and page_obj.has_other_pages()

    context = {
        'model': model,
        'page_obj': page_obj,
        'object_list': page_obj if is_paginated else queryset,
    }

    return render(request, template_name, context)
    
@login_required
@permission_required('comment.add_comment', raise_exception=True, exception=Http404)
def comment_create(request):
    model = Comment
    instance = model(created_by=request.user)
    form_class = CommentModelForm
    success_url = reverse('comment:comment_list')
    form_buttons = ['create', 'save_and_continue_editing']
    template_name = 'comment/comment_form.html'
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            if request.POST.get('save_and_continue_editing'):
                return redirect(reverse('comment:comment_update', kwargs={'pk': instance.pk}))
            return redirect(success_url)
        context = {'model': model, 'form': form, 'form_buttons': form_buttons}
        return render(request, template_name, context)
    form = form_class()
    context = {'model': model, 'form': form, 'form_buttons': form_buttons}
    return render(request, template_name, context)


@login_required
@permission_required('comment.change_comment', raise_exception=True, exception=Http404)
def comment_update(request, pk):
    model = Comment
    queryset = model.objects.all()
    instance = get_object_or_404(klass=queryset, pk=pk, created_by=request.user)
    form_class = CommentModelForm
    success_url = reverse('comment:comment_list')
    form_buttons = ['update', 'save_and_continue_editing']
    template_name = 'comment/comment_form.html'
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            if request.POST.get('save_and_continue_editing'):
                return redirect(reverse('comment:comment_update', kwargs={'pk': instance.pk}))
            return redirect(success_url)
        context = {'model': model, 'form': form, 'form_buttons': form_buttons}
        return render(request, template_name, context)
    form = form_class(instance=instance)
    context = {'model': model, 'form': form, 'form_buttons': form_buttons}
    return render(request, template_name, context)


@login_required
@permission_required('comment.delete_comment', raise_exception=True, exception=Http404)
def comment_delete(request, pk):
    model = Comment
    queryset = model.objects.all()
    instance = get_object_or_404(klass=queryset, pk=pk, created_by=request.user)
    success_url = reverse('comment:comment_list')
    template_name = 'comment/comment_confirm_delete.html'
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)


@login_required
@permission_required('comment.view_commentmessage', raise_exception=True, exception=Http404)
def comment_message_list(request,pk):
    model_comment = Comment
    comment = model_comment.objects.get(pk=pk)
    model = CommentMessage
    queryset = model.objects.filter(message_post=pk)
    paginate_by = 5
    template_name = 'comment/comment_message_list.html'
    page_number = request.GET.get('page', '')
    paginator = Paginator(queryset, paginate_by)
    page_obj = paginator.get_page(page_number)
    is_paginated = page_number.lower() != 'all' and page_obj.has_other_pages()
    

    context = {
        'model': model,
        'comment': comment,
        'page_obj': page_obj,
        'object_list': page_obj if is_paginated else queryset,
        "comment_pk": pk
    }

    return render(request, template_name, context)


@login_required
@permission_required('comment.add_commentmessage', raise_exception=True, exception=Http404)
def comment_message_create(request,pk):
    model = CommentMessage
    message_post = Comment.objects.get(pk=pk)
    instance = model(created_by=request.user, message_post=message_post)
    form_class = CommentMessageModelForm
    success_url = reverse('comment:comment_message_list', kwargs={'pk': pk})
    form_buttons = ['create', 'save_and_continue_editing']
    template_name = 'comment/comment_form.html'
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            if request.POST.get('save_and_continue_editing'):
                return redirect(reverse('comment:comment_message_update'))
            return redirect(success_url)
        context = {'model': model, 'form': form, 'form_buttons': form_buttons}
        return render(request, template_name, context)
    form = form_class()
    context = {'model': model, 'form': form, 'form_buttons': form_buttons}
    return render(request, template_name, context)


@login_required
@permission_required('comment.delete_commentmessage', raise_exception=True, exception=Http404)
def comment_message_delete(request, comment_pk, pk):
    model = CommentMessage
    queryset = model.objects.all()
    instance = get_object_or_404(klass=queryset, pk=pk, created_by=request.user)
    success_url = reverse('comment:comment_message_list', kwargs={'pk': comment_pk})
    template_name = 'comment/comment_confirm_delete.html'
    if request.method == 'POST':
        instance.delete()
        return redirect(success_url)
    context = {'model': model}
    return render(request, template_name, context)


@login_required
@permission_required('comment.change_commentmessage', raise_exception=True, exception=Http404)
def comment_message_update(request, comment_pk, pk):
    model = CommentMessage
    queryset = model.objects.all()
    instance = get_object_or_404(klass=queryset, pk=pk, created_by=request.user)
    form_class = CommentMessageModelForm
    success_url = reverse('comment:comment_message_list', kwargs={'pk': comment_pk})
    form_buttons = ['update', 'save_and_continue_editing']
    template_name = 'comment/comment_form.html'
    if request.method == 'POST':
        form = form_class(data=request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            if request.POST.get('save_and_continue_editing'):
                return redirect(reverse('comment:comment_update', kwargs={'pk': instance.pk}))
            return redirect(success_url)
        context = {'model': model, 'form': form, 'form_buttons': form_buttons}
        return render(request, template_name, context)
    form = form_class(instance=instance)
    context = {'model': model, 'form': form, 'form_buttons': form_buttons}
    return render(request, template_name, context)