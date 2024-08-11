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
        for episodio in listaEpisodios:
            print(f'\t{episodio}')
        print(f'Su genero es: \n\t{self.genero}')
        print(f'Su especie es: ')
        for especie in listaNombre:
            print(f'\t{especie}')
        print(f'Las naves que utiliza son: ')
        for nave in listaNave:
            print(f'\t{nave}')
        print(f'Los vehiculos que utiliza son: ')
        for vehiculo in listaVehiculo:
            print(f'\t{vehiculo}')
        