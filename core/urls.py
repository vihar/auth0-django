from django.contrib import admin
from django.urls import path, include
from .views import PostListView, index, logout

urlpatterns = [
    path("", index),
    path("codes", PostListView.as_view()),
    path("logout", logout),
    path("", include("django.contrib.auth.urls")),
    path("", include("social_django.urls")),
]
