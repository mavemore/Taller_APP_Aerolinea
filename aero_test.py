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
		""" 
		CE0: Adulto, CE10: Valido, CE21: Europa, CE31: 3, CE40: economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 3, 'economica')
		boleto2 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 3, 'economica')
		boleto3 = pasajero.Pasajero('Tercera', 'Internacional', 'Europa', 3, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,1417.5)

	def test_aerolinea_3(self):
		""" 
		CE1: Adulto, Internacional, Europa, 3, economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 10, 'economica')
		boleto2 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 10, 'economica')
		boleto3 = pasajero.Pasajero('Tercera', 'Internacional', 'Europa', 10, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,1512.0)

	def test_aerolinea_4(self):
		""" 
		CE0: Adulto, CE10: Valido, CE21: Europa, CE31: 3, CE40: economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 10, 'ejecutiva')
		boleto2 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 10, 'ejecutiva')
		boleto3 = pasajero.Pasajero('Tercera', 'Internacional', 'Europa', 10, 'ejecutiva')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,1572.0)


if __name__ == '__main__':
	unittest.main()