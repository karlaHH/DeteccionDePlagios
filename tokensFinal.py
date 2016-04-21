# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 20:47:00 2016

@author: Karlii
"""

import os

letras={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z'}
numeros={'1','2','3','4','5','6','7','8','9','0'}
caracteresEspeciales={'.',',',';',':','[',']','(',')','{','}','\\'}
operadoresAritmeticos={'+','*','/','%','-'}
operadoresRelacionales={'=','>','<','!'}
constantesAlfanumericas={'"',"'"}


aliasPalabrasReservadas={'and':64,'assert':65,'break':66,'class':67,'continue':68,'def':69,'del':70,
'elif':71,'else':72,'except':73,'exec':74,'finally':75,'for':76,'from':77,'global':78,
'if':79,'import':80,'in':81,'is':82,'lambda':83,'not':84,'or':85,'pass':86,'print':87,
'raise':88,'return':89,'try':90,'while':91,'with':92,'yield':93,'False':94,'None':95,
'True':96}
aliasOperadoresRelacionales={'==':97,'<':98,'>':99,'<=':100,'>=':101,'!=':102}
aliasOperadoresAritmeticos={'=':103,'+':104,'-':105,'*':106,'**':107}
aliasLibrerias={'csv':108,'os':109,'matplotlib':110,'operator':111,'colorama':112,'PIL':113,'math':114}
aliasCaracteresEspeciales={'.':115,',':116,';':117,':':118,'[':119,']':120,'(':121,')':122,'{':123,
'}':124,'\\':125}
aliasNumeros={'0':48,'1':49,'2':50,'3':51,'4':52,'5':53,'6':54,'7':55,'8':56,'9':57,}


pos=0
archivo=""
repeticiones=[]
repeticionesUnTipo=[]
concatenacionAliasTipo=""
tokensTotal=0


#Metodo: Archivos()
#Parametros: Ninguno
#Funcion: obtiene la ruta de cada uno de los archivos .py  y se guardan en una lista
#Variables de Retorno: lista de rutas de archivos .py(lstFiles)

def archivos(ruta):
    #global lstFiles
    #global lstNuevoFiles
    #Variable para la ruta al directorio
    #rootDir = 'C:/Users/Karlii/Documents/8Octavo/MineriaDatos/proyectoFinal/OCR_limpio/'
    rootDir = ruta
    #Lista vacia para incluir los ficheros
    lstFiles = []
    #Lista con todos los ficheros del directorio:
    
    #Crea una lista de los ficheros py que existen en el directorio y los incluye a la lista
    for dirName, subdirList, fileList in os.walk(rootDir):
        #print('\nDirectorio encontrado: %s' % dirName)
        for fname in fileList:
            (nombreFichero, extension) = os.path.splitext(fname)
            if(extension==".py"):
                lstFiles.append(dirName+"/"+nombreFichero+extension)
                #limpiarArchivoComen(original,nuevo)
            
    return lstFiles


#Funcion: abrir()
#Parametros: ruta, que es la ruta de cada uno de los archivos .py
#Descripcion: abre el archivo .py, lo lee y guarda su contenido en una variable
#Variables de Retorno: archivo, que es el archivo .py completo
def abrir(ruta):
    archivo=""
    archi=open(ruta,"r")
    archivo=archi.read()
    archi.close()
    return archivo

#Funcion: getCaracter()
#Parametros: archivo, que es la variable que almacena el archivo .py completo. posicion es un numero entero
#Descripcion: retorna el caracter que se encuentra en una posicion del archivo
#Variables de Retorno: caracter, es un caracter del archivo
def getCaracter(archivo,posicion):
    pos=posicion
    if(pos >= len(archivo)):
        return ""
    else:
        caracter=archivo[pos]
        return caracter
    
#Funcion: tokens()
#Parametros: archi, que es la variable que contiene el archivo .py completo
#Descripcion: se guardan los tokens del archivo en un arreglo, que se clasifican en 9 Tipo diferentes: letras,Numeros,OperadoresRelacionales
#       operadoresAritmeticos, caracteresEspeciales, y constantes alfanumericas
#Variables de Retorno: 
def tokens(archi,numArchivo):
    archivo=archi #variable que contiene el archivo completo
    global pos
    global aliasTipo
    pos=0
    arregloTokens=[] #arreglo donde se almacenan los tokens
    global concatenacionAliasTipo
    global tokensTotal
    tokensTotal=0
    
    while(pos<len(archivo)):
        
        caracter=getCaracter(archivo,pos)

        if(caracter in letras or caracter == '_'):
            #AutomataLetras
            arregloTokens.append(automataLetras(caracter,archivo))
            
            
        elif(caracter in numeros):
            #AutomataNumerosEnteros y Decimales
            arregloTokens.append(automataNumeros(caracter,archivo))
            
                    
        elif(caracter in operadoresRelacionales):
            #AutomataOperadoesRelaciones
            arregloTokens.append(automataOperadoresRelacionales(caracter,archivo))
            
            
        elif(caracter in operadoresAritmeticos):
            #AutomataOperadoresAritmeticos
            arregloTokens.append(automataOperadoresAritmeticos(caracter,archivo))
            
            
        elif(caracter in caracteresEspeciales):
            #AutomataCaracteresEspeciales
            arregloTokens.append(automataCaracteresEspeciales(caracter))
            
            
        elif(caracter in constantesAlfanumericas):
            #AutomataOperadoresRelaciones
            arregloTokens.append(automataConstantesAlfanumericas(caracter,archivo))
            
        else:
            #tokensTotal+=1
            pos+=1
    #print(len(arregloTokens))
    tokensTotal=len(arregloTokens)

    concatenacion=creaCSV(arregloTokens,numArchivo)
    
    #Aplicacion de Metodos de busqueda
    buscarRepeticionUnCaracter(concatenacion)
    buscarRepeticionUnCaracterTipo(concatenacionAliasTipo)
    buscarRepeticionDosCaracteres(concatenacionAliasTipo)
    buscarRepeticionTresCaracteres(concatenacionAliasTipo)
    buscar4Tuplas(concatenacionAliasTipo)

        

""" AUTOMATAS DE TODO  """
#Automata de nombre de Variables
def automataLetras(caracter,archivo):
    global pos
    global tokensTotal

    tokens=""
    if(caracter == '_' or caracter in letras):
        tokens=caracter
        pos+=1
        caracter=getCaracter(archivo,pos)

        while(caracter=='_' or caracter in letras or caracter in numeros):
            tokens=tokens+caracter
            pos+=1
            caracter=getCaracter(archivo,pos)
        tokensTotal+=1

        return tokens



#Automata de Numeros Enteros y Decimales
def automataNumeros(caracter,archivo):
    global pos
    tokens=""
    #global tokensTotal
    
    if(caracter == '-' or caracter == '+'):
        tokens+=caracter
        pos+=1
        caracter=getCaracter(archivo,pos)
        if(caracter in numeros):
            tokens+=caracter
            pos+=1
            caracter=getCaracter(archivo,pos)
            while(caracter in numeros):
                tokens+=caracter
                pos+=1
                caracter=getCaracter(archivo,pos)
            if(caracter == '.'):
                tokens+=caracter
                pos+=1
                caracter=getCaracter(archivo,pos)
                if(caracter in numeros):
                    tokens+=caracter
                    pos+=1
                    caracter=getCaracter(archivo,pos)
                    while(caracter in numeros):
                        tokens+=caracter
                        pos+=1
                        caracter=getCaracter(archivo,pos)
                    #tokensTotal+=1
                    return tokens
                    
            else:
                #tokensTotal+=1
                return tokens
                
                
    elif(caracter in numeros):
        tokens+=caracter
        pos+=1
        caracter=getCaracter(archivo,pos)
        #print("Caracter",caracter)
        while(caracter in numeros):
            tokens+=caracter
            pos+=1
            caracter=getCaracter(archivo,pos)
        if(caracter == '.'):
            tokens+=caracter
            pos+=1
            caracter=getCaracter(archivo,pos)
            if(caracter in numeros):
                tokens+=caracter
                pos+=1
                caracter=getCaracter(archivo,pos)
                while(caracter in numeros):
                    tokens+=caracter
                    pos+=1
                    caracter=getCaracter(archivo,pos)
                #tokensTotal+=1
                return tokens
                
        else:
            #tokensTotal+=1
            return tokens


#Automata de Caracteres Especiales
def automataCaracteresEspeciales(caracter):
    tokens=""
    global pos
    #global tokensTotal
    
    if(caracter in caracteresEspeciales):
        tokens = caracter
        pos+=1
        #tokensTotal+=1
        return tokens

#Automata de Operadores Aritmeticos
def automataOperadoresAritmeticos(caracter,archivo):
    tokens=""
    global pos
    #global tokensTotal
    
    if(caracter in operadoresAritmeticos):        
        tokens+=caracter
        pos+=1
        caracter = getCaracter(archivo,pos)
        if(caracter == '*' or caracter == '/'):
            tokens+=caracter
            pos+=1
            #tokensTotal+=1
            return tokens
        else:
            #tokensTotal+=1
            return tokens

#Automata de Operadores Relacionales
def automataOperadoresRelacionales(caracter,archivo):
    tokens=""
    global pos
    #global tokensTotal
    
    if(caracter == '<' or caracter == '>'):
        tokens+=caracter
        pos+=1
        caracter=getCaracter(archivo,pos)
        if(caracter=='='):
            tokens+=caracter
            pos+=1
            #tokensTotal+=1
            return tokens
        else:            
            #tokensTotal+=1
            return tokens
            
    elif(caracter == '=' or caracter == '!'):
        tokens+=caracter
        pos+=1

        caracter=getCaracter(archivo,pos)
        if(caracter == '='):
            tokens+=caracter
            pos+=1
            #tokensTotal+=1
            return tokens
        else:
            #tokensTotal+=1
            return tokens


#Automata de Constantes Alfanumericas
def automataConstantesAlfanumericas(caracter,archivo):
    tokens=""
    #global tokensTotal
    #global archivo
    global pos
    if(caracter == '"'):
        tokens+=caracter
        pos+=1
        caracter=getCaracter(archivo,pos)
        while(caracter != '"'):
            tokens+=caracter
            pos+=1
            caracter=getCaracter(archivo,pos)
        if(caracter == '"'):
            tokens+=caracter
            pos+=1
            #tokensTotal+=1
            return tokens
            
    elif(caracter == "'"):
        tokens+=caracter
        pos+=1
        caracter=getCaracter(archivo,pos)
        while(caracter != "'"):
            tokens+=caracter
            pos+=1
            caracter=getCaracter(archivo,pos)
        if(caracter == "'"):
            tokens+=caracter
            pos+=1
            #tokensTotal+=1
            return tokens

#Creacion de archivo CSV que es la tabla de Tokens
def creaCSV(arreglo,numeroArchivo):
    global concatenacionAliasTipo
    
    concatenacionAliasTipo=""
    num=0
    token=""
    rutaa="C:/Users/Karlii/Documents/8Octavo/MineriaDatos/proyectoFinal/tablaTokensExcel/tablaTokensOcr"+str(numeroArchivo)+".csv"
    archivoCSV=open(rutaa,"w")
    archivoCSV.write('Num.,Token,Descripcion,Alias\n')
    concatenacionAlias=""

    for i in arreglo:
        
        if (i in aliasPalabrasReservadas):
            alias=chr(aliasPalabrasReservadas[i])
            num+=1
            descripcion='Palabra Reservada'
            token=i
            archivoCSV.write(str(num)+','+str(token)+','+descripcion+','+alias+'\n')
            concatenacionAliasTipo+=chr(33)
            #escribir.writerow(token)#se escribe en el data
        elif(i in aliasOperadoresAritmeticos):
            alias=chr(aliasOperadoresAritmeticos[i])
            num+=1
            descripcion='Operador Aritmetico'
            token=i
            archivoCSV.write(str(num)+','+token+','+descripcion+','+alias+'\n')
            concatenacionAliasTipo+=chr(34)
            #escribir.writerow(token)#se escribe en el data
        elif(i in aliasOperadoresRelacionales):
            alias=chr(aliasOperadoresRelacionales[i])
            num+=1
            descripcion='Operador Relacional'
            token=i
            archivoCSV.write(str(num)+','+token+','+descripcion+','+alias+'\n')
            concatenacionAliasTipo+=chr(35)
        elif(i in aliasLibrerias):
            alias=chr(aliasLibrerias[i])
            num+=1
            descripcion='Libreria'
            token=i
            archivoCSV.write(str(num)+','+token+','+descripcion+','+alias+'\n')
            concatenacionAliasTipo+=chr(36)
            #escribir.writerow(token)#se escribe en el data
        elif(i in aliasCaracteresEspeciales):
            alias=chr(aliasCaracteresEspeciales[i])
            num+=1
            descripcion='Caracter Especial'
            token=i
            if token == ",":
                token="coma"
                alias=chr(116)
            concatenacionAliasTipo+=chr(37)
                #token="','"
            archivoCSV.write(str(num)+','+token+','+descripcion+','+alias+'\n')
            # escribir.writerow(token)#se escribe en el data
        elif(i[0] in aliasNumeros):
            tamI=len(i)
            if(tamI == 1):
                alias=chr(aliasNumeros[i])
                num+=1
                descripcion='Numero entero'
                token=i
                archivoCSV.write(str(num)+','+token+','+descripcion+','+alias+'\n')
                concatenacionAliasTipo+=chr(38)
            elif(i.find('.')==-1):
                alias=chr(58)
                num+=1
                descripcion='Numero Entero'
                token=i
                archivoCSV.write(str(num)+','+token+','+descripcion+','+alias+'\n')
                concatenacionAliasTipo+=chr(38)
            else:
                alias=chr(59)
                num+=1
                descripcion='Numero Decimal'
                token=i
                archivoCSV.write(str(num)+','+token+','+descripcion+','+alias+'\n')
                concatenacionAliasTipo+=chr(39)
            
            #escribir.writerow(token)#se escribe en el data
        elif(i[0] in constantesAlfanumericas ):
            alias=chr(60)
            num+=1
            descripcion='Constantes Alfanumericas'
            token=i
            archivoCSV.write(str(num)+','+token+','+descripcion+','+alias+'\n')
            concatenacionAliasTipo+=chr(40)
        else:
            alias=chr(61)
            num+=1
            descripcion='Identificador'
            token=i
            archivoCSV.write(str(num)+','+token+','+descripcion+','+alias+'\n')
            concatenacionAliasTipo+=chr(41)
        concatenacionAlias+=alias
            
           # escribir.writerow(token)
    #escribir.writerow(arreglo)
    #print (concatenacionAlias)
    rutaConcatenacionAliasTipo="C:/Users/Karlii/Documents/8Octavo/MineriaDatos/proyectoFinal/concatenacionTipoAlias/concatenacionAliasTipo"+str(numeroArchivo)+".txt"
    archivoConcatenacion=open(rutaConcatenacionAliasTipo,"w")
    archivoConcatenacion.write(concatenacionAliasTipo)
    archivoConcatenacion.close()
    rutaConcatenacion="C:/Users/Karlii/Documents/8Octavo/MineriaDatos/proyectoFinal/concatenacion/concatenacion"+str(numeroArchivo)+".txt"
    archivoConcatenacion=open(rutaConcatenacion,"w")   
    archivoConcatenacion.write(concatenacionAlias)
    archivoConcatenacion.close()
    
    
    archivoCSV.close()
    return concatenacionAlias


""" METODOS DE BUSQUEDA """
#Metodo 1 busca de un caracter
def buscarRepeticionUnCaracter(concatenacion):
    global repeticiones
    repCaracter=0
    global tokensTotal
    cadena=concatenacion.capitalize()
    for i in range(48,126):
        repCaracter=cadena.count(chr(i))
        razonRepCara=repCaracter/tokensTotal
        repeticiones.append(razonRepCara)


def buscarRepeticionUnCaracterTipo(concatenacion):
    global repeticiones
    global tokensTotal
    repCaracter=0
    cadena=concatenacion.capitalize()
    for  k in range(33,42):
        repCaracter=cadena.count(chr(k))
        razonRepCara=repCaracter/tokensTotal
        repeticiones.append(razonRepCara)
    

#Metodo 2 busca de parejas de caracteres
def buscarRepeticionDosCaracteres(concatenacion):
    global repeticiones
    arregloParejas=[]
    global tokensTotal

    concaCapitalize=concatenacion.capitalize()
    for i in range(33,42):
        repeticion=0
        for j in range(33,42):
            if i != j:
                
                caracter1=chr(i)
                caracter2=chr(j)
            
                conca1=caracter1+caracter2
                arregloParejas.append(conca1)
                repeticion=concaCapitalize.count(conca1)
                razonRepCara=repeticion/tokensTotal
                repeticiones.append(razonRepCara)
            elif i == 37 and j == 37:
                caracter1=chr(i)
                caracter2=chr(j)
            
                conca1=caracter1+caracter2
                arregloParejas.append(conca1)
                repeticion=concaCapitalize.count(conca1)
                razonRepCara=repeticion/tokensTotal
                repeticiones.append(razonRepCara)
    
    #print(repeticiones)
    #print(arregloParejas)
    #print(len(repeticiones))

#Metodo 3 busca de 3 tuplas de caracteres
def buscarRepeticionTresCaracteres(concatenacion):
    global repeticiones
    arregloParejas=[]
    global tokensTotal

    concaCapitalize=concatenacion.capitalize()
    for i in range(33,42):
        repeticion=0
        for j in range(33,42):
            repeticion=0
            for h in range(33,42):
                if(i!=j):
                    if( j!=h):
                        caracter1=chr(i)
                        caracter2=chr(j)
                        caracter3=chr(h)
                        conca1=caracter1+caracter2+caracter3
                        arregloParejas.append(conca1)
                        repeticion=concaCapitalize.count(conca1)
                        razonRepCara=repeticion/tokensTotal
                        repeticiones.append(razonRepCara)
                elif(i==37 and j==37 and h==37):
                    caracter1=chr(i)
                    caracter2=chr(j)
                    caracter3=chr(h)
                    conca1=caracter1+caracter2+caracter3
                    arregloParejas.append(conca1)
                    repeticion=concaCapitalize.count(conca1)
                    razonRepCara=repeticion/tokensTotal
                    repeticiones.append(razonRepCara)
                elif(i==37 and j==37):
                    caracter1=chr(i)
                    caracter2=chr(j)
                    caracter3=chr(h)
                    conca1=caracter1+caracter2+caracter3
                    arregloParejas.append(conca1)
                    repeticion=concaCapitalize.count(conca1)
                    razonRepCara=repeticion/tokensTotal
                    repeticiones.append(razonRepCara)
                elif(j==37 and h==37):
                    caracter1=chr(i)
                    caracter2=chr(j)
                    caracter3=chr(h)
                    conca1=caracter1+caracter2+caracter3
                    arregloParejas.append(conca1)
                    repeticion=concaCapitalize.count(conca1)
                    razonRepCara=repeticion/tokensTotal
                    repeticiones.append(razonRepCara)

def buscar4Tuplas(concatenacion):
    global repeticiones
    global tokensTotal
    concaCapitalize=concatenacion.capitalize()
    for i in range(33,42):
        repeticion=0
        for j in range(33,42):
            repeticion=0
            for h in range(33,42):
                repeticion=0
                for k in range(33,42):
                    if(i != j and j != h and h != k):
                        caracter1=chr(i)
                        caracter2=chr(j)
                        caracter3=chr(h)
                        caracter4=chr(k)
                        conca1=caracter1+caracter2+caracter3+caracter4 
                        repeticion=concaCapitalize.count(conca1)
                        razonRepCara=repeticion/tokensTotal
                        repeticiones.append(razonRepCara)
                    elif(i==37 and j==37 and h==37 and k==37):
                        caracter1=chr(i)
                        caracter2=chr(j)
                        caracter3=chr(h)
                        caracter4=chr(k)
                        conca1=caracter1+caracter2+caracter3+caracter4 
                        repeticion=concaCapitalize.count(conca1)
                        razonRepCara=repeticion/tokensTotal
                        repeticiones.append(razonRepCara)
                    elif(i == 37 and h == 37 and j == 37):
                        caracter1=chr(i)
                        caracter2=chr(j)
                        caracter3=chr(h)
                        caracter4=chr(k)
                        conca1=caracter1+caracter2+caracter3+caracter4 
                        repeticion=concaCapitalize.count(conca1)
                        razonRepCara=repeticion/tokensTotal
                        repeticiones.append(razonRepCara)
                    elif(i == 37 and h == 37):
                        caracter1=chr(i)
                        caracter2=chr(j)
                        caracter3=chr(h)
                        caracter4=chr(k)
                        conca1=caracter1+caracter2+caracter3+caracter4 
                        repeticion=concaCapitalize.count(conca1)
                        razonRepCara=repeticion/tokensTotal
                        repeticiones.append(razonRepCara)
                    elif(h==37 and j ==37 and k==37):
                        caracter1=chr(i)
                        caracter2=chr(j)
                        caracter3=chr(h)
                        caracter4=chr(k)
                        conca1=caracter1+caracter2+caracter3+caracter4 
                        repeticion=concaCapitalize.count(conca1)
                        razonRepCara=repeticion/tokensTotal
                        repeticiones.append(razonRepCara)
                    elif(j==37 and k == 37):
                        caracter1=chr(i)
                        caracter2=chr(j)
                        caracter3=chr(h)
                        caracter4=chr(k)
                        conca1=caracter1+caracter2+caracter3+caracter4 
                        repeticion=concaCapitalize.count(conca1)
                        razonRepCara=repeticion/tokensTotal
                        repeticiones.append(razonRepCara)
                    elif(h==37 and j==37):
                        caracter1=chr(i)
                        caracter2=chr(j)
                        caracter3=chr(h)
                        caracter4=chr(k)
                        conca1=caracter1+caracter2+caracter3+caracter4 
                        repeticion=concaCapitalize.count(conca1)
                        razonRepCara=repeticion/tokensTotal
                        repeticiones.append(razonRepCara)
    
    
                    
    
    
            
"""LIMPIAR CODIGOS """
#limpia Codigo    
def limpiarCodigo(archi,num):
    archivo=archi
    global pos
    tokens=""
    pos=0
    #arregloTokens=[]
    
    while(pos<len(archivo)):
        #print(">>",pos)
        caracter=getCaracter(archivo,pos)
        #print("**",caracter)
        if(caracter == '"' and getCaracter(archivo,pos+1) == '"' and getCaracter(archivo,pos+2) == '"'):          
            tokens+=str(limpiaComentComillaDoble(caracter,archivo))
            
        elif(caracter == "'" and getCaracter(archivo,pos+1) == "'" and getCaracter(archivo,pos+2) == "'"):          
            tokens+=str(limpiaComentComilla(caracter,archivo))
            
        elif(caracter in constantesAlfanumericas):
            #AutomataOperadoresRelaciones
            tokens+=(automataConstantesAlfanumericas(caracter,archivo))
#        if(caracter  == "'"):
#            tokens+=limpiaComentComilla(caracter,archivo)
            
        elif(caracter == "#"):
            tokens+=limpiaComenGato(archivo,caracter)
        else:
            tokens+=caracter
            #arregloTokens.append(caracter)
            pos+=1
    #print(tokens)
    #creaCSV(arregloTokens)
            
    #x=open("C:/Users/Karlii/Documents/8Octavo/MineriaDatos/proyectoFinal/OCRs/sinComentarios/limpio.txt","w")
    rutaNueva="C:/Users/Karlii/Documents/8Octavo/MineriaDatos/proyectoFinal/OCRs/sinComentarios/ocr"+str(num)+".py"
    x=open(rutaNueva,"w")
#    for i in arregloTokens:
    x.write(tokens+"\n")
#    x.close()


#Limpiar Codigo Comilla simple '
def limpiaComentComilla(caracter,archivo):
    global pos
    token=""
    
    if(caracter == "'" and getCaracter(archivo,pos+1) == "'" and getCaracter(archivo,pos+2) == "'"):
        pos+=3
        caracter=getCaracter(archivo,pos)
        while(caracter != "'"):
            pos+=1
            caracter=getCaracter(archivo,pos)
        if(caracter == "'" and getCaracter(archivo,pos+1) == "'" and getCaracter(archivo,pos+2) == "'"):
            pos+=3
            token=""
            return token
    


#limpiar Codigo Comilla Doble
def limpiaComentComillaDoble(caracter,archivo):
    global pos

    token=""
    if(caracter == '"' and getCaracter(archivo,pos+1) == '"' and getCaracter(archivo,pos+2) == '"'):
        pos+=3
        caracter=getCaracter(archivo,pos)
        while(caracter != '"'):
            pos+=1
            caracter=getCaracter(archivo,pos)
        if(caracter == '"' and getCaracter(archivo,pos+1) == '"' and getCaracter(archivo,pos+2) == '"'):
            pos+=3
            token=" "
            return str(token)
    
    
#limpia comentarios que inicien con #
def limpiaComenGato(archivo,caracter):
    global pos
    token=""
    if(caracter == "#"):
        token+=caracter
        pos+=1
        caracter = getCaracter(archivo,pos)
            
        while(caracter != "\n"):
            token=""
            pos+=1
            caracter=getCaracter(archivo,pos)
        if(caracter == "\n"):
            token="\n"
            pos+=1
            return token
    
        
            
            
#Menu
def menu():
    listaPY=[]
    global repeticiones
    global tokensTotal
# Seleccionar la carpeta donde se encuentras los archivos .py
    print("\n\n Escribir la ruta de la carpeta donde se encuentran todos los archivos '.py'")
    ruta=input()
    #ruta = 'C:/Users/Karlii/Documents/8Octavo/MineriaDatos/proyectoFinal/OCR_limpio/'
    listaPY=archivos(ruta)
    #print(listaPY)
    
#Limpiar cada uno de los codigos
    num=1
    print("\n INICIO... Eliminando comentarios de los archivos .py seleccionados")
    for i in listaPY:
        
        archivo=abrir(i)
        #print("#",num,"archivito",i)
        #print(archivo)
        #print(len(archivo))
        limpiarCodigo(archivo,num)
       
        num+=1
    print("\n FIN... Codigos limpios *u* ")
        
#Se realizan los tokens en cada archivo .py
    arregloTokensTotal=[]
    rutaCodigosLimpios="C:/Users/Karlii/Documents/8Octavo/MineriaDatos/proyectoFinal/OCRs/sinComentarios/"
    listaRutas=archivos(rutaCodigosLimpios)
    numArchivo=1
    for j in listaRutas:
        #print(j)
        archivoLimpio=abrir(j)
        #Se concatenan los alias de cada uno de los archivos .py
        tokens(archivoLimpio,numArchivo)        
        arregloTokensTotal.append(tokensTotal)
        numArchivo+=1
    print(arregloTokensTotal)
    #print(repeticiones)
#Se crea Dataset
    archivoDataset=open("dataset.csv","w")
    header="Archivo,"
    for k in range(1,5451):
        header+="Caracteristica #"+str(k)+","
    
    archivoDataset.write(header+"\n")
    numArchivo=1
    caracteristicas=1
    i=0
    print("Total Datos=",len(repeticiones))
    while(i<len(repeticiones)):
        caracteristicas=1
        if caracteristicas==1:
            escribir="Instancia #"+str(numArchivo)
        while(caracteristicas < 5451):
            escribir+=","+str(repeticiones[i])
            caracteristicas+=1
            i+=1
        #print("numeroArchivo",numArchivo)
        numArchivo+=1
        #print(i)
        
        archivoDataset.write(escribir+"\n")
    archivoDataset.close()
menu()
    
