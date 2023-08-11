# Este archivo se crea de la terminal
import json
from diccionarios import *

# Sección Tareas y menús
def menuTexto():
    
    BdD = obtenerDatosJSON()
    
    while True:
        for key in indicaciones:
            print(indicaciones[key])

        opc = opciones['Menú inicial']
        eleccion = opcionMultiple(opc['text'],opc['Opciones'],opc['SiError'])
        if eleccion == '1':
            agregarProyecto()
        elif eleccion == '3':
            modificarProyecto()
        elif eleccion == '4':
            borrarProyecto()
        elif eleccion == '5':
            imprimirProyectos()
        else:
            print(mensajes['Salida'])
            break  
#


def agregarProyecto(BdD):
    # Agrega elementos a la lista de proyectos

    ID = len(BdD)+1
    elemento = []
    for key in task:
        elemento[key] = input(task[key])
        
    BdD[ID] = elemento
#

def modificarProyecto(BdD):
    print('Seguir acá, modificar proyecto, en modificarElemento')
    while True:
        ID = mostrarProyecto(BdD)
        print(mensajes['Conf Mod Proyecto'])
        opcion = opcionMultiple(opciones['Modificar Proyecto']['text'])
        if opcion != 'n':
            break
    
    modificarElemento(BdD)
#

def mostrarProyecto(BdD):
    print(mensajes['Mostrar Proyecto'])
    while True:
        try:
            ID = int(input('->'))
        except:
            print(mensajes['Error ID'])

        if ID not in range(1, len(BdD)):
            print(mensajes['Error ID rango'])
        else:
            break

    print(mensajes['Conf Mostrar Proyecto'])
    text = 'ID'
    print(f"{text:<15} | {ID:<15}")
    for key in BdD[ID]:
        print(f"{key:<15} | {BdD[ID][key]:<15}")

    return ID
#
def modificarElemento(BdD):
    print('seguir acá modificar elemento')

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

# Sección Funciones auxiliares
def opcionMultiple(text, opciones = ['S', 'n', ''], siError ='Solo \033[34m S, N\033[0m son valores válidos'):
    # Itera hasta conseguir que se introduzcan solo los valores permitidos.
    while True:
        opcion = input(text).strip()
        if opcion.lower() not in opciones:
          print(siError)
        else:
          break
    return opcion


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
def actualizarDiccionarioJSON(id,BdD):
  for key in BdD[id].keys():
    print(f"Si desea modificar el {key}, ingrese el nuevo valor")
    print("""caso contrario, ingrese "enter" """)
    nuevoValor = input("->")
    if nuevoValor == 0:
      continue
    print(f"¿Es {key} el valor correcto? ingrese (s)i o (n)o")
    conf = opcionMultiple("->")
    if conf == "s":
      text = f"Ingrese el nuevo {key}: \033[34m"
      BdD[id][key] = verificarAccion(text)
#

