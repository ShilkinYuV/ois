from django.shortcuts import render
from .models import Certificatestore
# Create your views here.
def yantar(request):
	cert = Certificatestore.objects.all().order_by('commentary')
	return render(request, 'yantar/cert.html', {'cert': cert})