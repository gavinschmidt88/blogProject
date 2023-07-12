from .forms import PostForm
from .forms import NewPostForm
from .models import Post
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404


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
