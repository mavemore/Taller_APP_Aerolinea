# -*- coding: utf-8 -*-
import unittest
import pasajero
import calculo_funciones

class TestAerolinea(unittest.TestCase):

 ######## PRUEBAS TALLER #############
	def test_aerolinea_3(self):
		"""CE1: Ejemplo1"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 3, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 3, 'economica')
		boleto3 = pasajero.Pasajero('Adulto', 'Internacional', 'Sudamerica', 3, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1101.00)

	def test_aerolinea_5(self):
		"""CE2: Ejemplo2"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Norteamerica', 7, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Norteamerica', 7, 'economica')
		lista_pasajero = [boleto1,boleto2]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 924.00)
	def test_aerolinea_6(self):
		"""CE3: Ejemplo3"""
		
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 12, 'ejecutiva')
		lista_pasajero = [boleto1]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 580.00)


if __name__ == '__main__':
	unittest.main()