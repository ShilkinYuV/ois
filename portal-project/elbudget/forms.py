from django import forms
from django.forms import ModelForm, widgets

from .models import EbRequest

class EbRequestForm(ModelForm):

    class Meta:
        model = EbRequest
        fields = '__all__'

        widgets = {
            'ADDED_ROLES':forms.CheckboxSelectMultiple(),
            'GETTING_TIME': forms.DateInput(attrs={
                'type': 'date'
            }),
            'MESSAGE_DATA': forms.DateInput(attrs={
                'type': 'date'
            }),
        }