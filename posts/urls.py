from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='posts'),
    path('new_post/', views.create_post, name='create_post'),
]