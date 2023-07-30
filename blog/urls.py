from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    # path("", views.index, name="index"),
    path("posts/", views.AllPostsView.as_view(), name="all_posts"),
    path("posts/<slug:slug>/", views.PostDetailView.as_view(), name="post_detail"),
]
