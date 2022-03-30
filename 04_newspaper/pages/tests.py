from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    def test_view_url_by_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

    def test_view_uses_correct_template(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'home.html')


class SignupPageTests(TestCase):

    username = "newuser"
    email = "newuser@email.com"

    def test_signup_page_staus_code(self):
        res = self.client.get("/accounts/signup/")
        self.assertEqual(res.status_code, 200)

    def test_signup_url_by_name(self):
        res = self.client.get(reverse('signup'))
        self.assertEqual(res.status_code, 200)

    def test_signup_correct_template(self):
        res = self.client.get(reverse('signup'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'registration/signup.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)