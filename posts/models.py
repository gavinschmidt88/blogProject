from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.core.exceptions import ObjectDoesNotExist


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        editable=False,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.id:
            # New post, set the 'created_by' field to the current user
            request = kwargs.pop('request', None)
            if request and not isinstance(request.user, AnonymousUser):
                try:
                    user = request.user
                    self.created_by = user
                except ObjectDoesNotExist:
                    pass
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
