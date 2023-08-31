import re
def lexer(contenido):
    lineas = contenido.split("\n")
    tokens = []
    for i in range(len(lineas)):
        linea = quitar_espacios(lineas[i])
        if "defVar" in linea:
            palabra = linea.split(" ")
            if "defVar" in linea[0]:
                if len(linea) == 3:
                    primer_token = "Variable"
                    segundo_token = "Nombre"
                    tercer_token = "Valor"
                    token = (primer_token,segundo_token,tercer_token)
                if len(linea) > 3 or len(linea) < 3:
                    token = "No valido"
            else:
                 token = "No valido"  
        if "defProc" in linea:
            palabra = linea.split(" ")
            if "defProc" in linea[0]:
                if "(" and ")" in linea:
                    
                     
        tokens.append(token)
            
    return lista
def quitar_espacios(expresion):
    expresion = expresion.strip()
    return expresion
def cargar_archivo(archivo):
    contenido = open(archivo,"r").read()
    lista = lexer(contenido)
    return lista
    
print(cargar_archivo("ejemploFull.txt"))
    