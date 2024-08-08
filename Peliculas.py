class Pelicula:
    def __init__(self, titulo, productor, especies, vehiculos, planetas, personajes, nave_espacial, id_episodio, lanzamiento, opening_crawl, director, url) -> None:
        self.titulo=titulo
        self.productor=productor
        self.especies=especies
        self.vehiculos=vehiculos
        self.planetas=planetas
        self.personajes=personajes
        self.nave_espacial=nave_espacial
        self.id_episodio=id_episodio
        self.lanzamiento=lanzamiento
        self.opening_crawl=opening_crawl
        self.director=director
        self.url=url
    
    def show(self):
        print(f"El titulo es: {self.titulo}")
        print(f"El numero de episodio es: {self.id_episodio}")
        print(f"La fecha de lanzamiento es: {self.lanzamiento}")
        print(f"El frase de inicio es: {self.opening_crawl}")
        print(f"El director es: {self.director}")