from django.db import models
from django.contrib.auth.models import User

LIKE_CHOICES = [
    ('like', 'Like'),
    ('dislike', 'Dislike'),
]


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    like_count = models.PositiveIntegerField(default=0)
    dislike_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
