class Especie: 
    def __init__(self, nombre, clasificacion, planeta_origen, lengua_materna, personaje_especie):
        self.nombre = nombre
        self.clasificacion = clasificacion
        self.planeta_origen = planeta_origen
        self.lengua_materna = lengua_materna
        self.personaje_especie = personaje_especie
        
    def show(self):
        print(f'El nombre es: {self.nombre}')
        print(f'La clasificacion es: {self.clasificacion}')
        print(f'El planeta de origen es: {self.planeta_origen}')
        print(f'La lengua materna es: {self.lengua_materna}')
        print(f'Los personajes de esta especie son: {self.personaje_especie}')

        