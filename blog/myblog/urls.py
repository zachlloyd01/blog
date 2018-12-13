from django.urls import path, include
from django.views.generic import ListView, DetailView
from myblog.models import Post
from django.conf.urls import url

urlpatterns = [
    path('', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25],template_name="myblog/blog.html")),
    url('(?P<pk>\d+)', DetailView.as_view(model=Post, template_name = 'myblog/post.html')),
]
