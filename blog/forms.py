from django.forms import ModelForm
from .models import Post, Category
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
