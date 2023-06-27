from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views import generic
from posts.models import Post


def create_account(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to the login page after successful user creation
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'create_account.html', {'form': form})


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


def user_posts(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        user_posts = Post.objects.filter(created_by_id=request.user)
        context = {'user_posts': user_posts}
        return render(request, "accounts/profile.html", context)
    else:
        return render(request, 'accounts/profile.html')


# def ProfileView(request):


def EditProfileView(request):
    return render(request, 'accounts/edit.html')
