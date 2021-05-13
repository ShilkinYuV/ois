from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required, permission_required

@permission_required('home.view_news', login_url="/login/")
def reqs(request):
    eblist = EbRequest.objects.all()
    return render(request, 'elbudget/ebList.html', {'eblist': eblist})

def reqDetails(request, pk):
    ebdetails = EbRequest.objects.get(id=pk)
    return render(request, 'elbudget/detailedReq.html', {'ebdetails': ebdetails})