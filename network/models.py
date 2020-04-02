from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    liked_by = models.ManyToManyField(User, related_name='likes', blank=True)

    def __str__(self):
        return f"{self.title} | {self.author} | {self.liked_by}"

    class Meta:
        ordering = ('-added', )
