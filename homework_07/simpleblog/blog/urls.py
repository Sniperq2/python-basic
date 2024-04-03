from django.urls import path, include

from .views import PostsListView

urlpatterns = [
    path("", PostsListView.as_view(), name="posts"),
    path("__debug__/", include("debug_toolbar.urls")),
]
