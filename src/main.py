from core.webscraper import WebScraper
import json
from tqdm import tqdm
import threading
import os

pokemon_list = []

def write_to_json(dir, data):
    with open(dir, 'a') as pd:
        pd.write(json.dumps(data))
        pd.write(",\n")
        pd.close()

def get_pokemon_id(pokemon_ref):
    result = pokemon_ref.find('#')
    return pokemon_ref[result:]

def get_pokemon_name(pokemon_ref):
    result = pokemon_ref.find('#')
    return pokemon_ref[:result]

def get_pokemon(start_it, end_it, starting_page):
    web_scraper = WebScraper(starting_page)

    for x in tqdm(range(start_it, end_it)):
        pokemon_ref = web_scraper.web_scrape('div', {'class' : 'pokedex-pokemon-pagination-title'})
        pokemon_ref = "".join([line.strip() for line in pokemon_ref.text.split("\n")])

        pokemon_description = web_scraper.web_scrape('p', {'class' : 'version-y active'})
        pokemon_description = "".join([line.strip() for line in pokemon_description.text.split("\n")])

        pokemon_list.append({'id': get_pokemon_id(pokemon_ref),
                             'name' : get_pokemon_name(pokemon_ref),
                             'description' : pokemon_description})
        web_scraper.change_page(web_scraper.web_scrape('a', {'class' : 'next'}).get('href'))

def create_pokedex():
    t1 = threading.Thread(target=get_pokemon, args=(0, 404, '/uk/pokedex/bulbasaur'))
    t2 = threading.Thread(target=get_pokemon, args=(0, 403, '/uk/pokedex/luxray'))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    with open('src/core/pokedex.json', 'a') as pd:
        pd.write(json.dumps(pokemon_list))

def find_pokemon():
    search_id = input("Input pokemon id: ")
    pokedex = json.loads(open("src/core/pokedex.json").read())
    for i in pokedex:
        if i['id'] == search_id:
            print(i['name'] + i['id'])
            print(i['description'])
            return

    print("Pokemon with that 'id' does not exist.")



def main():
    if not os.path.exists("src/core/pokedex.json"):
        print("Fetching data...")
        create_pokedex()
        print("Finished.")

    find_pokemon()    

main()