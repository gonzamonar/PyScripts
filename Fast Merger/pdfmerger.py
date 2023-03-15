from PyPDF2 import PdfMerger
import os
import sys


def pdfmerge(file_list : list, docname : str):
    """
    The pdfmerge function takes a list of PDF files and merges them into one file.
    
    :param file_list: Path list of files that will be merged
    :param docname : str: Name the file that will be created
    :no return
    :doc-author: Gonzalo Monar
    """
    merger = PdfMerger()

    for file in file_list:
        try:
            merger.append(file)
        except:
            end_exec(merger, f"No se pudo encontrar el archivo {file}")
    
    try:
        merger.write(docname)
    except:
        end_exec(merger, "Nombre de archivo inválido. Inténtelo nuevamente.")

    merger.close()


def end_exec(merger : PdfMerger, message : str):
    """
    The end_exec function is used to end the execution of the program.
    It takes two arguments:
        merger : PdfMerger - The merger object that was created at the beginning of this script.
        message : str - A string containing a message to be printed before ending execution.
    
    :param merger : PdfMerger: Close the merger object
    :param message : str: Print a message to the console
    :return: Prints the message and closes the merger
    :doc-author: Gonzalo Monar
    """
    merger.close()
    sys.exit(message)


def pdfmergefolder(folderpath : str, docname : str):
    """
    The pdfmergefolder function takes a folder path and a document name as arguments.
    It then walks through the folder, appending each file to a list of files.
    Finally, it calls the pdfmerge function with that list of files and the document name.
    
    :param folderpath : str: Specify the folder that contains all of the pdfs you want to merge
    :param docname : str: Name the merged pdf file
    :no return
    :doc-author: Gonzalo Monar
    """
    file_list = []
    for _, _, file_names in os.walk(folderpath):
        for file in sorted(file_names):
            file_list.append(f"{folderpath}/{file}")
        print(f">>> Merging {folderpath} in {docname}")
        pdfmerge(file_list, docname)