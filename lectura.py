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
                dato_value = int(dato_value)
                if dato_value > 0:
                    dato_value = 1
                add_data.lista_datos.insertar_dato(tiempo_data, amplitud_data, dato_value)
                
        return route_doc



    except ET.ParseError:
        print("Error al cargar archivo.")
        time.sleep(2)
        return None

    
def process_data():
   print("Cargando...")
   time.sleep(1)
   print("\nSenal Cargada ya convertida: \n")
   Senales.print_Senal()

def test2():
    datos = 0
    tmp = Senales.cabeza
    Ruta = "Senal5"
    text = '''digraph Matrix{\n
                node [shape=circle]\n
                Mat[label="''' + tmp.nombre + '''", style=filled, fillcolor=wheat, group=1, width=1]\n
                e0[shape=point, width=0]\n
                e1[shape=point, width=0]\n
            '''

    while tmp is not None:
        text += f'''Mat{datos}t[label="t = {tmp.tiempo}\nA = {tmp.amplitud}\nDato = {tmp.dato_value}", style=filled, fillcolor=wheat, width=0.25]\n'''

        datos += 1
        tmp = tmp.siguiente

    # Agregar flechas entre los nodos
    tmp = Senales.cabeza
    for i in range(datos - 1):
        text += f'''Mat{i}t -> Mat{i + 1}t [label="t"]\n'''

    text += "}"

    try:
        src = graphviz.Source(text, format="png")
        src.render(Ruta)
        if os.path.exists(Ruta):
            os.remove(Ruta)
        os.startfile(f"{Ruta}.png")
        print(f"Atención: Se guardo el archivo con el nombre: {Ruta}.png")
    except:
        print("Error")

def test():
    datos = 0
    tmp = Senales.cabeza
    Ruta = "Senal9"
    text = '''digraph Matrix{\n
                node [shape=circle]\n
                Mat[label=''' + str(tmp.nombre) + ''', style = filled, fillcolor = wheat, group = 1, width = 1]\n
                e0[shape= point, width = 0]\n
                e1[shape= point, width = 0]\n
            '''

    while tmp != None:
        if hasattr(tmp, 'tiempo') and hasattr(tmp, 'amplitud'):
            # Este nodo utiliza 'tiempo' y 'amplitud'
            text += '''Mat''' + str(datos) + '''t[label = "''' + tmp.tiempo + '''", style = filled, fillcolor = gray, width = 0.25]\n
                A[label = "''' + tmp.amplitud + '''", style = filled, fillcolor = wheat, width = 0.25]\n
            '''
        elif hasattr(tmp, 'tiempo_data') and hasattr(tmp, 'amplitud_data'):
            # Este nodo utiliza 'tiempo_data' y 'amplitud_data'
            text += '''Mat''' + str(datos) + '''t[label = "''' + tmp.tiempo_data + '''", style = filled, fillcolor = wheat, width = 0.25]\n
                A[label = ''' + tmp.amplitud_data + '''", style = filled, fillcolor = wheat, width = 0.25]\n
            '''

        datos += 1
        tmp = tmp.siguiente

    # Agregar flechas entre los nodos
    tmp = Senales.cabeza
    for i in range(datos - 1):
        text += '''Mat''' + str(i) + '''t -> Mat''' + str(i + 1) + '''t [label = "t"]\n
            Mat''' + str(i) + '''t -> A\n
        '''

    text += "}"

    try:
        src = graphviz.Source(text, format="png")
        src.render(Ruta)
        if os.path.exists(Ruta):
            os.remove(Ruta)
        os.startfile(str(Ruta) + ".png")
        print("Atención: Se guardo el archivo con el nombre: " + str(Ruta) + ".png")
    except:
        print("Error")



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

def grafo(datos):
    dot = Digraph(comment='Datos de senal')

    for dato in datos:
        dot.node(f'{dato.tiempo_data}',f'{dato.amplitud_data}',f'{dato.dato_value}')
    
    for i in range(len(datos) - 1):
        dot.edge(f'{datos[i].tiempo_data}', f'{datos[i+1].tiempo_data}')

    dot.render('Senal', format='png')

""" def create_Matrix(lista_Datos):
    Max_row = max(int(dato)) """