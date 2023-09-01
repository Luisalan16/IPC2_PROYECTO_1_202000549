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
        # dato se refiere al nodo creado anteriormente
        nuevo = Dato(tiempo_data, amplitud_data, dato_value)

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
            print(
                f'[t = {tmp.tiempo_data}]|[A = {tmp.amplitud_data}]|[ {tmp.dato_value} ]|')
            tmp = tmp.siguiente

    # Método para remover un nodo

    def remove_dato(self, nombre, tiempo, amplitud, dato):
        if self.len > 0:  # Si el tamaño de la lista es mayor a 0
            tmp = self.cabeza  # el nodo primero
            if tmp.nombre == nombre and tmp.tiempo == tiempo and tmp.amplitud == amplitud and tmp.dato == dato:  # Si el dato es igual a la variable
                # entonces el nodo a eliminar es el actual (tiempo, amplitud o nombre)
                remover = tmp
                # se actualiza el apuntador luego de eliminar uno anterior
                self.cabeza = remover.siguiente
                tmp = None
                self.len -= 1  # la lista se irá reduciendo
            else:
                while tmp.siguiente.nombre != nombre and tmp.siguiente.tiempo != tiempo and tmp.siguiente.amplitud != amplitud and tmp.siguiente.dato != dato:
                    if tmp.siguiente.siguiente == None:
                        return False
                    else:
                        tmp = tmp.siguiente
                data_removed = tmp.siguiente
                if data_removed.siguiente == None:
                    tmp.siguiente = None
                else:
                    tmp.siguiente = data_removed.siguiente
                self.len -= 1

    # Método para modificar dato
    def __setdata__(self, index, new_dato):
        if index >= 0 and index < self.len:
            tmp = self.cabeza
            for i in range(index):
                tmp = tmp.siguiente
            tmp.tiempo = new_dato
            tmp.amplitud = new_dato
            tmp.nombre = new_dato
        else:
            raise Exception("No existe posición")

    # Método para tomar los valores


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
        # dato se refiere al nodo creado anteriormente
        nuevo = Senal(nombre, tiempo, amplitud)

        # si el primer nodo esta vacio entonces apuntara al nuevo nodo agregado
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            tmp = self.cabeza
            # si la cabeza no es nulo o vacio entonces apuntara al siguiente
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nuevo

    """ def create_graph_senal(self):
        datos = 0
        tmp = self.cabeza
        Ruta = "Senal"
        text = '''digraph Matrix{\n
                node [shape=circle]\n
                Mat[label='''+str(tmp.nombre)+''', style = filled, fillcolor = wheat, group = 1, width = 1];\n
                e0[shape= point, width = 0];\n
                e1[shape= point, width = 0];\n'''
        
        while tmp != None:
            text = '''t[label='''+(tmp.tiempo)+''', style = filled, fillcolor = wheat, width = 0.25];\n
                A[label='''+(tmp.amplitud)+''', style = filled, fillcolor = wheat, width = 0.25];'''
            datos += 1
            tmp = tmp.siguiente
        
        try:
            src = graphviz.Source(text, format="png")
            src.render(Ruta)
            if os.path.exists(Ruta):
                os.remove(Ruta)
            os.startfile(str(Ruta)+".png")
            print("Atención: Se guardo el archivo con el nombre: "+str(Ruta)+".png")
        except :
            print("Error") """

                

    def get_senal(self, nombre):
        tmp=self.cabeza
        while tmp is not None:
            if tmp.nombre == nombre:
                return tmp
            tmp=tmp.siguiente
        return None

    def print_Senal(self):
        tmp=self.cabeza
        while tmp is not None:
            print(
                f'[Nombre = {tmp.nombre}]| [t = {tmp.tiempo}]|A = [{tmp.amplitud}]')
            tmp.lista_datos.print_datos()
            tmp=tmp.siguiente
