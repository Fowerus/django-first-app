from django.urls import path

from postsApp import views

urlpatterns = [
	path('',views.main, name = 'posts_main'),
	path('posts/',views.main,name = 'posts_main'),

	path('posts/create/',views.create, name = 'posts_create'),
	path('posts/post/<int:post>/',views.post, name = 'posts_post'),
	path('posts/update/<int:post_id>',views.update, name = 'posts_update'),
	path('posts/delete/<int:post_id>',views.delete, name = 'posts_delete'),

	path('posts/<str:user_login>',views.users_post, name = 'posts_user'),
	path('posts/<str:user_login>/<str:topic>',views.users_post_topic, name = 'posts_user_topic'),

	path('posts/<str:topic>/',views.topic, name = 'posts_topic'),

	path('posts/post/<int:post>/like',views.like_registration,name = 'posts_like_registration')
]