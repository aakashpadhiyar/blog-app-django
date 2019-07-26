from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Post
# Create your tests here.

class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects_create_user(
            username ='testuser',
            email='test@email.com',
            password='secret',

        )

        self.post = Post.objects_create(
            title='A good title',
            body='Nick body content',
            author=self.user,
        )

    def test_string_representation(self):
        post = Post(title='A sample title')
        self.asserEqual(str(post, post.title))
