# Generated by Django 4.2.1 on 2023-07-19 16:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0009_remove_post_dislike_count_remove_post_like_count_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='likedislike',
            unique_together={('user', 'post')},
        ),
    ]
