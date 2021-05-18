from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
from django.views import generic
import json


@permission_required('home.view_news', login_url="/login/")
def reqs(request):
    eblist = EbRequest.objects.all()
    return render(request, 'elbudget/EbReqList.html', {'eblist': eblist})


def updateReq(request, pk):
    ebdetails = EbRequest.objects.get(id=pk)
    EbReqForm = EbRequestForm(instance=ebdetails)
    
    if request.method == 'POST':
        EbReqForm = EbRequestForm(
            request.POST, request.FILES, instance=ebdetails)
        if EbReqForm.is_valid():
            EbReqForm.save()
        return redirect('elbudget')
    return render(request, 'elbudget/EbDetailedReq.html', {'EbReqForm': EbReqForm})


def createReq(request):
    EbReqForm = EbRequestForm()
    
    if request.method == 'POST':
        EbReqForm = EbRequestForm(request.POST, request.FILES)
        if EbReqForm.is_valid():
            EbReqForm.save()
        return redirect('elbudget')
    return render(request, 'elbudget/EbCreateReq.html', {'EbReqForm': EbReqForm})

def createOrg(request):
    # EbReqForm = EbRequestForm()
    ebOrgForm = EbOrgForm()
    if request.method == 'POST':
        ebOrgForm = EbOrgForm(request.POST, request.FILES)
        if ebOrgForm.is_valid():
            ebOrgForm.save()
        return redirect('elbudget')
    return render(request, 'elbudget/EbCreateORG.html', {'ebOrgForm': ebOrgForm})


def change_choice(request,pk):
    if request.method == 'GET':
        val = request.GET["selectedValue"]
         
        all_clients = []
        for client in Worker.objects.filter(ORG_INN=val).values('id', 'FIO'):
            all_clients.append({'id': client['id'], 'FIO': client['FIO']})
        # queryset = WORKER.objects.filter(ORG_INN=val)
        # print(queryset)
        # print(val)
        print(all_clients)
        return HttpResponse(json.dumps(all_clients), content_type="application/json")
    else:
        return HttpResponse('no')
        