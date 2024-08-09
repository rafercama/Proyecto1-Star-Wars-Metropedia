from src.models import Character
import pandas as pd
import plotly.express as px

def leer_personajes_csv():
    ruta_csv = 'data/csv/characters.csv'
    return pd.read_csv(ruta_csv)

def generar_grafico_personajes_por_planeta():
    # Leer los datos del archivo CSV
    df_personajes = leer_personajes_csv()

    # Crear objetos Character a partir de los datos
    personajes = []
    for _, row in df_personajes.iterrows():
        personaje = Character(
            name=row['name'],
            homeworld=row['homeworld'],
            films=row.get('films', ''), # Usa un valor por defecto si no está presente
            gender=row['gender'],
            species=row['species'],
            vehicles=row.get('vehicles', ''),  # Usa un valor por defecto si no está presente
            starships=row.get('starships', '')  # Usa un valor por defecto si no está presente
        )
        personajes.append(personaje)

    # Contar la cantidad de personajes por planeta
    conteo_personajes = df_personajes['homeworld'].value_counts()

    # Crear el gráfico
    fig = px.bar(conteo_personajes, x=conteo_personajes.index, y=conteo_personajes.values,
                labels={'x': 'Planeta', 'y': 'Número de Personajes'},
                title='Número de Personajes Nacidos en Cada Planeta')

    # Mostrar el gráfico
    fig.show()


class StarshipVisualizer:
    @staticmethod
    def leer_naves_csv():
        ruta_csv = 'data/csv/starships.csv'
        return pd.read_csv(ruta_csv)

    @staticmethod
    def graficar_longitud():
        df_naves = StarshipVisualizer.leer_naves_csv()
        fig = px.bar(df_naves, x='name', y='length', title='Longitud de las Naves')
        fig.show()

    @staticmethod
    def graficar_capacidad_carga():
        df_naves = StarshipVisualizer.leer_naves_csv()
        fig = px.bar(df_naves, x='name', y='cargo_capacity', title='Capacidad de Carga de las Naves')
        fig.show()

    @staticmethod
    def graficar_clasificacion_hiperimpulsor():
        df_naves = StarshipVisualizer.leer_naves_csv()
        fig = px.box(df_naves, x='hyperdrive_rating', title='Clasificación de Hiperimpulsor de las Naves')
        fig.show()

    @staticmethod
    def graficar_mglt():
        df_naves = StarshipVisualizer.leer_naves_csv()
        fig = px.box(df_naves, x='MGLT', title='MGLT (Modern Galactic Light Time) de las Naves')
        fig.show()


    @staticmethod
    def safe_mode(series):
        mode_values = series.mode()
        if len(mode_values) > 0:
            return mode_values[0]
        else:
            return None


    @staticmethod
    def mostrar_estadisticas():
        df_naves = StarshipVisualizer.leer_naves_csv()

        # Calcular estadísticas básicas por clase de nave
        stats = df_naves.groupby('starship_class').agg({
            'hyperdrive_rating': ['mean', 'max', 'min', StarshipVisualizer.safe_mode],
            'MGLT': ['mean', 'max', 'min', StarshipVisualizer.safe_mode],
            'max_atmosphering_speed': ['mean', 'max', 'min', StarshipVisualizer.safe_mode],
            'cost_in_credits': ['mean', 'max', 'min', StarshipVisualizer.safe_mode]
        })

        # Formatear la salida para una mejor visualización
        pd.options.display.float_format = '{:.2f}'.format  # Formato para números decimales
        pd.options.display.max_columns = None  # Mostrar todas las columnas
        pd.options.display.width = 1000  # Ancho máximo de la tabla

        # Mostrar las estadísticas formateadas con estructura
        print("\n" + "-"*50)
        print("Estadísticas Básicas por Clase de Nave")
        print("-"*50 + "\n")
        for starship_class, data in stats.iterrows():
            print(f"Clase de Nave: {starship_class}")
            print("-" * 50)
            print(data.to_string())
            print("-" * 50 + "\n")