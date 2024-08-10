import csv
from Usuario import Usuario
from Mision import Mision
from Planetas import Planetas

class App:
    usuarios_obj=[]
    misiones_obj=[]
    planetas_csv=[]

    def start(self):
        None

    def construir_mision(self):
        print("Ingrese sus datos para poder construir una mision: ")
        cedula=int(input("\tCedula: "))
        usuario_seleccionado=self.buscar_usuario_lineal(cedula)
        if not usuario_seleccionado:
            nombre=input("\tNombre: ")
            apellido=input("\tApellido: ")
        else:
            nombre=usuario_seleccionado.nombre
            apellido=usuario_seleccionado.apellido
        print("Puede comenzar a construir su mision.")
        nombre_mision=input("Ingrese el nombre de la mision: ")


    def seleccionar_planeta(self):
            planetas = []
            with open("planets.csv",'r') as f:
                reader = csv.DictReader(f)
                for fila in reader:
                    planeta = Planetas(planeta['id'], planeta['name'])
                    planetas.append(planeta)
            print("Seleccione el planeta destino: ")
            contador=1
            for planeta in self.planetas_csv:
                print(f'\t{contador}-{planeta.nombre}')
                contador+=1
            eleccion=int(input("--> "))
            planeta=self.planetas_csv[eleccion-1]


    def buscar_usuario_lineal(self, cedula):
                    for usuario in self.usuarios_obj:
                        if usuario.cedula==cedula:
                            return usuario
                    return None
                    
