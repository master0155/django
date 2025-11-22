from django.shortcuts import render, get_object_or_404
from django.views import View
from ..post import Post


class PostView(View):
    def get(self, request, *args, **kwargs):
        post_list = Post.objects.filter(status=1)
        return render(request, 'index.html', {'post_list': post_list})


class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug, status=1)
        return render(request, 'post_detail.html', {'post': post})