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
def buscar_personajes(listaPersonaje, personaje_ingresado):
    personajes = []
    for personaje in listaPersonaje:
        if personaje_ingresado.lower() in personaje.nombre.lower():
            for personaje.nombre in listaPersonaje:
                return personaje.url
            print(personaje.url)
            
            '''personajes.append(personaje)
            return personajes'''






    





    
    



        