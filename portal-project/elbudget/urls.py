from django.urls import path
from . import views

urlpatterns = [
	path('', views.reqs, name="elbudget"),
	path('detailed/<str:pk>/', views.updateReq, name="updateReq"),
	path('create-request/',views.createReq, name='createReq'),
	path('create-request/change_choice/',views.change_choice, name='change_choice')
]		