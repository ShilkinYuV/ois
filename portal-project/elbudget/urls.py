from django.urls import path
from . import views

urlpatterns = [
	path('', views.reqs, name="elbudget"),
	path('detailed/<str:pk>/', views.updateReq, name="updateReq"),
	path('detailed/<str:pk>/change_choice/', views.change_choice, name="change_choice"),
	path('create-request/',views.createReq, name='createReq'),
	path('create-request/change_choice/',views.change_choice, name='change_choice'),
	path('org-list/create-org/',views.createOrg, name='create_org'),
	path('org-list/',views.orgs, name='org_list'),
	path('view-doc/<str:path>/',views.ViewOrgs, name='view_doc'),
]		