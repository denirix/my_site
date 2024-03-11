from django.urls import path
from . import views
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title = "My API", default_version="1.0.0", description="Documentation for my API"
    ),
    public=True
)

urlpatterns = [
    # path("posts", views.post),
    path("", views.index2, name = "index2"),
    path("createpost", views.createpost),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('login/', views.LoginView.as_view()),
    path('posts', views.PostListCreate.as_view()),
    path(
        "posts/<int:pk>",
        views.PorstRetrieveUpdateDestroy.as_view(), name="updatepost"
    ),
    path('editpost/<int:post_id>/', views.edit_post, name='edit_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger")
]
