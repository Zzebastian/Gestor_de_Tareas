# Este archivo se crea de la terminal
import json
from diccionarios import *

# Sección Tareas y menús
def menuTexto():
    
    BdD = obtenerDatosJSON()
    ind = indicaciones['tareas']
    while True:
        for key in ind:
            print(ind[key])

        opc = opciones['Menú inicial']
        eleccion = opcionMultiple(opc['text'],opc['Opciones'],opc['siError'])
        print('\033[0m')
        if eleccion == '1':
            agregarProyecto(BdD)
        elif eleccion == '2':
            modificarProyecto(BdD)
        elif eleccion == '3':
            borrarProyecto(BdD)
        elif eleccion == '4':
            imprimirProyectos(BdD)
        else:
            print(mensajes['Salida'])
            guardarDatosJSON(BdD)
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

    while True:
        ID = mostrarProyecto(BdD)
        print(mensajes['Conf Mod Proyecto'])
        opcion = opcionMultiple(base)
        if opcion != 'n':
            break
    
    ocurrio = modificarElemento(BdD, ID)
    if ocurrio == False:
        print(mensajes['Modificación anulada'])
    else:
        print(mensajes['Modificacion exitosa'])
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
    IDstr = str(ID)
    print(f'{text:<15} | {ID}')
    for key in BdD[IDstr]:
        print(f'{key:<15} | {BdD[IDstr][key]}')

    return IDstr
#
def modificarElemento(BdD, ID):

    ind = indicaciones['modificar']
    
    for key in ind:
        print(ind[key])

    opc = opciones['Modificar elemento']
    eleccion = opcionMultiple(opc['text'],opc['Opciones'],opc['siError'])
    if eleccion == 's':
        return False
    
    print(mensajes['Modificación nuevo valor'])
    text = tuplaElemento(int(eleccion)-1)
    BdD[ID][text] = input(base)
#
    

def borrarProyecto(BdD):
    
    IDstr = mostrarProyecto(BdD)
    print(mensajes['Borrar Proyecto'])
    conf = input(base)
    if conf.lower() == 's':
        BdD[IDstr] = {}
        print(mensajes['Borrado exitoso'])
    else:
        print(mensajes['Borrado anulado'])
#
    

def imprimirProyectos(BdD):

    
    for ID in BdD:
        text = 'ID'
        print(f'{text:<15} | {ID}')

        for key in BdD[ID]:
            print(f'{key:<15} | {BdD[ID][key]}')

        print('\n@@@@@@@@\n')
#

# Sección Funciones auxiliares
def opcionMultiple(text, opciones = ['s', 'n', ''], siError =' \033[0mSolo \033[34mS, N\033[0m son valores válidos'):
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


