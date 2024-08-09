class Especie: 
    def __init__(self, nombre, altura, clasificacion, planeta_origen, lengua_materna, personaje_especie, url):
        self.nombre = nombre
        self.altura = altura
        self.clasificacion = clasificacion
        self.planeta_origen = planeta_origen
        self.lengua_materna = lengua_materna
        self.personaje_especie = personaje_especie
        self.url = url

    def show(self, listaNombres, nombrePlaneta, listaEpisodios):
        
        print(f'El nombre es: {self.nombre}')
        print(f'La clasificacion es: {self.clasificacion}')
        print(f'El planeta de origen es: {nombrePlaneta}')
        print(f'La lengua materna es: {self.lengua_materna}')
        print('Los personajes de esta especie son:')
        print(*listaNombres, sep = "\t\n")
        print('Los episodios en los que aparece esta especie son:')
        print(*listaEpisodios, sep = "\t\n")

        