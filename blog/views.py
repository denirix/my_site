from django.shortcuts import render
from django.http import HttpResponse

def my_site(request):
    return HttpResponse("Hello my blog!")
# Create your views here.
def my_site1(request):
    return HttpResponse("Hello my blog part 1!")

def my_site2(request):
    return HttpResponse("Hello my blog part 2!")

def index2(request):
    return render(request, "index.html")
