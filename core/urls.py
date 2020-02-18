from django.urls import path

from .views import TweetView

urlpatterns = [
    path('', TweetView.as_view(), None, "/"),
    path('<int:pk>/', TweetView.as_view(), None, "/"),
]