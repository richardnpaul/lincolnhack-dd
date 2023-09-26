# Django Imports
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase

# Local Imports
from .views import login_page


class LoginPageTest(TestCase):
    def test_root_url_resolves_to_the_login_page_view(self):
        found = resolve("/")
        self.assertEqual(found.func, login_page)

    def test_root_url_page_returns_correct_html(self):
        request = HttpRequest()
        response = login_page(request)
        expected_html = render_to_string("login_page.html")
        self.assertEqual(response.content.decode(), expected_html)
