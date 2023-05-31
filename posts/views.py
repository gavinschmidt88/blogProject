from django.shortcuts import render, redirect
from .forms import NewPostForm
from .models import Post
from django.core.paginator import Paginator


def post_list(request):
    all_posts = Post.objects.all()
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'posts/post_list.html', {'posts': posts})


def create_post(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:posts")
    else:
        form = NewPostForm()

    return render(request, 'posts/new_post.html', {'form': form})
