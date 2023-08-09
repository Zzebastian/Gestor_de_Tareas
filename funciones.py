# Este archivo se crea de la terminal

from diccionarios import *

listaProyectos = []
elemento = {}

def tarea():
    global elemento
    for key in task:
        elemento[key] = input(task[key])
    return elemento
#

def agregarProyecto():
    # Agrega elementos a la lista de proyectos
    global listaProyectos
    elemento = tarea()
    listaProyectos.append(elemento)
#

def imprimirProyectos():
    global listaProyectos
    for proy in listaProyectos:
        for key in task:
            print(proy[key])
        print('\n@@@@@@@@\n')
#

