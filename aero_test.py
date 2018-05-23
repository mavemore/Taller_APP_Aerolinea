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
		"""CE0, CE10, CE20, CE30, CE40, CE50
		Vuelo internacional, Europa, 2 adultos y 1 nino, Mayo, economica"""
		valor_total=0
		
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 5, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 5, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 5, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)

		self.assertEqual(valor_total,1540.00)

	def test_aerolinea_3(self):
		"""CE0, CE10, CE20, CE31, CE40, CE50
		Vuelo internacional, Europa, 2 adultos y 1 nino, Enero, economica"""
		valor_total=0
		
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 1, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 1, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 1, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)

		self.assertEqual(valor_total,1470.00)

	def test_aerolinea_4(self):
		"""CE0, CE10, CE20, CE32, CE40, CE50
		Vuelo internacional, Europa, 2 adultos y 1 nino, Diciembre, economica"""
		valor_total=0
		
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 12, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 12, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 12, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)

		self.assertEqual(valor_total,1568.00)

	def test_aerolinea_5(self):
		"""CE0, CE10, CE20, CE30, CE40, CE50
		Vuelo internacional, Norteamerica, 3 adultos, Junio, ejecutiva"""
		valor_total=0
		
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Norteamerica', 6, 'ejecutiva')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Norteamerica', 6, 'ejecutiva')
		boleto3 = pasajero.Pasajero('Adulto', 'Internacional', 'Norteamerica', 6, 'ejecutiva')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)

		self.assertEqual(valor_total,1446.00)

if __name__ == '__main__':
	unittest.main()