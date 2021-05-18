from django.urls import path
from . import views

urlpatterns = [
	path('journal', views.reqs, name="elbudget"),
	path('journal/detailed/<str:pk>/', views.updateReq, name="updateReq"),
	path('journal/detailed/<str:pk>/change_choice/', views.change_choice, name="change_choice"),
	path('journal/create-request/',views.createReq, name='createReq'),
	path('journal/create-request/change_choice/',views.change_choice, name='change_choice'),
	path('org-list/create-org/',views.createOrg, name='create_org'),
	path('org-list/',views.orgs, name='org_list'),
	path('org-list/detailed/<str:pk>/',views.updateOrg, name='orgUpdate'),
	path('view-doc/<str:path>/',views.ViewOrgs, name='view_doc'),
	path('workers', views.workers, name='workerList'),
	path('workers/create-worker/', views.createWorker, name='workerCreate'),
	path('workers/detailed/<str:pk>/', views.updateWorker, name='workerUpdate'),
]		