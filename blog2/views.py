from django.shortcuts import render
from django.http import HttpResponse

def my_site(request):
    return HttpResponse("Hello my blog2!")
# Create your views here.
def my_site1(request):
    return HttpResponse("Hello my blog2 part 1!")

def my_site2(request):
    return HttpResponse("Hello my blog2 part 2!")
