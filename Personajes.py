class Personaje:
    def __init__(self, nombre, planeta_origen, genero, url, uid):
        self.nombre = nombre
        self.planeta_origen = planeta_origen
        self.genero = genero
        self.url =url
        self.uid =uid
        
    def show(self, nombrePlaneta, listaNombre, listaEpisodios, listaNave, listaVehiculo):
        print(f'\nSu nombre es: \n\t{self.nombre}')
        print(f'Su planeta de origen es: \n\t{nombrePlaneta}')
        print(f'Los titulos en los que aparecen son: ')
        print(*listaEpisodios, sep = "\t\t\n")
        print(f'Su genero es: \n\t{self.genero}')
        print(f'Su especie es: ')
        print(*listaNombre, sep = "\t\t\n")
        print(f'Las naves que utiliza son: ')
        print(*listaNave, sep = "\t\t\n")
        print(f'Los vehiculos que utiliza son: ')
        print(*listaVehiculo, sep = "\t\t\n")

        