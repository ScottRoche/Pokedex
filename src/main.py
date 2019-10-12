from core.webscraper import WebScraper
import json


def write_to_json(dir, data):
    with open(dir, 'w') as pd:
        json.dump(data, pd)

def main():
    web_scraper = WebScraper('https://www.pokemon.com/uk/pokedex/bulbasaur')
    data = web_scraper.web_scrape('div', {'class' : 'pokedex-pokemon-pagination-title'})
    write_to_json('src/core/pokedex.json', data)

main()