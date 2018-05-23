import unittest
import pasajero
import calculo_funciones

class TestAerolinea(unittest.TestCase):

	def test_aerolinea_1(self):
		"""P1: 
		Vuelo internacional, Europa, 2 adultos y 1 nino, Abril, economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 4, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1540.00)

	def test_aerolinea_2(self):
		"""P2
		Vuelo nacional, 1 adultos y 1 nino, febrero, ejecutiva"""
		boleto1 = pasajero.Pasajero('Adulto', 'Nacional', '', 2, 'ejecutiva')
		boleto2 = pasajero.Pasajero('Niño', 'Nacional', '', 2, 'ejecutiva')
		lista_pasajero = [boleto1,boleto2]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,124.00)
	def test_aerolinea_3(self):
		"""P2
		Vuelo nacional, 1 adultos y 1 tercera edad, noviembre, economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Nacional', '', 11, 'economica')
		boleto2 = pasajero.Pasajero('Tercera', 'Nacional', '', 11, 'economica')
		lista_pasajero = [boleto1,boleto2]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,100.80)

if __name__ == '__main__':
	unittest.main()