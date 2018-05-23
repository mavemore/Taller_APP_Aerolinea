import unittest
import pasajero
import calculo_funciones

class TestAerolinea(unittest.TestCase):

	def test_aerolinea_1(self):
		"""CE0: Ejemplo
		Vuelo internacional, Europa, 2 adultos y 1 nino, Abril, economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 4, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1540.00)

	def test_aerolinea_enero(self):
		"""Vuelo internacional, Europa, 1 adulto, enero, económica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 1, 'economica')
		lista_pasajero = [boleto1]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,525)

	def test_aerolinea_abril(self):
		"""Vuelo internacional, Europa, 1 adulto, abril, económica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
		lista_pasajero = [boleto1]
		valor_total =  calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,550)

	def test_aerolinea_septiembre(self):
		"""Vuelo internacional, Europa, 1 adulto, septiembre, económica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 9, 'economica')
		lista_pasajero = [boleto1]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,560)

if __name__ == '__main__':
	unittest.main()