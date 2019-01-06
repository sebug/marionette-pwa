#!python
from marionette_driver import By

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
        items = self.client.find_elements(By.CSS_SELECTOR, ".menu a.item")
        for item in items:
            if item.text == title:
                item.click()
                return InformationPage(self.client)
