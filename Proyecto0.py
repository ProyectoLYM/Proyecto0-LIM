
def quitar_espacios(expresion):
    expresion = expresion.strip()
    return expresion


def cargar_archivo(archivo):
    contenido = open(archivo,"r").read()
    return contenido
    
    
print(cargar_archivo("ejemploFull.txt"))


def definicionVariable(linea):
    palabra = linea.split(" ")
    if "defVar" in palabra[0]:
        if len(palabra) == 3:
            token = "Valido"
        if len(palabra) > 3 or len(palabra) < 3:
            token = "No valido"
    else:
        token = "No valido"
    return token 
            

def definicionProceso(linea):
    palabra = linea.split(" ")
    if "defProc" in palabra[0]:
        if len(palabra[1] != 0):
            if "(" and ")" in linea:
                parametros = linea.split("(")
                parametro = parametros.split(",")
                if parametro > linea.count(","):
                    token = "Valido"
            else:
                token = "No valido"
        else:
            token = "No valido"
    else:
        token = "No valido"
    return token


def condicionalif(lineas, i):
    linea = quitar_espacios(lineas[i])
    Encontro = False
    if "if" in linea:
            palabra = linea.split(" ")
            if "if" in palabra[0]:
                if "{" in linea:
                    token = "Valido"
                else:
                    while (Encontro == False and i < len(lineas)):
                        if "{" in lineas[i]:
                            Encontro = True
                            token = "Valido"
                        elif "{" not in lineas[i] and lineas[i].size != 0:
                            Encontro = True
                            token = "No valido"
                        i += 1
    return token
        
        
def condicionalelse(lineas, i):
    linea = quitar_espacios(lineas[i])
    Encontro = False
    if "else" in linea:
            palabra = linea.split(" ")
            if "else" in palabra[0]:
                if "{" in linea:
                    token = "Valido"
                else:
                    while (Encontro == False and i < len(lineas)):
                        if "{" in lineas[i]:
                            Encontro = True
                            token = "Valido"
                        elif "{" not in lineas[i] and len(lineas[i]) != 0:
                            Encontro = True
                            token = "No valido"
                        else:
                            i += 1
    return token        
        
        
def ciclos(lineas, i):
    linea = quitar_espacios(lineas[i])
    encontro = False
    if "while" in linea:
        palabra = linea.split(" ")
        if "while" in palabra[0]:
            if "{" in linea:
                token = "Valido"
            else:
                while (encontro == False and i < len(lineas)):
                    if "{" in lineas[i]:
                        encontro = True
                        token = "Valido"
                    elif "{" not in lineas[i] and len(lineas[i]) != 0:
                        encontro = True
                        token = "No valido"
                    i += 1
    return token 
                        
        
def contarCondicionales(linea):
    ifs = 0
    elses = 0
    invalido = False
    i = 0
    while i < len(linea) and not invalido:
        if "if" in linea:
            ifs += 1
        if "else" in linea:
            elses += 1
            if elses > ifs:
                token = "No valido"
                invalido = True
            else:
                token = "Valido"
            i += 1
    return token 


def contarbrackets(contenido):
    centinela = True
    x = 0
    opbracket = 0
    clbracket = 0
    while(centinela and x < len(contenido)):
        if "{" in contenido[x]:
            opbracket += 1
        if "}" in contenido[x]:
            clbracket += 1 
        centinela = opbracket >= clbracket
        x += 1
    if centinela == True:
        token = "Valido"
    else:
        token == "Invalido"
    return token


def funcionJump(linea):
    spaces = linea.replace(" ", "")
    index = linea.find("jump")
    slice = linea[index:len(spaces) + 1]
    if "(" in slice and ")" in slice:
        if slice.find("(") > slice.find(")"):
            token = "Valido"
        else:
            token = "No valido"
    else:
        token = "No valido" 
    return token 


def funcionWalk(linea):
    spaces = linea.replace(" ", "")
    index = linea.find("walk")
    slice = linea[index:len(spaces) + 1]
    if "(" in slice and ")" in slice:
        if slice.find("(") > slice.find(")"):
            token = "Valido"
        else:
            token = "No valido"
    else:
        token = "No valido" 
    return token 
    

def funcionWalk2(linea):
    direccion = ["front", "right", "left", "back"]
    coord = ["north", "south", "west", "east"]
    index = linea.find("walk")
    for i in range(4):
        if direccion[i] in linea:
            lenght = len(direccion[i])
            index_value = linea.find(direccion[i])
        elif coord[i] in linea:
            lenght = len(coord[i])
            index_value = linea.find(coord[i])
        else:
            token = "No valido"
        slice = linea.replace(" ", "")
        slice1 = slice[index:index_value + lenght]
        if "(" in slice1 and ")" in slice1:
            if slice1.find("(") > slice1.find(")"):
                token = "Valido"
            else:
                token = "No valido"
        else:
            token = "No valido"
        return token
            
        
def funcionLeap(linea):
    spaces = linea.replace(" ", "")
    index = linea.find("leap")
    slice = linea[index:len(spaces) + 1]
    if "(" in slice and ")" in slice:
        if slice.find("(") > slice.find(")"):
            token = "Valido"
        else:
            token = "No valido"
    else:
        token = "No valido" 
    return token         
            
            
def funcionLeap2(linea):
    direccion = ["front", "right", "left", "back"]
    coord = ["north", "south", "west", "east"]
    index = linea.find("leap")
    for i in range(4):
        if direccion[i] in linea:
            lenght = len(direccion[i])
            index_value = linea.find(direccion[i])
        elif coord[i] in linea:
            lenght = len(coord[i])
            index_value = linea.find(coord[i])
        else:
            token = "No valido"
        slice = linea.replace(" ", "")
        slice1 = slice[index:index_value + lenght]
        if "(" in slice1 and ")" in slice1:
            if slice1.find("(") > slice1.find(")"):
                token = "Valido"
            else:
                token = "No valido"
        else:
            token = "No valido"
        return token    
    
    
def turn(linea):
    lista = ["left", "right", "around"]
    indice = linea.find("turn")
    for i in range(3):
        if lista[i] in linea:
            param = linea.find(lista[i])
        else:
            token = "No valido"
        palabra = linea.replace(" ", "")
        palabra = palabra[indice:param+1]
        if "(" in palabra and ")" in palabra:
            if palabra.find("(") > palabra.find(")"):
                token = "Valido"
            else:
                token = "No valido"
        else: 
            token = "No valido"
    return token
       
        
def turnto(linea):
    lista = ["north", "south", "east", "west"]
    indice = linea.find("turnto")
    for i in range(4):
        if lista[i] in linea:
            param = linea.find(lista[i])
        else:
            token = "No valido"
        palabra = linea.replace(" ", "")
        palabra = palabra[indice:param+1]
        if "(" in palabra and ")" in palabra:
            if palabra.find("(") > palabra.find(")"):
                token = "Valido"
            else:
                token = "No valido"
        else: 
            token = "No valido"
    return token


def drop(linea):
    palabra = linea.replace(" ", "")
    indice = linea.find("drop")
    palabra1 = linea[indice:len(palabra) - 1]
    if "(" in palabra and ")" in palabra1:
        param = palabra1.find("(")
        param2 = palabra1.find(")")
        palabra = palabra1[param:param2]
        try:
            int(palabra)
            token = "Valido"
        except(TypeError):
            token = "No valido"
    else:
        token = "No valido"
    return token
    
    
def get(linea):
    palabra = linea.replace(" ", "")
    indice = linea.find("get")
    palabra1 = linea[indice:len(palabra) - 1]
    if "(" in palabra and ")" in palabra1:
        param = palabra1.find("(")
        param2 = palabra1.find(")")
        palabra = palabra1[param:param2]
        try:
            int(palabra)
            token = "Valido"
        except(ValueError):
            token = "No valido"
    else:
        token = "No valido"
    return token
    
    
def grab(linea):
    palabra = linea.replace(" ", "")
    indice = linea.find(grab)
    palabra1 = linea[indice:len(palabra) - 1]
    if "(" in palabra and ")" in palabra1:
        param = palabra1.find("(")
        param2 = palabra1.find(")")
        palabra = palabra1[param:param2]
        try:
            x = int(palabra)
            token = "Valido"
        except(ValueError ):
            token = "No valido"
    else:
        token = "No valido"
    return token


def letGo(linea):
    palabra = linea.replace(" ", "")
    indice = linea.find("letgo")
    palabra1 = linea[indice:len(palabra) - 1]
    if "(" in palabra and ")" in palabra1:
        param = palabra1.find("(")
        param2 = palabra1.find(")")
        palabra = palabra1[param:param2]
        try:
            x = int(palabra)
            token = "Valido"
        except(ValueError ):
            token = "No valido"
    else:
        token = "No valido"
    return token


def nop(linea):
    palabra = linea.replace(" ", "")
    indice = linea.find("letgo")
    palabra = linea[indice:indice+3]
    if "(" in palabra and ")" in palabra:
        abrir = palabra.find("(")
        cerrar = palabra.find(")")
        if (cerrar - abrir) == 1:
            token = "Valido"
        else:
            token = "No valido"
    else:
        token = "No valido"
    return token
    
          
def parser(tokens):
    correcto = True
    i = 0
    while(correcto and i < len(tokens)):
        if tokens[i] != "Valido":
            correcto = False
        else:
            i += 1
    return correcto
            
        
def resultado(archivo):
    archivo = "ejemploFull.txt"
    carga = cargar_archivo(archivo)
    respuesta = parser(carga)
    if respuesta == True:
        res = print("La sintaxis es correcta: True")
    else:
        res = print("La sintaxis no es correcta: False")
    return res
    
    
def lexer(contenido):
    lineas = contenido.split("\n")
    tokens = []
    for i in range(len(lineas)):
        linea = quitar_espacios(lineas[i])
        if "defVar" in linea:
            token = definicionVariable 
        if "defProc" in linea:
            token = definicionProceso
        if "if" in linea or "else" in linea:
            palabra = linea.split(" ")
            if "if" in palabra[0]:
                if "{" in linea or "{" in lineas[i + 1]:
                    
                     
        tokens.append(token)
            
    return lista