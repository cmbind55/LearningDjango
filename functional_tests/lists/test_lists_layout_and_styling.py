from .lists_base import FunctionalTest


class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Edith goes to the home page
        lists_server_url = '%s%s' % (self.server_url, '/lists')
        self.browser.get(lists_server_url)
        self.browser.set_window_size(800, 600)

        # She notices the input box is nicely centered
        inputbox = get_item_input_box(self)
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            400,
            delta=5
        )
