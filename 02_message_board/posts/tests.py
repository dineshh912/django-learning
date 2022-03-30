from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.

class PostModelTest(TestCase):

    def setUp(self):
        Post.objects.create(text='hee')

    def test_text_content(self):
        post=Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'hee')


class HomePageViewTest(TestCase):

    def setUp(self):
        Post.objects.create(text="hello world")

    def test_page_status(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_url_by_name(self):
        res = self.client.get(reverse('Home'))
        self.assertEqual(res.status_code, 200)

    def test_url_template(self):
        res = self.client.get(reverse('Home'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'posts/home.html')
    