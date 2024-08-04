import requests
from src.api import get_movies,get_character_name,search_character, get_planets,get_species_list,get_species_details, get_character, get_film, get_planet_name
from src.models import Film, Species, Planet, Character

def list_movies():
    """Lista de películas de la saga."""
    peliculas = get_movies()
    for pelicula in peliculas:
        film = Film(
            title=pelicula['properties']['title'],
            episode_id=pelicula['properties']['episode_id'],
            release_date=pelicula['properties']['release_date'],
            opening_crawl=pelicula['properties']['opening_crawl'],
            director=pelicula['properties']['director']
        )
        print(f"Título: {film.title}")
        print(f"Episodio: {film.episode_id}")
        print(f"Fecha de lanzamiento: {film.release_date}")
        print(f"Texto inicial: {film.opening_crawl}")
        print(f"Director: {film.director}")
        print()

def list_species():
    """Lista de especies de la saga."""
    especies_list = get_species_list()
    datos_peliculas = requests.get('https://www.swapi.tech/api/films').json()['result']

    for especie in especies_list:
        detalles_especie = get_species_details(especie['url'])
        propiedades = detalles_especie.get('properties', {})

        especie_instance = Species(
            name=propiedades.get('name', 'Desconocida'),
            height=propiedades.get('average_height', 'Desconocido'),
            classification=propiedades.get('classification', 'Desconocido'),
            homeworld=get_planet_name(propiedades.get('homeworld', '')),
            language=propiedades.get('language', 'Desconocido'),
            characters=[get_character_name(url) for url in propiedades.get('people', [])],
            films=[pelicula['properties']['title'] for pelicula in datos_peliculas if especie['url'] in pelicula['properties']['species']]
        )

        print(f"Nombre: {especie_instance.name}")
        print(f"Altura: {especie_instance.height}")
        print(f"Clasificación: {especie_instance.classification}")
        print(f"Planeta de origen: {especie_instance.homeworld}")
        print(f"Idioma: {especie_instance.language}")
        
        print("Personajes:")
        for nombre in especie_instance.characters:
            print(f"  - {nombre}")

        print("Aparece en:")
        for titulo in especie_instance.films:
            print(f"  - {titulo}")

        print()

def list_planets():
    """Lista de planetas de la saga."""
    planetas = get_planets()
    for planet_data in planetas:
        films = []
        characters = []

        if 'films' in planet_data:
            for film_url in planet_data['films']:
                film_id = film_url.split('/')[-1]
                pelicula = get_film(film_id)
                films.append(pelicula.get('title', 'Desconocida'))
        
        if 'residents' in planet_data:
            for resident_url in planet_data['residents']:
                resident_id = resident_url.split('/')[-1]
                personaje = get_character(resident_id)
                characters.append(personaje.get('name', 'Desconocido'))
        
        planet = Planet(
            name=planet_data.get('name', 'Desconocido'),
            orbital_period=planet_data.get('orbital_period', 'Desconocido'),
            rotation_period=planet_data.get('rotation_period', 'Desconocido'),
            population=planet_data.get('population', 'Desconocido'),
            climate=planet_data.get('climate', 'Desconocido'),
            films=films,
            characters=characters
        )

        print(f"Nombre: {planet.name}")
        print(f"Período Orbital: {planet.orbital_period}")
        print(f"Período de Rotación: {planet.rotation_period}")
        print(f"Población: {planet.population}")
        print(f"Clima: {planet.climate}")
        print(f"Terreno: {planet_data.get('terrain', 'Desconocido')}")
        print(f"Agua Superficial: {planet_data.get('surface_water', 'Desconocido')}")
        
        print("Aparece en:")
        if planet.films:
            for film in planet.films:
                print(f"  - {film}")
        else:
            print("  - No se encontraron películas")
        
        print("Residentes:")
        if planet.characters:
            for character in planet.characters:
                print(f"  - {character}")
        else:
            print("  - No se encontraron residentes")
        
        print()

def display_menu():
        while True:
            print("===== Menú Principal =====")
            print("1. Lista de Películas")
            print("2. Lista de Especies")
            print("3. Lista de Planetas")
            print("4. Buscar Personaje")
            print("5. Salir")
            
            option = input("Elige una opción (1-5): ")
            
            if option == "1":
                print("\nLista de Películas:")
                list_movies()
            elif option == "2":
                print("\nLista de Especies:")
                list_species()
            elif option == "3":
                print("\nLista de Planetas:")
                list_planets()
            elif option == "4":
                search_query = input("Introduce el nombre del personaje a buscar: ")
                search_character(search_query)
            elif option == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida. Por favor, elige una opción entre 1 y 5.")
            
            print("\n")


if __name__ == "__main__":
    display_menu()