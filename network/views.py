from rest_framework import generics

from .serializers import PostSerializer
from .models import Post

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
# from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer


class LikePost(APIView):

	def post(self, request, pk):
		if request.user.is_authenticated:
			post = get_object_or_404(Post, id=pk)
			if request.user in post.liked_by.all():
				post.liked_by.remove(request.user)
			else:
				post.liked_by.add(request.user)
			post.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)