from infoAPI import cargarPelis, cargarEspecies, cargarPersonajes, cargarPlaneta, cargarNaves, cargarVehiculos
from funciones import mostrar_peliculas, mostrar_especies, mostrar_planetas, buscar_personajes

class App:
    def start(self):

        # listaPeliculas = cargarPelis()
        # listaEspecies = cargarEspecies()
        # listaPersonajes = cargarPersonajes()
        # listaPlanetas = cargarPlaneta()

        while True:
            print("\n\t\tBienvenido al mundo de Star Wars\n")
            menu=int(input("Seleccione una opcion del menu:\n\n\t1. Ver peliculas de la saga\n\t2. Ver especies de seres vivos de la saga\n\t3. Ver planetas\n\t4. Buscar personaje\n\t5. Grafico de cantidad de personajes en cada planeta\n\t6. Graficos de caracteristicas de naves\n\t7. Estadisticas sobre naves\n\t8. Construir mision\n\t9. Modificar mision\n\t10. Visualizar misiones\n\t11. Guardar misiones\n\t12. Cargar misiones\n\t13. Salir\n\t----> "))
            if menu==1:
                listaPeliculas = cargarPelis()
                mostrar_peliculas(listaPeliculas)
            elif menu==2:
                # mostrar_especies(listaEspecies, listaPeliculas, listaPersonajes, listaPlanetas)
                None
            elif menu==3:
                # mostrar_planetas(listaPeliculas, listaPlanetas, listaPersonajes)
                None
            elif menu==4:
                listaPeliculas = cargarPelis()
                listaPersonajes = cargarPersonajes()
                listaEspecies = cargarEspecies()
                listaNaves = cargarNaves()
                listaVehiculos = cargarVehiculos()
                while True:
                    personaje_ingresado = input("\nIngrese el nombre del personaje que desea buscar y si desea regresar al menu ingrese 0: \n---> ")
                    if personaje_ingresado == "0":
                        break
                    else:
                        busqueda = buscar_personajes(listaPersonajes, personaje_ingresado, listaNaves, listaPeliculas, listaEspecies, listaVehiculos)
                        
                
            elif menu==5:
                None
            elif menu==6:
                None
            elif menu==7:
                None
            elif menu==8:
                None
            elif menu==9:
                None
            elif menu==10:
                None
            elif menu==11:
                None
            elif menu==12:
                None
            elif menu==13:
                print("\nVuelva pronto y que la fuerza te acompane")
                break
            elif menu > 13: 
                print('Ingrese una opcion valida')