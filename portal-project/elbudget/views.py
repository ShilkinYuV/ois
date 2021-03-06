from django.http.response import FileResponse, Http404
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
    user_last_name = request.user.last_name
    user_first_name = request.user.first_name
    user = user_last_name + " " + user_first_name
    EbReqForm = EbRequestForm(user, instance=ebdetails)
    if request.method == 'POST':
        EbReqForm = EbRequestForm(user,
                                  request.POST, request.FILES, instance=ebdetails)
        if EbReqForm.is_valid():
            EbReqForm.save()
        return redirect('elbudget')
    return render(request, 'elbudget/EbCreateUpdateReq.html', {'EbReqForm': EbReqForm})

def createReq(request):
    print(request.path)
    user_last_name = request.user.last_name
    user_first_name = request.user.first_name
    user = user_last_name + " " + user_first_name
    EbReqForm = EbRequestForm(user)
    if request.method == 'POST':
        EbReqForm = EbRequestForm(user, request.POST, request.FILES)
        if EbReqForm.is_valid():
            EbReqForm.save()
        return redirect('elbudget')
    return render(request, 'elbudget/EbCreateUpdateReq.html', {'EbReqForm': EbReqForm})

def orgs(request):
    orgList = Organization.objects.all()
    return render(request, 'elbudget/EbOrgList.html', {'orgList': orgList})

def createOrg(request):
    ebOrgForm = EbOrgForm()
    if request.method == 'POST':
        ebOrgForm = EbOrgForm(request.POST, request.FILES)
        if ebOrgForm.is_valid():
            ebOrgForm.save()
        return redirect('org_list')
    return render(request, 'elbudget/EbCreateUpdateOrg.html', {'ebOrgForm': ebOrgForm})

def updateOrg(request,pk):
    orgDetails = Organization.objects.get(INN=pk)

    ebOrgForm = EbOrgForm(instance=orgDetails)
    if request.method == 'POST':
        ebOrgForm = EbOrgForm(request.POST, request.FILES)
        if ebOrgForm.is_valid():
            ebOrgForm.save()
        return redirect('org_list')
    return render(request, 'elbudget/EbCreateUpdateOrg.html', {'ebOrgForm': ebOrgForm})

def workers(request):
    ebWorkerslist = Worker.objects.all()
    return render(request, 'elbudget/EbWorkerList.html', {'ebWorkerslist': ebWorkerslist})

def updateWorker(request, pk):
    workersList = Worker.objects.get(id=pk)
    ebWorkerForm = EbWorkerForm(instance=workersList)
    if request.method == 'POST':
        ebWorkerForm = EbWorkerForm(request.POST, request.FILES, instance=workersList)
        if ebWorkerForm.is_valid():
            ebWorkerForm.save()
        return redirect('workerList')
    return render(request, 'elbudget/EbCreateUpdateWorkers.html', {'EbWorkerForm': ebWorkerForm})

def createWorker(request):
    ebWorkerForm = EbWorkerForm()
    if request.method == 'POST':
        ebWorkerForm = EbWorkerForm(request.POST, request.FILES)
        if ebWorkerForm.is_valid():
            ebWorkerForm.save()
        return redirect('workerList')
    return render(request, 'elbudget/EbCreateUpdateWorkers.html', {'EbWorkerForm': ebWorkerForm})

def change_choice(request, pk=1):
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

def ViewOrgs(request, path):
    try:
        return FileResponse(open(path, 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
