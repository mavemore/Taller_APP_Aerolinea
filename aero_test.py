import unittest
import pasajero
import calculo_funciones

class TestAerolinea(unittest.TestCase):

	'''

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

		'''

	#ID1
	def test_aerolinea_temporada_baja(self):
		"""Vuelo Internacional, Europa, 2 adultos y un adulto mayor, Enero, economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 1, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 1, 'economica')
		boleto3 = pasajero.Pasajero('Tercera', 'Internacional', 'Sudamerica', 1, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1050.00)

	#ID2
	def test_aerolinea_temporada_media(self):
		"""Vuelo internacional, Europa, 1 adultos y 2 nino, Mayo, ejecutiva"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Norteamerica', 5, 'ejecutiva')
		boleto2 = pasajero.Pasajero('Niño', 'Internacional', 'Norteamerica', 5, 'ejecutiva')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Norteamerica', 5, 'ejecutiva')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1226.00)

	#ID3
	def test_aerolinea_temporada_alta(self):
		"""Vuelo internacional, Sudamerica, 5 adultos, Noviembre, economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 11, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 11, 'economica')
		boleto3 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 11, 'economica')
		boleto4 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 11, 'economica')
		boleto5 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 11, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3,boleto4,boleto5]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1960.00)


if __name__ == '__main__':
	unittest.main()