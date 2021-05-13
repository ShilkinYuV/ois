from django.urls import path
from . import views

urlpatterns = [
	path('', views.reqs, name="elbudget"),
	path('detailed/<str:pk>/', views.reqDetails, name="ebdetails"),
]