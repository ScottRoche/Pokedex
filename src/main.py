from core.webscraper import WebScraper
import json
from tqdm import tqdm
import threading

pokemon_list = []

def write_to_json(dir, data):
    with open(dir, 'a') as pd:
        pd.write(json.dumps(data))
        pd.write(",\n")
        pd.close()

def get_pokemon(start_it, end_it):
    web_scraper = WebScraper('/uk/pokedex/bulbasaur')

    for x in tqdm(range(start_it, end_it)):
        pokemon_name = web_scraper.web_scrape('div', {'class' : 'pokedex-pokemon-pagination-title'})
        pokemon_name = "".join([line.strip() for line in pokemon_name.text.split("\n")])

        pokemon_description = web_scraper.web_scrape('p', {'class' : 'version-y active'})
        pokemon_description = "".join([line.strip() for line in pokemon_description.text.split("\n")])

        pokemon_list.append({'name' : pokemon_name, 'description' : pokemon_description})
        web_scraper.change_page(web_scraper.web_scrape('a', {'class' : 'next'}).get('href'))

def main():
    t1 = threading.Thread(target=get_pokemon, args=(0, 404))
    t2 = threading.Thread(target=get_pokemon, args=(405, 808))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    with open('src/core/pokedex.json', 'w') as pd:
        pd.write(json.dumps(pokemon_list))

main()