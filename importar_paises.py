""" Script para importar datos desde el .csv que contiene 
todos los nombres de los paises.

Se debe importar este archivo desde shell_plus de django extensions.
"""
import csv
from users.models.profile import Countries
with open('paises.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(str(row['nombre']))
		pais = Countries()
		pais.country_name = str(row['nombre'])
		pais.save()