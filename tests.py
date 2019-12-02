import unittest
from pedidos import actualizar_ganancias_rappitendero, actualizar_ganancias_cliente

class PruebasActualizarGanancias(unittest.TestCase):

    def test_actualizar_ganancias_rappitendero(self):
        print("Testeando actualizacion de ganancias del rappitendero con valor de pedido igual a 0.")
        self.assertEqual(actualizar_ganancias_rappitendero(0), 0)
        print("Testeando actualizacion de ganancias del rappitendero con valor de pedido menor a 0.")        
        self.assertEqual(actualizar_ganancias_rappitendero(-1100), 0)   
        print("Testeando actualizacion de ganancias del rappitendero con valor de pedido mayor a 0.")              
        self.assertEqual(actualizar_ganancias_rappitendero(200), 10)
        print("Testeando instancia devuelta de la actualizacion de ganancias del rappitendero.")         
        self.assertIsInstance(actualizar_ganancias_rappitendero(5050), float)
        print("Testeando que el valor devuelto de la actualizacion de ganancias del rappitendero sea mayor al recibido.")                 
        self.assertGreaterEqual(1000, actualizar_ganancias_rappitendero(1000))
        print("Testeando que el valor devuelto de la actualizacion de ganancias del rappitendero sea el '%5' del pedido.\n")
        self.assertEqual(actualizar_ganancias_rappitendero(200), round(0.05*200),2)        


    def test_actualizar_ganancias_cliente(self):
        print("Testeando actualizacion de ganancias del cliente con valor de pedido igual a 0.")
        self.assertEqual(actualizar_ganancias_cliente(0), 0)
        print("Testeando actualizacion de ganancias del cliente con valor de pedido menor a 0.")        
        self.assertEqual(actualizar_ganancias_cliente(-1100), 0)   
        print("Testeando actualizacion de ganancias del cliente con valor de pedido entre 1 y 199")              
        self.assertEqual(actualizar_ganancias_cliente(15), 0.75)
        print("Testeando actualizacion de ganancias del cliente con valor de pedido entre 200 y 1000")              
        self.assertEqual(actualizar_ganancias_cliente(550), 55)      
        print("Testeando actualizacion de ganancias del cliente con valor de pedido mayor a 1000.")              
        self.assertEqual(actualizar_ganancias_cliente(4700), 705)          
        print("Testeando instancia devuelta de la actualizacion de ganancias del cliente.")         
        self.assertIsInstance(actualizar_ganancias_cliente(5050), float)
        print("Testeando que el valor devuelto de la actualizacion de ganancias del cliente sea mayor al recibido.\n")                 
        self.assertGreaterEqual(1000, actualizar_ganancias_cliente(1000))


if __name__ == '__main__':
    unittest.main()