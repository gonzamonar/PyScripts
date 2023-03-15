from pdfmerger import pdfmerge
import os
import sys

help = """
Ayuda del programa merge.py

Call & Args:
merge.py [arg1-mandatory] [arg2-mandatory] [arg3-optional]
El programa toma 2 o 3 argumentos.

Los args 1 y 2 (mand.) contienen el path completo
(con filename.pdf) de los archivos a mergear,
relativo al directorio actual.

El tercer arg (opt.) es para dar nombre
al archivo mergeado. Incluir extensión ".pdf".
(Por defecto es "merged_document.pdf")

Ejemplo:
>>> merge.py Archivo1.pdf Archivo2.pdf Archivos.pdf
"""

args = sys.argv

# Help call
if len(args) > 1 and args[1].lower() in ('help', '-help', 'h', '-h', '/?', '/help'):
    sys.exit(help)

# Enforce number of args
if len(args) > 4 or len(args) < 3:
    sys.exit("El programa sólo acepta de 2 a 3 argumentos.")

# Check for 3rd arg [optional name] >> Assign docname
try:
    docname = args[3]
except:
    docname = "merged_document.pdf"

# Create list with file paths
files = [f"{os.getcwd()}/{args[1]}", f"{os.getcwd()}/{args[2]}"]

# Merge & output outcome
pdfmerge(files, docname)
print("Proceso realizado con éxito.")