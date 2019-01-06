#!python

from marionette_driver.marionette import Marionette
from pages import InformationPage
from marionette_driver import Wait
from marionette_driver import expected

def get_first_url():
    urls = open("urls.txt", "r")
    url = urls.readline()
    return url.strip()

def navigate(url):
    client = Marionette(host='localhost', port=2828)
    client.start_session()
    client.navigate(url)
    start_page = InformationPage(client)
    exhibitor_page = start_page.navigate_to_page("Exhibitors")
    exhibitor_widget = exhibitor_page.get_exhibitor_widget()
    exhibitors = exhibitor_widget.get_exhibitors()
    for exhibitor in exhibitors:
        print exhibitor



if __name__ == "__main__":
    navigate(get_first_url())


