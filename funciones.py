import requests as rq
import pandas as pd
import matplotlib.pyplot as mpl
import numpy as np

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

        personaje_planeta = rq.get(personaje.planeta_origen).json()
        nombrePlaneta = personaje_planeta['result']['properties']['name']



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
        
        
        if personaje_ingresado.lower() in personaje_nombre:
            print(f'{contador}.- {personaje.nombre}')
            personajes[contador] =  personaje
            contador += 1

            personaje_planeta = rq.get(personaje.planeta_origen).json()
            nombrePlaneta = personaje_planeta['result']['properties']['name'] #trae el nombre planeta de origen del personaje 

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
    
###############################################################################################################
#Empece a trabajar con las csv para menu 5, 6 y 7

def personaje_csv(): #trae informacion de personaje de csv
    caminoArchivo = 'characters.csv'
    info = pd.read_csv(caminoArchivo)
    return info 


def persona_Planeta(info): #trae el grafico de la cantidad de personajes por planeta de origen
    personajeXplaneta = info.groupby('homeworld').size() 
    personajeXplaneta_dict = personajeXplaneta.to_dict()

    nombrePlaneta = list(personajeXplaneta_dict.keys())
    numNacidos = list(personajeXplaneta_dict.values())
    fig, ax = mpl.subplots(figsize=(10,7))

    ax.bar(nombrePlaneta, numNacidos)
    ax.set_xlabel('Planeta de Origen')
    ax.set_ylabel('Cantidad de Personajes')
    ax.set_title('Cantidad de Personajes por Planeta de Origen')
    ax.set_xticks(range(len(nombrePlaneta)))  #Establece las posiciones de los ticks
    ax.set_xticklabels(nombrePlaneta, rotation=45, ha='right') # Rotacion de los nombres de los planetas

    fig.tight_layout()  # Ajustar el layout para que no se sobrepongan las etiquetas
    mpl.show() 

info = personaje_csv()
persona_Planeta(info)

def caracteristica_Nave():
    while True:
        submenu = int(input("Ingrese el numero del grafico desea consultar: \n\n1. Longirud de la nave\n2. Capacidad de carga\n3. Clasificacion de hiperimpulsor\n4. MGLT (Modern Galactic Light Time)\n5. Salir\n\t----> "))
        if submenu == 1: #trae el grafico de longitud por nave
            caminoArchivo = 'starships.csv'
            infoNave = pd.read_csv(caminoArchivo)

            longitudXnave_dict = pd.Series(infoNave.length.values, index=infoNave.name).to_dict()

            nombreNave = list(longitudXnave_dict.keys())
            longitud = list(longitudXnave_dict.values())
            fig, ax = mpl.subplots(figsize=(10,7))

            ax.bar(nombreNave, longitud)
            ax.set_xlabel('Nombre de la nave')
            ax.set_ylabel('Longitud')
            ax.set_title('Longitud por nave')
            ax.set_xticks(range(len(nombreNave)))  #Establece las posiciones de los ticks
            ax.set_xticklabels(nombreNave, rotation=45, ha='right') # Rotacion de los nombres de las naves

            fig.tight_layout()  # Ajustar el layout para que no se sobrepongan las etiquetas
            mpl.show()

        elif submenu == 2: #trae el grafico de capacidad por nave
            caminoArchivo = 'starships.csv'
            infoNave = pd.read_csv(caminoArchivo)

            capacidadXnave_dict = pd.Series(infoNave.cargo_capacity.values, index=infoNave.name).to_dict()

            nombreNave = list(capacidadXnave_dict.keys())
            capacidad = list(capacidadXnave_dict.values())
            fig, ax = mpl.subplots(figsize=(10,7))

            ax.bar(nombreNave, capacidad)
            ax.set_xlabel('Nombre de la nave')
            ax.set_ylabel('Capacidad')
            ax.set_title('Capacidad por nave')
            ax.set_xticks(range(len(nombreNave)))  #Establece las posiciones de los ticks
            ax.set_xticklabels(nombreNave, rotation=45, ha='right') # Rotacion de los nombres de las naves

            fig.tight_layout()  # Ajustar el layout para que no se sobrepongan las etiquetas
            mpl.show()
            
        elif submenu == 3: 
            caminoArchivo = 'starships.csv'
            infoNave = pd.read_csv(caminoArchivo)

            hiperimpulsorXnave_dict = pd.Series(infoNave.hyperdrive_rating.values, index=infoNave.name).to_dict()

            nombreNave = list(hiperimpulsorXnave_dict.keys())
            hiperimpulsor = list(hiperimpulsorXnave_dict.values())
            fig, ax = mpl.subplots(figsize=(10,7))

            ax.bar(nombreNave, hiperimpulsor)
            ax.set_xlabel('Nombre de la nave')
            ax.set_ylabel('Clasificacion del hiperimpulsor')
            ax.set_title('Clasificacion del hiperimpulsor por nave')
            ax.set_xticks(range(len(nombreNave)))  #Establece las posiciones de los ticks
            ax.set_xticklabels(nombreNave, rotation=45, ha='right') # Rotacion de los nombres de las naves

            fig.tight_layout()  # Ajustar el layout para que no se sobrepongan las etiquetas
            mpl.show()
            
        elif submenu == 4:
            caminoArchivo = 'starships.csv'
            infoNave = pd.read_csv(caminoArchivo)

            mgltXnave_dict = pd.Series(infoNave.MGLT.values, index=infoNave.name).to_dict()

            nombreNave = list(mgltXnave_dict.keys())
            mglt = list(mgltXnave_dict.values())
            fig, ax = mpl.subplots(figsize=(10,7))

            ax.bar(nombreNave, mglt)
            ax.set_xlabel('Nombre de la nave')
            ax.set_ylabel('Modern Galactic Light Time')
            ax.set_title('Modern Galactic Light Time por nave')
            ax.set_xticks(range(len(nombreNave)))  #Establece las posiciones de los ticks
            ax.set_xticklabels(nombreNave, rotation=45, ha='right') # Rotacion de los nombres de las naves

            fig.tight_layout()  # Ajustar el layout para que no se sobrepongan las etiquetas
            mpl.show()
            
        elif submenu == 5:
            break
        else: 
            print("Ingrese un valor valido, tiene que ingresar un numero del 1 al 5")

#caracteristica_Nave()

def estadistica_Nave():
    caminoArchivo = 'starships.csv'
    infoNave = pd.read_csv(caminoArchivo)
    
    #Estadisticas de clasificacion de hiperimpulsor 
    minHiperimpulsor = pd.Series(infoNave.hyperdrive_rating.values).min()
    maxHiperimpulsor = pd.Series(infoNave.hyperdrive_rating.values).max()
    promHiperimpulsor = pd.Series(infoNave.hyperdrive_rating.values).mean()
    modaHiperimpulsor = pd.Series(infoNave.hyperdrive_rating.values).mode().iloc[0]

    #Estadisticas de MGTL
    minMGTL = pd.Series(infoNave.MGLT.values).min()
    maxMGTL = pd.Series(infoNave.MGLT.values).max()
    promMGTL = pd.Series(infoNave.MGLT.values).mean()
    modaMGTL = pd.Series(infoNave.MGLT.values).mode().iloc[0]

    #Estadisticas de la velocidad maxima en atmosfera 
    minVelocidad = pd.Series(infoNave.max_atmosphering_speed.values).min()
    maxVelocidad = pd.Series(infoNave.max_atmosphering_speed.values).max()
    promVelocidad = pd.Series(infoNave.max_atmosphering_speed.values).mean()
    modaVelocidad = pd.Series(infoNave.max_atmosphering_speed.values).mode().iloc[0]

    #Estadisticas de costos en creditos
    minCosto = pd.Series(infoNave.cost_in_credits.values).min()
    maxCosto = pd.Series(infoNave.cost_in_credits.values).max()
    promCosto = pd.Series(infoNave.cost_in_credits.values).mean()
    modaCosto = pd.Series(infoNave.cost_in_credits.values).mode().iloc[0]

    lista_min = [minHiperimpulsor, minMGTL, minVelocidad, minCosto]
    lista_max = [maxHiperimpulsor, maxMGTL, maxVelocidad, maxCosto]
    lista_prom = [promHiperimpulsor, promMGTL, promVelocidad, promCosto]
    lista_moda = [modaHiperimpulsor, modaMGTL, modaVelocidad, modaCosto]

    cuadro = pd.DataFrame(columns=["Caracteristicas", "Promedio", "Moda", "Maximo", "Minimo"])
    caracteristcas = ["Clasificacion de Hiperimpulsor", "Modern Galactic Light Time", "Velocidad maxima de atmosfera", "Costo en creditos"]
    cuadro["Caracteristicas"] = np.array(caracteristcas)
    cuadro["Promedio"] = np.array(lista_prom)
    cuadro["Moda"] = np.array(lista_moda)
    cuadro["Maximo"] = np.array(lista_max)
    cuadro["Minimo"] = np.array(lista_min)    
    print(cuadro)

estadistica_Nave()