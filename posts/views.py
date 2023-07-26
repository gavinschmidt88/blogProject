from .models import Post
from .forms import PostForm
from .forms import NewPostForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
import random


def post_list(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'posts/post_list.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by_id = request.user.id
            post.save()
            return redirect("posts:posts")
    else:
        form = NewPostForm()

    return render(request, 'posts/new_post.html', {'form': form})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})


def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        user_posts = Post.objects.filter(created_by_id=request.user)
        context = {'user_posts': user_posts}

        if form.is_valid():
            form.save()
            return render(request, "accounts/profile.html", context)
    else:
        form = PostForm(instance=post)

    context = {'form': form}
    return render(request, 'posts/edit_post.html', context)


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    user_posts = Post.objects.filter(created_by_id=request.user)
    context = {'user_posts': user_posts}
    return render(request, 'accounts/profile.html', context)


def like_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        user = request.user  # Assuming you have authenticated users
        print('success')

        if user in post.liked_users.all():
            post.liked_users.remove(user)
        else:
            post.liked_users.add(user)
            post.disliked_users.remove(user)

        return JsonResponse({'like_count': post.like_count()})
    else:
        return JsonResponse({'error': 'Invalid request'})


def dislike_post(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        user = request.user  # Assuming you have authenticated users

        if user in post.disliked_users.all():
            post.disliked_users.remove(user)
        else:
            post.disliked_users.add(user)
            post.liked_users.remove(user)

        return JsonResponse({'dislike_count': post.dislike_count()})
    else:
        return JsonResponse({'error': 'Invalid request'})


def display_random_posts(request):
    # Get all the posts
    all_posts = Post.objects.all()

    # Randomly select 6 posts
    selected_posts = random.sample(list(all_posts), 6)

    # Pass the selected posts to the template context
    return render(request, 'home.html', {'selected_posts': selected_posts})
