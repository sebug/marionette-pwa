#!python

from marionette_driver.marionette import Marionette
from pages import InformationPage

def get_first_url():
    urls = open("urls.txt", "r")
    url = urls.readline()
    return url.strip()

def navigate(url):
    client = Marionette(host='localhost', port=2828)
    client.start_session()
    client.navigate(url)
    start_page = InformationPage(client)
    start_page.print_menu_items()



if __name__ == "__main__":
    navigate(get_first_url())


