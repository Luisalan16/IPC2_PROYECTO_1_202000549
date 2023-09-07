import xml.etree.ElementTree as ET  
import time
from linked_list import *
from graphviz import Digraph
import os 
import sys


Senales = lista_senales()

def incializar():

    while True:
        start = input("¿Deseas volver a iniciar el sistema? s/n \n")
        if start.lower() == 's':
            print("Inicializando...")
            time.sleep(2)
            python = sys.executable
            os.execl(python, python, *sys.argv)

        elif start.lower() == 'n':
            print("Ok, regresamos...")
            time.sleep(1)
            break
        else:
            print("Opción invalida, por favor presione 's o n' ")

    
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
                dato_value = int(dato_value)
                if dato_value > 0:
                    dato_value = 1
                add_data.lista_datos.insertar_dato(tiempo_data, amplitud_data, dato_value)
       
        return route_doc
        


    except ET.ParseError:
        print("Error al cargar archivo.")
        time.sleep(2)
        return None
    
def write_xml():

    root = ET.Element("senalReducida")
    for i in range(len(root, 'Senales')):
        nombre_s = ET.SubElement('senal')
        nombre = ET.SubElement(nombre_s, 'dato')
        tiempo = i.set('t')
        amplitud = i.set('A')
        Senales.insertar_senal(nombre, tiempo, amplitud)
        add_data = Senales.get_senal(nombre)

    
def process_data():
   print("Cargando...")
   time.sleep(1)
   print("\nSenal Cargada ya convertida: \n")
   Senales.print_Senal()
   
def graph():
    print("Generando gráfica...")
    time.sleep(2)
    Senales.graph_senal()  
   
