from django.urls import path
from .views_1 import HomePageView,UserListView,UserDetailView,PostListView,PostDetailView,UserPostsView,CreateUserView,CreatePostView,UpdateUserView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('users/',UserListView.as_view(),name='user_list'),
    path('users/<str:username>',UserDetailView.as_view(),name = 'user_detail'),
    path('posts/',PostListView.as_view(),name = 'post_list' ),
    path('posts/<int:post_id>',PostDetailView.as_view(),name='post_detail'),
    path('users/<str:username>/posts/', UserPostsView.as_view(), name='user_posts'),
    path('create/',CreateUserView.as_view(),name = 'create_user'),
    path('users/post/<str:username>/',CreatePostView.as_view(),name = 'create_post'),
    path('users/<str:username>/update/', UpdateUserView.as_view(), name='update_user'),
    
]
 