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

def create_graph_senal():
        datos = 0
        tmp = Senales.cabeza
        Ruta = "Senal3"
        text = '''digraph Matrix{\n
                node [shape=circle]\n
                Mat[label='''+str(tmp.nombre)+''', style = filled, fillcolor = wheat, group = 1, width = 1]\n
                e0[shape= point, width = 0]\n
                e1[shape= point, width = 0]\n
                '''
        
        while tmp != None:
            text += '''Mat'''+str(datos)+'''t[label = "t = '''+(tmp.tiempo)+'''", style = filled, fillcolor = wheat, width = 0.25]\n
                A[label = "A = '''+(tmp.amplitud)+'''", style = filled, fillcolor = wheat, width = 0.25]\n
            '''
        

            datos += 1
            tmp = tmp.siguiente
        """ for i in range(datos-1,-1,-1):
            text += '''\nMat'''+str(i)+'''->t''''''->A''' """
        text +="}"
        
        try:
            src = graphviz.Source(text, format="png")
            src.render(Ruta)
            if os.path.exists(Ruta):
                os.remove(Ruta)
            os.startfile(str(Ruta)+".png")
            print("Atención: Se guardo el archivo con el nombre: "+str(Ruta)+".png")
        except :
            print("Error")
