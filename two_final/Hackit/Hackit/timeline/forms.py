from django import forms
from .models import Post,Post_1


class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('text', 'photo')

class PostForm_1(forms.ModelForm):
	class Meta:
		model = Post_1
		fields = ('text_1',)