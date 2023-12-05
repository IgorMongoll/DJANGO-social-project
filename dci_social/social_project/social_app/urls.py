from django.urls import path
from .views import home,user_list,user_details,post_detail,post_list,user_posts,create_user,create_post,update_user

urlpatterns = [
    path('',home,name='home'),
    path('users/',user_list,name='user_list'),
    path('users/<str:username>/',user_details,name='user_detail'),
    path('posts/',post_list,name='post_list'),
    path('posts/<int:post_id>/',post_detail,name='post_detail'),
    path('users/<str:username>/posts/',user_posts,name='user_posts'),
    path('create/',create_user,name='create_user'),
    path('users/post/<str:username>/', create_post, name='create_post'),
    path('users/<str:username>/update/', update_user, name='update_user'),

    
]
