import requests

# URL base para la API SWAPI (Star Wars API)
BASE_URL = "https://www.swapi.tech/api"

def get_movies():
    """
    Obtiene una lista de todas las películas disponibles en la API SWAPI.
    
    Returns:
        list: Una lista de diccionarios con la información de cada película si la solicitud fue exitosa,
              de lo contrario, devuelve una lista vacía.
    """
    response = requests.get(f"{BASE_URL}/films")
    if response.status_code == 200:
        return response.json()["result"]
    return []

def get_species_list():
    """
    Obtiene una lista de todas las especies disponibles en la API SWAPI.
    
    Returns:
        list: Una lista de diccionarios con la información de cada especie si la solicitud fue exitosa,
              de lo contrario, devuelve una lista vacía.
    """
    response = requests.get(f"{BASE_URL}/species")
    if response.status_code == 200:
        return response.json()["results"]
    return []

def get_species_details(species_url):
    """
    Obtiene los detalles de una especie específica usando su URL en la API SWAPI.
    
    Args:
        species_url (str): La URL de la especie en la API SWAPI.
    
    Returns:
        dict: Un diccionario con los detalles de la especie si la solicitud fue exitosa,
              de lo contrario, devuelve un diccionario vacío.
    """
    response = requests.get(species_url)
    if response.status_code == 200:
        return response.json()['result']
    return {}


def get_planets():
    """
    Obtiene una lista de todos los planetas disponibles en la API SWAPI y sus detalles.
    
    Returns:
        list: Una lista de diccionarios con los detalles de cada planeta si la solicitud fue exitosa,
              de lo contrario, devuelve una lista vacía.
    """
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
    """
    Obtiene los detalles de un personaje específico usando su ID en la API SWAPI.
    
    Args:
        char_id (str): El ID del personaje en la API SWAPI.
    
    Returns:
        dict: Un diccionario con los detalles del personaje si la solicitud fue exitosa,
              de lo contrario, devuelve un diccionario vacío.
    """
    response = requests.get(f"{BASE_URL}/people/{char_id}")
    if response.status_code == 200:
        return response.json()["result"]["properties"]
    return {}

def get_all_films():
    """
    Obtiene una lista de todas las películas disponibles en la API SWAPI.
    
    Returns:
        list: Una lista de diccionarios con la información de cada película si la solicitud fue exitosa,
              de lo contrario, devuelve una lista vacía.
    """
    response = requests.get(f"{BASE_URL}/films")
    if response.status_code == 200:
        return response.json()["result"]
    return []


def get_planet_name2(planet_id):
    """
    Obtiene el nombre de un planeta usando su ID en la API SWAPI.
    
    Args:
        planet_id (str): El ID del planeta en la API SWAPI.
    
    Returns:
        str: El nombre del planeta si la solicitud fue exitosa,
             de lo contrario, devuelve "Desconocido".
    """
    response = requests.get(f"{BASE_URL}/planets/{planet_id}")
    if response.status_code == 200:
        return response.json()["result"]["properties"]["name"]
    return "Desconocido"

def get_planet_name1(planet_id):
    """
    Obtiene el nombre de un planeta usando su URL en la API SWAPI.
    
    Args:
        planet_id (str): La URL del planeta en la API SWAPI.
    
    Returns:
        str: El nombre del planeta si la solicitud fue exitosa,
             de lo contrario, devuelve "Unknown".
    """
    if not planet_id:
        return "Unknown"
    response = requests.get(planet_id)
    if response.status_code == 200:
        return response.json()['result']['properties']['name']
    return "Unknown"

def get_character_name(character_url):
    """
    Obtiene el nombre de un personaje usando su URL en la API SWAPI.
    
    Args:
        character_url (str): La URL del personaje en la API SWAPI.
    
    Returns:
        str: El nombre del personaje si la solicitud fue exitosa,
             de lo contrario, devuelve "Unknown".
    """
    response = requests.get(character_url)
    if response.status_code == 200:
        return response.json()['result']['properties']['name']
    return "Unknown"

def obtener_especies():
    """
    Obtiene un diccionario con la relación entre personajes y sus especies correspondientes.
    
    Returns:
        dict: Un diccionario donde las claves son URLs de personajes y los valores son nombres de especies.
    """
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
    """
    Obtiene una lista de nombres a partir de una lista de URLs de recursos en la API SWAPI.
    
    Args:
        urls (list): Una lista de URLs de recursos en la API SWAPI.
    
    Returns:
        list: Una lista de nombres obtenidos de los recursos correspondientes en las URLs.
    """
    nombres = []
    for url in urls:
        response = requests.get(url)
        data = response.json()
        nombres.append(data['result']['properties']['name'])
    return nombres

def obtener_peliculas():
    """
    Obtiene un diccionario con la relación entre personajes y las películas en las que aparecen.
    
    Returns:
        dict: Un diccionario donde las claves son URLs de personajes y los valores son listas de títulos de películas.
    """
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
    """
    Obtiene el nombre de un planeta a partir de su URL en la API SWAPI.
    
    Args:
        url (str): La URL del planeta en la API SWAPI.
    
    Returns:
        str: El nombre del planeta si la solicitud fue exitosa.
    """
    response = requests.get(url)
    planeta_data = response.json()
    return planeta_data['result']['properties']['name']


def search_character(cadena):
    """
    Busca y muestra información detallada sobre personajes cuyo nombre coincida con la cadena proporcionada.

    Args:
        cadena (str): La cadena de texto a buscar en los nombres de los personajes.

    Comportamiento:
        - La función realiza una solicitud a la API SWAPI para obtener una lista de todos los personajes.
        - Filtra los personajes cuyos nombres contengan la cadena proporcionada, sin importar mayúsculas o minúsculas.
        - Para cada personaje encontrado, se obtiene su información detallada, incluyendo:
            - Nombre del personaje.
            - Nombre del planeta de origen.
            - Lista de películas en las que aparece.
            - Género del personaje.
            - (Comentado) Especie del personaje.
            - (Comentado) Naves asociadas al personaje.
            - (Comentado) Vehículos asociados al personaje.
        - Si no se encuentran personajes que coincidan con la cadena, se notifica al usuario.

    Ejemplo de uso:
        search_character("Luke")
        # Este ejemplo buscará y mostrará información sobre todos los personajes cuyos nombres contengan "Luke".
    """
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