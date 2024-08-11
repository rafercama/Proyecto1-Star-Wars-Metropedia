from src.api import get_movies,get_character_name,search_character, get_planets,get_species_list,get_species_details, get_character, get_all_films, get_planet_name1, get_planet_name2
from src.models import Film, Species, Planet
from src.data_processing import generar_grafico_personajes_por_planeta, StarshipVisualizer
from src.utils import mostrar_menu_graficos_naves, gestion_misiones
from src.mission_manager import MissionManager

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
        print("-" * 50)

def list_species():
    """Lista de especies de la saga."""
    print("Buscando datos, por favor espere...")
    print("-" * 50)
    especies_list = get_species_list()
    datos_peliculas = get_movies()

    for especie in especies_list:
        detalles_especie = get_species_details(especie['url'])
        propiedades = detalles_especie.get('properties', {})

        especie_instance = Species(
            name=propiedades.get('name', 'Desconocida'),
            height=propiedades.get('average_height', 'Desconocido'),
            classification=propiedades.get('classification', 'Desconocido'),
            homeworld=get_planet_name1(propiedades.get('homeworld', '')),
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

        print("-" * 50)


def list_planets():
    """Lista de planetas de la saga."""
    print("Buscando datos, por favor espere...")
    print("-" * 50)
    planetas = get_planets()

    """Lista de planetas y su relación con películas y personajes."""
    # planets_dict = {}
    # characters_dict = {}

    # Obtener todas las películas
    # films = get_all_films()

    # for film in films:
    #     film_title = film['properties']['title']
    #     film_planets = film['properties']['planets']
    #     # Relacionar planetas con películas
    #     for planet_url in film_planets:
    #         planet_id = planet_url.split('/')[-1]
    #         if planet_id not in planets_dict:
    #             planets_dict[planet_id] = {
    #                 'name': get_planet_name2(planet_id),
    #                 'films': [],
    #                 'characters': []
    #             }
    #         planets_dict[planet_id]['films'].append(film_title)

    # Iterar sobre la lista de planetas obtenidos
    for planet_data in planetas:
        films = []
        characters = []
        
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

        print("-" * 50)
        # if planet_id in planets_dict:
        #     print("  Aparece en los episodios:")
        #     for film in planets_dict[planet_id]['films']:
        #         print(f"    - {film}")

        # print()





def display_menu():
    mission_manager = MissionManager()

    while True:
        print("===== Menú Principal =====")
        print("1. Lista de Películas")
        print("2. Lista de Especies")
        print("3. Lista de Planetas")
        print("4. Buscar Personaje")
        print("5. Mostrar Gráfico de Personajes por Planeta")
        print("6. Gráficos de Naves")
        print("7. Mostrar estadísticas de Naves")
        print("8. Gestión de Misiones")
        print("9. Salir")
        
        option = input("Elige una opción (1-9): ")
        
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
             while True:
                    search_query = input("Introduce el nombre del personaje a buscar: ").strip()
                    print("Buscando datos, por favor espere...")
                    print("-" * 50)
                    if not search_query:
                        print("El nombre del personaje no puede estar vacío. Intente nuevamente.")
                    else:
                        search_character(search_query)
                        break
        elif option == "5":
            print("\nGenerando gráfico de personajes por planeta...")
            generar_grafico_personajes_por_planeta()
        elif option == "6":
            mostrar_menu_graficos_naves()
        elif option == "7":
            StarshipVisualizer.mostrar_estadisticas()
        elif option == "8":
            gestion_misiones(mission_manager)
        elif option == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 9.")
        
        print("\n")


if __name__ == "__main__":
    display_menu()
