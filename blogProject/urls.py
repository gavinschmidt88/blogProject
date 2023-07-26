from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', views.display_random_posts, name='home'),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('posts/', include('posts.urls')),
]
