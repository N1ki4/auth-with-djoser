from django.urls import path
from .views import PostList, PostDetail, LikePost


urlpatterns = [
    path('', PostList.as_view(), name='posts_list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/<int:pk>/like/', LikePost.as_view(), name='like_post'),
]
