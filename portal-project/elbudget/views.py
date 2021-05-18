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

def orgs(request):
    orgList = Organization.objects.all()
    return render(request, 'elbudget/EbOrgList.html', {'orgList': orgList})

def updateReq(request, pk):
    ebdetails = EbRequest.objects.get(id=pk)
    user_last_name = request.user.last_name
    user_first_name = request.user.first_name
    user = user_last_name + " " + user_first_name
    EbReqForm = EbRequestForm(user,instance=ebdetails)
    
    if request.method == 'POST':
        EbReqForm = EbRequestForm(
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
        EbReqForm = EbRequestForm(request.POST, request.FILES)
        if EbReqForm.is_valid():
            EbReqForm.save()
        return redirect('elbudget')
    return render(request, 'elbudget/EbCreateUpdateReq.html', {'EbReqForm': EbReqForm})

def createOrg(request):
    ebOrgForm = EbOrgForm()
    if request.method == 'POST':
        ebOrgForm = EbOrgForm(request.POST, request.FILES)
        if ebOrgForm.is_valid():
            ebOrgForm.save()
        return redirect('elbudget')
    return render(request, 'elbudget/EbCreateORG.html', {'ebOrgForm': ebOrgForm})


def change_choice(request,pk=1):
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

    # wdith open(path, 'rb') as pdf:
    #     response = HttpResponse(pdf.read(), mimetype='application/pdf')
    #     response['Content-Disposition'] = 'inline;filename=some_file.pdf'
    #     return response
    # pdf.close