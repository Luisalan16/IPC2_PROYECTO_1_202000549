from lectura import *
import time
from linked_list import *


""" METODO PARA ELEGIR EN EL MENU """
def eleccion(opcion):
    while True:
        try:
            entrada = int(input("¿Que desea realizar?, escoge una opción: \n"))
            return entrada
        except:
            print("La opcion ingresada no es válida\n"+
                  "Intentelo de nuevo")


""" MENU PRINCIPAL """
def menuP():
    print("\n|==========================================|")
    print("|      CENTRO DE INVESTIGACIONES USAC      |")
    print("|==========================================|")
    print("|--------------Menu Principal--------------|")
    print("|      1. Cargar archivo                   |")
    print("|      2. Procesar archivo                 |")
    print("|      3. Escribir archivo salida          |")
    print("|      4. Mostrar datos del estudiante     |")
    print("|      5. Generar grafica                  |")
    print("|      6. Inicializar sistema              |")
    print("|      0. Salir                            |")
    print("|==========================================|\n")

def Infopersonal():
    print("|==========================================|")
    print("|        INFORMACION DEL ESTUDIANTE        |")
    print("|==========================================|")
    print("|--------------[    Nombre    ]------------|")
    print("|        Luis Daniel Salán Letona          |")
    print("|------------------------------------------|")
    print("|--------------[    Carne     ]------------|")
    print("|                 202000549                |")
    print("|------------------------------------------|")
    print("|--------------[    Curso     ]------------|")
    print("|                    IPC 2                 |")
    print("|------------------------------------------|")
    print("|--------------[    Seccion   ]------------|")
    print("|                       C                  |")
    print("|------------------------------------------|")
    print("|                 0. Salir                 |")
    print("|==========================================|\n")
    
while menuP:
    menuP()
    opcion = eleccion(1)
    if opcion == 1:
        time.sleep(1)
        load_file()
    elif opcion == 2:
        time.sleep(1)
        print("[--Muestra--]")
        process_data()
    elif opcion == 4:
        info = True
        print("Cargando....")
        time.sleep(1)
        while info:
            Infopersonal()
            opcion = eleccion(1)
            if opcion == 0:
                info = False
    elif opcion == 5:
        create_graph_senal()
    elif opcion == 0:
        print("Saliendo...")
        time.sleep(1.5)
        Menu = False
        break