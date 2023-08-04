from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Post, Author
from django.views.generic import ListView, View
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


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


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "comment_form": CommentForm(),
            "comments": post.comments.all()
        }
        return render(request, "blog/post_detail.html", context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "comment_form": CommentForm(),
            "comments": post.comments.all()
        }
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post_detail", args=[slug]))

        return render(request, "blog/post_detail.html", context)
