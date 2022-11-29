from django.urls import path, include
from .views import home, add_story

urlpatterns = [
    path('', home, name="home"),
    path('add-story/', add_story, name="add_story"),
]
