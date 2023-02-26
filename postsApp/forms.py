from django import forms

from .models import Posts,Topics


class CreatePostForm(forms.ModelForm):

	class Meta:
		model = Posts
		fields = ['title','text','topic']



class UpdatePostForm(forms.ModelForm):

	class Meta:
		model = Posts
		fields = ['title','text','topic']