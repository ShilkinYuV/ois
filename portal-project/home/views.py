from django.shortcuts import render
from .models import *
import datetime

def home(request):
	now = datetime.datetime.now()
	duty = DutyForToday.objects.filter(date=now)
	news = News.objects.all().order_by('-id')[:4]
	date_dict = dict()
	date_dict['news'] = news
	date_dict['duty'] = duty
	return render(request, 'home/index.html', date_dict)

def details(request, id):
	det = News.objects.filter(id = id)
	return render(request, 'home/details.html', {'det': det})
