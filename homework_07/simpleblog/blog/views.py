from django.views.generic.list import ListView

from .models import Post


class PostsListView(ListView):
    model = Post
    context_object_name = 'posts'