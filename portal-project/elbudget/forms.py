from django import forms
from django.forms import ModelForm, widgets

from .models import EbRequest

class EbRequestForm(ModelForm):

    class Meta:
        model = EbRequest
        fields = '__all__'

        widgets = {
            'ORG_INN': forms.Select(attrs={
                'class': 'form-select'
            }),
            'REQUEST_TYPE': forms.Select(attrs={
                'class': 'form-select'
            }),
            'EXECUTOR': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'TRACK_NUMBER': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'MESSAGE_NUMBER': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'RESULT': forms.Select(attrs={
                'class': 'form-select'
            }),
            'NUMBER': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'COMMENT': forms.Textarea(attrs={
                'class': 'form-control',
                'style': 'height: 100px'
            }),
            'CLIENT_ID': forms.Select(attrs={
                'class': 'form-select'
            }),
            'RESP_PERSONE_ID': forms.Select(attrs={
                'class': 'form-select'
            }), 
            'IsDEBTOR': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
            'ADDED_ROLES':forms.CheckboxSelectMultiple(attrs={
                'style':'list-style-type: none'
            }),
            'GETTING_TIME': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'MESSAGE_DATA': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
        }