import graphviz
import os
# Se crea el nodo
class Dato:
    def __init__(self, tiempo_data, amplitud_data, dato_value):
        self.tiempo_data = tiempo_data
        self.amplitud_data = amplitud_data
        self.dato_value = dato_value
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return str(self.tiempo_data, self.amplitud_data, self.dato_value)

# Se crea la lista para guardar los datos
class lista_datos:
    def __init__(self):
        self.cabeza = None

    # Se crea el método para insertar datos a la lista
    def insertar_dato(self, tiempo_data, amplitud_data, dato_value):
        nuevo = Dato(tiempo_data, amplitud_data, dato_value) # dato se refiere al nodo creado anteriormente
        
        # si el primer nodo esta vacio entonces apuntara al nuevo nodo agregado
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            tmp = self.cabeza
            # si la cabeza no es nulo o vacio entonces apuntara al siguiente 
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    # Se crea método para imprimir los datos de la lista
    def print_datos(self):
        tmp = self.cabeza
        while tmp is not None:
            print(f'[t = {tmp.tiempo_data}]|[A = {tmp.amplitud_data}]|[ {tmp.dato_value} ]|')
            tmp = tmp.siguiente
    
    def graph_data(self,parent):
        data= 1
        txt = ""
        key = True
        iterador = 0
        tmp = self.cabeza
       
        while tmp is not None:
            if key: 
                txt += f'd{data}[label="{tmp.dato_value}"]\n {parent}->d{data}\n'
                data +=1
                iterador += 1
                if iterador== 4:
                    key = False
            else:
                txt += f'd{data}[label="{tmp.dato_value}"]\n'   
                data +=1
            tmp = tmp.siguiente
        for i in range(data):
            if i <=data-4 and i>0:
                txt += f'd{i}->d{i+4}\n' 
        return txt


class Senal:
    def __init__(self, nombre, tiempo, amplitud):
        self.nombre = nombre
        self.tiempo = tiempo
        self.amplitud = amplitud
        self.siguiente = None
        self.lista_datos = lista_datos()

    def __str__(self):
        return (self.nombre, self.tiempo, self.amplitud)
    
# Se crea la lista para guardar los datos
class lista_senales:
    def __init__(self):
        self.cabeza = None
        self.len = 0

    # Se crea el método para insertar datos a la lista
    def insertar_senal(self, nombre, tiempo, amplitud):
        nuevo = Senal(nombre, tiempo, amplitud) # dato se refiere al nodo creado anteriormente
        
        # si el primer nodo esta vacio entonces apuntara al nuevo nodo agregado
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            tmp = self.cabeza
            # si la cabeza no es nulo o vacio entonces apuntara al siguiente 
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo
    def get_senal(self, nombre):
        tmp = self.cabeza
        while tmp is not None:
            if tmp.nombre==nombre :
                return tmp
            tmp=tmp.siguiente
        return None
    def print_Senal(self):
        tmp = self.cabeza
        while tmp is not None:
            print(f'[Nombre = {tmp.nombre}]| [t = {tmp.tiempo}]|A = [{tmp.amplitud}]')
            tmp.lista_datos.print_datos()
            tmp = tmp.siguiente
    def graph_senal(self):
        
        tmp = self.cabeza
        while tmp is not None:
            ruta = tmp.nombre
            txt=""" digraph """+tmp.nombre+"""{\n node [shape= circle]\n"""+ tmp.nombre+"""[label="""+tmp.nombre+"""]\n"""
            txt+=f'T[label="T={tmp.tiempo}"] \n A[label="A={tmp.amplitud}"]\n'
            txt+=f'{tmp.nombre}->T\n{tmp.nombre}->A\n'
            txt+=tmp.lista_datos.graph_data(tmp.nombre)
            txt+='}'
            print(txt)
            try:

                src = graphviz.Source(txt,format="png")
                src.render(ruta)
                if os.path.exists(ruta):
                    os.remove(ruta)
                print("Atención: Se guardo el archivo con el nombre: "+str(ruta)+".png")
            except :
                print("Error")
            tmp = tmp.siguiente

    