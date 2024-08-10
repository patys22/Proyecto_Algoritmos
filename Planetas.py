import csv

# Clase que representa un Planeta
class Planetas:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

# Leer planetas desde el archivo CSV
def leer_planetas_desde_csv(ruta_archivo):
    lista_planetas = []
    with open(ruta_archivo, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            planeta = Planetas(
                row['id'], row['name']
            )
            lista_planetas.append(planeta)
    return lista_planetas

# Mostrar planetas disponibles
def mostrar_planetas(planetas):
    print("Seleccione el planeta destino:")
    contador=1
    for planeta in planetas:
        print(f'\t{contador}-{planeta.nombre}')
        contador+=1
    planeta_seleccionado=int(input("--> "))
    planeta=planetas[planeta_seleccionado-1]

# Permitir al usuario seleccionar un planeta
def seleccionar_planeta(planetas):
    eleccion = int(input("Ingrese el número del planeta que desea seleccionar: "))
    planeta_seleccionado = planetas[eleccion - 1]
    print(f'Has seleccionado el planeta {planeta_seleccionado.nombre}.')
    return planeta_seleccionado

# Construir la misión
def construir_mision():
    # Paso 1: Pedir el nombre de la misión
    nombre_mision = input("Ingrese el nombre de la misión: ")

    # Paso 2: Leer planetas desde el archivo CSV
    ruta_archivo_csv = 'planets.csv'
    planetas = leer_planetas_desde_csv(ruta_archivo_csv)

    # Paso 3: Mostrar la lista de planetas y seleccionar uno
    mostrar_planetas(planetas)
    planeta_seleccionado = seleccionar_planeta(planetas)

    # Resumen de la misión
    print(f'\nMisión "{nombre_mision}" creada con éxito.')
    print(f'Destino: {planeta_seleccionado.nombre}\n')  