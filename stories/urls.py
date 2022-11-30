from django.urls import path, include
from .views import home, add_story, like_story

urlpatterns = [
    path('', home, name="home"),
    path('add-story/', add_story, name="add_story"),
    path('like-story/<int:pk>/', like_story, name="like_story"),
]
