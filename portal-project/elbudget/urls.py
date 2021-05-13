from django.urls import path
from . import views

urlpatterns = [
	path('', views.reqs, name="elbudget"),
	path('detailed/<str:pk>/', views.updateReq, name="updateReq"),
	path('create-request/',views.createReq, name='createReq')
]