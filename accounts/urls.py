from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("accounts/profile/", views.user_posts, name="profile"),
    path('profile/edit/', views.edit_profile, name='edit'),
    path('user/<str:username>/', views.user_posts, name='user_posts'),
]
