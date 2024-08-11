class Personaje:
    def __init__(self, nombre, planeta_origen, genero, url):
        self.nombre = nombre
        self.planeta_origen = planeta_origen
        self.genero = genero
        self.url =url
    
    def show(self):
        print(f'Su nombre es: {self.nombre}')
        print(f'Su planeta de origen es: {self.planeta_origen}')
        print(f'Los titulos en los que aparecen son: ')
        print(f'Su genero es: {self.genero}')
        print(f'Su especie es: ')
        print(f'Las naves que utiliza son: ')
        print(f'Los vehiculos que utiliza son: ')

        