from django.db import models
from django.contrib.auth import get_user_model
from .validators import validate_file_extension
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
User = get_user_model()


class Story(models.Model):
    story = models.TextField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = models.ManyToManyField("comments.Comment", blank=True, related_name="story_comments")
    likes = models.ManyToManyField("likes.Like", blank=True, related_name="story_likes")
    image = models.ImageField(upload_to="stories",blank=True, null=True)
    title = models.CharField(max_length=255)
    anonymus = models.BooleanField(default=False)
    video = models.FileField(upload_to="videos", validators=[validate_file_extension], blank=True, null=True, storage=VideoMediaCloudinaryStorage)
    
    class Meta:
        verbose_name_plural = "Stories"
    
    def __str__(self):
        return self.title

    
    
    @property
    def get_photo_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return ""

    @property
    def get_video_url(self):
        if self.video and hasattr(self.video, 'url'):
            return self.video.url
        else:
            return ""    

class Report(models.Model):
    story= models.ForeignKey(Story, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.reporter.name} reported story {self.story.title}"

