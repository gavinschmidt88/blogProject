import random
from posts.models import Post
from django.shortcuts import render


def HomeView(request):
    return render(request, 'blogProject/home.html')


def display_random_posts(request):
    # Get all the posts
    all_posts = Post.objects.all()

    # Randomly select 3 posts
    selected_posts = random.sample(list(all_posts), 3)

    # Pass the selected posts to the template context
    return render(request, 'blogProject/home.html', {'selected_posts': selected_posts})
