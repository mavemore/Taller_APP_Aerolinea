import unittest
import pasajero
import calculo_funciones

class TestAerolinea(unittest.TestCase):

	def test_aerolinea_1(self):
		"""CE0: Ejemplo
		Vuelo internacional, Europa, 2 adultos y 1 nino, Abril, economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
		boleto3 = pasajero.Pasajero('Nino', 'Internacional', 'Europa', 4, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1540.00)

	def test_aerolinea_2(self):
		"""CE0,CE2,CE4,CE6,CE10 
		Vuelo Internacional, Europa, 1 nino y 1 adulto, Febrero, Ejecutiva"""
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 2, 'ejecutiva')
		boleto3 = pasajero.Pasajero('Nino', 'Internacional', 'Europa', 2, 'ejecutiva')
		lista_pasajero = [boleto2,boleto3]
		valor_total= calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,985)

	def test_aerolinea_3(self):
		"""CE0,CE2,CE4,CE6,CE10 
		  Vuelo nacional,  2 adultos, Noviembre, economica"""
		boleto1 = pasajero.Pasajero('Adulto', 'Nacional', '', 11, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Nacional', '', 11, 'economica')
		lista_pasajero = [boleto1,boleto2]
		valor_total= calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total,112)

if __name__ == '__main__':
	unittest.main()