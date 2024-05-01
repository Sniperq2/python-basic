from django.views.generic import DetailView
from django.views.generic.list import ListView

from .models import Post


class PostsListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'posts/post_list.html'
    extra_context = {'title': 'Posts List'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ShowPost(DetailView):
    model = Post
    template_name = 'posts/post.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
