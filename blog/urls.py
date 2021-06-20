from django.urls import path
from blog.views import (
    PostDetailView,
    PostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    search, CommentDeleteView)

from blog.api.views import (PostListAPI,
                            PostDetailAPI,
                            PostUpdateAPI,
                            PostDeleteAPI,
                            PostCreateAPI,
                            PostLikeToggleAPI,)

urlpatterns = [
    path('', PostListView.as_view(), name='blog'),

    path('api/', PostListAPI.as_view(), name='blog-api'),
    path('api/post/<int:pk>/', PostDetailAPI.as_view(), name='post-api-detail'),
    path('api/post/<int:pk>/update/', PostUpdateAPI.as_view(), name='post-api-update'),
    path('api/post/<int:pk>/delete/', PostDeleteAPI.as_view(), name='post-api-delete'),
    path('api/post/create/', PostCreateAPI.as_view(), name='post-api-detail'),
    path('api/post/<int:pk>/like', PostLikeToggleAPI.as_view(), name='post-api-like'),

    path('user/<str:username>', UserPostListView.as_view(), name='user-blog'),
    path('search/', search, name='search'),

    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),


    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]