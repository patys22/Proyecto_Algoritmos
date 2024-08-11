from infoAPI import cargarPelis, cargarEspecies, cargarPersonajes, cargarPlaneta
from funciones import mostrar_peliculas, mostrar_especies, mostrar_planetas, buscar_personajes
from Usuario import Usuario

class App:
    def start(self):

        listaPeliculas = cargarPelis()
        listaEspecies = cargarEspecies()
        listaPersonajes = cargarPersonajes()
        listaPlanetas = cargarPlaneta()

        while True:
            print("\n\t\tBienvenido al mundo de Star Wars\n")
            menu=int(input("Seleccione una opcion del menu:\n\n\t1. Ver peliculas de la saga\n\t2. Ver especies de seres vivos de la saga\n\t3. Ver planetas\n\t4. Buscar personaje\n\t5. Grafico de cantidad de personajes en cada planeta\n\t6. Graficos de caracteristicas de naves\n\t7. Estadisticas sobre naves\n\t8. Construir mision\n\t9. Modificar mision\n\t10. Visualizar misiones\n\t11. Guardar misiones\n\t12. Cargar misiones\n\t13. Salir\n\t----> "))
            if menu==1:
                mostrar_peliculas(listaPeliculas)
            if menu==2:
                mostrar_especies(listaEspecies, listaPeliculas, listaPersonajes, listaPlanetas)
            if menu==3:
                mostrar_planetas(listaPeliculas, listaPlanetas, listaPersonajes)
            if menu==4:
                personaje_ingresado = input("Ingrese el nombre del personaje que desea buscar: ")
                busqueda = buscar_personajes(listaPersonajes, personaje_ingresado)
            if menu==5:
                None
            if menu==6:
                None
            if menu==7:
                None
            if menu==8:
                None
            if menu==9:
                None
            if menu==10:
                None
            if menu==11:
                None
            if menu==12:
                None
            if menu==13:
                print("\nVuelva pronto y que la fuerza te acompane")
                break
            elif menu > 13: 
                print('Ingrese una opcion valida')

    
