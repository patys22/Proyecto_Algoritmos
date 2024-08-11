import APIs
class App:
    peliculas_obj=[]
    def start(self):
        while True:
            menu=input('''
    A. Lista de Películas de la saga
    B. Lista de las especies de seres vivos de la saga
    C. Lista de planetas
    D. Buscar personaje
    E. Gráfico de cantidad de personajes nacidos en cada planeta
    F. Gráficos de características de naves
    G. Estadísticas sobre naves
    H. Construir misión
    I. Modificar misión
    J. Visualizar misión
    K. Guardar misiones
    L. Cargar misiones
    -->''')
            
    def crear_pelicula():
        peliculas=APIs["properties"]
        for pelicula in peliculas:
            None