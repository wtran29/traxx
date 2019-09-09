from django.db import models
from django.contrib.auth import get_user_model


class Track(models.Model):
    traxx_user = models.ForeignKey(get_user_model(), null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


