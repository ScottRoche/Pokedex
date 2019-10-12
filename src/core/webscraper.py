import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

class WebScraper:

    def __init__(self, page_url):
        self.page_url = 'https://www.pokemon.com' + page_url

    ## Changes the page url
    def change_page(self, page_url):
        self.page_url = 'https://www.pokemon.com' + page_url

    ## Returns the HTML code
    def web_scrape(self, name, attrs):
        uClient = urlopen(self.page_url)
        page_html = uClient.read()
        uClient.close()

        ## Parse HTML
        page_soup = soup(page_html, "html.parser")
        result = page_soup.find(name, attrs)
        return result