from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def start(request):
    eblist = EbRequest.objects.all()
    return render(request, 'elbudget/ebList.html', {'eblist': eblist})