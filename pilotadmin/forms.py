from django import forms

from .models import Pilotadmin


class PilotadminModelForm(forms.ModelForm):
    class Meta:
        model = Pilotadmin
        exclude = []
