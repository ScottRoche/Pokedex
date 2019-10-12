from core.webscraper import WebScraper
import json

def write_to_json(dir, data):
    with open(dir, 'a') as pd:
        pd.write(json.dumps(data))
        pd.write(",\n")
        pd.close()

def main():
    web_scraper = WebScraper('/uk/pokedex/bulbasaur')

    for x in range(10):
        print(x)
        result = web_scraper.web_scrape('div', {'class' : 'pokedex-pokemon-pagination-title'})
        result = "".join([line.strip() for line in result.text.split("\n")])
        write_to_json('src/core/pokedex.json', {'name' : result})
        web_scraper.change_page(web_scraper.web_scrape('a', {'class' : 'next'}).get('href'))

main()