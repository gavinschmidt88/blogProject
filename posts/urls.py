from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='posts'),
    path('new_post/', views.create_post, name='create_post'),
    path('edit/<int:post_id>/', views.edit_post, name='edit_post'),
    # path('edit/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]
