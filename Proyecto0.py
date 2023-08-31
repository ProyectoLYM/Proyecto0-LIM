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

def correctorDefinicioneVariables(lista):
    respuestaFinal = False
    listaDefiniciones = ["defvar", "defproc"]
    respuesta = []
    for i in range(len(lista)):
        expresion = corrector(lista[i])
        if listaDefiniciones[0] in expresion:
            x = expresion.split(" ")
            if len(x == 3):
                respuesta.append(True)
            else:
                respuesta.append(False)
        if listaDefiniciones[1] in expresion:
            x = expresion.split(" ")
            if len(x == 3):
                if "(" in x[2] and ")" in x[2] and "," in x[2]:
                    if x[2].find("(") < x[2].find(")") and x[2].count(",") == 1:
                        respuesta.append(True) 
                else:
                    respuesta.append(False)
            else:
                respuesta.append(False)
    if respuesta.size() == lista.size():
        respuestaFinal = True
    return respuestaFinal
                
      
def lexer(lista):
    listaDefiniciones = ["jump","walk","leap", "turn", "turnto", "drop", "get", "grab", "letgo", "nop"]
    listaAbreviaciones = ["ju","wa","le","tu","tt", "dr", "ge", "gr", "lg", "np"]
    listaFinal = []
    for i in range(len(lista)):
        expresion = corrector(lista[i])
        for char in range(len(listaDefiniciones)):
            if expresion in char():
                listaFinal.append(expresion.split(" "))
                