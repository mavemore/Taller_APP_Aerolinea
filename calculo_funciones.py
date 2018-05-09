"""Este modulo posee las funciones necesarias para calcular
el valor total de los pasajes de la aerolinea."""
import pasajero

def  obtener_valor_base(categoria_pasajero, tipo_destino):
	"""Retorna el valor base del boleto de acuerdo a la categoria del 
	pasajero y su destino."""
	valor_base = 0
	if tipo_destino == 'Nacional':
		if categoria_pasajero == "Adulto":
			valor_base = 50
		elif categoria_pasajero == "Niño":
			valor_base = 30
		elif categoria_pasajero == "Tercera":
			valor_base = 40
	elif tipo_destino == 'Internacional':
		if categoria_pasajero == "Adulto":
			valor_base = 300
		elif categoria_pasajero == "Niño":
			valor_base = 200
		elif categoria_pasajero == "Tercera":
			valor_base = 250
	return valor_base

def obtener_valor_region(region):
	"""Retorna el valor adicional por la region del destino."""
	valor_region = 0
	if region == "Sudamerica":
		valor_region = 50
	elif region == "Norteamerica":
		valor_region = 120
	elif region == "Europa":
		valor_region = 200
	return valor_region

def obtener_valor_temporada(valor_base, valor_region, mes):
	"""Retorna el valor adicional por la temporada en que se viaje."""
	valor_base_calculo = valor_base + valor_region
	porcentaje = 0
	if mes > 0 and mes<4:
		porcentaje = 5
	elif mes>= 4 and mes<9:
		porcentaje = 10
	elif mes>=9 and mes<=12:
		porcentaje = 12
	valor_temporada = valor_base_calculo*porcentaje/100
	return valor_temporada

def obtener_valor_clase(clase):
	"""Retorna el valor adicional por la clase en la vuele el pasajero."""
	valor_clase = -1
	if clase == 'economica':
		valor_clase = 0
	elif clase == 'ejecutiva':
		valor_clase = 20
	return valor_clase

def obtener_total_pasajero(valor_base, valor_region, valor_temporada, valor_clase):
	"""Retorna el valor total del boleto de un pasajero"""
	return valor_base + valor_region + valor_temporada + valor_clase

def obtener_total(lista_pasajeros):
	"""Retorna el valor total de los boletos de una lista de pasajeros"""
	valor_total = 0
	if len(lista_pasajeros) > 0 and len(lista_pasajeros)<9:
		for boleto in lista_pasajeros:
			valor_base = obtener_valor_base(boleto.categoria_pasajero, boleto.tipo_destino)
			valor_region = 0
			if boleto.tipo_destino == 'Internacional':
				valor_region = obtener_valor_region(boleto.region)
			valor_temporada = obtener_valor_temporada(valor_base, valor_region, boleto.mes)
			valor_clase = obtener_valor_clase(boleto.clase)
			valor_total_pasajero = obtener_total_pasajero(valor_base, valor_region, valor_temporada, valor_clase)
			valor_total+= valor_total_pasajero
	return valor_total