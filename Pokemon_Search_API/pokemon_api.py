import requests
import os
from sys import platform

# Function for clearing the console
def clear() -> None:
    """
    Clearing the console
    """
        # clearing console
    if platform == 'win32':
        os.system('cls')
    elif platform == 'linux' or platform == 'linux2':
        os.system('clear')

# loop for repetition
while True:
    print("Welcome to the pokemon name search data base.")
    pokemon_name = input("Which pokemon do you want to learn about (name) or\
 'q' to quit? ")
    if pokemon_name.lower() == 'q': # to exit the search
        break

    clear() # clear the console
    pokemon_name = pokemon_name.strip()

    # making an API request
    req = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        )
    if req.status_code == 200: # successful api request
        requested_pokemon = req.json()
        # processing the data 
        requested_pokemon_name = requested_pokemon['name'] if \
            requested_pokemon['name'] else 'NoName'# string
        requested_pokemon_abilities = [] # list of strings
        for ability in requested_pokemon['abilities']:
            requested_pokemon_abilities.append(ability['ability']['name'])
        if not requested_pokemon_abilities:
            requested_pokemon_abilities.append("NoAbilities")
        requested_pokemon_species = requested_pokemon['species']['name'] if \
            requested_pokemon['species']['name'] else 'NoName'
        requested_pokemon_weight = requested_pokemon['weight'] if \
            requested_pokemon['weight'] else 'NoWeight'
        requested_pokemon_moves = []
        for move in requested_pokemon['moves']:
            requested_pokemon_moves.append(move['move']['name'])
        if not requested_pokemon_moves:
            requested_pokemon_moves.append("NoMoves")

        pokemon_info_dashboard = """
        You were searching for : {pk_name}
        !! Database found a match with the folowing data !!
        Name: {api_pk_name}
        Has following abilities: {api_pk_abilities}
        Species: {api_species}
        Has folowing moves: {api_moves}
        Weight: {api_weight}
        """.format(pk_name=pokemon_name, api_pk_name=requested_pokemon_name, \
            api_pk_abilities = ', '.join(requested_pokemon_abilities), \
                api_species = requested_pokemon_species, \
                    api_weight = requested_pokemon_weight, \
                        api_moves = ', '.join(requested_pokemon_moves))

        print(pokemon_info_dashboard)

    else: # API request failed
        print("Name: {} dosen't exists in our database".format(pokemon_name))
        print("Server responded with an Error: {}".format(req.status_code))
        print("Try again !")