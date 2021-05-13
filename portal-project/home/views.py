from django.shortcuts import render
from .models import *
import datetime
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User

@permission_required('home.view_news', login_url="/login/")
def home(request):
	now = datetime.datetime.now()
	duty = DutyForToday.objects.filter(date=now)
	# print(duty.kabinet_five)
	news = News.objects.all().order_by('-id')[:4]
	date_dict = dict()
	date_dict['news'] = news
	date_dict['duty'] = duty

	return render(request, 'home/index.html', date_dict)

def details(request, id):
	det = News.objects.get(id = id)
	return render(request, 'home/details.html', {'det': det})
