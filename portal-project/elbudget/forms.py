from django import forms
from django.forms import ModelForm, widgets

from .models import *

class EbRequestForm(ModelForm):
	def __init__(self, user, *args, **kwargs):
		super(EbRequestForm, self).__init__(*args, **kwargs)
		self.user = user
		self.fields['EXECUTOR'].initial = self.user

	class Meta:
		model = EbRequest
		fields = '__all__'

		widgets = {
	        'ORG_INN': forms.Select(attrs={
	            'class': 'form-select org', 
	            'onchange': "myFunction()"
	        }),
	        'REQUEST_TYPE': forms.Select(attrs={
	            'class': 'form-select'
	        }),
	        'RESP_PERSONE_ID': forms.Select(attrs={
	            'class': 'form-select clnt'
	        }),
	        'EXECUTOR': forms.TextInput(attrs={
	            'class': 'form-control',
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
	            'class': 'form-select clnt'
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

class EbOrgForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"
        widgets = {
            'INN': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'NAME': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'DOC_RESP_PERSON': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }

class EbWorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = "__all__"
        widgets = {
            'FIO': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'ORG_INN': forms.Select(attrs={
	            'class': 'form-select clnt'
            }),
            'DOC_AGREEMENT': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'ADDITIONAL_INFO': forms.Textarea(attrs={
                'class': 'form-control'
            }),
			'RESP_PERSONE': forms.CheckboxInput(attrs={
	            'class': 'form-check-input'
	        })
        }