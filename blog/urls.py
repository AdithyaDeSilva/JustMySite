from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name = 'homePage'),
    path("posts",views.posts, name="postsPage"), 
    path("posts/<slug:slug>",views.postDetails, name="postDetailPage") # /posts/first-post
]
