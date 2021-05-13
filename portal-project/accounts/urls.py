from django.contrib.auth import views
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'account'
urlpatterns = [
	path('', LoginView.as_view(), name='login'),
	# path('logout/', LogoutView.as_view(), name='logout'),
	path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]