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


	def test_temporada_1(self):
		'''  Caso temporada mes entre 4 y 8 '''
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 2, 'economica')
		valor_base = calculo_funciones.obtener_valor_base(boleto1.categoria_pasajero, boleto1.tipo_destino)
		valor_region = calculo_funciones.obtener_valor_region(boleto1.region)
		valor_temporada = calculo_funciones.obtener_valor_temporada(valor_base, valor_region, boleto1.mes)
		self.assertEqual(valor_temporada, 25)

	def test_temporada_2(self):
		'''  Caso temporada mes entre 1 y 3 '''
		boleto1 = pasajero.Pasajero('Adulto', 'Nacional', 'Europa', 4, 'economica')
		valor_base = calculo_funciones.obtener_valor_base(boleto1.categoria_pasajero, boleto1.tipo_destino)
		valor_region = calculo_funciones.obtener_valor_region(boleto1.region)
		valor_temporada = calculo_funciones.obtener_valor_temporada(valor_base, valor_region, boleto1.mes)
		self.assertEqual(valor_temporada, 25)

	def test_temporada_3(self):
		'''  Caso temporada mes entre 8 y 12 '''
		boleto1 = pasajero.Pasajero('Niño', 'Internacional', 'Sudamerica', 10, 'economica')
		valor_base = calculo_funciones.obtener_valor_base(boleto1.categoria_pasajero, boleto1.tipo_destino)
		valor_region = calculo_funciones.obtener_valor_region(boleto1.region)
		valor_temporada = calculo_funciones.obtener_valor_temporada(valor_base, valor_region, boleto1.mes)
		self.assertEqual(valor_temporada, 30)


if __name__ == '__main__':
	unittest.main()


#valor_temporada = obtener_valor_temporada(valor_base, valor_region, boleto.mes)*/