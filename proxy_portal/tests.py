from django.test import TestCase
from django.test import SimpleTestCase


# Create your tests here.


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)

    def test_add_page_status_code(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 200)

    def test_del_page_status_code(self):
        response = self.client.get('/del/')
        self.assertEqual(response.status_code, 200)

    def test_edit_page_status_code(self):
        response = self.client.get('/edit/')
        self.assertEqual(response.status_code, 200)
