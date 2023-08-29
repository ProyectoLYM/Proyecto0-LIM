def cargar_archivo(archivo):
    archivo = open(archivo)
    lista = []
    linea = archivo.readline()
    while len(linea) > 0:
        lista.append[linea]
        linea.readline()
    return lista
    


def corrector(expresion):
    expresion = expresion.strip()
    expresion = expresion.lowercase()
    
    
def lexer(expression):
    listai = ["jump","walk","leap", "turn", "turnto", "drop", "get", "grab", "letgo", "nop"]
    listaf = ["ju","wa","le","tu","tt", "dr", "ge", "gr", "lg", "np"]
    