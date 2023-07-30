from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Post, Author
from django.views.generic import DetailView, ListView
from .forms import  CommentForm
# Create your views here.


# def index(request):
#     author = Author.objects.get(first_name="Gokulakrishnan")
#     posts = Post.objects.all()
#     return render(request, "blog/index.html", {"posts": posts, "author": author})


class HomeView(ListView):
    template_name = "blog/index.html"
    model = Post
    paginate_by = 3
    context_object_name = "posts"

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        qs = qs.order_by("id")
        return qs


class AllPostsView(ListView):
    template_name = "blog/all_post.html"
    model = Post
    context_object_name = "posts"

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        qs = qs.order_by("id")
        return qs


class PostDetailView(DetailView):
    template_name = "blog/post_detail.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm()
        return context

