from infoAPI import cargarPelis, cargarEspecies, cargarPersonajes, cargarPlaneta, cargarNaves, cargarVehiculos
from funciones import mostrar_peliculas, mostrar_especies, mostrar_planetas, buscar_personajes, estadistica_Nave, caracteristica_Nave, persona_Planeta, personaje_csv
import csv
from Usuario import Usuario
from Mision import Mision
from Planeta_csv import Planeta_csv
from Nave_csv import Nave_csv
from Armas_csv import Armas_csv
from Integrantes_csv import Integrantes_csv
from funciones_paty import App_paty
from Usuario import Usuario

import atexit
import os

def borrar_archivo_misiones():
    if os.path.exists("misiones.txt"):
        os.remove("misiones.txt")
        print("Archivo 'misiones.txt' borrado al cerrar el programa.")

atexit.register(borrar_archivo_misiones)
class App:
    usuarios_obj=[]
    misiones_obj=[]
    misiones_usuarios={}

    def start(self):
        
        listaPeliculas = cargarPelis()
        listaEspecies = cargarEspecies()
        listaPersonajes = cargarPersonajes()
        listaPlanetas = cargarPlaneta()
        listaNaves = cargarNaves()
        listaVehiculos = cargarVehiculos()

        while True:
            try:
                print("\n\t\tBienvenido al mundo de Star Wars\n")
                menu = int(input("Seleccione una opcion del menu:\n\n\t1. Ver peliculas de la saga\n\t2. Ver especies de seres vivos de la saga\n\t3. Ver planetas\n\t4. Buscar personaje\n\t5. Grafico de cantidad de personajes en cada planeta\n\t6. Graficos de caracteristicas de naves\n\t7. Estadisticas sobre naves\n\t8. Construir mision\n\t9. Modificar mision\n\t10. Visualizar misiones\n\t11. Salir\n\t----> "))
            except ValueError:
                print("Por favor, ingrese un número válido.")
                continue

            if menu==1:
                listaPeliculas = cargarPelis()
                mostrar_peliculas(listaPeliculas)
            elif menu==2:
                mostrar_especies(listaEspecies, listaPeliculas, listaPersonajes, listaPlanetas)
            elif menu==3:
                mostrar_planetas(listaPeliculas, listaPlanetas, listaPersonajes)
            elif menu==4:
                while True:
                    personaje_ingresado = input("\nIngrese el nombre del personaje que desea buscar y si desea regresar al menu ingrese 0: \n---> ")
                    if personaje_ingresado == "0":
                        break
                    else:
                        busqueda = buscar_personajes(listaPersonajes, personaje_ingresado, listaNaves, listaPeliculas, listaEspecies, listaVehiculos)
            elif menu==5:
                info = personaje_csv()
                persona_Planeta(info)
            elif menu==6:
                caracteristica_Nave()
            elif menu==7:
                estadistica_Nave()
            elif menu==8:
                self.construir_mision()
                self.gestionar_misiones()
            elif menu==9:
                self.modificar_mision()
            elif menu==10:
                self.visualizar_mision()
            elif menu==11:
                print("\nVuelva pronto y que la fuerza te acompañe")
                break
            elif menu <= 0 and menu > 11: 
                print('Ingrese una opcion valida')

    


    def construir_mision(self):
        print("Ingrese sus datos para poder construir una mision: ")
        cedula = int(input("\tCedula: "))
        usuario_seleccionado = self.buscar_usuario_lineal(cedula)
        if not usuario_seleccionado:
            nombre = input("\tNombre: ")
            apellido = input("\tApellido: ")
            self.registrar_usuario(cedula, nombre, apellido)
        else:
            nombre = usuario_seleccionado.nombre
            apellido = usuario_seleccionado.apellido
        print("Puede comenzar a construir su misión.")
        nombre_mision = input("\nIngrese el nombre de la misión: ")
        
        planeta = self.seleccionar_planeta()
        nave = self.seleccionar_nave()
        armas = self.seleccionar_armas()
        integrantes = self.seleccionar_integrantes()

        print("\nResumen de la Mision:")
        print(f"Nombre de la mision: {nombre_mision}")
        print(f"Planeta destino: {planeta.nombre}")
        print(f"Nave a utilizar: {nave.nombre}")
        print("Armas a utilizar:")
        for arma in armas:
            print(f"- {arma.nombre}")
        print("Integrantes de la mision:")
        for integrante in integrantes:
            print(f"- {integrante.nombre}")

        mision = {
            "nombre_mision": nombre_mision,
            "planeta": planeta,
            "nave": nave,
            "armas": armas,
            "integrantes": integrantes
        }

        if cedula in self.misiones_usuarios:
            self.misiones_usuarios[cedula].append(mision)
        else:
            self.misiones_usuarios[cedula] = [mision]
        
        self.misiones_obj.append(mision)
        self.guardar_misiones()

    def guardar_misiones(self):
        with open("misiones.txt", "w") as f:
            for cedula, misiones in self.misiones_usuarios.items():
                f.write(f"Usuario: {cedula}\n")
                for mision in misiones:
                    f.write(f"\tMision: {mision['nombre_mision']}\n")
                    f.write(f"\t\tPlaneta: {mision['planeta'].nombre}\n")
                    f.write(f"\t\tNave: {mision['nave'].nombre}\n")
                    f.write(f"\t\tArmas: {', '.join([arma.nombre for arma in mision['armas']])}\n")
                    f.write(f"\t\tIntegrantes: {', '.join([integrante.nombre for integrante in mision['integrantes']])}\n")
                f.write("\n")
        print("Misiones guardadas con exito en misiones.txt")

    def registrar_usuario(self, cedula, nombre, apellido):
        nuevo_usuario = Usuario(cedula, nombre, apellido)
        self.usuarios_obj.append(nuevo_usuario)

    def buscar_usuario_lineal(self, cedula):
        for usuario in self.usuarios_obj:
            if usuario.cedula == cedula:
                return usuario
        return None
    
    def seleccionar_planeta(self):
        lista_planetas = []
        with open("planets.csv", 'r') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                planeta = Planeta_csv(fila['id'], fila['name'])
                lista_planetas.append(planeta)
        print("Seleccione el planeta destino:")
        contador = 1
        for planeta in lista_planetas:
            print(f'\t{contador}-{planeta.nombre}')
            contador += 1
        planeta_seleccionado = int(input("--> "))
        if planeta_seleccionado > 0 and planeta_seleccionado <= len(lista_planetas):
            return lista_planetas[planeta_seleccionado - 1]
        else:
            print("Seleccion invalida.")
            return self.seleccionar_planeta()
    
    def seleccionar_nave(self):
        lista_naves = []
        with open("starships.csv", 'r') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                nave = Nave_csv(fila['id'], fila['name'], fila['model'], fila['manufacturer'], fila['cost_in_credits'], fila['length'], fila['max_atmosphering_speed'], fila['crew'], fila['passengers'],fila['cargo_capacity'], fila['consumables'], fila['hyperdrive_rating'], fila['MGLT'],fila['starship_class'], fila['pilots'], fila['films'])
                lista_naves.append(nave)
        print("Seleccione la nave a utilizar:")
        contador = 1
        for nave in lista_naves:
            print(f'\t{contador}-{nave.nombre}')
            contador += 1
        nave_seleccionada = int(input("--> "))
        if nave_seleccionada > 0 and nave_seleccionada <= len(lista_naves):
            return lista_naves[nave_seleccionada - 1]
        else:
            print("Selección invalida.")
            return self.seleccionar_nave()
    
    def seleccionar_armas(self):
        lista_armas = []
        with open("weapons.csv", "r") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                arma = Armas_csv(fila['id'], fila['name'], fila['model'], fila['manufacturer'], fila['cost_in_credits'], fila['length'], fila['type'], fila['description'], fila['films'])
                lista_armas.append(arma)
        print("\nSeleccione hasta 7 armas:")
        contador = 1
        for arma in lista_armas:
            print(f'\t{contador}-{arma.nombre}')
            contador += 1
        try:
            indices_seleccionados = input("Ingrese las armas que desea seleccionar separadas por comas: ").split(",")
            armas_seleccionadas = []
            for index in indices_seleccionados:
                num = int(index.strip())
                if num > 0 and num <= len(lista_armas):
                    armas_seleccionadas.append(lista_armas[num - 1])
                else:
                    print("\nIngrese solo numeros validos")
                    return self.seleccionar_armas()
        except ValueError:
            print("\nIngrese solo numeros validos")
            return self.seleccionar_armas()
        if len(armas_seleccionadas) > 7:
           print("\nSolo puedes seleccionar hasta 7 armas")
           return self.seleccionar_armas()
        return armas_seleccionadas
        
    def seleccionar_integrantes(self):
        lista_integrantes = []
        with open("characters.csv", "r") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                integrante = Integrantes_csv(fila['id'], fila['name'], fila['species'], fila['gender'], fila['height'], fila['weight'], fila['hair_color'], fila['eye_color'], fila['skin_color'], fila['year_born'], fila['homeworld'], fila['year_died'], fila['description'])
                lista_integrantes.append(integrante)
        print("\nSeleccione hasta 7 integrantes:")
        contador = 1
        for integrante in lista_integrantes:
            print(f'\t{contador}-{integrante.nombre}')
            contador += 1
        try:
            indices_seleccionados = input("Ingrese los integrantes que desea seleccionar separados por comas: ").split(",")
            integrantes_seleccionados = []
            for index in indices_seleccionados:
                num = int(index.strip())
                if num > 0 and num <= len(lista_integrantes):
                    integrantes_seleccionados.append(lista_integrantes[num - 1])
                else:
                    print("\nIngrese solo números válidos")
                    return self.seleccionar_integrantes()
        except ValueError:
            print("\nIngrese solo numeros validos")
            return self.seleccionar_integrantes()
        if len(integrantes_seleccionados) > 7:
           print("\nSolo puedes seleccionar hasta 7 integrantes")
           return self.seleccionar_integrantes()
        return integrantes_seleccionados
        
    def gestionar_misiones(self):
        while len(self.misiones_obj) < 5:
            continuar = input("Desea crear una nueva mision? (s/n): ").lower()
            if continuar != 's':
                break
            self.construir_mision()
    
    def modificar_mision(self):
        cedula = int(input("Ingrese su cedula para acceder a sus misiones: "))
        if cedula in self.misiones_usuarios:
            misiones = self.misiones_usuarios[cedula]
            print("\nMisiones disponibles:")
            contador = 1
            for mision in misiones:
                print(f'\t{contador}-{mision["nombre_mision"]}')
                contador += 1
            mision_seleccionada = int(input("Ingrese el numero de la mision que desea modificar--> "))
            if mision_seleccionada > 0 and mision_seleccionada <= len(misiones):
                mision = misiones[mision_seleccionada - 1]
                print("\n¿Qué desea modificar?\n1. Planeta \n2. Nave \n3. Armas \n4. Integrantes")
                opcion = int(input("--> "))
                if opcion == 1:
                    nuevo_planeta = self.seleccionar_planeta()
                    mision['planeta'] = nuevo_planeta
                    print(f"\nPlaneta cambiado a {nuevo_planeta.nombre}")
                elif opcion == 2:
                    nueva_nave = self.seleccionar_nave()
                    mision['nave'] = nueva_nave
                    print(f"\nNave cambiada a {nueva_nave.nombre}")
                elif opcion == 3:
                    self.modificar_armas(mision)
                elif opcion == 4:
                    self.modificar_integrantes(mision)
                else:
                    print("Seleccion invalida.")
                    return self.modificar_mision()
            else:
                print("\nIngrese solo numeros validos.")
                return self.modificar_mision()
        else:
            print("No se encontraron misiones para esta cedula.")
            return self.modificar_mision()

    def modificar_armas(self, mision):
        print("\nArmas actuales:")
        contador = 1
        for arma in mision['armas']:
            print(f'\t{contador}-{arma.nombre}')
            contador += 1
        print("\nQué desea hacer?\n1. Agregar armas\n2. Eliminar armas")
        opcion = int(input("--> "))
        if opcion == 1:
            nuevas_armas = self.seleccionar_armas()
            mision['armas'].extend(nuevas_armas)
        elif opcion == 2:
            contador = 1
            for arma in mision['armas']:
                print(f'\t{contador}-{arma.nombre}')
                contador += 1
            armas_a_eliminar = input("Ingrese los numeros de las armas a eliminar separadas por comas: ").split(",")
            indices_a_eliminar = [int(index.strip()) - 1 for index in armas_a_eliminar]
            for index in sorted(indices_a_eliminar, reverse=True):
                if index >= 0 and index < len(mision['armas']):
                    del mision['armas'][index]
                else:
                    print(f"Índice {index + 1} fuera de rango.")
        else:
            print("Selección invalida.")
            return self.modificar_armas(mision)

    def modificar_integrantes(self, mision):
        print("\nIntegrantes actuales:")
        contador = 1
        for integrante in mision['integrates']:
            print(f'\t{contador}-{integrante.nombre}')
            contador += 1
        print("\n¿Qué desea hacer?\n1. Agregar integrantes\n2. Eliminar integrantes")
        opcion = int(input("--> "))
        if opcion == 1:
            nuevos_integrantes = self.seleccionar_integrantes()
            mision['integrantes'].extend(nuevos_integrantes)
        elif opcion == 2:
            contador = 1
            for integrante in mision['integrates']:
                print(f'\t{contador}-{integrante.nombre}')
                contador += 1
            integrantes_a_eliminar = input("Ingrese los números de los integrantes a eliminar, separadas por comas: ").split(",")
            indices_a_eliminar = [int(index.strip()) - 1 for index in integrantes_a_eliminar]
        for index in sorted(indices_a_eliminar, reverse=True):
                if index > 0 and index <= len(mision['integrantes']):
                    del mision['integrantes'][index]
                else:
                    print(f"Índice {index + 1} fuera de rango.")
        else:
            print("Selección inválida.")
            return self.modificar_integrantes(mision)

    def visualizar_mision(self):
        cedula = int(input("Ingrese su cedula para acceder a sus misiones: "))
        if cedula in self.misiones_usuarios:
            misiones = self.misiones_usuarios[cedula]
            print("\nMisiones disponibles:")
            contador = 1
            for mision in misiones:
                print(f'\t{contador}-{mision["nombre_mision"]}')
                contador += 1
            mision_seleccionada = int(input("Ingrese el numero de la mision para ver los detalles--> "))
            if mision_seleccionada > 0 and mision_seleccionada <= len(misiones):
                mision = misiones[mision_seleccionada - 1]
                print("\nDetalles de la Misión:")
                print(f"Nombre de la misión: {mision['nombre_mision']}")
                print(f"Planeta destino: {mision['planeta'].nombre}")
                print(f"Nave a utilizar: {mision['nave'].nombre}")
                print("Armas a utilizar:")
                for arma in mision['armas']:
                    print(f"- {arma.nombre}")
                print("Integrantes de la misión:")
                for integrante in mision['integrantes']:
                    print(f"- {integrante.nombre}")
                while True:
                    print("\nDesea ver más informacion?")
                    opcion = int(input("1. Nave\n2. Armas\n3. Integrantes\n4. Salir\n--> "))
                    if opcion == 1:
                        print("\nInformacion de la Nave:")
                        print(f"Nombre: {mision['nave'].nombre}")
                        print(f"Modelo: {mision['nave'].modelo}")
                        print(f"Fabricante: {mision['nave'].fabricante}")
                        print(f"Costo en creditos: {mision['nave'].costo_en_creditos}")
                        print(f"Largo: {mision['nave'].largo}")
                        print(f"Velocidad en atmosfera: {mision['nave'].velocidad_en_atmosfera}")
                        print(f"Tripulacion: {mision['nave'].tripulacion}")
                        print(f"Pasajeros: {mision['nave'].pasajeros}")
                        print(f"Capacidad: {mision['nave'].capacidad}")
                        print(f"Consumibles: {mision['nave'].consumibles}")
                        print(f"Calificacion del hiperimpulsor: {mision['nave'].calificación_hiperimpulsor}")
                        print(f"MGLT: {mision['nave'].MGLT}")
                        print(f"Clase: {mision['nave'].clase}")
                        print(f"Pilotos: {mision['nave'].pilotos}")
                        print(f"Peliculas: {mision['nave'].peliculas}")
                    elif opcion == 2:
                        print("\nInformacion de las Armas:")
                        contador = 1
                        for arma in mision['armas']:
                            print(f'''\t{contador}. Nombre: {arma.nombre} 
                                  Modelo: {arma.modelo} 
                                  Fabricante: {arma.fabricante} 
                                  Costo en creditos: {arma.costo_en_creditos} 
                                  Largo: {arma.largo} 
                                  Tipo: {arma.tipo} 
                                  Descripcion: {arma.descripcion} 
                                  Peliculas: {arma.peliculas}''')
                            contador += 1
                    elif opcion == 3:
                        print("\nInformacion de los Integrantes:")
                        contador = 1
                        for integrante in mision['integrantes']:
                            print(f'''\t{contador}. Nombre: {integrante.nombre} 
                                  Especie: {integrante.especie} 
                                  Genero: {integrante.genero} 
                                  Altura: {integrante.altura} 
                                  Peso: {integrante.peso} 
                                  Color de cabello: {integrante.color_cabello}
                                  Color de ojos: {integrante.color_ojos} 
                                  Color de piel: {integrante.color_piel} 
                                  Año de nacimiento: {integrante.año_nacimiento} 
                                  Planeta: {integrante.planeta} 
                                  Año de muerte: {integrante.año_muerte} 
                                  Descripcion: {integrante.descripcion}''')
                            contador += 1
                    elif opcion == 4:
                        break
                    else:
                        print("Opcion invalida. Intentelo de nuevo.")
            else:
                print("\nIngrese solo numeros validos.")
                return self.visualizar_mision()
        else:
            print("No se encontraron misiones para esta cedula.")
            return self.visualizar_mision()
        
