from django.core.urlresolvers import resolve
from django.template.loader import render_to_string
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest

# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/lists/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        #expected_html = render_to_string('lists/home.html')
        #self.assertTrue(response.content.startswith(b'<html>'),msg='ACTUAL CONTENT: {}'.format(response.content))
        self.assertIn(b'<title>', response.content)
        #self.assertTrue(response.content.endswith(b'</html>'))

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)

        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string(
            'lists/index.html',
            {'new_item_text':  'A new list item',
             'page_title': 'To-Do',}
        )
        self.assertEqual(response.content.decode(), expected_html)