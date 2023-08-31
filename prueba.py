def lexer(contenido):
    lineas = contenido.split('\n')
    return lineas

def parser(archivo):
    contenido = open(archivo, "r").read()
    tokens = lexer(contenido)
    return tokens




