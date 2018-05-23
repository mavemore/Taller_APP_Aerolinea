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
		"""P1"""
		boleto1 = pasajero.Pasajero('Adulto','Internacional','Europa',3,'economica')
		"""P2"""
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 9, 'economica')
		"""P3"""
		boleto3= pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,1635)

if __name__ == '__main__':
	unittest.main()