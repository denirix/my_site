from django.urls import path
from . import views

urlpatterns = [
    path("", views.my_site),
    path("article1", views.my_site1),
    path("article2", views.my_site2)
]
