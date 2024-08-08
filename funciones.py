import requests as rq

from Peliculas import Pelicula
from Naves import Naves
from Vehiculos import Vehiculos

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
    print(listaPeliculas[0].titulo) 


#buscar personaje: da la nave que utiliza cada personaje 
def cargarNaves():
    listaNaves = []
    navesdb = rq.get('https://www.swapi.tech/api/starships?page=1&limit=90').json()
    for results in navesdb['results']:
        naveInfo = rq.get(results["url"]).json()
        pilotos_naves = naveInfo['result']['properties']['pilots']
        url = naveInfo['result']['properties']['url']
        nuevoPiloto = Naves(pilotos_naves, url)
        listaNaves.append(nuevoPiloto)
    print(listaNaves)


#buscar personaje: da el vehiculo que utiliza cada personaje      
def cargarVehiculos():
    listaVehiculos = []
    vehiculosdb = rq.get('https://www.swapi.tech/api/vehicles?page=1&limit=90').json()
    for results in vehiculosdb['results']:
        vehiculoInfo = rq.get(results["url"]).json()
        pilotos_vehiculos = vehiculoInfo['result']['properties']['pilots']
        url = vehiculoInfo['result']['properties']['url']
        nuevoPiloto = Naves(pilotos_vehiculos, url)
        listaVehiculos.append(nuevoPiloto)

def cargarPlaneta():
    listaPlaneta = []
    planetadb = rq.get('https://www.swapi.tech/api/planets?page=1&limit=90').json()
    for results in planetadb['results']:
        None
    


    

        
        
