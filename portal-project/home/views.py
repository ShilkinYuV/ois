from django.shortcuts import render
from .models import News

def home(request):
	news = News.objects.all()
	return render(request, 'home/index.html', {'news': news})

def details(request, id):
	det = News.objects.filter(id = id)
	return render(request, 'home/details.html', {'det': det})
