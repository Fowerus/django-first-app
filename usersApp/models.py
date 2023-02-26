from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager


class UserManager(BaseUserManager):
	def create_user(self,login,password = None):
		if not login:
			raise ValueError('You need to write a login')

		user = self.model(login = login)
		user.set_password(password)
		user.save(using=self._db)

		return user


	def create_superuser(self,login,password):
		user = self.create_user(
				login = login,
				password = password
			)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using = self._db)

		return user



class Users(AbstractBaseUser):
	login = models.CharField(max_length = 30,unique = True)
	last_login = models.DateTimeField(verbose_name = 'last login', auto_now = True,blank=True, null=False)
	is_admin = models.BooleanField(default = False)
	is_staff = models.BooleanField(default = False)
	is_superuser = models.BooleanField(default = False)
	is_active = models.BooleanField(default = True)

	username = None
	USERNAME_FIELD = 'login'

	objects = UserManager()


	def has_perm(self, perm = None, obj=None):
		return self.is_admin

	def has_module_perms(self, module):
		return True

	def __str__(self):
		return self.login


	class Meta:
		verbose_name_plural = 'Users'
		verbose_name = 'User'