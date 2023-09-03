def quitar_espacios(expresion):
    expresion = expresion.strip()
    return expresion


def cargar_archivo(archivo):
    contenido = open(archivo,"r").read()
    lista = lexer(contenido)
    espacios = quitar_espacios(lista)
    return espacios


def lexer(contenido):
    lineas = contenido.split("\n")
    return lineas



    

    
#print(cargar_archivo("ejemploFull.txt"))
    



