from django.contrib.auth import views
from django.urls import path

urlpatterns = [
	path('', views.LoginView.as_view(), name='login'),
]