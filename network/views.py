from rest_framework import generics

from .serializers import PostSerializer
from .models import Post

from rest_framework.views import APIView


class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class LikePost(APIView):
	serializer_class = PostSerializer

	def post(self, request, post_pk, liked_by):
		pass