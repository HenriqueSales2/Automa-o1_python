import os

#Biblioteca que trabalha com arquivos com extensão PDF
#No terminal ou no prompt de comando digitar: pip install pypdf2
import PyPDF2

from tkinter.filedialog import askdirectory

def main():

    merger = PyPDF2.PdfMerger() # junta os arquivos

    #caminhoPasta = ("C:/Users/ALUNO/Desktop/python 536/Automacao1/Arquivos/")
    caminhoPasta = askdirectory(title="Selecione uma pasta")
    caminhoPasta = caminhoPasta+'/'

    # print(caminhoPasta)
    
    lista_arquivos = os.listdir(caminhoPasta)
    lista_arquivos.sort() #sort vai organizar os arquivos os colocando em ordem

    # print(lista_arquivos)

    for arquivo in lista_arquivos:
        if ".pdf"  in arquivo:
            merger.append(f"{caminhoPasta+arquivo}") # append coloca os arquivos sempre no final

    merger.write(f"{caminhoPasta}Nota Final.pdf")

if __name__ == "__main__":
    main()