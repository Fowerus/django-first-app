from django.db import models
from usersApp.models import Users


class Posts(models.Model):
	title = models.CharField(max_length = 70,blank = False, verbose_name = 'Title')
	text = models.TextField(verbose_name = 'Content')
	date_create = models.DateTimeField(auto_now_add = True)
	date_update = models.DateTimeField(auto_now = True)
	topic = models.ForeignKey('Topics',on_delete=models.SET_DEFAULT,null = False, default = 1)
	author = models.CharField(max_length = 30,blank = False)
	likes = models.BinaryField(blank = True)


	class Meta:
		verbose_name_plural = 'Posts'
		verbose_name = 'Post'
		ordering = ['-date_create']





class Topics(models.Model):
	name = models.CharField(max_length = 20)
	date_create = models.DateTimeField(auto_now_add = True)


	class Meta:
		verbose_name_plural = 'Topics'
		verbose_name = 'Topic'
		ordering = ['date_create']


	def __str__(self):
		return self.name



class PostsLikes(models.Model):
	user = models.IntegerField(verbose_name = 'User')
	post = models.IntegerField(verbose_name = 'Post')
	like = models.BooleanField(verbose_name = 'Like')
	date_update = models.DateTimeField(auto_now = True)

	def __str__(self):
		return f'user: {Users.objects.get(id = self.user).login} | post: {Posts.objects.get(self.post).title}'


	class Meta:
		verbose_name_plural = 'PostsLikes'
		verbose_name = 'Like'
		ordering = ['-date_update']