from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView
from blog.models import BlogPost


class BlogPostDetail(DetailView):
    model = BlogPost
    template_name = "blog/blogpost/detail.html"

class BlogPostList(ListView):
    model = BlogPost
    template_name = "blog/blogpost/list.html"


