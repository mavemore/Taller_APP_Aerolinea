import unittest
import pasajero
import calculo_funciones


class TestAerolinea(unittest.TestCase):
	def test_temporada_1(self):
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 1, 'ejecutiva')
		lista_pasajero = [boleto1]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 545.00)

	def test_temporada_2(self):
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'ejecutiva')
		lista_pasajero = [boleto1]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 570.00)

	def test_temporada_3(self):
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 10, 'ejecutiva')
		lista_pasajero = [boleto1]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 580)


if __name__ == '__main__':
	unittest.main()





