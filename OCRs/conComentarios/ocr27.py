# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:18:42 2016

@author: josue
"""
#caracteristicas
#import matplotlib.pyplot as plt
import matplotlib.image as mpimg #importar una funcion de la libreria matplotlib y guardamos como mpimg
import csv#importamos libreria para archivos csv
import os#importamos librerias de sistema operativo

#inicio del programa
archivo= open('DataSetNew.csv', 'w', newline='') 
salida = csv.writer(archivo) #se transfiere el archivo a esta variable para poder escribir en el
 
def FilasEntreColumnas(tam):#Se declara la función Filas entre Columnas que recibe la variable tam
    FilasColumnas=tam[0]/tam[1] #FilasColumnas es una variable
    print("Procesando imagen: ",FilasColumnas)#Imprimimos la variable FilasColumnas para verificar el proceso
    return FilasColumnas#Devolvemos el valor de la variable como resultado de la operación
    #Segunda caracteristica
    #El area del caracter Número de Bits Blancos
def Area(tam, mat):#En esta función realizamos la busqueda de los Bits Blancos
    areaB=0 #Bits blancos
    areaN=0 #Bits negros
    for i in range(0,tam[0]): #for recorre las filas
        for j in range(0,tam[1]): #for recorre las columnas
            if(mat[i][j]!=0): #condicion para clasificar el valor del bits
                areaN=areaN+1 #si se cumple aumenta el contador de bits negros
            else:
                areaB=areaB+1 #si no cumple aumentan el contador de bits blancos
    print("Número de Blancos: " ,areaB)     
            #fin del for j
        #fin del for i  
    return areaB#Devolvemos el valor de Bits Blancos que es el resultado
        #Caracteristicas: CANTIDAD DE CORTES EN FILAS
#Tercer caracteristica número de cortes en la fila a un cuarto de la imagen 
def FilasDeCorteUnCuarto(tam,mat):#En esta caracteristica realizaremos la medida de un cuarto de la imagen
    cortes1=0#Iniciamos un contador
    CFuncuarto=int(tam[1]/4)#CFuncuarto en el resultado de nuestra operación de el tamaño de filas entre cuatro
    Aux1=mat[CFuncuarto][0]#Aux1 nos ayuda a inicializar nuestra matriz
    for i in range(0,tam[1]):#For para recorrer las filas 
        if(Aux1!=mat[CFuncuarto][i]):#Si Aux1 es diferente de a lo que contiene la matriz
            Aux1=mat[CFuncuarto][i]#Verificacion de existencia de cortes o cambios
            cortes1=cortes1+1#Entonces nuestro contador se incrementa
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la fila a 1/4: ",cortes1)
    return cortes1#Retornamos el valor de nuestro contador
#Cuarta caracteristica número de cortes en la fila en medio de la imagen     
def FilasCorteEnMedio(tam,mat):#En esta caracteristica realizaremos la medida de en medio de la imagen en filas
    cortes2=0#Inicializamos nuestro contador
    CFenmedio=int(tam[0]/2)#CFenmedio es el resultado de la división de tamaño de filas entre dos
    Aux=mat[CFenmedio][0]#Aux es una variable que nos ayuda a inicializar nuestra matriz
    for i in range(0,tam[1]):#For para recorrer las filas 
        if(Aux!=mat[CFenmedio][i]):#Si Aux es diferente a lo que tenemos dentro de la matriz
            Aux=mat[CFenmedio][i]#Verificacion de existencia de cortes o cambios
            cortes2=cortes2+1#Entonces nuestro contador se incrementa
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la fila de en medio: ",cortes2)
    return cortes2#Retornamos el valor de nuestro contador
#Quinta caracteristica número de cortes en la fila a tres cuartos de la imagen          
def FilasDeCorteTresCuartos(tam,mat):#En esta caracteristica realizaremos la medida a tres cuartos de la imagen en filas
    cortes3=0#Inicializamos el contador
    CFtrescuatro=int((tam[0]/4)*3)#CFtrescuartos es el resultado de nuestra operación de el tamaño de filas entre cuatro por tres
    Aux2=mat[CFtrescuatro][0]#Aux2 es una variable que nos ayuda a inicializar nuestra matriz
    for i in range(0,tam[1]):#for para poder recorrer las filas
        if(Aux2!=mat[CFtrescuatro][i]):#Si el Aux2 es diferente a lo que tenemos dentro de la matriz
            Aux2=mat[CFtrescuatro][i]#Verificación de existencia de cortes o cambios
            cortes3=cortes3+1#Entonces nuestro contador se incrementa
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la fila a 3/4: ",cortes3)
    return cortes3#Retornamos el valor cortes3
        #Caracteristicas: CANTIDAD DE CORTES EN COLUMNAS
#Sexta caracteristica número de cortes en la columna a un cuartos de la imagen          
def ColumnasCortesAUnCuarto(tam,mat):#En esta caracteristica realizaremos la medida a un cuartos de la imagen en columnas
    cortes4=0#Inicializamos el contador
    CCuncuarto=int(tam[1]/4)#CCuncuarto el resultado de nuestra operación de el tamaño de columnas entre cuatro
    Aux4=mat[0][CCuncuarto]#Aux4 es una variable que nos ayuda a inicializar la matriz
    for i in range(0,tam[0]):#for para recorrer la columna
        if(Aux4!=mat[i][CCuncuarto]):#Si Aux4 es diferente a lo que tengamos en la matriz
            Aux4=mat[i][CCuncuarto]#Verificacion de existencia de cortes o cambios
            cortes4=cortes4+1#Entonces nuestro contador lo incrementamos
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la columna a 1/4: ",cortes4)
    return cortes4#Retornamos el valor cortes4
#Septima caracteristica número de cortes en la columa en medio de la imagen              
def ColumnasCorteEnMedio(tam,mat):#En esta caracteristica realizaremos la medida de en medio de la imagen en columnas
    cortes5=0#Iniciaizamos nuestro contador 
    CCenmedio=int(tam[1]/2)#CCenmedio es nuestro resultado de la operacion del ancho entre dos
    Aux3=mat[0][CCenmedio]#Aux3 es una variable que nos ayuda a inicializar la matriz
    for i in range(0,tam[0]):#for para recorrer la columna
        if(Aux3!=mat[i][CCenmedio]):#Si Aux3 es diferente a lo que tengamos en la matriz
            Aux3=mat[i][CCenmedio]#Verificacion de existencia de cortes o cambios
            cortes5=cortes5+1#Entonces nuestro contador lo incrementamos
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la columna de en medio: ",cortes5)
    return cortes5#Retornamos el valor cortes5
#Octava caracteristica número de cortes en la columa a tres cuartos de la imagen                  
def ColumnasCortesATresCuartos(tam,mat):#En esta caracteristica realizaremos la medida a tres cuartos de la imagen en columnas
    cortes6=0#Inicializamos un contador
    CCtrescuartos=int((tam[1]/4)*3)#CCtrescuartos es el resultado de nuestra operación de el tamaño de columnas entre cuatro por tres
    Aux5=mat[0][CCtrescuartos]#Aux5 es una variable que nos ayuda a inicializar la matriz
    for i in range(0,tam[0]):#for para recorrer la columna
        if(Aux5!=mat[i][CCtrescuartos]):##Si Aux5 es diferente a lo que tengamos en la matriz
            Aux5=mat[i][CCtrescuartos]#Verificacion de existencia de cortes o cambios
            cortes6=cortes6+1#Entonces nuestro contador lo incrementamos
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la columna a 3/4: ",cortes6)
    return cortes6#Retornamos el valor de nuestro contador cortes6
        #Caracteristicas: RELACION DE AREAS EN FILAS
#Novena caracteristica la relación de pixeles blancos en la fila a un cuarto de la imagen              
def AreaDeFilasAUnCuarto(tam,mat):#En esta función encontramos el número de píxeles en la fila 1/4
    cont1=0#contador de píxeles
    uncuarto=int(tam[0]/4)#la variable uncuarto la obtenemos de la division entre cuatro para obtener un cuarto
    mat[uncuarto][0]#inicializamos la matriz
    for i in range(0,tam[1]):#for para recorrer la fila que esta a un cuarto de la imagen
        if (mat[uncuarto][i]!=0):#condicion para contar píxeles
            
            cont1=cont1+1#si se cumple la condicion if incrementa nuestro contador 
        #fin de condicion if
    #fin de ciclo for
    cont1/tam[1]
    print("Número de píxeles en la fila a 1/4: ",cont1)
    return cont1#retornamos el valor de nuestro contador 
#Decima caracteristica la relación de pixeles blancos en la fila de en medio de la imagen
def AreaDeFilasEnMedio(tam,mat):#En esta funcion buscamos encontrar el nùmero de pìxeles en la fila de en medio 
    cont2=0#contador de píxeles
    enmedio=int(tam[0]/2)#la variable enmedio es el resultado de la matriz entre dos en filas
    mat[enmedio][0]#inicializamos nuestra matriz
    for i in range(0,tam[1]):#For para recorrer las filas
        if (mat[enmedio][i]!=0):#If es la condicion para contar los píxeles
            
            cont2=cont2+1#si se cumple aumenta el contador de píxeles
        #fin de condicion if    
    #fin de ciclo for
    cont2/tam[1]
    print("Número de píxeles en la fila de en medio: ",cont2)
    return cont2 #retornamos el valor de cuestro contador
#Onceava caracteristica la relación de pixeles blancos en la fila a tres cuarto de la imagen    
def AreaDeFilasTresCuartos(tam,mat):#En esta función enconmtramos el número de píxeles en la fila 3/4
    cont3=0#Inicializamos un contador
    trescuatro=int((tam[0]/4)*3)#Para obtener tres cuartos de la imagen hacemos la division entre cuatro y la multiplicamos por tres
    mat[trescuatro][0]#inicializamos la matriz
    for i in range(0,tam[1]):##for para recorrer la fila que esta a tres cuartos de la imagen
        if (mat[trescuatro][i]!=0):##condicion para contar píxeles
            
            cont3=cont3+1##si se cumple la condicion if incrementa nuestro contador 
        #fin de condicion if
    #fin de ciclo for            
    cont3/tam[1]
    print("Número de píxeles en la fila a 3/4: ",cont3)
    return cont3#retornamos el valor de nuestro contador         
        #Caracteristicas RELACION DE AREAS EN COLUMNAS
#Doceava caracteristica la relación de pixeles blancos en la columna a un cuarto de la imagen    
def AreadeColumnasAUnCuarto(tam,mat):#esta funcion buscamos encontrar el nùmero de pìxeles en la columna a 1/4 de la imagen 
    cont4=0#inicializamos un contador
    Cuncuarto=int(tam[1]/4)#La variable Cuncuarto es el resultado de el nùmero de columnas entre cuatro
    mat[Cuncuarto][0]#inicializamos la matriz
    for i in range(0,tam[0]):#For para recorrer las columnas
        if (mat[i][Cuncuarto]!=0):#If es la condicion para contar los píxeles
            
            cont4=cont4+1#si se cumple aumenta nuestro contador
        #fin de condicion if
    #fin de ciclo for 
    cont4/tam[0]
    print("Número de píxeles en la columna a 1/4: ",cont4)
    return cont4#retornamos el valor de nuestro contador 
#Treceava caracteristica la relación de pixeles blancos en la columna de en medio de la imagen    
def AreaDeColumnasEnMedio(tam,mat):#En esta funcion buscamos encontrar el nùmero de pìxeles en la columna de en medio 
    cont5=0#inicializamo un contador 
    Cenmedio=int(tam[1]/2)#La variable Cenmedio es el resultado de la matriz entre dos en Columnas
    mat[Cenmedio][0]#Inicializamos la matriz 
    for i in range(0,tam[0]):#For para recorrer las columnas
        if (mat[i][Cenmedio]!=0):#If es la condicion para contar los píxeles
            
            cont5=cont5+1#si se cumple aumenta nuestro contador
        #fin de condicion if
    #fin de ciclo for 
    cont5/tam[0]
    print("Número de píxeles en la columna de en medio: ",cont5)
    return cont5#retornamos el valor de nuestro contador
#Catorceava caracteristica la relación de pixeles blancos en la columna a tres cuarto de la imagen        
def AreaDeColumnasTresCuartos(tam,mat):#esta funcion buscamos encontrar el nùmero de pìxeles en la columna a 3/4 de la imagen 
    cont6=0#inicializamos el contador
    Ctrescuatro=int((tam[1]/4)*3)#La variable Ctrescuartos hacemos la division del nùmero de columnas entre cuatro y lo multiplicamos por tres
    mat[Ctrescuatro][0]#Inicializamos la matriz
    for i in range(0,tam[0]):#for para poder recorrer las columnas 
        if (mat[i][Ctrescuatro]!=0):#If si la condicion se cumple se cuentan los píxeles
            
            cont6=cont6+1#Se incrementa nuestro contador
        #fin de condicion if
    #fin de ciclo for 
    cont6/tam[0]
    print("Número de píxeles en la columna a 3/4: ",cont6)
    return cont6#Retornamos el valor de nuestro contador

clase=-1 #Creamos la variable clase que servira para indicara a que numero pertenecen las caracteristicas obtenidas
root='arialSegmented' #nombre de la carpeta que contiene las imagenes
#inicia for
#dirName que indica el nombre del directorio principal y subcarpetas
#subdirList que indica las subcarpetas de cada carpeta
#fileList que proporciona una lista con los nombres de los archivos de cada carpeta
for dirName, subdirList, fileList in os.walk(root): #for para recorer los archivos de la carpeta principal
    #for para recorer las subcarpetas. fname es para obtener el nombre de cada imagen
    for fname in fileList: #for para obtener los nombre de las imagenes
        nameima=dirName+'/'+fname #obtengo la ruta de la imagen
        img=mpimg.imread(nameima) #se obtienen los datos de la imagen en una variable
        #imgplot = plt.imshow(img)
        mat=img #copio los datos de la imagen en la variable mat (es una matriz) para procesarla
        tam=mat.shape #obtengo las dimenciones de la matriz mat
        Razon=FilasEntreColumnas(tam)#Primera caracteristica Filas entre Columnas
        area=Area(tam,mat)#Segunda caracteristica El Ârea de la Imagen
        FCorteC=FilasDeCorteUnCuarto(tam,mat)#Tercer caracteristica
        FCorteM=FilasCorteEnMedio(tam,mat)#Cuarta caracteristica
        FCorteTC=FilasDeCorteTresCuartos(tam,mat)#Quinta Caracteristica
        CCortesC=ColumnasCortesAUnCuarto(tam,mat)#Sexta Caracteristica
        CCortesM=ColumnasCorteEnMedio(tam,mat)#Septima Caracteristica
        CCortesTC=ColumnasCortesATresCuartos(tam,mat)#Octava Caracteristica
        AFilasC=AreaDeFilasAUnCuarto(tam,mat)#Novena Caracteristica
        AFilasM=AreaDeFilasEnMedio(tam,mat)#Decima Caracteristica
        AFilasTC=AreaDeFilasTresCuartos(tam,mat)#DecimaPrimera Caracteristica
        AColumnasC=AreadeColumnasAUnCuarto(tam,mat)#DecimaSegunda Caracteristica
        AColumnasM=AreaDeColumnasEnMedio(tam,mat)#DecimaTercera Caracteristiva
        AColumnasTC=AreaDeColumnasTresCuartos(tam,mat)#DecimaCuarta Caracteristica
        #escribo las caracteristicas en el archivo csv
        salida.writerow([Razon,area,FCorteC,FCorteM,FCorteTC,CCortesC,CCortesM,CCortesTC,AFilasC,AFilasM,AFilasTC,AColumnasC,AColumnasM,AColumnasTC,clase])
        #Fin del segundo for
    clase=clase+1 #aumento la clase en uno cuando termine de leer una subcarpeta
    #fin del primer for
archivo.close() #Se cierra el archivo
#fin del programa 


# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 19:28:48 2016

@author: josue
"""
#import matplotlib.pyplot as plt
import matplotlib.image as mpimg #importar una funcion de la libreria matplotlib y guardamos como mpimg
import csv#importamos libreria para archivos csv
import math#importar libreria para funciones matematicas
Archivo= open('DataSetNew.csv')#se abre el archivo csv
lns=csv.reader(Archivo) #Leemos el archivo Dataset.csv
dataset=list(lns)#la variable dataset contendra el dataset en forma de lista
print("Nombre de la imagen: ")#impresion de pantalla
NImagen=(input())#variable de tipo int
img=mpimg.imread(NImagen)#leemos la imagen y guardamos en una variable
mat=img #copio los datos de la imagen en la variable mat (es una matriz) para procesarla
tam=mat.shape#obtenemos las medidas de la imagen en alto y ancho
#Mostramos la imagen
#imgplot=plt.imshow(img)


#Imprimimos las dimensiones de la imagen como referencia del numero de filas y columnas que la conforman 
print('][][][][][][][][]][][][][][][][][][][][][][][][][][][][][][][][][][][')
#print('Dimenciones de la imagen ',tam)

def FilasEntreColumnas(tam):#Se declara la función Filas entre Columnas que recibe la variable tam
    FilasColumnas=tam[0]/tam[1] #FilasColumnas es una variable
    print("Procesando imagen: ",FilasColumnas)#Imprimimos la variable FilasColumnas para verificar el proceso
    return FilasColumnas#Devolvemos el valor de la variable como resultado de la operación
    #Segunda caracteristica
    #El area del caracter Número de Bits Blancos
def Area(tam, mat):#En esta función realizamos la busqueda de los Bits Blancos
    areaB=0 #Bits blancos
    areaN=0 #Bits negros
    for i in range(0,tam[0]): #for recorre las filas
        for j in range(0,tam[1]): #for recorre las columnas
            if(mat[i][j]!=0): #condicion para clasificar el valor del bits
                areaN=areaN+1 #si se cumple aumenta el contador de bits negros
            else:
                areaB=areaB+1 #si no cumple aumentan el contador de bits blancos
    print("Número de Blancos: " ,areaB)     
            #fin del for j
        #fin del for i  
    return areaB#Devolvemos el valor de Bits Blancos que es el resultado
        #Caracteristicas: CANTIDAD DE CORTES EN FILAS
#Tercer caracteristica número de cortes en la fila a un cuarto de la imagen 
def FilasDeCorteUnCuarto(tam,mat):#En esta caracteristica realizaremos la medida de un cuarto de la imagen
    cortes1=0#Iniciamos un contador
    CFuncuarto=int(tam[1]/4)#CFuncuarto en el resultado de nuestra operación de el tamaño de filas entre cuatro
    Aux1=mat[CFuncuarto][0]#Aux1 nos ayuda a inicializar nuestra matriz
    for i in range(0,tam[1]):#For para recorrer las filas 
        if(Aux1!=mat[CFuncuarto][i]):#Si Aux1 es diferente de a lo que contiene la matriz
            Aux1=mat[CFuncuarto][i]#Verificacion de existencia de cortes o cambios
            cortes1=cortes1+1#Entonces nuestro contador se incrementa
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la fila a 1/4: ",cortes1)
    return cortes1#Retornamos el valor de nuestro contador
#Cuarta caracteristica número de cortes en la fila en medio de la imagen     
def FilasCorteEnMedio(tam,mat):#En esta caracteristica realizaremos la medida de en medio de la imagen en filas
    cortes2=0#Inicializamos nuestro contador
    CFenmedio=int(tam[0]/2)#CFenmedio es el resultado de la división de tamaño de filas entre dos
    Aux=mat[CFenmedio][0]#Aux es una variable que nos ayuda a inicializar nuestra matriz
    for i in range(0,tam[1]):#For para recorrer las filas 
        if(Aux!=mat[CFenmedio][i]):#Si Aux es diferente a lo que tenemos dentro de la matriz
            Aux=mat[CFenmedio][i]#Verificacion de existencia de cortes o cambios
            cortes2=cortes2+1#Entonces nuestro contador se incrementa
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la fila de en medio: ",cortes2)
    return cortes2#Retornamos el valor de nuestro contador
#Quinta caracteristica número de cortes en la fila a tres cuartos de la imagen          
def FilasDeCorteTresCuartos(tam,mat):#En esta caracteristica realizaremos la medida a tres cuartos de la imagen en filas
    cortes3=0#Inicializamos el contador
    CFtrescuatro=int((tam[0]/4)*3)#CFtrescuartos es el resultado de nuestra operación de el tamaño de filas entre cuatro por tres
    Aux2=mat[CFtrescuatro][0]#Aux2 es una variable que nos ayuda a inicializar nuestra matriz
    for i in range(0,tam[1]):#for para poder recorrer las filas
        if(Aux2!=mat[CFtrescuatro][i]):#Si el Aux2 es diferente a lo que tenemos dentro de la matriz
            Aux2=mat[CFtrescuatro][i]#Verificación de existencia de cortes o cambios
            cortes3=cortes3+1#Entonces nuestro contador se incrementa
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la fila a 3/4: ",cortes3)
    return cortes3#Retornamos el valor cortes3
        #Caracteristicas: CANTIDAD DE CORTES EN COLUMNAS
#Sexta caracteristica número de cortes en la columna a un cuartos de la imagen          
def ColumnasCortesAUnCuarto(tam,mat):#En esta caracteristica realizaremos la medida a un cuartos de la imagen en columnas
    cortes4=0#Inicializamos el contador
    CCuncuarto=int(tam[1]/4)#CCuncuarto el resultado de nuestra operación de el tamaño de columnas entre cuatro
    Aux4=mat[0][CCuncuarto]#Aux4 es una variable que nos ayuda a inicializar la matriz
    for i in range(0,tam[0]):#for para recorrer la columna
        if(Aux4!=mat[i][CCuncuarto]):#Si Aux4 es diferente a lo que tengamos en la matriz
            Aux4=mat[i][CCuncuarto]#Verificacion de existencia de cortes o cambios
            cortes4=cortes4+1#Entonces nuestro contador lo incrementamos
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la columna a 1/4: ",cortes4)
    return cortes4#Retornamos el valor cortes4
#Septima caracteristica número de cortes en la columa en medio de la imagen              
def ColumnasCorteEnMedio(tam,mat):#En esta caracteristica realizaremos la medida de en medio de la imagen en columnas
    cortes5=0#Iniciaizamos nuestro contador 
    CCenmedio=int(tam[1]/2)#CCenmedio es nuestro resultado de la operacion del ancho entre dos
    Aux3=mat[0][CCenmedio]#Aux3 es una variable que nos ayuda a inicializar la matriz
    for i in range(0,tam[0]):#for para recorrer la columna
        if(Aux3!=mat[i][CCenmedio]):#Si Aux3 es diferente a lo que tengamos en la matriz
            Aux3=mat[i][CCenmedio]#Verificacion de existencia de cortes o cambios
            cortes5=cortes5+1#Entonces nuestro contador lo incrementamos
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la columna de en medio: ",cortes5)
    return cortes5#Retornamos el valor cortes5
#Octava caracteristica número de cortes en la columa a tres cuartos de la imagen                  
def ColumnasCortesATresCuartos(tam,mat):#En esta caracteristica realizaremos la medida a tres cuartos de la imagen en columnas
    cortes6=0#Inicializamos un contador
    CCtrescuartos=int((tam[1]/4)*3)#CCtrescuartos es el resultado de nuestra operación de el tamaño de columnas entre cuatro por tres
    Aux5=mat[0][CCtrescuartos]#Aux5 es una variable que nos ayuda a inicializar la matriz
    for i in range(0,tam[0]):#for para recorrer la columna
        if(Aux5!=mat[i][CCtrescuartos]):##Si Aux5 es diferente a lo que tengamos en la matriz
            Aux5=mat[i][CCtrescuartos]#Verificacion de existencia de cortes o cambios
            cortes6=cortes6+1#Entonces nuestro contador lo incrementamos
        #fin de condicion if
    #fin de ciclo for 
    print("Número de cortes en la columna a 3/4: ",cortes6)
    return cortes6#Retornamos el valor de nuestro contador cortes6
        #Caracteristicas: RELACION DE AREAS EN FILAS
#Novena caracteristica la relación de pixeles blancos en la fila a un cuarto de la imagen              
def AreaDeFilasAUnCuarto(tam,mat):#En esta función encontramos el número de píxeles en la fila 1/4
    cont1=0#contador de píxeles
    uncuarto=int(tam[0]/4)#la variable uncuarto la obtenemos de la division entre cuatro para obtener un cuarto
    mat[uncuarto][0]#inicializamos la matriz
    for i in range(0,tam[1]):#for para recorrer la fila que esta a un cuarto de la imagen
        if (mat[uncuarto][i]!=0):#condicion para contar píxeles
            
            cont1=cont1+1#si se cumple la condicion if incrementa nuestro contador 
        #fin de condicion if
    #fin de ciclo for
    cont1/tam[1]
    print("Número de píxeles en la fila a 1/4: ",cont1)
    return cont1#retornamos el valor de nuestro contador 
#Decima caracteristica la relación de pixeles blancos en la fila de en medio de la imagen
def AreaDeFilasEnMedio(tam,mat):#En esta funcion buscamos encontrar el nùmero de pìxeles en la fila de en medio 
    cont2=0#contador de píxeles
    enmedio=int(tam[0]/2)#la variable enmedio es el resultado de la matriz entre dos en filas
    mat[enmedio][0]#inicializamos nuestra matriz
    for i in range(0,tam[1]):#For para recorrer las filas
        if (mat[enmedio][i]!=0):#If es la condicion para contar los píxeles
            
            cont2=cont2+1#si se cumple aumenta el contador de píxeles
        #fin de condicion if    
    #fin de ciclo for
    cont2/tam[1]
    print("Número de píxeles en la fila de en medio: ",cont2)
    return cont2 #retornamos el valor de cuestro contador
#Onceava caracteristica la relación de pixeles blancos en la fila a tres cuarto de la imagen    
def AreaDeFilasTresCuartos(tam,mat):#En esta función enconmtramos el número de píxeles en la fila 3/4
    cont3=0#Inicializamos un contador
    trescuatro=int((tam[0]/4)*3)#Para obtener tres cuartos de la imagen hacemos la division entre cuatro y la multiplicamos por tres
    mat[trescuatro][0]#inicializamos la matriz
    for i in range(0,tam[1]):##for para recorrer la fila que esta a tres cuartos de la imagen
        if (mat[trescuatro][i]!=0):##condicion para contar píxeles
            
            cont3=cont3+1##si se cumple la condicion if incrementa nuestro contador 
        #fin de condicion if
    #fin de ciclo for            
    cont3/tam[1]
    print("Número de píxeles en la fila a 3/4: ",cont3)
    return cont3#retornamos el valor de nuestro contador         
        #Caracteristicas RELACION DE AREAS EN COLUMNAS
#Doceava caracteristica la relación de pixeles blancos en la columna a un cuarto de la imagen    
def AreadeColumnasAUnCuarto(tam,mat):#esta funcion buscamos encontrar el nùmero de pìxeles en la columna a 1/4 de la imagen 
    cont4=0#inicializamos un contador
    Cuncuarto=int(tam[1]/4)#La variable Cuncuarto es el resultado de el nùmero de columnas entre cuatro
    mat[Cuncuarto][0]#inicializamos la matriz
    for i in range(0,tam[0]):#For para recorrer las columnas
        if (mat[i][Cuncuarto]!=0):#If es la condicion para contar los píxeles
            
            cont4=cont4+1#si se cumple aumenta nuestro contador
        #fin de condicion if
    #fin de ciclo for 
    cont4/tam[0]
    print("Número de píxeles en la columna a 1/4: ",cont4)
    return cont4#retornamos el valor de nuestro contador 
#Treceava caracteristica la relación de pixeles blancos en la columna de en medio de la imagen    
def AreaDeColumnasEnMedio(tam,mat):#En esta funcion buscamos encontrar el nùmero de pìxeles en la columna de en medio 
    cont5=0#inicializamo un contador 
    Cenmedio=int(tam[1]/2)#La variable Cenmedio es el resultado de la matriz entre dos en Columnas
    mat[Cenmedio][0]#Inicializamos la matriz 
    for i in range(0,tam[0]):#For para recorrer las columnas
        if (mat[i][Cenmedio]!=0):#If es la condicion para contar los píxeles
            cont5/tam[0]
            cont5=cont5+1#si se cumple aumenta nuestro contador
        #fin de condicion if
    #fin de ciclo for 
    cont5/tam[0]
    print("Número de píxeles en la columna de en medio: ",cont5)
    return cont5#retornamos el valor de nuestro contador
#Catorceava caracteristica la relación de pixeles blancos en la columna a tres cuarto de la imagen        
def AreaDeColumnasTresCuartos(tam,mat):#esta funcion buscamos encontrar el nùmero de pìxeles en la columna a 3/4 de la imagen 
    cont6=0#inicializamos el contador
    Ctrescuatro=int((tam[1]/4)*3)#La variable Ctrescuartos hacemos la division del nùmero de columnas entre cuatro y lo multiplicamos por tres
    mat[Ctrescuatro][0]#Inicializamos la matriz
    for i in range(0,tam[0]):#for para poder recorrer las columnas 
        if (mat[i][Ctrescuatro]!=0):#If si la condicion se cumple se cuentan los píxeles
            
            cont6=cont6+1#Se incrementa nuestro contador
        #fin de condicion if
    #fin de ciclo for 
    cont6/tam[0]
    print("Número de píxeles en la columna a 3/4: ",cont6)
    return cont6#Retornamos el valor de nuestro contador

def knn(Razon,area,FCorteC,FCorteM,FCorteTC,CCortesC,CCortesM,CCortesTC,AFilasC,AFilasM,AFilasTC,AColumnasC,AColumnasM,AColumnasTC):
    print('><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><')    
    print("Numero de vecinos a considerar: ",end="")
    NumerokVecinos=int(input())#la variable NumerokVecinos contendra el numero de vecinos que evaluaremos
    contador=0#variable contador   
    for i in dataset:#for para poder recorrer el dataset en todas las posiciones    
        dataset[contador][0]=float(dataset[contador][0])#Convertirmos a flotante dataset en su posición [contador][0]
        dataset[contador][1]=int(dataset[contador][1])#Convertirmos a entero dataset en su posición [contador][1]
        dataset[contador][2]=int(dataset[contador][2])#Convertirmos a entero dataset en su posición [contador][2]
        dataset[contador][3]=int(dataset[contador][3])#Convertirmos a entero dataset en su posición [contador][3]
        dataset[contador][4]=int(dataset[contador][4])#Convertirmos a entero dataset en su posición [contador][4]
        dataset[contador][5]=int(dataset[contador][5])#Convertirmos a entero dataset en su posición [contador][5]
        dataset[contador][6]=int(dataset[contador][6])#Convertirmos a entero dataset en su posición [contador][6]
        dataset[contador][7]=int(dataset[contador][7])#Convertirmos a entero dataset en su posición [contador][7]
        dataset[contador][8]=int(dataset[contador][8])#Convertirmos a entero dataset en su posición [contador][8]
        dataset[contador][9]=int(dataset[contador][9])#Convertirmos a entero dataset en su posición [contador][9]
        dataset[contador][10]=int(dataset[contador][10])#Convertirmos a entero dataset en su posición [contador][10]
        dataset[contador][11]=int(dataset[contador][11])#Convertirmos a entero dataset en su posición [contador][11]
        dataset[contador][12]=int(dataset[contador][12])#Convertirmos a entero dataset en su posición [contador][12]
        dataset[contador][13]=int(dataset[contador][13])#Convertirmos a entero dataset en su posición [contador][13]
        dataset[contador][14]=int(dataset[contador][14])#Convertirmos a entero dataset en su posición [contador][14]
#Aplicamos la formula para obtener la distancia Euclidiana, es decir una sumatoria de cada caracteristica del dataset
#menos cada caracteristica de la imagen a clasificar
        interna=((dataset[contador][0]-Razon)**2)+((dataset[contador][1]-area)**2)+((dataset[contador][2]-FCorteC)**2)+((dataset[contador][3]-FCorteM)**2)+((dataset[contador][4]-FCorteTC)**2)+((dataset[contador][5]-CCortesC)**2)+((dataset[contador][6]-CCortesM)**2)+((dataset[contador][7]-CCortesTC)**2)+((dataset[contador][8]-AFilasC)**2)+((dataset[contador][9]-AFilasM)**2)+((dataset[contador][10]-AFilasTC)**2)+((dataset[contador][11]-AColumnasC)**2)+((dataset[contador][12]-AColumnasM)**2)+((dataset[contador][13]-AColumnasTC)**2)
        raiz=math.sqrt(interna)#la segunda parte de la formula es obtener la raiz cuadrada de la sumatoria
        dataset[contador].append(raiz)#agregamos una nueva fila a nuestra matriz que contendra la raiz cuadrada de cada instancia
        dataset[contador].append(contador)#agregamos una nueva fila a nuestra matriz que contendra el contador de cada instancia
        contador=contador+1#Incrementamos un número al contador
              
    dataset.sort(key=lambda dataset: dataset[15])#Ordenamos de menor a mayor las distancias 
    
    print('********************************************************************')
    print('\t Información general: ')
    print('    Formato de la Imagen: .png ')
    print('    Número de instancias: ',contador)
    print('    Número de Caracteristicas: 14')
    print('    Número de Clases: 10 ')
    print('    Nombre de las clases:{0,1,2,3,4,5,6,7,8,9}')
    print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| \n')   

    ContadorClase0=0#Variable de tipo int
    ContadorClase1=0#Variable de tipo int
    ContadorClase2=0#Variable de tipo int
    ContadorClase3=0#Variable de tipo int
    ContadorClase4=0#Variable de tipo int
    ContadorClase5=0#Variable de tipo int
    ContadorClase6=0#Variable de tipo int
    ContadorClase7=0#Variable de tipo int
    ContadorClase8=0#Variable de tipo int
    ContadorClase9=0#Variable de tipo int
    
    for i in range(0,NumerokVecinos):
          if(dataset[i][14]==0):
              ContadorClase0=ContadorClase0+1#Incrementamos el contador 
              
          if (dataset[i][14]==1):
              ContadorClase1=ContadorClase1+1 
          
          if (dataset[i][14]==2):
              ContadorClase2=ContadorClase2+1
        
          if (dataset[i][14]==3):
              ContadorClase3=ContadorClase3+1
          
          if (dataset[i][14]==4):
              ContadorClase4=ContadorClase4+1
        
          if (dataset[i][14]==5):
              ContadorClase5=ContadorClase5+1
          
          if (dataset[i][14]==6):
              ContadorClase6=ContadorClase6+1
        
          if (dataset[i][14]==7):
              ContadorClase7=ContadorClase7+1
         
          if (dataset[i][14]==8):
              ContadorClase8=ContadorClase8+1
          
          if (dataset[i][14]==9):
              ContadorClase9=ContadorClase9+1      
          
          print('# Instancia',dataset[i][16],' | Distancia obtenida  ',dataset[i][15],' | Clase ',dataset[i][14])
    print('*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+')
    print('Resumen de instancias')
    print('Se encontraron: ',ContadorClase0,'instancias de la clase : 0') 
    print('Se encontraron: ',ContadorClase1,'instancias de la clase : 1')
    print('Se encontraron: ',ContadorClase2,'instancias de la clase : 2')
    print('Se encontraron: ',ContadorClase3,'instancias de la clase : 3')
    print('Se encontraron: ',ContadorClase4,'instancias de la clase : 4')
    print('Se encontraron: ',ContadorClase5,'instancias de la clase : 5')
    print('Se encontraron: ',ContadorClase6,'instancias de la clase : 6')
    print('Se encontraron: ',ContadorClase7,'instancias de la clase : 7')
    print('Se encontraron: ',ContadorClase8,'instancias de la clase : 8')
    print('Se encontraron: ',ContadorClase9,'instancias de la clase : 9\n\t')
    
    if(ContadorClase0>ContadorClase1):#Si ContadorClase0 es mayor que todas las demas clases 
        if(ContadorClase0>ContadorClase2):
            if(ContadorClase0>ContadorClase3):
                if(ContadorClase0>ContadorClase4):
                    if(ContadorClase0>ContadorClase5):
                        if(ContadorClase0>ContadorClase6):
                            if(ContadorClase0>ContadorClase7):
                                if(ContadorClase0>ContadorClase8):
                                    if(ContadorClase0>ContadorClase9):
                                        print('La Imagen es un 0');#Entonces la imagen nueva pertenece a esta clase
    
    if(ContadorClase1>ContadorClase0):#Si ContadorClase1 es mayor que todas las demas
        if(ContadorClase1>ContadorClase2):
            if(ContadorClase1>ContadorClase3): 
                if(ContadorClase1>ContadorClase4):
                    if(ContadorClase1>ContadorClase5):
                        if(ContadorClase1>ContadorClase6):
                            if(ContadorClase1>ContadorClase7):
                                if(ContadorClase1>ContadorClase8):
                                    if(ContadorClase1>ContadorClase9):
                                        print('La Imagen es un 1');#Entonces la imagen nueva pertenece a esta clase
    
    if(ContadorClase2>ContadorClase0):#Si ContadorClase2 es mayor que todas las demas
        if(ContadorClase2>ContadorClase1):
            if(ContadorClase2>ContadorClase3): 
                if(ContadorClase2>ContadorClase4):
                    if(ContadorClase2>ContadorClase5):
                        if(ContadorClase2>ContadorClase6):
                            if(ContadorClase2>ContadorClase7):
                                if(ContadorClase2>ContadorClase8):
                                    if(ContadorClase2>ContadorClase9):
                                        print('La Imagen es un 2');#Entonces la imagen nueva pertenece a esta clase
      
    if(ContadorClase3>ContadorClase0):#Si ContadorClase3 es mayor que todas las demas
        if(ContadorClase3>ContadorClase1):
            if(ContadorClase3>ContadorClase2):
                if(ContadorClase3>ContadorClase4):
                    if (ContadorClase3>ContadorClase5):
                        if(ContadorClase3>ContadorClase6):
                            if(ContadorClase3>ContadorClase7):
                                if(ContadorClase3>ContadorClase8):
                                    if(ContadorClase3>ContadorClase9):
                                        print('La Imagen es un 3');#Entonces la imagen nueva pertenece a esta clase
    
    if(ContadorClase4>ContadorClase1):#Si ContadorClase4 es mayor que todas las demas
        if(ContadorClase4>ContadorClase2):
            if(ContadorClase4>ContadorClase3):
                if(ContadorClase4>ContadorClase0):
                    if(ContadorClase4>ContadorClase5):
                        if(ContadorClase4>ContadorClase6):
                            if(ContadorClase4>ContadorClase7):
                                if(ContadorClase4>ContadorClase8):
                                    if(ContadorClase4>ContadorClase9):
                                        print('La Imagen es un 4');#Entonces la imagen nueva pertenece a esta clase
    
    if(ContadorClase5>ContadorClase1):#Si ContadorClase5 es mayor que todas las demas
        if(ContadorClase5>ContadorClase2):
            if(ContadorClase5>ContadorClase3):
                if(ContadorClase5>ContadorClase4):
                    if (ContadorClase5>ContadorClase0):
                        if (ContadorClase5>ContadorClase6):
                            if (ContadorClase5>ContadorClase7):
                                if (ContadorClase5>ContadorClase8):
                                    if (ContadorClase5>ContadorClase9):
                                        print('La Imagen es un 5');#Entonces la imagen nueva pertenece a esta clase
    
    if(ContadorClase6>ContadorClase1):#Si ContadorClase6 es mayor que todas las demas
        if(ContadorClase6>ContadorClase2):
            if(ContadorClase6>ContadorClase3):
                if(ContadorClase6>ContadorClase4):
                    if(ContadorClase6>ContadorClase5):
                        if(ContadorClase6>ContadorClase0):
                            if(ContadorClase6>ContadorClase7):
                                if(ContadorClase6>ContadorClase8):
                                    if(ContadorClase6>ContadorClase9):
                                        print('La Imagen es un 6');#Entonces la imagen nueva pertenece a esta clase
    
    if(ContadorClase7>ContadorClase1):#Si ContadorClase7 es mayor que todas las demas
        if(ContadorClase7>ContadorClase2):
            if(ContadorClase7>ContadorClase3):
                if(ContadorClase7>ContadorClase4):
                    if(ContadorClase7>ContadorClase5):
                        if(ContadorClase7>ContadorClase6):
                            if(ContadorClase7>ContadorClase0):
                                if(ContadorClase7>ContadorClase8):
                                    if(ContadorClase7>ContadorClase9):
                                        print('La Imagen es un 7');#Entonces la imagen nueva pertenece a esta clase
    
    if(ContadorClase8>ContadorClase1):#Si ContadorClase8 es mayor que todas las demas
        if(ContadorClase8>ContadorClase2):
            if(ContadorClase8>ContadorClase3):
                if(ContadorClase8>ContadorClase4):
                    if(ContadorClase8>ContadorClase5):
                        if(ContadorClase8>ContadorClase6):
                            if(ContadorClase8>ContadorClase7):
                                if(ContadorClase8>ContadorClase0):
                                    if(ContadorClase8>ContadorClase9):
                                        print('La Imagen es un 8');#Entonces la imagen nueva pertenece a esta clase
    
    if(ContadorClase9>ContadorClase0):#Si ContadorClase9 es mayor que todas las demas
        if(ContadorClase9>ContadorClase1):
                if(ContadorClase9>ContadorClase2):
                    if(ContadorClase9>ContadorClase3):
                        if(ContadorClase9>ContadorClase4):
                            if(ContadorClase9>ContadorClase5):
                                if(ContadorClase9>ContadorClase6):
                                    if(ContadorClase9>ContadorClase7):
                                        if(ContadorClase9>ContadorClase8):
                                            print('La Imagen es un 9');#Entonces la imagen nueva pertenece a esta clase
                                            

Razon=FilasEntreColumnas(tam)#Primera caracteristica Filas entre Columnas
area=Area(tam,mat)#Segunda caracteristica El Ârea de la Imagen
FCorteC=FilasDeCorteUnCuarto(tam,mat)#Tercer caracteristica
FCorteM=FilasCorteEnMedio(tam,mat)#Cuarta caracteristica
FCorteTC=FilasDeCorteTresCuartos(tam,mat)#Quinta Caracteristica
CCortesC=ColumnasCortesAUnCuarto(tam,mat)#Sexta Caracteristica
CCortesM=ColumnasCorteEnMedio(tam,mat)#Septima Caracteristica
CCortesTC=ColumnasCortesATresCuartos(tam,mat)#Octava Caracteristica
AFilasC=AreaDeFilasAUnCuarto(tam,mat)#Novena Caracteristica
AFilasM=AreaDeFilasEnMedio(tam,mat)#Decima Caracteristica
AFilasTC=AreaDeFilasTresCuartos(tam,mat)#DecimaPrimera Caracteristica
AColumnasC=AreadeColumnasAUnCuarto(tam,mat)#DecimaSegunda Caracteristica
AColumnasM=AreaDeColumnasEnMedio(tam,mat)#DecimaTercera Caracteristiva
AColumnasTC=AreaDeColumnasTresCuartos(tam,mat)#DecimaCuarta Caracteristica
#Mandamos los valores de cada caracteristica a la función knn
knn(Razon,area,FCorteC,FCorteM,FCorteTC,CCortesC,CCortesM,CCortesTC,AFilasC,AFilasM,AFilasTC,AColumnasC,AColumnasM,AColumnasTC)#
