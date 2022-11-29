from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Story(models.Model):
    story = models.TextField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField("comments.Comment", blank=True, related_name="story_comments")
    likes = models.ManyToManyField("likes.Like", blank=True, related_name="story_likes")
    image = models.ImageField(upload_to="stories",blank=True, null=True)
    title = models.CharField(max_length=255)
    anonymus = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Stories"
    
    @property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return ""