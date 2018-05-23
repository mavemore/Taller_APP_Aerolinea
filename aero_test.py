import unittest
import pasajero
import calculo_funciones

class TestAerolinea(unittest.TestCase):

        def test_aerolinea_1(self):
                """CE31: 
                Vuelo internacional, Europa, 2 adultos y 1 nino, Abril, economica"""
                boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
                boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
                boleto3 = pasajero.Pasajero('Nino', 'Internacional', 'Europa', 4, 'economica')
                lista_pasajero = [boleto1,boleto2,boleto3]
                valor_total = calculo_funciones.obtener_total(lista_pasajero)
                self.assertEqual(valor_total, 1540.00)

        def test_aerolinea_2(self):
                """CE30:
                Vuelo internacional, Norteamerica, 1 adulto, 1 nino y 1 tercera edad, Febrero, ejecutiva"""
                boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Norteamerica', 2, 'ejecutiva')
                boleto2 = pasajero.Pasajero('Nino', 'Internacional', 'Norteamerica', 2, 'ejecutiva')
                boleto3 = pasajero.Pasajero('Tercera', 'Internacional', 'Norteamerica', 2, 'ejecutiva')
                lista_pasajero = [boleto1,boleto2,boleto3]
                valor_total = calculo_funciones.obtener_total(lista_pasajero)
                self.assertEqual(valor_total, 1225.50)

        def test_aerolinea_3(self):
                """CE32:
                Vuelo internacional, Sudamerica, 2 adulto, 1 nino y 3 tercera edad, Diciembre, economica"""
                boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 12, 'economica')
                boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 12, 'economica')
                boleto3 = pasajero.Pasajero('Nino', 'Internacional', 'Sudamerica', 12, 'economica')
                boleto4 = pasajero.Pasajero('Tercera', 'Internacional', 'Sudamerica', 12, 'economica')
                boleto5 = pasajero.Pasajero('Tercera', 'Internacional', 'Sudamerica', 12, 'economica')
                boleto6 = pasajero.Pasajero('Tercera', 'Internacional', 'Sudamerica', 12, 'economica')
                lista_pasajero = [boleto1,boleto2,boleto3,boleto4,boleto5,boleto6]
                valor_total = calculo_funciones.obtener_total(lista_pasajero)
                self.assertEqual(valor_total, 2072.00)


if __name__ == '__main__':
	unittest.main()
