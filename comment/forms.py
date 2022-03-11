from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Comment, CommentMessage


class CommentModelForm(forms.ModelForm):
    class Meta:
        widgets = {
            'post_date': forms.DateInput(attrs={'type': 'date'}),
            'comment': forms.Textarea(attrs={'rows': 4, 'class': 'ckeditor4'}),
        }
        model = Comment
        exclude = ['created_by']

class CommentMessageModelForm(forms.ModelForm):
    class Meta:
        widgets = {
            'message_date': forms.DateInput(attrs={'type': 'date', 'readonly': ''}),
            'message_content': forms.Textarea(attrs={'rows': 4, 'class': 'ckeditor4'})
        }
        model = CommentMessage
        exclude = ['message_create_by']
