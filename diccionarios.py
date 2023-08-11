

# Es importante verificar que la base de datos y la variable "task" posean las mismas llaves
# De lo contrario habrá problemas en la implementación.
task = {'Proyecto': 'Ingresar Nombre de proyecto: ',
        'Github': 'Ingresar web de Github: ',
        'Estado': 'Ingresar estado proyecto: ',
        'Tarea siguiente': 'Ingresar tarea siguiente: ',
        'Notas': 'Si hay notas, agréguelas: ',
        'Instrucciones': 'Ingrese la consigna del proyecto: '
        }

indicaciones = {'Menu': '\033[0m¿Qué desea hacer?',
                'Agregar Proyecto': 'Ingrese (\033[34m1\033[0m) si desea agregar un proyecto nuevo',
                'Modificar Proyecto': 'Ingrese (\033[34m2\033[0m) si desea modificar un proyecto existente',
                'Borrar Proyecto': 'Ingrese (\033[34m3\033[0m) si desea eliminar un proyecto existente',
                'Listar Proyectos': 'Ingrese (\033[34m4\033[0m) si desea listar los proyectos existentes',
                'Salir': 'Ingrese (\033[34mS\033[0m) para salir del menú',
                # '': 'Ingrese (\033[34m   \033[0m) ',
                }

opciones = {'Menú inicial': {'text': '-> \033[34m', 'Opciones': ['1','2','3','4', 's'],
                   'siError': '\033[0mSolo se admiten los valores\033[34m 1, 2, 3, 4\033[0m y\033[34m S\033[0m'},
            'Modificar Proyecto' : {'text': '->'}
            }

mensajes = {'Salida': 'Usted ha salido exitosamente',
            'Mostrar Proyecto': 'Ingrese Id del proyecto deseado',
            'Error ID': 'Hay un error en el ID ingresado (no es un número entero)',
            'Error ID rango': 'Hay un error en el ID ingresado (el mismo está fuera de rango)',
            'Conf Mostrar Proyecto': 'Verifique que el proyecto elegido sea el correcto',
            'Conf Mod Proyecto': '¿Desea modificar el proyecto presentado?',
            }
