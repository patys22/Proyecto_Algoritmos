class Planeta:
    def __init__(self,nombre, periodo_orbita, periodo_rotacion, cantidad_habitantes, clima, url ):
        self.nombre = nombre
        self.periodo_orbita = periodo_orbita
        self.periodo_rotacion = periodo_rotacion
        self.cantidad_habitantes = cantidad_habitantes
        self.clima = clima 
        self.url = url
    
    def show(self, listaEpisodios, listaOrigen):
        print(f"El nombre es: {self.nombre} ")
        print(f'El periodo de orbita es: {self.periodo_orbita}')
        print(f'El periodo de rotacion es: {self.periodo_rotacion}')
        print(f'El tipo de clima es: {self.clima}')
        print('Los episodios en los que aparece este planeta son:')
        print(*listaEpisodios, sep = "\t\n")
        print('Los personajes que aparecen en este planeta son:')
        print(*listaOrigen, sep = "\t\n")
        print()
        
    
       
        
