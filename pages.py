#!python
from marionette_driver import By
from marionette_driver import Wait
from marionette_driver import expected

class InformationPage:
    """A progressive information page, gives access to the components"""
    def __init__(self, client):
        self.client = client

    def print_menu_items(self):
        items = self.client.find_elements(By.CSS_SELECTOR, ".menu a.item")
        for item in items:
            if item.text:
                print item.text

    def navigate_to_page(self, title):
        Wait(self.client).until(expected.element_not_displayed('css selector', '.main-loader'))
        items = self.client.find_elements(By.CSS_SELECTOR, ".menu a.item")
        for item in items:
            if item.text == title:
                item.click()
                return InformationPage(self.client)

    def get_exhibitor_widget(self):
        # wait until the loader disappears
        Wait(self.client).until(expected.element_not_displayed('css selector', '.main-loader'))
        return ExhibitorWidget(self.client)


class ExhibitorWidget:
    """An exhibitor list"""
    def __init__(self, client):
        self.client = client

    def get_exhibitors(self):
        Wait(self.client).until(expected.element_present('css selector', 'informationpagepart-eventexhibitorslist a.header'))
        headers = self.client.find_elements(By.CSS_SELECTOR, "informationpagepart-eventexhibitorslist a.header")
        for header in headers:
            yield header.text

