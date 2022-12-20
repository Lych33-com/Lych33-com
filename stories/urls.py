from django.urls import path, include
from .views import home, add_story, like_story, report_story,story_detail, add_comment, delete_comment

urlpatterns = [
    path('', home, name="home"),
    path('add-story/', add_story, name="add_story"),
    path('like-story/<int:pk>/', like_story, name="like_story"),
    path("report-story/<int:pk>/",report_story, name="report_story"),
    path("story/<int:pk>/", story_detail, name="story_detail"),
    path("add-comment/<int:pk>/",add_comment, name="add_comment"),
    path("delete-comment/<int:pk>/",delete_comment, name="delete_comment"),
]
