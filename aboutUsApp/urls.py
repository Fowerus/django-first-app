from django.urls import path

from aboutUsApp import views

urlpatterns = [
	path('',views.main)
]