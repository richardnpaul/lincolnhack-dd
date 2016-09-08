from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from .views import login_page


class LoginPageTest(TestCase):

    def test_root_url_resolves_to_the_login_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, login_page)

    def test_root_url_page_returns_correct_html(self):
        request = HttpRequest()
        response = login_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>LincolnHack 2016</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))