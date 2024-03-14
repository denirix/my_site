from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.views.generic import TemplateView
from rest_framework import generics
from .serializers import Postserializer
from django.views.decorators.cache import cache_page
from .task import my_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def test_cel(request):
    my_task.delay()
    return HttpResponse("Started!")

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


@login_required(login_url='login')
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

@login_required(login_url='login')
def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('index2')

@login_required(login_url='login')
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

def schedule_task(request):
    interval, err = IntervalSchedule.objects.get_or_create(
        every=30, period=IntervalSchedule.SECONDS
    )

    PeriodicTask.objects.create(
        interval=interval,
        name="evgen-schedule",
        task="blog.task.my_task",
        # args=json.dump(["arg1", True]),
        # on_off=True,
    )
    return HttpResponse("Scheduled!")

def registration_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('index2')
    return render(request, 'registration.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index2')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index2')
