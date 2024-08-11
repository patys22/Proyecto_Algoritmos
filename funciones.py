import requests as rq

def mostrar_peliculas(listaPeliculas):
    contador = 1
    print('Las peliculas de la saga Star Wars son:')
    for pelicula in listaPeliculas:
        print(f'\n________________________________\n{contador}.\n')
        pelicula.show()
        contador += 1

# funcion para el mostrar las ultimas funciones del menu 2
def mostrar_especies(listaEspecies, listaPeliculas, listaPersonajes, listaPlanetas):
    print('Las especies de la saga Star Wars son:')
    for especie in listaEspecies:
        listaNombres = []
        listaEpisodios = []
        nombrePlaneta = None
        personaje_especie = especie.personaje_especie
        especie_planeta = especie.planeta_origen
        
        for personaje in personaje_especie: #trae los nombres de los personajes en las especies
            for p in listaPersonajes:
                if personaje == p.url:
                    listaNombres.append(p.nombre)
        for planeta in listaPlanetas: #trae los 
            if especie_planeta == planeta.url:
                nombrePlaneta = planeta.nombre

        for pelicula in listaPeliculas:
            for urlEspecie in pelicula.especies:
                if especie.url == urlEspecie:
                    listaEpisodios.append(pelicula.titulo)
        print(f'\n________________________________\n')
        especie.show(listaNombres, nombrePlaneta, listaEpisodios)
    
#funcion para mostrar las ultimas funciones del menu 3
def mostrar_planetas(listaPeliculas, listaPlanetas, listaPersonajes):
    for planeta in listaPlanetas:
        listaEpisodios = []
        listaOrigen = []
        for pelicula in listaPeliculas:
            for urlPlaneta in pelicula.planetas:
                if planeta.url == urlPlaneta:
                    listaEpisodios.append(pelicula.titulo)
        for personaje in listaPersonajes:
                if personaje.planeta_origen == planeta.url:
                    listaOrigen.append(personaje.nombre)
        planeta.show(listaEpisodios, listaOrigen)

#funcion para mostrar el menu 4
def buscar_personajes(listaPersonaje, personaje_ingresado, listaNaves, listaPeliculas, listaEspecies, listaVehiculos):
    personajes = {}
    contador = 1 
    listaNave = []
    listaNombre = []
    listaEpisodios = []
    listaVehiculo = []
    nombrePlaneta = None
    #planeta_personaje = especie.personaje_especie
    for personaje in listaPersonaje:
        personaje_nombre = personaje.nombre.lower()
        
        #trae planeta origen del personaje 
        if personaje_ingresado.lower() in personaje_nombre:
            print(f'{contador}.- {personaje.nombre}')
            personajes[contador] =  personaje
            contador += 1
            personaje_planeta = rq.get(personaje.planeta_origen).json()
            nombrePlaneta = personaje_planeta['result']['properties']['name'] #trae el nombre planeta de origen

            for especie in listaEspecies: #trae la especie del personaje
                for urlPersonaje in especie.personaje_especie:
                    if personaje.url == urlPersonaje:
                        listaNombre.append(especie.nombre)

            for pelicula in listaPeliculas: #trae los nombres de las peliculas en las que sale ese personaje
                for urlPersonaje in pelicula.personajes:
                    if personaje.url == urlPersonaje:
                        listaEpisodios.append(pelicula.titulo)
            
            for nave in listaNaves: # trae la nave de cada personaje
                for urlPersonaje in nave.piloto_nave:
                    if personaje.url == urlPersonaje:
                        listaNave.append(nave.nombre)

            for vehiculo in listaVehiculos: #trae el vehiculo de cada personaje 
                for urlPersonaje in vehiculo.piloto_vehiculo:
                    if personaje.url == urlPersonaje:
                        listaVehiculo.append(vehiculo.nombre)
            

    aux = True
    errorAux = True
    while aux:
        menu_personajes = int(input('\nSeleccione el numero del personaje del que desea obtener informacion y si desea desea salir escriba 0: \n----> '))
        for key, value in personajes.items():
            if menu_personajes == key:
                value.show(nombrePlaneta, listaNombre, listaEpisodios, listaNave, listaVehiculo)
                errorAux= False
                break
            elif menu_personajes == 0:
                aux = False
                break
        if errorAux and aux:  
            print('Introduzca un valor valido')
        errorAux: True
    
