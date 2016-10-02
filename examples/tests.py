from os.path import isfile, join
from datetime import date
from django.contrib.staticfiles import finders
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase

from examples.views import home_page
from histoslide_example.settings import STATIC_URL
from histoslide.models import Slide

# Create your tests here.

class HomePageTest(TestCase):

    def addTestSlide(self):
        slide = Slide(Name = 'Test 1000 x 1000', ScannedBy = '', ScannedDate = date.today(), InsertedBy = '', InsertedDate = date.today(), SlideType = 2, UrlPath = 'static/slides/test1000x1000.jpg')
        slide.save()

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>histoslide example</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))

    def test_histoslide_js_is_available(self):
        abs_path = finders.find('histoslide/js/openseadragon.min.js')
        self.assertTrue(isfile(abs_path))

    def test_home_page_loads_openseadragon_js_from_histoslide(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn(join(STATIC_URL,'histoslide/js/openseadragon.min.js'), response.content)

    def test_home_page_loads_image(self):
        self.addTestSlide()
        slide = Slide.objects.get(pk=1)
        self.assertEqual('Test 1000 x 1000', slide.Name)


