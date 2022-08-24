from django.urls import path
from blog.views import BlogPostDetail
app_name = "blog"

urlpatterns = [
    path("blogpost/detail", BlogPostDetail.as_view, name="blogpost-detail")

]