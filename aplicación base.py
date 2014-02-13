# _*_ coding utf-8 _*_

import requests
import json	

print
"""
1.Almeria
2.Cadiz
3.Cordoba
4.Granada
5.Huelva
6.Jaen
7.Malaga
8.Sevilla

"""
ciudades = {1:"Almeria",2:"Cadiz",3:"Cordoba",4:"Granada",5:"Huelva",6:"Jaen",7:"Malaga",8:"Sevilla"} 
ciudad = raw_input ("De que ciudad quieres saber la temperatura actual?: ")

Resultado = requests.get('http://api.openweathermap.org/data/2.5/weather'),params={'q':"%:,spain"%ciudades[ciudad]}
direccion = json.loads(respuesta.text)

temp = direccion["main"]["temp"]
grados = temp -273

print "La temperatura actual en %s es de %s ºC" % (ciudades[ciudad],grados)
