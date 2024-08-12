import pandas as pd
from src.models import Mission

class MissionManager:
    def __init__(self):
         # Inicializa la lista de misiones y carga los datos de armas y personajes desde archivos CSV.
        self.missions = []
        self.weapons_df = self.leer_armas_csv() # Carga los datos de armas en un DataFrame.
        self.characters_df = self.leer_personajes_csv() # Carga los datos de personajes en un DataFrame.

    def leer_armas_csv(self):
        # Lee el archivo CSV que contiene información sobre las armas y devuelve un DataFrame.
        ruta_csv = 'data/csv/weapons.csv'
        return pd.read_csv(ruta_csv)

    def leer_personajes_csv(self):
        # Lee el archivo CSV que contiene información sobre los personajes y devuelve un DataFrame.
        ruta_csv = 'data/csv/characters.csv'
        return pd.read_csv(ruta_csv)

    def mostrar_armas_disponibles(self):
        # Muestra la lista de armas disponibles con su ID y tipo.
        print("Armas disponibles:")
        for index, row in self.weapons_df.iterrows():
            print(f"{row['id']}. {row['name']} ({row['type']})")

    def mostrar_personajes_disponibles(self):
        # Muestra la lista de personajes disponibles con su ID, planeta de origen y especie.
        print("Personajes disponibles:")
        for index, row in self.characters_df.iterrows():
            print(f"{row['id']}. {row['name']} (Homeworld: {row['homeworld']}, Species: {row['species']})")

    def definir_mision(self):
        # Define una nueva misión con nombre, planeta destino, nave, armas y equipo.
        # Se valida que no haya más de 5 misiones definidas y que todos los campos sean válidos.
        if len(self.missions) >= 5:
            print("No se pueden definir más de 5 misiones.")
            return

        # Validación para el nombre de la misión
        while True:
            name = input("Nombre de la misión: ").strip()
            if not name:
                print("El nombre de la misión no puede estar vacío o contener solo espacios. Intente nuevamente.")
            else:
                break

        # Validación para el planeta destino
        while True:
            destination = input("Planeta destino: ").strip()
            if not destination:
                print("El planeta destino no puede estar vacío o contener solo espacios. Intente nuevamente.")
            else:
                break

        # Validación para la nave a utilizar
        while True:
            starship = input("Nave a utilizar: ").strip()
            if not starship:
                print("La nave a utilizar no puede estar vacía o contener solo espacios. Intente nuevamente.")
            else:
                break

        # Selección de armas (hasta 7)
        weapons = []
        self.mostrar_armas_disponibles()
        print("Selecciona hasta 7 armas ingresando el número correspondiente. Deja el campo vacío para terminar.")
        while len(weapons) < 7:
            weapon_id = input(f"Arma {len(weapons) + 1}: ").strip()
            if weapon_id == "":
                break
            if weapon_id.isdigit():
                weapon_id = int(weapon_id)
                if weapon_id in self.weapons_df['id'].values:
                    weapon_name = self.weapons_df.loc[self.weapons_df['id'] == weapon_id, 'name'].values[0]
                    if weapon_name not in weapons:
                        weapons.append(weapon_name)
                    else:
                        print("Esta arma ya está seleccionada.")
                else:
                    print("ID de arma no válida. Intente nuevamente.")
            else:
                print("Entrada no válida. Por favor, ingrese un número de ID válido.")

        # Selección de integrantes del equipo (hasta 7)
        team = []
        self.mostrar_personajes_disponibles()
        print("Selecciona hasta 7 integrantes del equipo ingresando el número correspondiente. Deja el campo vacío para terminar.")
        while len(team) < 7:
            member_id = input(f"Integrante {len(team) + 1}: ").strip()
            if member_id == "":
                break
            if member_id.isdigit():
                member_id = int(member_id)
                if member_id in self.characters_df['id'].values:
                    member_name = self.characters_df.loc[self.characters_df['id'] == member_id, 'name'].values[0]
                    if member_name not in team:
                        team.append(member_name)
                    else:
                        print("Este integrante ya está seleccionado.")
                else:
                    print("ID de integrante no válida. Intente nuevamente.")
            else:
                print("Entrada no válida. Por favor, ingrese un número de ID válido.")

        mission = Mission(name, destination, starship, weapons, team)
        self.missions.append(mission)
        print("-" * 50)
        print("Misión definida exitosamente.\n")
        print("-" * 50)

    def mostrar_misiones(self):
        # Muestra la lista de misiones definidas con todos sus detalles.
        if not self.missions:
            print("No hay misiones definidas.")
            return

        for i, mission in enumerate(self.missions):
            print(f"\nMisión {i + 1}:")
            print(f"Nombre: {mission.name}")
            print(f"Planeta destino: {mission.destination}")
            print(f"Nave a utilizar: {mission.starship}")
            print(f"Armas: {', '.join(mission.weapons) if mission.weapons else 'Ninguna'}")
            print(f"Integrantes: {', '.join(mission.team) if mission.team else 'Ninguno'}")
            print("-" * 50)

    def modificar_mision(self):
        # Permite modificar los detalles de una misión existente.
        # Primero muestra todas las misiones, luego solicita la selección de la misión a modificar.
        self.mostrar_misiones()
        if not self.missions:
            return

        try:
            mission_index = int(input("Selecciona el número de la misión a modificar: ").strip()) - 1
            if mission_index < 0 or mission_index >= len(self.missions):
                print("Número de misión no válido.")
                return
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")
            return

        mission = self.missions[mission_index]
        print(f"Modificando misión: {mission.name}")
        
        while True:
            print("\n1. Modificar nombre")
            print("2. Modificar planeta destino")
            print("3. Modificar nave")
            print("4. Modificar armas")
            print("5. Modificar integrantes")
            print("6. Salir")
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                while True:
                    nuevo_nombre = input("Nuevo nombre de la misión: ").strip()
                    if not nuevo_nombre:
                        print("El nombre de la misión no puede estar vacío. Intente nuevamente.")
                    else:
                        mission.name = nuevo_nombre
                        break
            elif opcion == "2":
                while True:
                    nuevo_planeta = input("Nuevo planeta destino: ").strip()
                    if not nuevo_planeta:
                        print("El planeta destino no puede estar vacío. Intente nuevamente.")
                    else:
                        mission.destination = nuevo_planeta
                        break
            elif opcion == "3":
                while True:
                    nueva_nave = input("Nueva nave a utilizar: ").strip()
                    if not nueva_nave:
                        print("La nave a utilizar no puede estar vacía. Intente nuevamente.")
                    else:
                        mission.starship = nueva_nave
                        break
            elif opcion == "4":
                self.modificar_armas(mission)
            elif opcion == "5":
                self.modificar_integrantes(mission)
            elif opcion == "6":
                break
            else:
                print("Opción no válida. Intente nuevamente.")


    def modificar_armas(self, mission):
        # Permite modificar la lista de armas de una misión.
        # Se puede agregar o eliminar armas de la misión seleccionada.
        while True:
            print(f"\nArmas actuales: {', '.join(mission.weapons)}")
            print("1. Agregar arma")
            print("2. Eliminar arma")
            print("3. Volver")
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                if len(mission.weapons) >= 7:
                    print("No se pueden agregar más de 7 armas.")
                    continue
                self.mostrar_armas_disponibles()
                while True:
                    weapon_id = input("ID del arma a agregar: ").strip()
                    if weapon_id == "":
                        print("El ID del arma no puede estar vacío. Intente nuevamente.")
                        continue
                    if not weapon_id.isdigit() or int(weapon_id) not in self.weapons_df['id'].values:
                        print("ID de arma no válida. Intente nuevamente.")
                        continue
                    weapon_name = self.weapons_df.loc[self.weapons_df['id'] == int(weapon_id), 'name'].values[0]
                    mission.weapons.append(weapon_name)
                    break
            elif opcion == "2":
                while True:
                    arma_a_eliminar = input("Nombre del arma a eliminar: ").strip()
                    if not arma_a_eliminar:
                        print("Nombre de arma no puede estar vacío. Intente nuevamente.")
                        continue
                    if arma_a_eliminar in mission.weapons:
                        mission.weapons.remove(arma_a_eliminar)
                        break
                    else:
                        print("Arma no encontrada en la misión.")
            elif opcion == "3":
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def modificar_integrantes(self, mission):
        # Permite modificar la lista de integrantes de una misión.
        # Se puede agregar o eliminar integrantes del equipo seleccionado.
        while True:
            print(f"\nIntegrantes actuales: {', '.join(mission.team)}")
            print("1. Agregar integrante")
            print("2. Eliminar integrante")
            print("3. Volver")
            opcion = input("Selecciona una opción: ").strip()

            if opcion == "1":
                if len(mission.team) >= 7:
                    print("No se pueden agregar más de 7 integrantes.")
                    continue
                self.mostrar_personajes_disponibles()
                while True:
                    member_id = input("ID del integrante a agregar: ").strip()
                    if member_id == "":
                        print("El ID del integrante no puede estar vacío. Intente nuevamente.")
                        continue
                    if not member_id.isdigit() or int(member_id) not in self.characters_df['id'].values:
                        print("ID de integrante no válida. Intente nuevamente.")
                        continue
                    member_name = self.characters_df.loc[self.characters_df['id'] == int(member_id), 'name'].values[0]
                    mission.team.append(member_name)
                    break
            elif opcion == "2":
                while True:
                    integrante_a_eliminar = input("Nombre del integrante a eliminar: ").strip()
                    if not integrante_a_eliminar:
                        print("Nombre del integrante no puede estar vacío. Intente nuevamente.")
                        continue
                    if integrante_a_eliminar in mission.team:
                        mission.team.remove(integrante_a_eliminar)
                        break
                    else:
                        print("Integrante no encontrado en la misión.")
            elif opcion == "3":
                break
            else:
                print("Opción no válida. Intente nuevamente.")

    def visualizar_mision(self):
        self.mostrar_misiones()
        if not self.missions:
            return
        try:
            mission_index = int(input("Selecciona el número de la misión a visualizar: ")) - 1
            if mission_index < 0 or mission_index >= len(self.missions):
                print("Número de misión no válido.")
                return
        except ValueError:
            print("Entrada no válida. Por favor, introduce un número.")
            return

        mission = self.missions[mission_index]
        print("-" * 50)
        print(mission)
        print("-" * 50)

    def guardar_misiones(self):
        # Guarda la lista de misiones en un archivo de texto.
        # Las misiones se guardan en un formato estructurado para facilitar la carga posterior.
        with open('data/missions.txt', 'w') as file:
            for mission in self.missions:
                file.write(str(mission) + '\n')
        print("Misiones guardadas exitosamente en data/missions.txt.")

    def cargar_misiones(self):
        # Carga las misiones desde un archivo de texto.
        # Las misiones se cargan y agregan a la lista existente de misiones.
        try:
            with open('data/missions.txt', 'r') as file:
                content = file.read().strip()
                if not content:
                    print("El archivo de misiones está vacío.")
                    return
                missions_data = content.split('\n\n')
                for mission_data in missions_data:
                    lines = mission_data.split('\n')
                    name = lines[0].split(': ')[1]
                    destination = lines[1].split(': ')[1]
                    starship = lines[2].split(': ')[1]
                    weapons = lines[3].split(': ')[1].split(', ')
                    team = lines[4].split(': ')[1].split(', ')
                    mission = Mission(name, destination, starship, weapons, team)
                    self.missions.append(mission)
            print("Misiones cargadas exitosamente desde data/missions.txt.")
        except FileNotFoundError:
            print("El archivo de misiones no existe.")