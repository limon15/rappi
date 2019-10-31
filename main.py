from common import devolver_opcion_elegida_validada_desde_lista
from informes import informes
from pedidos import pedido_manual
from simulaciones import simulacion_de_pedidos
from prettytable import PrettyTable, ALL
from cargar_data import carga_manual, cargar_predefinida

def imprimir_titulo_seccion(seccion):
    t = PrettyTable(['{}'.format(seccion.upper())])
    t.border = True  
    t.hrules = ALL    
    t.padding_width = 30
    t.vertical_char = ' '
    t.horizontal_char = "."    
    t.junction_char = "."
    print(t, "\n")

def imprimir_titulo_inicio_rappi():
    t = PrettyTable(['Bienvenido a Rappi ~'])
    t.border = True  
    t.hrules = ALL    
    t.vertical_char = '|'
    t.horizontal_char = "|"    
    t.junction_char = "|"
    t.padding_width = 30
    print(t, "\n")

def menu():
    imprimir_titulo_inicio_rappi()
    restaurantes = []
    clientes = []
    rappitenderos = []
    opciones = ["Carga de informacion predefinida.",  "Carga de informacion manual.", "Pedido manual.", "Simulacion de pedidos.", "Informes.", "Salir."] 
    tabulacion = 1
    opcion_elegida = devolver_opcion_elegida_validada_desde_lista(opciones, tabulacion)
    salir = len(opciones)-1
    while opcion_elegida != salir:   
        if (opcion_elegida == 0):
            imprimir_titulo_seccion("carga de informacion predefinida")
            clientes, restaurantes, rappitenderos = cargar_predefinida(clientes, restaurantes, rappitenderos)
        elif (opcion_elegida == 1):
            imprimir_titulo_seccion("carga de informacion manual")
            clientes, restaurantes, rappitenderos = carga_manual(clientes, restaurantes, rappitenderos)
        elif (opcion_elegida == 2):
            imprimir_titulo_seccion("pedido manual")
            pedido_manual(clientes, restaurantes, rappitenderos)
        elif (opcion_elegida == 3):
            imprimir_titulo_seccion("simulaciones")
            clientes, restaurantes, rappitenderos = simulacion_de_pedidos(clientes, restaurantes, rappitenderos)
        elif (opcion_elegida == 4):
            imprimir_titulo_seccion("informes")         
            informes(clientes, restaurantes, rappitenderos)
        opcion_elegida = devolver_opcion_elegida_validada_desde_lista(opciones, tabulacion)    
    saludo = "Gracias por utilizar nuestros servicios ¡Hasta pronto!"
    print(saludo)

menu()

                       