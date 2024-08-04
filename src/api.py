import requests

BASE_URL = "https://www.swapi.tech/api"

def get_movies():
    response = requests.get(f"{BASE_URL}/films")
    if response.status_code == 200:
        return response.json()["result"]
    return []

def get_species_list():
    response = requests.get(f"{BASE_URL}/species")
    if response.status_code == 200:
        return response.json()["results"]
    return []

def get_species_details(species_url):
    response = requests.get(species_url)
    if response.status_code == 200:
        return response.json()['result']
    return {}

def get_planets():
    response = requests.get(f"{BASE_URL}/planets")
    if response.status_code == 200:
        data = response.json()
        if 'results' in data:
            planets = []
            for planet in data['results']:
                planet_response = requests.get(planet['url'])
                if planet_response.status_code == 200:
                    planet_details = planet_response.json()['result']
                    planets.append(planet_details['properties'])
            return planets
    return []

def get_character(char_id):
    response = requests.get(f"{BASE_URL}/people/{char_id}")
    if response.status_code == 200:
        return response.json()["result"]["properties"]
    return {}

def get_film(film_id):
    response = requests.get(f"{BASE_URL}/films/{film_id}")
    if response.status_code == 200:
        return response.json()["result"]["properties"]
    return {}

def get_planet_name(planet_url):
    if not planet_url:
        return "Unknown"
    response = requests.get(planet_url)
    if response.status_code == 200:
        return response.json()['result']['properties']['name']
    return "Unknown"

def get_character_name(character_url):
    response = requests.get(character_url)
    if response.status_code == 200:
        return response.json()['result']['properties']['name']
    return "Unknown"

def get_species_name(species_id):
    if not species_id:
        return "Unknown"
    response = requests.get(f"{BASE_URL}/species/{species_id}")
    if response.status_code == 200:
        return response.json()["result"]["properties"]["name"]
    return "Unknown"

def get_vehicle(vehicle_id):
    response = requests.get(f"{BASE_URL}/vehicles/{vehicle_id}")
    if response.status_code == 200:
        return response.json()["result"]["properties"]["name"]
    return "Unknown"

def get_starship(starship_id):
    response = requests.get(f"{BASE_URL}/starships/{starship_id}")
    if response.status_code == 200:
        return response.json()["result"]["properties"]["name"]
    return "Unknown"

def get_character_info(character_url):
    response = requests.get(character_url)
    if response.status_code == 200:
        return response.json().get('result', {}).get('properties', {})
    return {}

def search_character(query):
    """Buscar personaje por una cadena de caracteres."""
    response = requests.get(f"{BASE_URL}/people/?name={query}")
    if response.status_code == 200:
        characters = response.json()["result"]
        
        if not characters:
            print(f"No se encontraron personajes que coincidan con '{query}'")
            return

        for char in characters:
            character = char["properties"]
            print(f"Nombre: {character['name']}")
            print(f"Planeta de origen: {get_planet_name(character['homeworld'])}")

            # Obtener información adicional del personaje
            character_info = get_character_info(character['url'])

            print("Aparece en:")
            if 'films' in character_info:
                for film_url in character_info['films']:
                    film_id = film_url.split('/')[-1]
                    film = get_film(film_id)
                    print(f"  - {film.get('title', 'Desconocido')}")
            else:
                print("  - No se encontraron películas")

            print(f"Género: {character_info.get('gender', 'Desconocido')}")
            species_name = get_species_name(character_info.get('species', [None])[0])
            print(f"Especie: {species_name}")

            print("Vehículos:")
            if 'vehicles' in character_info:
                for vehicle_url in character_info['vehicles']:
                    vehicle_id = vehicle_url.split('/')[-1]
                    vehicle = get_vehicle(vehicle_id)
                    print(f"  - {vehicle}")
            else:
                print("  - No se encontraron vehículos")

            print("Naves estelares:")
            if 'starships' in character_info:
                for starship_url in character_info['starships']:
                    starship_id = starship_url.split('/')[-1]
                    starship = get_starship(starship_id)
                    print(f"  - {starship}")
            else:
                print("  - No se encontraron naves estelares")
            print()