from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    story = models.ForeignKey("stories.Story", on_delete=models.CASCADE)
    text = models.TextField(max_length=500)