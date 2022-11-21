from django.db import models

class Advert(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="ads")
    body = models.TextField(max_length=1000)
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)