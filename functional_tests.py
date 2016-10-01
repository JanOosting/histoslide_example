from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_view_the_first_image(self):
        # Check out the examples homepage
        self.browser.get('http://localhost:8000')
        # The title contains 'histoslide example'
        self.assertIn('histoslide example', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('histoslide example', header_text)
        # The page shows the first slide on the site
        openseadragon_panes = self.browser.find_elements_by_class_name('openseadragon-container')
        self.assertEqual(1, len(openseadragon_panes))
        # The page shows thumbnails of all slides on the site

        # Clicking on a thumbnail shows the slide

        # Slides can be shown either by Openseadragon or by Google Maps API

if __name__ == '__main__':
    unittest.main()