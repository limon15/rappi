# ● Restaurante
# ○ Nombre: string. Debe tener no menos que 5 caracteres y no más que 25.
# ○ Dirección: string. No debe estar vacía.
# ○ Teléfono: string. Puede contener únicamente números, espacios, guiones, signo
# ‘+’ y paréntesis.
# ○ Posición. Tupla que contiene:
# ■ Latitud: flotante.
# ■ Longitud: flotante.
# ○ Radio de entrega: flotante. Debe considerarse el km como su unidad.
# ○ Platos ofrecidos: conjunto de platos (ver entidad siguiente).
# ○ Total de ventas: flotante. Representa el acumulado de ventas del restaurante.
# ○ Moneda: igual al Plato, ver más abajo.

# ● Plato
# ○ Nombre: string. Debe tener no menos que 5 caracteres y no más que 25.
# ○ Precio: flotante

# ● Pedido
# ○ Conjunto de 1 o más platos con la cantidad pedida
# ○ Destino: Cliente

# ● Rappitendero
# ○ Nombre: string.
# ○ Propina acumulada: flotante.
# ○ Posición actual:
# ■ Latitud: flotante
# ■ Longitud: flotante
# ○ Pedido actual: Pedido que está siendo llevado al cliente
# 1

# ● Cliente
# ○ Nombre de usuario: string de entre 3 y 12 caracteres alfanuméricos, sin
# espacios.
# ○ Contraseña: string de 8 o más caracteres conteniendo por lo menos un dígito, un
# carácter en mayúscula, un carácter en minúscula y un símbolo.
# ○ Teléfono: string, misma restricción que para el restaurante.
# ○ Dirección: string.
# ○ Tupla
# ■ Latitud: flotante.
# ■ Longitud: flotante.
# ○ Rappicréditos: flotante.
import cargar_data

print("\t\tBienvenido a Rappi.\n")
def menu():
  def pedir_numero_entero():
    correcto = False
    num = 0
    while(not correcto):
      try:
        num = int(input("Introduce un numero entero referido a las opciones del menu: "))
        correcto = True
      except ValueError:
        print('Error. La opcion ingresada no es un numero entero.')
    return num

  salir = False
  opcion = 0

  while not salir:

    print("\n\t 1 - Carga de informacion predefinida.\n\t 2 - Carga de informacion manual.\n\t 3 - Pedido manual.\n\t 4 - Simulacion de pedidos.\n\t 5 - Informes.\n\t 6 - Salir.\n\n")

    opcion = pedir_numero_entero()

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
        print ("Opcion 2")
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
