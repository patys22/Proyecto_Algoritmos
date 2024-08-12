import csv
from Usuario import Usuario
from Mision import Mision
from Planeta_csv import Planeta_csv
from Nave_csv import Nave_csv
from Armas_csv import Armas_csv
from Integrantes_csv import Integrantes_csv

class App_paty:
    usuarios_obj=[]
    misiones_obj=[]

    def start(self):
        self.construir_mision()
        self.gestionar_misiones()
       
    def construir_mision(self):
        print("Ingrese sus datos para poder construir una mision: ")
        cedula=int(input("\tCedula: "))
        usuario_seleccionado=self.buscar_usuario_lineal(cedula)
        if not usuario_seleccionado:
            nombre=input("\tNombre: ")
            apellido=input("\tApellido: ")
            self.registrar_usuario(cedula, nombre, apellido)
        else:
            nombre=usuario_seleccionado.nombre
            apellido=usuario_seleccionado.apellido
        print("Puede comenzar a construir su mision.")
        nombre_mision=input("\nIngrese el nombre de la mision: ")
        
        planeta=self.seleccionar_planeta()
        nave=self.seleccionar_nave()
        armas=self.seleccionar_armas()
        integrantes=self.seleccionar_integrantes()

        print("\nResumen de la Misión:")
        print(f"Nombre de la misión: {nombre_mision}")
        print(f"Planeta destino: {planeta.nombre}")
        print(f"Nave a utilizar: {nave.nombre}")
        print("Armas a utilizar:")
        for arma in armas:
            print(f"- {arma.nombre}")
        print("Integrantes de la mision:")
        for integrante in integrantes:
            print(f"- {integrante.nombre}")

        return {
            "nombre_mision": nombre_mision,
            "planeta": planeta,
            "nave": nave,
            "armas": armas,
            "integrantes": integrantes
        }
    
    def registrar_usuario(self, cedula, nombre, apellido):
        nuevo_usuario = Usuario(cedula, nombre, apellido)
        self.usuarios_obj.append(nuevo_usuario)

    def buscar_usuario_lineal(self, cedula):
        for usuario in self.usuarios_obj:
            if usuario.cedula==cedula:
                return usuario
        return None
    
    def seleccionar_planeta(self):
        lista_planetas = []
        with open("planets.csv", 'r') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                planeta = Planeta_csv(
                    fila['id'], fila['name']
                )
                lista_planetas.append(planeta)
        print("Seleccione el planeta destino:")
        contador=1
        for planeta in lista_planetas:
            print(f'\t{contador}-{planeta.nombre}')
            contador+=1
        planeta_seleccionado=int(input("--> "))
        if planeta_seleccionado > 0 and planeta_seleccionado <= len(lista_planetas):
            return lista_planetas[planeta_seleccionado-1]
        else:
            print("Selección inválida.")
            return self.seleccionar_planeta()
        
    
    def seleccionar_nave(self):
        lista_naves = []
        with open("starships.csv", 'r') as f:
            lector = csv.DictReader(f)
            for fila in lector:
                nave = Nave_csv(
                    fila['id'], fila['name']
                )
                lista_naves.append(nave)
        print("Seleccione la nave a utilizar:")
        contador=1
        for nave in lista_naves:
            print(f'\t{contador}-{nave.nombre}')
            contador+=1
        nave_seleccionada=int(input("--> "))
        return lista_naves[nave_seleccionada-1]

    def seleccionar_armas(self):
        lista_armas = []
        with open("weapons.csv", "r") as f:
            lector = csv.DictReader(f)
            for fila in lector:
                arma = Armas_csv(
                        fila['id'], fila['name']
                    )
                lista_armas.append(arma)
        print("\nSeleccione hasta 7 armas:")
        contador = 1
        for arma in lista_armas:
            print(f'\t{contador}-{arma.nombre}')
            contador+=1
        try:
            indices_seleccionados = input("Ingrese las armas que desea seleccionar separadas por comas: ").split(",")
            armas_seleccionadas = []
            for index in indices_seleccionados:
                num = int(index.strip())
                if num > 0 and num <= len(lista_armas):
                    armas_seleccionadas.append(lista_armas[num - 1])
                else:
                    print("\nIngrese solo números válidos")
                    return self.seleccionar_armas()
        except ValueError:
            print("\nIngrese solo números válidos")
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
                integrante = Integrantes_csv(
                        fila['id'], fila['name']
                        )
                lista_integrantes.append(integrante)
        print(f"\nSeleccione hasta 7 integrantes:")
        contador = 1
        for integrante in lista_integrantes:
            print(f'\t{contador}-{integrante.nombre}')
            contador+=1
        indices_seleccionados = input(f"Ingrese los integrantes que desee seleccionar separados por comas: ").split(",")
        integrantes_seleccionados = [lista_integrantes[int(index) - 1] for index in indices_seleccionados if 0 < int(index) <= len(lista_integrantes)]
        if len(integrantes_seleccionados) > 7:
            print(f"\nSolo puedes seleccionar hasta 7 integrantes")
            return self.seleccionar_integrantes()
        return integrantes_seleccionados
        
    def gestionar_misiones(self):
        misiones_obj = []
        while len(misiones_obj) < 5:
            continuar = input("¿Desea crear una nueva mision? (s/n): ").lower()
            if continuar != 's':
                break
            mision = self.construir_mision()
            misiones_obj.append(mision)
            print(f"Mision '{mision['nombre_mision']}' creada con exito")

    def acceder_misiones(self):
        cedula = int(input("Ingrese su cédula para acceder a sus misiones: "))
        misiones_usuario = self.buscar_misiones_por_cedula(cedula)
        
        if not misiones_usuario:
            print("No se encontraron misiones para esta cédula.")
            return self.acceder_misiones()
        else:
            print("\nMisiones disponibles:")
            contador=1
            for mision in misiones_usuario:
                print(f'\t{contador}-{mision.nombre}')
                contador+=1
            mision_seleccionada=int(input("Ingrese el número de la misión para ver los detalles--> "))
            if mision_seleccionada > 0 and mision_seleccionada <= len(misiones_usuario):
                    mision_seleccionada.append(misiones_usuario[mision_seleccionada - 1])
            else:
                print("\nIngrese solo números válidos")
                return self.acceder_misiones()
            
    def ver_mision(self, mision):
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

    def buscar_mision_lineal(self, cedula):
            for mision in self.misiones_obj:
                if mision.cedula==cedula:
                    return mision
            return None

    def buscar_misiones_por_cedula(self, cedula):
        misiones_usuario = [mision for mision in self.misiones_obj if mision['cedula'] == cedula]
        return misiones_usuario
    
    def modificar_mision(self):
        if len(self.misiones_obj) == 0:
            print("No tienes misiones registradas para modificar")
            return
        contador = 1
        for mision in self.misiones_obj:
            print(f"{contador}. {mision['nombre_mision']}")
            contador += 1
        seleccion = int(input("Ingrese el número de la misión que desea modificar--> "))
        if 0 <= seleccion < len(self.misiones_obj):
            mision = self.misiones_obj[seleccion-1]
            self.editar_mision(mision)
        else:
            print("Selección inválida.")




    def editar_mision(self, mision):
        while True:
            print('''
                  ¿Que desea modificar?
                  1. Cambiar planeta
                  2. Cambiar nave
                  3. Agregar armas
                  4. Eliminar armas
                  5. Agregar integrantes
                  6. Eliminar integrantes
                  7. Finalizar edición''')
            opcion = input("Ingrese una opción--> ")

            if opcion == '1':
                mision['planeta'] = self.seleccionar_planeta()
            elif opcion == '2':
                mision['nave'] = self.seleccionar_nave()
            elif opcion == '3':
                nuevas_armas = self.seleccionar_armas()
                mision['armas'].extend(nuevas_armas)
            elif opcion == '4':
                self.eliminar_armas(mision)
            elif opcion == '5':
                mision['integrantes'] = self.seleccionar_integrantes()
            elif opcion == '6':
                nuevos_integrantes = self.seleccionar_integrantes()
                mision['integrantes'].extend(nuevos_integrantes)
            elif opcion == '7':
                print("Edición finalizada.")
                break
            else:
                print("Opción inválida, intente de nuevo.")

    def seleccionar_planeta_nuevo(self):
        print("Seleccione el nuevo planeta destino:")
        self.seleccionar_planeta()
        print("Planeta cambiado exitosamente.")

    def seleccionar_nave_nueva(self):
        print("Seleccione la nueva nave a utilizar:")
        self.seleccionar_nave()
        print("Nave cambiada exitosamente.")

    def seleccionar_armas_nuevas(self):
        self.seleccionar_armas()

    def eliminar_armas(self, mision):
        print("\nArmas actuales en la misión:")
        contador = 1
        for arma in mision['armas']:
            print(f"{contador}. {arma.nombre}")
            contador += 1
        indices = input("Ingrese los números de las armas que desea eliminar, separadas por comas: ").split(",")
        indices = [int(index) - 1 for index in indices if 0 <= int(index) - 1 < len(mision['armas'])]
        mision['armas'] = [arma for i, arma in enumerate(mision['armas']) if i not in indices]
        print("Armas eliminadas correctamente.")

    def eliminar_integrantes(self, mision):
        print("\nIntegrantes actualmente en la misión:")
        contador = 1
        for integrante in mision['integrante']:
            print(f"{contador}. {integrante.nombre}")
            contador += 1
        indices = input("Ingrese los números de los integrantes que desea eliminar, separados por comas: ").split(",")
        indices = [int(index) - 1 for index in indices if 0 <= int(index) - 1 < len(mision['integrantes'])]
        mision['integrantes'] = [integrante for i, integrante in enumerate(mision['integrantes']) if i not in indices]
        print("Integrantes eliminados correctamente.")

    def seleccionar_integrantes_nuevos(self):
        self.seleccionar_integrantes()

    
    
