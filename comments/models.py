from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="comment_owner")
    comment = models.TextField()
    story = models.ForeignKey("stories.Story", on_delete=models.CASCADE, blank=True, null=True, related_name="story_comments")
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering=("-id",)