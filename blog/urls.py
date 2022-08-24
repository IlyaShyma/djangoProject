from django.urls import path
from blog.views import BlogPostDetail, BlogPostList

app_name = "blog"

urlpatterns = [
    path("blogpost/<int:pk>/detail", BlogPostDetail.as_view(), name="blogpost-detail"),
    path("blogpost/list", BlogPostList.as_view(), name="blogpost-list"),


]