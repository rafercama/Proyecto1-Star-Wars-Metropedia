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
        planets = []
        for planet in data['results']:
            planet_response = requests.get(planet['url'])
            if planet_response.status_code == 200:
                planet_details = planet_response.json()['result']['properties']
                planets.append(planet_details)
        return planets
    return []

def get_character(char_id):
    response = requests.get(f"{BASE_URL}/people/{char_id}")
    if response.status_code == 200:
        return response.json()["result"]["properties"]
    return {}

def get_all_films():
    response = requests.get(f"{BASE_URL}/films")
    if response.status_code == 200:
        return response.json()["result"]
    return []

def get_planet_name2(planet_id):
    response = requests.get(f"{BASE_URL}/planets/{planet_id}")
    if response.status_code == 200:
        return response.json()["result"]["properties"]["name"]
    return "Desconocido"


def get_planet_name1(planet_id):
    if not planet_id:
        return "Unknown"
    response = requests.get(planet_id)
    if response.status_code == 200:
        return response.json()['result']['properties']['name']
    return "Unknown"


def get_character_name(character_url):
    response = requests.get(character_url)
    if response.status_code == 200:
        return response.json()['result']['properties']['name']
    return "Unknown"

def obtener_especies():
    url = 'https://www.swapi.tech/api/species'
    species_dict = {}
    while url:
        response = requests.get(url)
        data = response.json()
        for species in data['results']:
            species_detail_response = requests.get(species['url'])
            species_detail_data = species_detail_response.json()
            especie = species_detail_data['result']['properties']
            for person_url in especie['people']:
                species_dict[person_url] = especie['name']
        url = data['next']
    return species_dict


def obtener_nombres(urls):
    nombres = []
    for url in urls:
        response = requests.get(url)
        data = response.json()
        nombres.append(data['result']['properties']['name'])
    return nombres

def obtener_peliculas():
    url = 'https://www.swapi.tech/api/films'
    response = requests.get(url)
    data = response.json()
    peliculas = {}
    for film in data['result']:
        for character_url in film['properties']['characters']:
            if character_url not in peliculas:
                peliculas[character_url] = []
            peliculas[character_url].append(film['properties']['title'])
    return peliculas

def obtener_planeta(url):
    response = requests.get(url)
    planeta_data = response.json()
    return planeta_data['result']['properties']['name']


def search_character(cadena):
    url = 'https://www.swapi.tech/api/people'
    response = requests.get(url)
    data = response.json()
    personajes = data['results']

    # species_dict = obtener_especies()
    peliculas_dict = obtener_peliculas()

    resultados = [p for p in personajes if cadena.lower() in p['name'].lower()]
    if not resultados:
        print(f"No se encontraron personajes con el nombre '{cadena}'.")
        return

    for personaje in resultados:
        detalle_response = requests.get(personaje['url'])
        detalle_data = detalle_response.json()
        propiedades = detalle_data['result']['properties']

        nombre_planeta = obtener_planeta(propiedades['homeworld'])
        peliculas = peliculas_dict.get(personaje['url'], [])

        # nombre_especie = species_dict.get(personaje['url'], "Unknown")
        
        # naves = obtener_nombres(propiedades.get('starships', []))
        # vehiculos = obtener_nombres(propiedades.get('vehicles', []))

        print(f"Nombre: {propiedades['name']}")
        print(f"Planeta de origen: {nombre_planeta}")
        print(f"Títulos de episodios: {', '.join(peliculas) if peliculas else 'No se encontraron películas'}")
        print(f"Género: {propiedades['gender']}")
        # print(f"Especie: {nombre_especie}")
        # print(f"Naves: {', '.join(naves) if naves else 'No se encontraron naves estelares'}")
        # print(f"Vehículos: {', '.join(vehiculos) if vehiculos else 'No se encontraron vehículos'}")
        print("-" * 50)