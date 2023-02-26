from django.urls import path

from usersApp import views


urlpatterns = [
	path('',views.main,name = 'user_main'),
	path('main/',views.main,name = 'user_main'),
	path('login/',views.log_in,name = 'user_login'),
	path('registration/',views.registration,name = 'user_registration'),
	path('logout/',views.log_out,name = 'user_logout'),
	path('profile/<str:account_login>',views.profile,name = 'user_profile')
]
