from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

from .models import *

@permission_required('home.view_news', login_url="/login/")
def yantar(request):
    admin = Adminyantar.objects.all()
    if request.method == 'POST':
        post = request.POST
        if ('processing1' in post):
            certres = Certificatestore.objects.filter(fio=post['processing1']).order_by("commentary")
        elif ('control1' in post):
            certres = Certificatestore.objects.filter(fio=post['control1']).order_by("commentary")
        elif ('processing2' in post):
            certres = Certificatestore.objects.filter(fio=post['processing2']).order_by("commentary")
        elif ('control2' in post):
            certres = Certificatestore.objects.filter(fio=post['control2']).order_by("commentary")
    else:
        certres = Certificatestore.objects.order_by("commentary")

    all_date = dict()
    all_date['admin'] = admin
    all_date['certres'] = certres
    return render(request, 'yantar/cert.html', all_date)


def details(request, id):
    try:
        certres = Certificatestore.objects.get(pk=id)
    except Certificatestore.DoesNotExist:
        raise Http404("Certificate does not exist")
    return render(request, 'yantar/details.html', {'certres': certres})