from django.test import TestCase
from django.core.urlresolvers import resolve

from .views import login_page


class LoginPageTest(TestCase):

    def test_root_url_resolves_to_the_login_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, login_page)
