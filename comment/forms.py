from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Comment, CommentMessage


class CommentModelForm(forms.ModelForm):
    class Meta:
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'class': 'ckeditor4'}),
        }
        model = Comment
        exclude = ['created_by']

class CommentMessageModelForm(forms.ModelForm):
    class Meta:
        widgets = {
            'message_content': forms.Textarea(attrs={'rows': 4, 'class': 'ckeditor4'})
        }
        model = CommentMessage
        exclude = ['message_post','created_by']
