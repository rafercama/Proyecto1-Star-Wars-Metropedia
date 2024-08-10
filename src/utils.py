from src.data_processing import StarshipVisualizer

def mostrar_menu_graficos_naves():
    while True:
        print("\nGráficos de Naves:")
        print("a. Longitud de la nave")
        print("b. Capacidad de carga")
        print("c. Clasificación de hiperimpulsor")
        print("d. MGLT")
        
        graph_option = input("Elige una opción (a-d): ")
        
        if graph_option == "a":
            StarshipVisualizer.graficar_longitud()
        elif graph_option == "b":
            StarshipVisualizer.graficar_capacidad_carga()
        elif graph_option == "c":
            StarshipVisualizer.graficar_clasificacion_hiperimpulsor()
        elif graph_option == "d":
            StarshipVisualizer.graficar_mglt()
        else:
            print("Opción no válida.")
            continue  # Continúa al principio del bucle
        
        otra_accion = input("\n¿Deseas hacer otra gráfica de naves? (s/n): ").lower()
        if otra_accion != "s":
            break  # Sale del bucle y regresa al menú principal

def gestion_misiones(mission_manager):
    while True:
        print("\n===== Gestión de Misiones =====")
        print("1. Definir nueva misión")
        print("2. Modificar misión")
        print("3. Visualizar misión")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mission_manager.definir_mision()
        elif opcion == "2":
            mission_manager.modificar_mision()
        elif opcion == "3":
            mission_manager.visualizar_mision()
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente nuevamente.")