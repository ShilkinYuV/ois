from django.http.response import FileResponse, Http404
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.views import generic
import json

# Create your views here.
def manuals(request):
	return render(request, 'manuals/manuals.html')