import xml.etree.ElementTree as ET  
import time
from linked_list import *
from graphviz import Digraph



Senales = lista_senales()
    
# Se crea método para pedir ingresar ruta del archivo:
def load_file():

    try:
        route_doc = input("Por favor, Typee ruta del archivo: \n")    
        tree = ET.parse(route_doc)
        root = tree.getroot()
        print("\nCargando....")
        time.sleep(1)
        print("Archivo cargado con éxito! \n")

        for lista_senal in root.findall('senal'):
            nombre = lista_senal.get('nombre')
            tiempo = lista_senal.get('t')
            amplitud = lista_senal.get('A')
            Senales.insertar_senal(nombre, tiempo, amplitud)
            add_data = Senales.get_senal(nombre)
            for lista_datos in lista_senal.findall('dato'):
                tiempo_data = lista_datos.get('t')
                amplitud_data = lista_datos.get('A')
                dato_value = lista_datos.text
                add_data.lista_datos.insertar_dato(tiempo_data, amplitud_data, dato_value)
        return route_doc
    except ET.ParseError:
        print("Error al cargar archivo.")
        time.sleep(2)
        return None
    
def process_data():
   Senales.print_Senal()

def create_graph():
    grafo_matriz = Digraph(format='png')

    for senal in Senales.lista_senales:
        nombre = senal.nombre
        tiempo = senal.tiempo
        amplitud = senal.amplitud
        grafo_matriz.node(nombre, label=f"Nombre: {nombre}\nTiempo: {tiempo}\nAmplitud: {amplitud}")
        for dato in senal.lista_datos:
            tiempo_data = dato.tiempo_data
            amplitud_data = dato.amplitud_data
            dato_value = dato.dato_value
            grafo_matriz.node(f"{nombre}_{tiempo_data}_{amplitud_data}", label=f"Valor: {dato_value}")

    grafo_matriz.render('senales', view = True)
