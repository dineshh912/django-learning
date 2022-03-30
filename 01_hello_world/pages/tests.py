from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):

    def test_home_page_status(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
    

    def test_about_page_status(self):
        res = self.client.get("/about")
        self.assertEqual(res.status_code, 200)

