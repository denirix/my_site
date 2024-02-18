from django.urls import path
from . import views

urlpatterns = [
    path("first_post", views.first_post),
    path("second_post", views.second_post),
    path("", views.index2)
]
