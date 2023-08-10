# Este archivo se crea de la terminal
import json
from diccionarios import *

# Sección Tareas y menús
def menuTexto():
    while True:
        for key in indicaciones:
            print(indicaciones[key])

        eleccion = opcionMultiple()
        if eleccion == '1':
            agregarProyecto()
        elif eleccion == '3':
            modificarProyecto()
        elif eleccion == '4':
            borrarProyecto()
        elif eleccion == '5':
            imprimirProyectos()
        else:
            print(confirmaciones['Salida'])
            break



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
def modificarProyecto():
    print('Seguir acá, modificar proyecto')
#
def borrarProyecto():
    print('Seguir acá borrar proyecto')

def imprimirProyectos():
    print('Probablemente halla que revistar acá imprimir proyectos')
    global listaProyectos
    for proy in listaProyectos:
        for key in task:
            print(proy[key])
        print('\n@@@@@@@@\n')
#

# Sección Funcione auxiliares
def opcionMultiple(text, opciones = ["y", "n"], siError ="Only (y)es and (n)o are available options"):
    # Itera hasta conseguir que se introduzcan solo los valores permitidos.
    while True:
        opcion = input(text).strip()
        if opcion.lower() not in opciones:
          print(siError)
        else:
          break
    return (opcion)


# Sección JSON
def obtenerDatosJSON():
    # Obtiene los datos guardados en la base de datos, o bien, en caso de no tener, crea una nueva.
    try:
        with open("Gestor_de_Tareas/BdDProyectos.json") as file:
            BdD = json.load(file)
    except:
        BdD ={}
    return BdD
#
def guardarDatosJSON(BdD):
  with open("Gestor_de_Tareas/BdDProyectos.json", "w") as file:
    json.dump(BdD, file)
#

