from django.contrib import admin
from django.urls import path

from .api import ArticleListCreateAPIView, ArticleRetriveAPIView, ArticleRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('articles/', ArticleListCreateAPIView.as_view()),
    path("articles/<int:pk>", ArticleRetrieveUpdateDestroyAPIView.as_view()),
    # path("articles/del<id>", ArticleRetrieveUpdateDestroyAPIView.as_view()),
    # path("articles/up<id>", ArticleRetrieveUpdateDestroyAPIView.as_view()),
    # path("articles/<id>", ArticleRetrieveUpdateDestroyAPIView.as_view())
]
