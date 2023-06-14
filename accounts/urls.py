from django.urls import path
from .views import SignUpView
from . import views

# app_name = 'accounts'

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("accounts/profile/", views.ProfileView, name="profile"),
    path("", views.EditProfileView, name="edit"),
    path('user/<str:username>/', views.user_posts, name='user_posts'),
]
