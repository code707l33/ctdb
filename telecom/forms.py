from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Isp, IspGroup, PrefixListUpdateTask


class IspModelForm(forms.ModelForm):
    class Meta():
        model = Isp
        exclude = ['created_by', ]


class IspGroupModelForm(forms.ModelForm):
    class Meta():
        model = IspGroup
        exclude = ['created_by', ]


class PrefixListUpdateTaskModelForm(forms.ModelForm):
    prefix_list = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': _(
                    'For example:\n'
                    '\n'
                    '100.100.100.100/24,\n'
                    '100.100.200.100/22 le 24,\n'
                ),
                'row': 16
            }
        ),
    )

    class Meta():
        model = PrefixListUpdateTask
        exclude = ['created_by', ]
