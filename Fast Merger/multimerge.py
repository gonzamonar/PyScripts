from pdfmerger import pdfmergefolder
import os
import sys

help = """
Ayuda del programa multimerge.py

Call & Args:
multimerge.py [arg1-optional]
El programa toma 0 o 1 argumento.

El programa realiza un merge
secuencial en todas las carpetas
del directorio donde fue ejecutado
o el path ingresado en el arg 1 (opt.),
nombrando a cada merge como la carpeta
+ la extensión .pdf.

Ejemplo:
>>> multimerge.py Carpeta
"""

args = sys.argv

# Help call
if len(args) > 1 and args[1].lower() in ('help', '-help', 'h', '-h', '/?', '/help'):
    sys.exit(help)

# Enforce number of args
if len(args) > 2:
    sys.exit("El programa acepta de 0 a 1 argumento.")

# Check for 1st arg [optional folderpath] >> Assign root folder
folder = os.getcwd()
if len(args) > 1:
     folder += f"/{args[1]}"

# Walk through each folder and merge folder files
for root, dirs, _ in os.walk(folder):
    for dir_name in dirs:
        docname = dir_name + ".pdf"
        folderpath = f"{root}/{dir_name}"
        pdfmergefolder(folderpath, docname)

