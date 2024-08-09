class Film:
    def _init_(self, title, episode_id, release_date, opening_crawl, director):
        self.title = title
        self.episode_id = episode_id
        self.release_date = release_date
        self.opening_crawl = opening_crawl
        self.director = director

class Species:
    def _init_(self, name, height, classification, homeworld, language, characters, films):
        self.name = name
        self.height = height
        self.classification = classification
        self.homeworld = homeworld
        self.language = language
        self.characters = characters
        self.films = films

class Planet:
    def _init_(self, name, orbital_period, rotation_period, population, climate, films, characters):
        self.name = name
        self.orbital_period = orbital_period
        self.rotation_period = rotation_period
        self.population = population
        self.climate = climate
        self.films = films
        self.characters = characters

class Character:
    def _init_(self, name, homeworld, films, gender, species, vehicles, starships):
        self.name = name
        self.homeworld = homeworld
        self.films = films
        self.gender = gender
        self.species = species
        self.vehicles = vehicles
        self.starships = starships


class Starship:
    def _init_(self, id, name, model, manufacturer, cost_in_credits, length, max_atmosphering_speed, crew, passengers, cargo_capacity, consumables, hyperdrive_rating, MGLT, starship_class, pilots, films):
        self.id = id
        self.name = name
        self.model = model
        self.manufacturer = manufacturer
        self.cost_in_credits = cost_in_credits
        self.length = length
        self.max_atmosphering_speed = max_atmosphering_speed
        self.crew = crew
        self.passengers = passengers
        self.cargo_capacity = cargo_capacity
        self.consumables = consumables
        self.hyperdrive_rating = hyperdrive_rating
        self.MGLT = MGLT
        self.starship_class = starship_class
        self.pilots = pilots
        self.films = films


class Mission:
    def _init_(self, name, destination, starship, weapons, team):
        self.name = name
        self.destination = destination
        self.starship = starship
        self.weapons = weapons
        self.team = team

    def _str_(self):
        return (f"Nombre de la mision: {self.name}\n"
                f"Destino: {self.destination}\n"
                f"Nave: {self.starship}\n"
                f"Armas: {', '.join(self.weapons)}\n"
                f"Equipo: {', '.join(self.team)}")
