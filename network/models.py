from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-added', )
