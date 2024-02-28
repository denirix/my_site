from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def my_site(request):
    return HttpResponse("Hello my blog!")
# Create your views here.
def my_site1(request):
    return HttpResponse("Hello my blog part 1!")

def my_site2(request):
    return HttpResponse("Hello my blog part 2!")

def index2(request):
    return render(request, "index2.html")

def first_post(request):
    post = Post.objects.get(id=1)
    return render(request, "first_post.html", {'first_post': post})

def second_post(request):
    post = Post.objects.get(id=2)
    return render(request, "second_post.html", {'second_post': post})

def createpost(request):
    if request.method == "POST":
        new_post = PostForm(request.POST)
        if new_post.is_valid():
            new_post.save()
    post_form = PostForm()
    return render(request, 'create_post.html', {'post_form': post_form})
