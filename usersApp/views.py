from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .models import Users
from .forms import UserRegistrationForm,UserLoginForm


def main(request):
	return redirect('user_login')


def registration(request):
	if not request.user or request.user.is_authenticated == False:
		if request.method == 'POST':
			form = UserRegistrationForm(request.POST)
			if form.is_valid():
				try:
					form.save()
					return redirect('user_login')
				except:
					print('usersApp-registration | There were some problems on the server')
			else:
				messages.warning(request,'An account with this login has already been created or the data entered is incorrect')

		form = UserRegistrationForm()
		return render(request,'usersApp/registration.html',{'form':form})
	return redirect('posts_main')


def log_in(request):
	if not request.user or request.user.is_authenticated == False:
		if request.method == 'POST':
			user_login = request.POST.get("login")
			password = request.POST.get("password")

			if not request.user.is_authenticated:

				user = authenticate(login = user_login, password = password)

				if user is not None:
					if user.is_active:

						login(request,user)
						return redirect('posts_main')
					
					else:
						messages.info(request,"Your account has been disabled by an administrator")
				else:
					messages.warning(request,"Incorrect login or password")
			else:
				return redirect('posts_main')


		form = UserLoginForm()
		return render(request,'usersApp/login.html',{'form':form})

	return redirect('posts_main')


@login_required
def log_out(request):
	logout(request)
	return redirect('user_login')


@login_required
def profile(request,account_login):
	account = Users.objects.get(login = account_login)
	if account:
		return render(request,'usersApp/profile.html',{'user':account})
	return redirect('posts_main')