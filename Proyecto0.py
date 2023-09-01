import re
def lexer(contenido):
    lineas = contenido.split("\n")
    tokens = []
    for i in range(len(lineas)):
        linea = quitar_espacios(lineas[i])
        if "defVar" in linea:
            palabra = linea.split(" ")
            if "defVar" in palabra[0]:
                if len(palabra) == 3:
                    primer_token = "Variable"
                    segundo_token = "Nombre"
                    tercer_token = "Valor"
                    token = (primer_token,segundo_token,tercer_token)
                if len(palabra) > 3 or len(palabra) < 3:
                    token = "No valido"
            else:
                 token = "No valido"  
        if "defProc" in linea:
            palabra = linea.split(" ")
            if "defProc" in palabra[0]:
                if len(palabra[1] != 0):
                    if "(" and ")" in linea:
                        parametros = linea.split("(")
                        parametro = parametros.split(",")
                        if parametro > linea.count(","):
                            token = ("Proceso", "Nombre", "Parametros")
                    else:
                        token = "No valido"
                else:
                    token = "No valido"
            else:
                token = "No valido"
        if "if" in linea or "else" in linea:
            palabra = linea.split(" ")
            if "if" in palabra[0]:
                if "{" in linea or "{" in lineas[i + 1]:
                    
            
                            
                    
                    
                     
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
    