import cargar_data
import common

print("\t\tBienvenido a Rappi.\n")
def menu():

  salir = False
  opcion = 0
  restaurantes = []
  clientes = []
  rappitenderos = []
  while not salir:

    print("\n\t 1 - Carga de informacion predefinida.\n\t 2 - Carga de informacion manual.\n\t 3 - Pedido manual.\n\t 4 - Simulacion de pedidos.\n\t 5 - Informes.\n\t 6 - Salir.\n\n")

    opcion = common.pedir_numero_entero()

    if (opcion == 1):
      restaurantes = cargar_data.cargar_restaurantes()
      clientes = cargar_data.cargar_clientes()
      rappitenderos = cargar_data.cargar_rappitenderos()
      nombres_restaurantes = [dic['Nombre'] for dic in restaurantes]
      nombres_clientes = [dic['Nombre'] for dic in clientes]
      nombres_rappitenderos = [dic['Nombre'] for dic in rappitenderos]             
      print("Se cargaron {0} restaurantes:".format(len(nombres_restaurantes)), *[i for i in nombres_restaurantes], sep="\n\t")
      print("Se cargaron {0} clientes:".format(len(nombres_clientes)), *[i for i in nombres_clientes], sep="\n\t")
      print("Se cargaron {0} rappitenderos:".format(len(nombres_rappitenderos)), *[i for i in nombres_rappitenderos], sep="\n\t")
    #   index, value in enumerate(test_list)  
    elif (opcion == 2):
        volver_atras = False
        eleccion = 0
        while not volver_atras:
            print("\n\t 1 - Cargar un nuevo restaurante.\n\t 2 - Cargar un nuevo plato.\n\t 3 - Cargar un nuevo cliente.\n\t 4 - Cargar un nuevo rappitendero.\n\t 5 - Volver al menu anterior.\n\n")
            eleccion = common.pedir_numero_entero()
            if (eleccion == 1):
                cargar_data.cargar_nuevo_restaurante(restaurantes)               
            # elif (eleccion == 2):   
            #     print("Opcion 3")   
            # elif (eleccion == 3):
            # elif (eleccion == 4):
            elif (eleccion == 5):
                volver_atras = True                                                          
            else:
                print("Error. La opcion ingresada no se encuentra en el menu.")                

    elif (opcion == 3):
        print("Opcion 3")
    elif (opcion == 4):
        print("Opcion 4")
    elif (opcion == 5):
        print("Opcion 5")
    elif (opcion == 6):
        salir = True
    else:
        print("Error. La opcion ingresada no se encuentra en el menu.")

  print("Adios.")

menu()
