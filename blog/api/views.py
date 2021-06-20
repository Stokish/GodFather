from django.shortcuts import get_object_or_404
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     RetrieveUpdateAPIView,
                                     DestroyAPIView,
                                     CreateAPIView,
                                     )

from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        IsAdminUser,
                                        )

from  rest_framework import authentication

from rest_framework.filters import (SearchFilter, OrderingFilter)

from rest_framework.response import Response

from rest_framework.views import APIView

from blog.api.pagination import PostPageNumberPagination

from blog.api.permissions import IsAuthorOrReadOnly

from blog.api.serializer import (PostSerializer,
                                 PostDetailSerializer,
                                 PostCreateUpdateSerializer)
from blog.models import Post


class PostListAPI(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'content']
    pagination_class = PostPageNumberPagination


class PostDetailAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer


class PostCreateAPI(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostUpdateAPI(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class PostDeleteAPI(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


class PostLikeToggleAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        obj = get_object_or_404(Post, id=self.kwargs.get('pk'))
        user = self.request.user
        updated = False
        liked = False

        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else:
                liked = True
                obj.likes.add(user)

            updated = True
        data = {
            "updated": updated,
            "liked": liked
            }
        return Response(data)
