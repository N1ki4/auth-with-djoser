from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import status


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
	permission_classes = (IsAuthorOrReadOnly, )
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class PostList(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def perform_create(self, serializer):
		serializer.save(author=self.request.user)

class LikePost(APIView):
	serializer_class = PostSerializer

	def post(self, request, pk):
		if request.user.is_authenticated:
			post = get_object_or_404(Post, id=pk)
			if request.user in post.liked_by.all():
				post.liked_by.remove(request.user)
			else:
				post.liked_by.add(request.user)
			post.save()
			return Response({'success': True}, status=status.HTTP_201_CREATED)
		else:
			return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
