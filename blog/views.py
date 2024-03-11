from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.views.generic import TemplateView
from rest_framework import generics
from .serializers import Postserializer
from django.views.decorators.cache import cache_page

class PostListCreate(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer

class PorstRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = Postserializer
    lookup_field = "pk"

class LoginView(TemplateView):
    def get(request):
        pass

    def post(request):
        pass

    def put(request):
        pass

    def delete(request):
        pass

def index2(request):
    posts = Post.objects.all()
    return render(request, "index2.html", {'posts': posts})

def post(request):
    post = Post.objects.get(id=1)
    return render(request, "post.html", {'post': post})

@cache_page(60 * 15)
def createpost(request):
    if request.method == "POST":
        new_post = PostForm(request.POST)
        if new_post.is_valid():
            new_post.save()
        return redirect(index2)
    else:
        post_form = PostForm()
    context = {
        'post_form': post_form,
    }
    return render(request, 'create_post.html', context)

def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('index2')

def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('index2')
    return render(request, 'edit_post.html', {'form': form})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})
