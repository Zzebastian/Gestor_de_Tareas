
from funciones import *
# -*- coding: utf-8 -*- 

# menuTexto()

BdD = obtenerDatosJSON()

# menuTexto()
agregarProyecto(BdD)
# modificarProyecto(BdD)
# borrarProyecto(BdD)
imprimirProyectos(BdD)

guardarDatosJSON(BdD)
