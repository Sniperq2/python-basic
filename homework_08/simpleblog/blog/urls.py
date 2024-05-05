from django.urls import path, include

from .views import PostsListView, ShowPost

urlpatterns = [
    path("", PostsListView.as_view(), name="posts"),
    path('<int:post_pk>/', ShowPost.as_view(), name='post'),
    path("__debug__/", include("debug_toolbar.urls")),
]
