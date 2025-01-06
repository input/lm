from django.urls import path

from .views import BlogTagFeed


urlpatterns = [
    path('blog/tag/<slug:slug>/feed/', BlogTagFeed()),
]
