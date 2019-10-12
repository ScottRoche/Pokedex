import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

class WebScraper:

    def __init__(self, starting_url):
        self.starting_url = starting_url

    def web_scrape(self, name, attrs):
        uClient = urlopen(self.starting_url)
        page_html = uClient.read()
        uClient.close()
        
        ## HTML parsing.
        page_soup = soup(page_html, "html.parser")
        results = page_soup.find(name, attrs)
        pokemon = "".join([line.strip() for line in results.text.split("\n")])
        return {'name' : pokemon}