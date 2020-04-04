from django.test import TestCase
from ..models import Post
from django.contrib.auth.models import User


class TestModel(TestCase):

    def setUp(self):
        User.objects.create(
            username="Test", 
            password="testpwd123456",
        )
        user = User.objects.get(pk=1)
        Post.objects.create(
            author = user,
            title = "test title",
            text = "My first test text",
        )
    
    def test_post(self):
        post = Post.objects.get(pk=1)
        title = "test title"
        text = "My first test text"

        self.assertEqual(post.title, title)
        self.assertEqual(post.text, text)
