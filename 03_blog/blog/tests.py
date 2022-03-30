from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Post
# Create your tests here.

class BlogTests(TestCase):

    def setUp(self):

        self.user = get_user_model().objects.create_user(
            username = "testuser",
            email="test@email.com",
            password="secret"
        )

        self.post = Post.objects.create(
            title = "This is title",
            body = "this is body"
        )

    
    def test_string_representation(self):
        post = Post(title="This is title")
        self.assertEqual(str(post), post.title)

    
    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "This is title")
        self.assertEqual(f"{self.post.body}", "this is body")


    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_post_list_view(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "this is body")
        self.assertTemplateUsed(res, 'blog/home.html')

    def test_post_detatil_view(self):
        res = self.client.get("/post/1/")
        no_res = self.client.get("/post/10000/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(no_res.status_code, 404)
        self.assertContains(res, "this is body")
        self.assertTemplateUsed(res, "blog/post_detail.html")
        