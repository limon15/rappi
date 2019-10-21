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

def menu():
    print(




    )
    print("\t\tBienvenido a Rappi.\n Seleccione la opcion con la que desea operar:")

menu()
# def cargar_data_predefinida():


    # clientes = cargar_clientes()
    # rappitenderos = cargar_rappitenderos()

    # return restaurantes
    # , clientes, rappitenderos

# print(cargar_data_predefinida())
