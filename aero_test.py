import unittest
import pasajero
import calculo_funciones

class TestAerolinea(unittest.TestCase):
	"""
	def test_aerolinea_1(self):
		CE0: Ejemplo
		Vuelo internacional, Europa, 2 adultos y 1 nino, Abril, economica
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 4, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 4, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1540.00)
	"""		
	"""
	ID 1
	def test_aerolinea_1(self):
		
		CE0 CE2 CE4 CE10 CE6 CE9
		Vuelo internacional, Europa, 2 adultos y 1 nino, Febrero, economica
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 2, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 2, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 2, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1470.00)
	"""
		
	"""	
	ID 2
	
	def test_aerolinea_1(self):
	
		CE0 CE2 CE4 CE10 CE7 CE9
		Vuelo internacional, Europa, 2 adultos y 1 nino, Mayo, economica
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 5, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 5, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 5, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1540.00)
			
	"""
	"""
	ID 3
	def test_aerolinea_1(self):
		
		CE0 CE2 CE4 CE10 CE8 CE9
		Vuelo internacional, Europa, 2 adultos y 1 nino, Noviembre, economica	
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 11, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 11, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 11, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1568.00)
	"""	
	"""	
	ID 4
	def test_aerolinea_1(self):
		
		CE0 CE2 CE4 CE10 CE6 CE9
		Vuelo internacional, Europa, 2 adultos y 1 nino, Enero, economica	
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 1, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 1, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 1, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1470.00)
	"""
	
	"""
	ID 5"""	
	def test_aerolinea_1(self):
		"""		
		CE0 CE2 CE4 CE10 CE8 CE9
		Vuelo internacional, Europa, 2 adultos y 1 nino, Diciembre, economica"""	
		boleto1 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 11, 'economica')
		boleto2 = pasajero.Pasajero('Adulto', 'Internacional', 'Europa', 11, 'economica')
		boleto3 = pasajero.Pasajero('Niño', 'Internacional', 'Europa', 11, 'economica')
		lista_pasajero = [boleto1,boleto2,boleto3]
		valor_total = calculo_funciones.obtener_total(lista_pasajero)
		self.assertEqual(valor_total, 1568.00)	

		
	def test_aerolinea_2(self):
		"""Declarar clases de equivalencia utilizadas"""
		valor_total=0
		self.assertEqual(valor_total,0)

if __name__ == '__main__':
	unittest.main()
