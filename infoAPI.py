import requests as rq

from Peliculas import Pelicula
from Naves import Nave
from Vehiculos import Vehiculo
from Planeta import Planeta
from Especies import Especie
from Personajes import Personaje

def cargarPelis(): #esta funcion me permite acceder a la info de la api de peliculas
    listaPeliculas = []
    peliculasdb = rq.get('https://www.swapi.tech/api/films').json()
    for results in peliculasdb['result']:
        titulo = results['properties']['title']
        personajes = results['properties']['characters']
        director = results['properties']['director']
        id_episodio = results['properties']['episode_id']
        fecha = results['properties']['release_date']
        vehiculos = results['properties']['vehicles']
        naves = results['properties']['starships']
        planetas = results['properties']['planets']
        especies = results['properties']['species']
        opening_crawl = results['properties']['opening_crawl']
        productor = results['properties']['producer']
        url = results['properties']['url']
        

        nuevaPelicula = Pelicula(titulo, productor, especies, vehiculos, planetas, personajes, naves, id_episodio, fecha, opening_crawl, director, url)
        listaPeliculas.append(nuevaPelicula) #aqui ya tengo la info de toda la api de peliculas en la listaPeliculas
    return listaPeliculas


#buscar personaje: da la nave que utiliza cada personaje 
def cargarNaves():
    listaNaves = []
    navesdb = rq.get('https://www.swapi.tech/api/starships?page=1&limit=90').json()
    for results in navesdb['results']:
        naveInfo = rq.get(results["url"]).json()
        nombre = naveInfo['result']['properties']['name']
        pilotos_naves = naveInfo['result']['properties']['pilots']
        url = naveInfo['result']['properties']['url']
        nuevaNave = Nave(nombre, pilotos_naves, url)
        listaNaves.append(nuevaNave)
    return listaNaves

#buscar personaje: da el vehiculo que utiliza cada personaje      
def cargarVehiculos():
    listaVehiculos = []
    vehiculosdb = rq.get('https://www.swapi.tech/api/vehicles?page=1&limit=90').json()
    for results in vehiculosdb['results']:
        vehiculoInfo = rq.get(results["url"]).json()
        nombre = vehiculoInfo['result']['properties']['name']
        pilotos_vehiculos = vehiculoInfo['result']['properties']['pilots']
        url = vehiculoInfo['result']['properties']['url']
        nuevoVehiculo = Vehiculo(nombre, pilotos_vehiculos, url)
        listaVehiculos.append(nuevoVehiculo)
    return listaVehiculos

def cargarPlaneta(): #esta funcion permite entrar en la api de planeta
    listaPlaneta = []
    planetadb = rq.get('https://www.swapi.tech/api/planets?page=1&limit=90').json()
    for results in planetadb['results']:
        planetaInfo = rq.get(results['url']).json()
        nombre = planetaInfo['result']['properties']['name']
        periodoOrbita = planetaInfo['result']['properties']['rotation_period']
        periodoRotacion = planetaInfo['result']['properties']['orbital_period']
        cantidadHabitantes = planetaInfo['result']['properties']['population']
        clima = planetaInfo['result']['properties']['climate']
        url = planetaInfo['result']['properties']['url']
        nuevoPlaneta=Planeta(nombre, periodoOrbita, periodoRotacion, cantidadHabitantes, clima, url)
        listaPlaneta.append(nuevoPlaneta)
    return listaPlaneta

def cargarEspecies(): #buscar caracteristicas de las especies
    listaEspecies = []
    especiesdb = rq.get('https://www.swapi.tech/api/species?page=1&limit=5').json()
    # print(especiesdb)
    for results in especiesdb['results']:
        # print(results['url'])
        especiesInfo = rq.get(results['url']).json()
        nombre = especiesInfo['result']['properties']['name']
        altura = especiesInfo['result']['properties']['average_height']
        clasificacion = especiesInfo['result']['properties']['classification']
        planetaOrigen = especiesInfo['result']['properties']['homeworld']
        lenguaMaterna = especiesInfo['result']['properties']['language']
        personajeEspecie = especiesInfo['result']['properties']['people']
        url = especiesInfo['result']['properties']['url']
        nuevaEspecie=Especie(nombre, altura, clasificacion, planetaOrigen, lenguaMaterna, personajeEspecie,url)
        listaEspecies.append(nuevaEspecie)
    return listaEspecies

def cargarPersonajes(): #buscar caracteristicas de los personajes y toda la info que piden 
    listaPersonajes = []
    personajesdb = rq.get('https://www.swapi.tech/api/people?page=1&limit=5').json()
    for results in personajesdb['results']:
        personajeInfo = rq.get(results['url']).json()
        url = results['url']
        nombre = personajeInfo['result']['properties']['name']
        genero = personajeInfo['result']['properties']['gender']
        planetaOrigen = personajeInfo['result']['properties']['homeworld']
        uid = personajeInfo['result']['uid']
        nuevoPersonaje=Personaje(nombre, planetaOrigen, genero, url, uid)
        listaPersonajes.append(nuevoPersonaje)
    return listaPersonajes




    


    


    

        
        
