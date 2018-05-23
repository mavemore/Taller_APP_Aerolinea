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

	def test_aerolinea_2(self):
		"""Declarar clases de equivalencia utilizadas"""
		valor_total=0
		self.assertEqual(valor_total,0)

	def test_aerolinea_1(self):
		"""CE0: Ejemplo
		Vuelo internacional, Europa, 2 adultos y 1 nino, Abril, economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 3, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 3, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 3, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1470.00)

	def test_aerolinea_2(self):
		"""CE0: Ejemplo
		Vuelo internacional, Europa, 2 adultos y 1 nino, Abril, economica"""
		boleto4 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 9, 'economica')
		boleto5 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 9, 'economica')
		boleto6 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 9, 'economica')
		lista_pasajero = [boleto4,boleto5,boleto6]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1568.00)

	def test_aerolinea_3(self):
		"""CE0: Ejemplo
		Vuelo internacional, Europa, 2 adultos y 1 nino, Abril, economica"""
		boleto7 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 13, 'economica')
		boleto8 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 13, 'economica')
		boleto9 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 13, 'economica')
		lista_pasajero = [boleto7,boleto8,boleto9]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1400.00)

if __name__ == '__main__':
	unittest.main()