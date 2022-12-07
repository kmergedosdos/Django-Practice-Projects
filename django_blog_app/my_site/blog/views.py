from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Post


# Create your views here.

def home_page(request):
  latest_posts = Post.objects.all().order_by("-date")[:3]
  context = {
    "latest_posts": latest_posts
  }
  return render(request, 'blog/index.html', context)

def posts(request):
  sorted_posts = Post.objects.all().order_by("date")
  context = {
    "posts": sorted_posts
  }
  return render(request, 'blog/all-posts.html', context)

def post_detail(request, slug):
  filtered_post = get_object_or_404(Post, slug=slug)
  context = {
    "post": filtered_post,
    "tags": filtered_post.tags.all()
  }
  return render(request, 'blog/single-post.html', context)