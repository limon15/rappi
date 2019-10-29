from cargar_data import *
from common import pedir_numero_entero
from informes import informes


def menu():
    print("\t\tBienvenido a Rappi.\n")
    salir = False
    opcion = 0
    restaurantes = []
    clientes = []
    rappitenderos = []
    while not salir:
        print("\n\t 1 - Carga de informacion predefinida.\n\t 2 - Carga de informacion manual.\n\t 3 - Pedido manual.\n\t 4 - Simulacion de pedidos.\n\t 5 - Informes.\n\t 6 - Salir.\n\n")
        opcion = pedir_numero_entero()
        if (opcion == 1):
            restaurantes = cargar_restaurantes(restaurantes)
            clientes = cargar_clientes(clientes)
            rappitenderos = cargar_rappitenderos(rappitenderos)
        elif (opcion == 2):
            volver_atras = False
            eleccion = 0
            while not volver_atras:
                print("\n\t 1 - Cargar un nuevo restaurante.\n\t 2 - Cargar un nuevo plato.\n\t 3 - Cargar un nuevo cliente.\n\t 4 - Cargar un nuevo rappitendero.\n\t 5 - Volver al menu anterior.\n\n")
                eleccion = pedir_numero_entero()
                if (eleccion == 1):
                    restaurantes = cargar_nuevo_restaurante(restaurantes)
                    # print(restaurantes)              
                elif (eleccion == 2):
                    if restaurantes:
                        nombres_restaurantes = [dic['Nombre'] for dic in restaurantes]
                        print("\tElija el restaurante para el cual desea cargar el plato: ")
                        # print(*[i, nombres_restaurantes[i] for i in nombres_restaurantes])
                        for index, value in enumerate(nombres_restaurantes):
                            print("\t\t{} - {}".format(index, value))
                        eleccion = pedir_numero_entero()
                        validar_eleccion = input("La eleccion elegida fue: {}. Si es correcto escriba 'si' de lo contrario escriba 'no': ".format(restaurantes[eleccion]['Nombre']))
                        while not (validar_eleccion.upper() == 'SI'):
                            validar_eleccion = input("Le eleccion elegida fue: {}. Si es correcto escriba 'si' de lo contrario escriba 'no': ".format(restaurantes[eleccion]['Nombre']))
                        restaurantes[eleccion]['Platos'].extend(cargar_nuevo_plato())
                        # print(restaurantes[eleccion])
                        # print(restaurantes)
                    else: 
                        print("No hay restaurantes cargados. Primero cargue un restaurante.")    
                elif (eleccion == 3):
                    clientes = cargar_nuevo_cliente(clientes)                     
                elif (eleccion == 4):
                    rappitenderos = cargar_nuevo_rappitendero(rappitenderos)
                    # print(rappitenderos)                  
                elif (eleccion == 5):
                    volver_atras = True                                                          
                else:
                    print("Error. La opcion ingresada no se encuentra en el menu.")                

        elif (opcion == 3):
            print("Opcion 3")
        elif (opcion == 4):
            print("Opcion 4")
        elif (opcion == 5):
            informes(clientes, restaurantes, rappitenderos)
        elif (opcion == 6):
            salir = True
        else:
            print("Error. La opcion ingresada no se encuentra en el menu.")
    print("Adios.")

menu()

                       