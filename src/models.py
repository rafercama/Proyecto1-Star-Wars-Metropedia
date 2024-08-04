class Film:
    def __init__(self, title, episode_id, release_date, opening_crawl, director):
        self.title = title
        self.episode_id = episode_id
        self.release_date = release_date
        self.opening_crawl = opening_crawl
        self.director = director

class Species:
    def __init__(self, name, height, classification, homeworld, language, characters, films):
        self.name = name
        self.height = height
        self.classification = classification
        self.homeworld = homeworld
        self.language = language
        self.characters = characters
        self.films = films

class Planet:
    def __init__(self, name, orbital_period, rotation_period, population, climate, films, characters):
        self.name = name
        self.orbital_period = orbital_period
        self.rotation_period = rotation_period
        self.population = population
        self.climate = climate
        self.films = films
        self.characters = characters

class Character:
    def __init__(self, name, homeworld, films, gender, species, vehicles, starships):
        self.name = name
        self.homeworld = homeworld
        self.films = films
        self.gender = gender
        self.species = species
        self.vehicles = vehicles
        self.starships = starships
