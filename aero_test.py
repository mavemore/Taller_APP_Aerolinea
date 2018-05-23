import unittest
import pasajero
import calculo_funciones

class TestAerolinea(unittest.TestCase):

	def test_aerolinea_1(self):
		"""P1: Ejemplo
		Vuelo internacional, Europa, 2 adultos, Abril, economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
		lista_pasajero = [boleto1,boleto2]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1100.00)

	def test_aerolinea_2(self):
		"""P2: Ejemplo
		Vuelo nacional, 1 niño, Febrero, ejecutiva
		Vuelo internacional, 1 tercera edad, Europa, Diciembre, ejecutiva"""
		boleto1 = pasajero.Pasajero('Niño', 'Nacional', '', 2, 'ejecutiva')
		boleto2 = pasajero.Pasajero('Tercera', 'Internacional', 'Europa', 12, 'ejecutiva')
		lista_pasajero = [boleto1,boleto2]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 575.50)

	def test_aerolinea_3(self):
		"""P3: Ejemplo
		Vuelo internacional, 1 niño, Norteamérica, Octubre, económica"""
		boleto1 = pasajero.Pasajero('Niño', 'Internacional', 'Norteamerica', 10, 'economica')
		lista_pasajero = [boleto1]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 358.40)

if __name__ == '__main__':
	unittest.main()