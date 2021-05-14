from django.shortcuts import redirect, render
from .models import *
from .forms import EbRequestForm
from django.contrib.auth.decorators import login_required, permission_required


@permission_required('home.view_news', login_url="/login/")
def reqs(request):
    eblist = EbRequest.objects.all()
    return render(request, 'elbudget/ebList.html', {'eblist': eblist})


def updateReq(request, pk):
    ebdetails = EbRequest.objects.get(id=pk)
    EbReqForm = EbRequestForm(instance=ebdetails)

    if request.method == 'POST':
        EbReqForm = EbRequestForm(
            request.POST, request.FILES, instance=ebdetails)
        if EbReqForm.is_valid():
            EbReqForm.save()
        return redirect('elbudget')
    return render(request, 'elbudget/detailedReq.html', {'EbReqForm': EbReqForm})


def createReq(request):
    EbReqForm = EbRequestForm()

    if request.method == 'POST':
        EbReqForm = EbRequestForm(request.POST, request.FILES)
        if EbReqForm.is_valid():
            EbReqForm.save()
        return redirect('elbudget')
    return render(request, 'elbudget/newReqForm.html', {'EbReqForm': EbReqForm})
