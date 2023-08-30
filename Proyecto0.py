def cargar_archivo(archivo):
    archivo = open(archivo)
    lista = []
    linea = archivo.readline()
    while len(linea) > 0:
        lista.append[linea]
        linea.readline()
    return lista
    


def corrector(lista):
    expresion = expresion.strip()
    expresion = expresion.lowercase()
    return expresion
    
    
def lexer(lista):
    listaDefiniciones = ["jump","walk","leap", "turn", "turnto", "drop", "get", "grab", "letgo", "nop"]
    listaAbreviaciones = ["ju","wa","le","tu","tt", "dr", "ge", "gr", "lg", "np"]
    listaFinal = []
    for i in range(len(lista)):
        expresion = corrector(lista[i])
        for char in range(len(listaDefiniciones)):
            if expresion in char():
                listaFinal.append(expresion.split(" "))
                                
                