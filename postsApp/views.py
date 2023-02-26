from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


from .models import Posts,Topics
from .forms import CreatePostForm,UpdatePostForm


@login_required
def main(request):
	all_posts = Posts.objects.all()
	all_topics = Topics.objects.all()
	return render(request,'postsApp/main.html',{'all_posts':all_posts,'all_topics':all_topics})


@login_required
def create(request):
	if request.method == 'POST':
		form = CreatePostForm(request.POST)
		if form.is_valid():
			try:
				Posts(title = form.cleaned_data['title'],text = form.cleaned_data['text'],author = request.user.login,topic = form.cleaned_data['topic']).save()
			except:
				print('postsApp-create | There were some problems on the server')

			return redirect('posts_main')
	else:
		form = CreatePostForm()	
		return render(request,'postsApp/create.html',{'form':form})


@login_required
def delete(request,post_id):
	Posts.objects.get(id = post_id).delete()
	return redirect('posts_user',request.user.login)


@login_required
def update(request,post_id):
	post = Posts.objects.get(id = post_id)
	if request.user.login == post.author:
		if request.method == 'POST':
			form = UpdatePostForm(request.POST)
			if form.is_valid():
				try:
					post.title = form.cleaned_data['title']
					post.text = form.cleaned_data['text']
					post.author = request.user.login
					post.topic = form.cleaned_data['topic']
					post.save()
				except:
					print('postsApp-update | There were some problems on the server')

				return redirect('posts_post',post_id)

		form = UpdatePostForm()
		return render(request,'postsApp/update.html',{'form':form})
		
	return redirect('posts_main')


@login_required
def topic(request,topic):
	current_topic = Topics.objects.get(name = topic)
	if current_topic.id == 1:
		all_posts = Posts.objects.all()
	else:
		all_posts = Posts.objects.all().filter(topic = current_topic.id)
	all_topics = Topics.objects.all()

	return render(request,'postsApp/topic.html',{'all_posts':all_posts,'all_topics':all_topics,'current_topic':current_topic})


@login_required
def post(request,post):
	post = Posts.objects.get(id = post)
	return render(request,'postsApp/post.html',{'post':post})


@login_required
def users_post(request,user_login):
	if request.user.login == user_login:
		all_posts = Posts.objects.all().filter(author = user_login)
		all_topics = Topics.objects.all()
		return render(request,'postsApp/user.html',{'all_posts':all_posts,'all_topics':all_topics})

	return redirect('posts_main')


@login_required
def users_post_topic(request,user_login,topic):
	if request.user.login == user_login:
		current_topic = Topics.objects.get(name = topic)
		if current_topic.id == 1:
			all_posts = Posts.objects.all().filter(author = user_login)
		else:
			all_posts = Posts.objects.all().filter(author = user_login,topic = current_topic.id)
		all_topics = Topics.objects.all()
		return render(request,'postsApp/user_topic.html',{'all_posts':all_posts,'all_topics':all_topics,'current_topic':current_topic,'user_login':user_login})

	return redirect('posts_main')


@login_required
def like_registration(request):
	pass