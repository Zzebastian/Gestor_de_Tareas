# Abrirlo en modo debug, porque no encuentro errores

# -*- coding: utf-8 -*-

# Es importante verificar que la base de datos y la variable "task" posean las mismas llaves
# De lo contrario habrá problemas en la implementación.

base = '-> \033[34m'

task = {'Proyecto': 'Ingresar Nombre de proyecto: ',
        'Github': 'Ingresar web de Github: ',
        'Estado': 'Ingresar estado proyecto: ',
        'Tarea siguiente': 'Ingresar tarea siguiente: ',
        'Notas': 'Si hay notas, agréguelas: ',
        'Instrucciones': 'Ingrese la consigna del proyecto: '
        }

listaElementos = ['Proyecto','Github','Estado','Tarea siguiente','Notas','Instrucciones']

indicaciones = {'tareas': {'Menu': '\033[0m¿Qué desea hacer?',
                           'Agregar Proyecto': 'Ingrese (\033[34m1\033[0m) si desea agregar un proyecto nuevo',
                           'Modificar Proyecto': 'Ingrese (\033[34m2\033[0m) si desea modificar un proyecto existente',
                           'Borrar Proyecto': 'Ingrese (\033[34m3\033[0m) si desea eliminar un proyecto existente',
                           'Listar Proyectos': 'Ingrese (\033[34m4\033[0m) si desea listar los proyectos existentes',
                           'Salir': 'Ingrese (\033[34mS\033[0m) para salir del menú',
                           # '': 'Ingrese (\033[34m   \033[0m) ',
                           },
                'modificar': {'Menu': '\033[0m¿Qué desea modificar?',
                              '1': 'Ingrese (\033[34m1\033[0m) si desea modificar el nombre del proyecto',
                              '2': 'Ingrese (\033[34m2\033[0m) si desea modificar la web del proyecto',
                              '3': 'Ingrese (\033[34m3\033[0m) si desea modificar el estado del proyecto',
                              '4': 'Ingrese (\033[34m4\033[0m) si desea modificar la siguiente tarea del proyecto',
                              '5': 'Ingrese (\033[34m5\033[0m) si desea modificar las notas del proyecto',
                              '6': 'Ingrese (\033[34m6\033[0m) si desea modificar las instrucciones del proyecto',
                              'S': 'Ingrese (\033[34mS\033[0m) en caso que no desee modificar el proyecto',
                              }
                }

opciones = {'Menú inicial': {'text': base, 'Opciones': ['1','2','3','4', 's'],
                             'siError': '\033[0mSolo se admiten los valores\033[34m 1, 2, 3, 4\033[0m y\033[34m S\033[0m'},
            'Modificar elemento' : {'text': base, 'Opciones': ['1','2','3','4','5','6','s'],
                                    'siError': '\033[0mSolo se admiten los valores\033[34m 1, 2, 3, 4, 5, 6\033[0m y\033[34m S\033[0m'}
            }

mensajes = {'Salida': '\033[0mUsted ha salido exitosamente',
            'Mostrar Proyecto': '\033[0mIngrese Id del proyecto deseado',
            'Error ID': '\033[0mHay un error en el ID ingresado (no es un número entero)',
            'Error ID rango': '\033[0mHay un error en el ID ingresado (el mismo está fuera de rango)',
            'Conf Mostrar Proyecto': '\033[0mVerifique que el proyecto elegido sea el correcto',
            'Conf Mod Proyecto': '\033[0m¿Desea modificar el proyecto presentado? (S/n)',
            'Modificar elemento': '\033[0mDefina qué elemento desea modificar',
            'Modificación anulada': '\033[0mNo se ha realizado modificación alguna',
            'Modificación exitosa': '\033[0mLa modificación fue exitosa',
            'Modificación nuevo valor': '\033[0mIngrese el nuevo valor',
##            'Borrar Proyecto Definir': 'Ingrese la ID del proyecto a borrar',
            'Borrar Proyecto' : '\033[0mEl proceso de borrado es irreversible\nPresione (\033[34mS\033[0m) para borrar\nPresione cualquier tecla para cancelar',
            'Borrado exitoso': '\033[0mEl proyecto fue borrado de la base de datos',
            'Borrado anulado': '\033[0mEl proyecto se mantiene en la base de datos',
            }
