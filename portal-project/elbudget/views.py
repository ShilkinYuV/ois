from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required, permission_required

@permission_required('home.view_news', login_url="/login/")
def start(request):
    eblist = EbRequest.objects.all()
    return render(request, 'elbudget/ebList.html', {'eblist': eblist})