from django.urls import path

from .views import BlogFeedCustom, BlogTagFeed


urlpatterns = [
    path('blog/feed/', BlogFeedCustom()),
    path('blog/tag/<slug:slug>/feed/', BlogTagFeed()),
]
