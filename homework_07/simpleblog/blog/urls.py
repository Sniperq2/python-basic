from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('posts/', views.posts_list, name='posts'),
    path("__debug__/", include("debug_toolbar.urls")),
]
