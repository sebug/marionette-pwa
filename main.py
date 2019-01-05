#!python

from marionette_driver.marionette import Marionette

def get_first_url():
    urls = open("urls.txt", "r")
    url = urls.readline()
    return url.strip()

def navigate(url):
    client = Marionette(host='localhost', port=2828)
    client.start_session()
    client.navigate(url)
    print url


if __name__ == "__main__":
    navigate(get_first_url())


