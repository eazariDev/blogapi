# posts/tests.py

from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="secret",
            
        )
        
        cls.post = Post.objects.create(
            title = "test post",
            body = ("this is test post"),
            author = cls.user,
        )
        
    
    def test_post_model(self):
        self.assertEqual(self.post.title, "test post")
        self.assertEqual(self.post.body, "this is test post")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "test post")
        