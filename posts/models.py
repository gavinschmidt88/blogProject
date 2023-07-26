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
    liked_users = models.ManyToManyField(
        User, related_name='liked_posts', blank=True)
    disliked_users = models.ManyToManyField(
        User, related_name='disliked_posts', blank=True)

    def like_count(self):
        return self.liked_users.count()

    def dislike_count(self):
        return self.disliked_users.count()

    def __str__(self):
        return self.title


class LikeDislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # True for like, False for dislike
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensure a user can like/dislike a post only once
        unique_together = ['user', 'post']
