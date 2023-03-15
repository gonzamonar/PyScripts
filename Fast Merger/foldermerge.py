from pdfmerger import pdfmergefolder
import os
import sys

help = """
Ayuda del programa foldermerge.py

Call & Args:
merge.py [arg1-mandatory] [arg2-optional]
El programa toma 1 o 2 argumentos.

El primer arg (mand.) es el path de la carpeta
cuya totalidad de archivos se van a mergear
(relativo al directorio actual).

El segundo arg (opt.) es para dar nombre
al archivo mergeado. Por defecto es el
nombre de la carpeta con extensión .pdf.

Ejemplo:
>>> foldermerge.py "Nueva Carpeta" Archivos.pdf
"""

args = sys.argv

# Help call
if len(args) > 1 and args[1].lower() in ('help', '-help', 'h', '-h', '/?', '/help'):
    sys.exit(help)

# Enforce number of args
if len(args) > 3:
    sys.exit("El programa sólo acepta de 0 a 2 argumentos.")

# Check for 1st arg [mandatory folderpath] >> Assign folderpath
folderpath = os.getcwd()
try:
    folderpath += f"/{args[1]}"
except:
    folderpath += ""

# Check for 2nd arg [optional name] >> Assign docname
try:
    docname = args[2]
except:
    docname = f"{args[1]}.pdf"

# Merge the folder
pdfmergefolder(folderpath, docname)