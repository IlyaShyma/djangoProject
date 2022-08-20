from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from blog.models import BlogPost
class BlogPostDetail(DetailView):
    model =