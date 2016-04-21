# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:45:11 2016

@author(s): 
Luis Alberto Muñoz Cruz
Rafael Martinez Rocha
"""
#libreria de imagenes en python
from PIL import Image
#Libreria para generar la matriz de la imagen
import matplotlib.image as mpimg
#Libreria para lectura de directorios
import os
#Libreria para la manipulacion de arhcivos csv
import csv

#Nombre:RazonFilasColumnas
#Desc:Metodo para obtener la razon de filas/columnas
#Argumentos:numfilas,numcolumnas
#Regresa: la razon de las filas respecto a las columnas
def RazonFilasColumnas(numfilas,numcolumnas):
    #Operacion para obtener la razon de filas respecto a las columnas
    razonfilascolumnas = numfilas/numcolumnas
    #regresa: la razon de las filas respecto a las columnas
    return razonfilascolumnas

#Nombre:AreaBlancosNegros
#Desc:Metodo para obtener el area de la letra respecto al tamaño total de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: la razon del area de la letra respecto al tamaño de la imagen
def AreaBlancosNegros(imagenmatriz,numfilas,numcolumnas):
    #Lleva el conteo de los ceros
    contadorceros = 0
    #Lleva el conteo de los ceros    
    contadorunos = 0
    #Creacion de un arreglo que contenga la razon de los 1s y los 0s
    razonesarea = []
    #For recorre las filas de la matriz
    for x in range(numfilas):
        #for recorre las columnas de la matriz
        for y in range(numcolumnas):
            #Se realiza una comparacion para encontrar 0s
            if(imagenmatriz[x][y]==0):
                #Si hay un cero se aumenta en uno la variable contadorceros
                contadorceros = contadorceros + 1
            else:
                #Si hay un uno se aumenta en uno la variable contadorunos               
                contadorunos = contadorunos + 1
    #Se realiza la operacion para encontrar la razon del numero de ceros respecto al area total             
    razonunos = contadorceros/(numfilas*numcolumnas)
    #Se realiza la operacion para encontrar la razon del numero de unos respecto al area total
    razonceros = contadorunos/(numfilas*numcolumnas)
    #Utilizamos el arreglo razonesarea para guardar los dos resultados    
    razonesarea = [razonunos,razonceros]
    #Regresa: la razon del area de la letra respecto al tamaño de la imagen
    return razonesarea

#Nombre:AreaMitadSuperiorBlancosNegros
#Desc:Metodo para obtener el area de la letra respecto al tamaño total de la imagen usando solo la mitad superior de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: la razon de los 1s y 0s de la parte superior de la imagen respecto al tamaño original
def AreaMitadSuperiorBlancosNegros(imagenmatriz,numfilas,numcolumnas):
    #Lleva el conteo de los ceros
    contadorceros = 0
    #Lleva el conteo de los unos    
    contadorunos = 0
    #Creacion de un arreglo que contenga la razon de los 1s y los 0s
    razonesareamitad = []
    #Opereación para hallar la mitad del numero de filas
    mitadfilas = int(numfilas/2)
    #for que recorrre la matriz hasta la mitad de las filas
    for x in range(mitadfilas):
        #for que recorre la matriz por todas sus columnas
        for y in range(numcolumnas):
            #Se realiza una condicion para hallar los 1s y los 0s
            if(imagenmatriz[x][y]==0):
                #Si hay un cero se aumenta en uno la variable contadorceros
                contadorceros = contadorceros + 1
            else:
                #Si hay un cero se aumenta en uno la variable contadorunos
                contadorunos = contadorunos + 1
    #Se realiza la operacion para encontrar la razon del numero de unos de la parte superior de la imagen respecto al area total
    razonunos = contadorunos/(mitadfilas*numcolumnas)
    #Se realiza la operacion para encontrar la razon del numero de ceros de la parte superior de la imagen respecto al area total
    razonceros = contadorceros/(mitadfilas*numcolumnas)
    #Utilizamos el arreglo razonesarea para guardar los dos resultados    
    razonesareamitad = [razonunos,razonceros]
    #Regresa: la razon de los 1s y 0s de la parte superior de la imagen respecto al tamaño original
    return razonesareamitad
    
#Nombre:AreaCuartoSuperiorBlancosNegros
#Desc:Metodo para obtenerla razón del area de la letra respecto al tamaño total de la imagen usando solo la cuarta parte superior de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: la razon de los 1s y 0s de la parte superior de la imagen respecto al tamaño original
def AreaCuartoSuperiorBlancosNegros(imagenmatriz,numfilas,numcolumnas):
    #Lleva el conteo de los ceros
    contadorceros = 0
    #Lleva el conteo de los unos    
    contadorunos = 0
    #Creacion de un arreglo que contenga la razon de los 1s y los 0s
    razonesareacuarto = []
    #Opereación para hallar la mitad del numero de filas
    cuartofilas = int(numfilas/4)
    #for que recorrre la matriz hasta la mitad de las filas
    for x in range(cuartofilas):
        #for que recorre la matriz por todas sus columnas
        for y in range(numcolumnas):
            #Se realiza una condicion para hallar los 1s y los 0s
            if(imagenmatriz[x][y]==0):
                #Si hay un cero se aumenta en uno la variable contadorceros
                contadorceros = contadorceros + 1
            else:
                #Si hay un cero se aumenta en uno la variable contadorunos
                contadorunos = contadorunos + 1
    #Se realiza la operacion para encontrar la razon del numero de unos de la parte superior de la imagen respecto al area total
    razonunos = contadorunos/(cuartofilas*numcolumnas)
    #Se realiza la operacion para encontrar la razon del numero de ceros de la parte superior de la imagen respecto al area total
    razonceros = contadorceros/(cuartofilas*numcolumnas)
    #Utilizamos el arreglo razonesarea para guardar los dos resultados    
    razonesareacuarto = [razonunos,razonceros]
    #Regresa: la razon de los 1s y 0s de la parte superior de la imagen respecto al tamaño original
    return razonesareacuarto
    
#Nombre:AreaTresCuartoSuperiorBlancosNegros
#Desc:Metodo para obtenerla razón del area de la letra respecto al tamaño total de la imagen usando solo las tres cuarta partes superior de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: la razon de los 1s y 0s de la parte superior de la imagen respecto al tamaño original
def AreaTresCuartoSuperiorBlancosNegros(imagenmatriz,numfilas,numcolumnas):
    #Lleva el conteo de los ceros
    contadorceros = 0
    #Lleva el conteo de los unos    
    contadorunos = 0
    #Creacion de un arreglo que contenga la razon de los 1s y los 0s
    razonesareatrescuarto = []
    #Opereación para hallar la mitad del numero de filas
    trescuartofilas = int((numfilas/4)*3)
    #for que recorrre la matriz hasta la mitad de las filas
    for x in range(trescuartofilas):
        #for que recorre la matriz por todas sus columnas
        for y in range(numcolumnas):
            #Se realiza una condicion para hallar los 1s y los 0s
            if(imagenmatriz[x][y]==0):
                #Si hay un cero se aumenta en uno la variable contadorceros
                contadorceros = contadorceros + 1
            else:
                #Si hay un cero se aumenta en uno la variable contadorunos
                contadorunos = contadorunos + 1
    #Se realiza la operacion para encontrar la razon del numero de unos de la parte superior de la imagen respecto al area total
    razonunos = contadorunos/(trescuartofilas*numcolumnas)
    #Se realiza la operacion para encontrar la razon del numero de ceros de la parte superior de la imagen respecto al area total
    razonceros = contadorceros/(trescuartofilas*numcolumnas)
    #Utilizamos el arreglo razonesarea para guardar los dos resultados    
    razonesareatrescuarto = [razonunos,razonceros]
    #Regresa: la razon de los 1s y 0s de la parte superior de la imagen respecto al tamaño original
    return razonesareatrescuarto
   
#Nombre:RazonMitadVertical
#Desc:Metodo que obtiene la razon del area de unos de la columna central vertical de la imagen, con respecto al area total de la misma columna
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: Razon del area de blancos de la  columna con respecto a su area total  
def RazonMitadVertical(imagenmatriz,numfilas,numcolumnas):
    #Contador de unos dentro de la columna    
    contadorunos = 0
    #Se realiza una operacion para obtener el numero que es igual a la mitad del total de columnas de la imagen
    mitadcolumnas = int(numcolumnas/2)
    #for recorre las filas de la matriz
    for x in range(numfilas):
        #Cuando la posicion de la imagen sea igual a 1 se realizan las operaciones
        if(imagenmatriz[x][mitadcolumnas]==1):
            #Aumento de contador si se cumple la condicion
            contadorunos += 1
    #Razon de area de unos con respecto al area total
    razon = contadorunos/numfilas
    #Regresa: la razon calculada    
    return razon

#Nombre:RazonMitadHorizontal
#Desc:Metodo que obtiene la razon del area de unos de la fila central horizontal de la imagen, con respecto al area total de la misma fila
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: Razon del area de blancos de la  fila con respecto a su area total
def RazonMitadHorizontal(imagenmatriz,numfilas,numcolumnas):
    #Contador de unos dentro de la fila    
    contadorunos = 0
    #Se realiza una operacion para obtener el numero que es igual a la mitad del total de filas de la imagen
    mitadfilas = int(numfilas/2)
    #for recorre las columnas de la matriz
    for x in range(numcolumnas):
        #Cuando la posicion de la imagen sea igual a 1 se realizan las operaciones
        if(imagenmatriz[mitadfilas][x]==1):
            #Aumento de contador si se cumple la condicion
            contadorunos += 1
    #Razon de area de unos con respecto al area total
    razon = contadorunos/numcolumnas
    #Regresa: la razon calculada    
    return razon

#Nombre:RazonCuartoVertical
#Desc:Metodo que obtiene la razon del area de unos de la columna que corresponde a la cuarta parte vertical de la imagen, con respecto al area total de la misma columna
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: Razon del area de blancos de la  columna con respecto a su area total   
def RazonCuartoVertical(imagenmatriz,numfilas,numcolumnas):
    #Contador de unos dentro de la columna  
    contadorunos = 0
    #Se realiza una operacion para obtener el numero que es igual a la cuarta parte del total de columnas de la imagen
    cuartocolumnas = int(numcolumnas/4)
    #for recorre las filas de la matriz
    for x in range(numfilas):
        #Cuando la posicion de la imagen sea igual a 1 se realizan las operaciones
        if(imagenmatriz[x][cuartocolumnas]==1):
            #Aumento de contador si se cumple la condicion            
            contadorunos += 1
    #Razon de area de unos con respecto al area total
    razon = contadorunos/numfilas
    #Regresa: la razon calculada     
    return razon

#Nombre:RazonCuartoHorizontal
#Desc:Metodo que obtiene la razon del area de unos de la fila que corresponde a la cuarta parte horizontal de la imagen, con respecto al area total de la misma fila
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: Razon del area de blancos de la  fila con respecto a su area total   
def RazonCuartoHorizontal(imagenmatriz,numfilas,numcolumnas):
    #Contador de unos dentro de la fila    
    contadorunos = 0
    #Se realiza una operacion para obtener el numero que es igual a la cuarta parte del total de filas de la imagen
    cuartofilas = int(numfilas/4)
    #for recorre las filas de la matriz
    for x in range(numcolumnas):
        #Cuando la posicion de la imagen sea igual a 1 se realizan las operaciones
        if(imagenmatriz[cuartofilas][x]==1):
            #Aumento de contador si se cumple la condicion 
            contadorunos += 1
    #Razon de area de unos con respecto al area total
    razon = contadorunos/numcolumnas
    #Regresa: la razon calculada    
    return razon
   

#Nombre:RazonTresCuartoVertical
#Desc:Metodo que obtiene la razon del area de unos de la columna que corresponde a las tres cuartas partes vertical de la imagen, con respecto al area total de la misma columna
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: Razon del area de blancos de la  columna con respecto a su area total   
def RazonTresCuartoVertical(imagenmatriz,numfilas,numcolumnas):
    #Contador de unos dentro de la columna     
    contadorunos = 0
    #Se realiza una operacion para obtener el numero que es igual a las tres cuartas partes del total de columnas de la imagen
    trescuartocolumnas = int((numcolumnas/4)*3)
    #for recorre las filas de la matriz
    for x in range(numfilas):
        #Cuando la posicion de la imagen sea igual a 1 se realizan las operaciones
        if(imagenmatriz[x][trescuartocolumnas]==1):
            #Aumento de contador si se cumple la condicion 
            contadorunos += 1
    #Razon de area de unos con respecto al area total
    razon = contadorunos/numfilas
    #Regresa: la razon calculada    
    return razon

#Nombre:RazonTresCuartoHorizontal
#Desc:Metodo que obtiene la razon del area de unos de la fila que corresponde a las tres cuartas partes horizontal de la imagen, con respecto al area total de la misma fila
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: Razon del area de blancos de la  fila con respecto a su area total   
def RazonTresCuartoHorizontal(imagenmatriz,numfilas,numcolumnas):
    #Contador de unos dentro de la fila   
    contadorunos = 0
    #Se realiza una operacion para obtener el numero que es igual a las tres cuartas partes del total de filas de la imagen
    trescuartofilas = int((numfilas/4)*3)
    #for recorre las filas de la matriz
    for x in range(numcolumnas):
         #Cuando la posicion de la imagen sea igual a 1 se realizan las operaciones
        if(imagenmatriz[trescuartofilas][x]==1):
            #Aumento de contador si se cumple la condicion
            contadorunos += 1
    #Razon de area de unos con respecto al area total
    razon = contadorunos/numcolumnas
    #Regresa: la razon calculada   
    return razon
   
#Nombre:CortesMitadVertical
#Desc:Metodo que obtiene el numero de veces que toca una linea vertical al caracter dentro de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: el numero de cortes encontrados    
def CortesMitadVertical(imagenmatriz,numfilas,numcolumnas):
    #Guarda la posicion actual    
    apuntadoractual = 0
    #Guarda una posicion adelante de apuntadoractual 
    apuntadordelantero = 0
    #Lleva el conteo de los cortes hechos por la linea
    cortes = 0
    #Contador utilizado para la evaluacion de la fila 1 de la imagen
    filauno = 0
    #Se realiza una operacion para obtener el numero que es igual a la mitad del total de columnas de la imagen
    mitadcolumnas = int(numcolumnas/2)
    #for recorre las filas de la matriz
    for x in range(numfilas):
        #Igualamos apuntador actual a la fila actual del arreglo y justo a la mitad de columnas
        apuntadoractual = imagenmatriz[x][mitadcolumnas]
        #Evalua que el for no sobrepase el tamaño de la imagen para el apuntadordelantero
        if(x<numfilas-1):
            #Igualamos apuntadordelantero una fila adelante de la fila actual del arreglo y justo a la mitad de columnas
            apuntadordelantero = imagenmatriz[x+1][mitadcolumnas]
            #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (filauno==0 and imagenmatriz[0][mitadcolumnas]==1)):
                #Al cumplirse la condicion la variable cortes aumenta mas 1 su valor
                cortes = cortes + 1
                #Al cumplirse la condicion la variable filauno aumenta mas 1 su valor                
                filauno = filauno + 1
    #Regresa: el numero de cortes encontrados    
    return cortes
    

#Nombre:CortesMitadVertical
#Desc:Metodo que obtiene el numero de veces que toca una linea horizontal al  caracter dentro de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: el numero de cortes encontrados
def CortesMitadHorizontal(imagenmatriz,numfilas,numcolumnas):
    #Guarda la posicion actual        
    apuntadoractual = 0
    #Guarda una posicion adelante de apuntadoractual 
    apuntadordelantero = 0
    #Lleva el conteo de los cortes hechos por la linea
    cortes = 0
    #Contador utilizado para la evaluacion de la columna 1 de la imagen
    columnauno = 0
    #Se realiza una operacion para obtener el numero que es igual a la mitad del total de filas de la imagen
    mitadfilas = int(numfilas/2)
    #for recorre las columnas de la matriz
    for x in range(numcolumnas):
        #Igualamos apuntador actual a la fila actual del arreglo y justo a la mitad de columnas
        apuntadoractual = imagenmatriz[mitadfilas][x]
        #Evalua que el for no sobrepase el tamaño de la imagen para el apuntadordelantero
        if(x<numcolumnas-1):
            #Igualamos apuntadordelantero una fila adelante de la fila actual del arreglo y justo a la mitad de columnas            
            apuntadordelantero = imagenmatriz[mitadfilas][x+1]
            #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (columnauno==0 and imagenmatriz[mitadfilas][0]==1)):
                #Al cumplirse la condicion la variable cortes aumenta mas 1 su valor                
                cortes = cortes + 1
                #Al cumplirse la condicion la variable filauno aumenta mas 1 su valor
                columnauno = columnauno + 1
    #Regresa: el numero de cortes encontrados        
    return cortes

#Nombre:CortesCuartoVertical
#Desc:Metodo que obtiene el numero de veces que toca una linea vertical en la 
# cuarta parte del numero de columnas al caracter dentro de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: el numero de cortes encontrados
def CortesCuartoVertical(imagenmatriz,numfilas,numcolumnas):
    #Guarda la posicion actual            
    apuntadoractual = 0
    #Guarda una posicion adelante de apuntadoractual 
    apuntadordelantero = 0
    #Lleva el conteo de los cortes hechos por la linea    
    cortes = 0
    #Contador utilizado para la evaluacion de la fila 1 de la imagen    
    filauno = 0
    #Se realiza una operacion para obtener el numero que es igual a la cuarta parte del total de filas de la imagen    
    cuartocolumnas = int(numcolumnas/4)
    #for recorre las filas de la matriz    
    for x in range(numfilas):
        #Igualamos apuntador actual a la fila actual del arreglo y justo a un cuarto de columnas
        apuntadoractual = imagenmatriz[x][cuartocolumnas]
        #Evalua que el for no sobrepase el tamaño de la imagen para el apuntadordelantero
        if(x<numfilas-1):
            #Igualamos apuntadordelantero una fila adelante de la fila actual del arreglo y justo a la mitad de columnas            
            apuntadordelantero = imagenmatriz[x+1][cuartocolumnas]
            #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (filauno==0 and imagenmatriz[0][cuartocolumnas]==1)):
                #Al cumplirse la condicion la variable cortes aumenta mas 1 su valor                
                cortes = cortes + 1
                #Al cumplirse la condicion la variable filauno aumenta mas 1 su valor
                filauno = filauno + 1
    #Regresa: el numero de cortes encontrados        
    return cortes
            
#Nombre:CortesCuartoHorizontal
#Desc:Metodo que obtiene el numero de veces que toca una linea horizontal en la 
# cuarta parte del numero de columnas al caracter dentro de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: el numero de cortes encontrados            
def CortesCuartoHorizontal(imagenmatriz,numfilas,numcolumnas):
    #Guarda la posicion actual                
    apuntadoractual = 0
    #Guarda una posicion adelante de apuntadoractual 
    apuntadordelantero = 0
    #Lleva el conteo de los cortes hechos por la linea    
    cortes = 0
    #Contador utilizado para la evaluacion de la columna 1 de la imagen    
    columnauno = 0
    #Se realiza una operacion para obtener el numero que es igual a la cuarta parte del total de filas de la imagen   
    cuartofilas = int(numfilas/4)
    #for recorre las columnas de la matriz        
    for x in range(numcolumnas):
        #Igualamos apuntador actual a la fila actual del arreglo y justo a un cuarto de columnas
        apuntadoractual = imagenmatriz[cuartofilas][x]
        #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes
        if(x<numcolumnas-1):
            #Igualamos apuntadordelantero una fila adelante de la fila actual del arreglo y justo a la mitad de columnas            
            apuntadordelantero = imagenmatriz[cuartofilas][x+1]
            #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes            
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (columnauno==0 and imagenmatriz[cuartofilas][0]==1)):
                #Al cumplirse la condicion la variable cortes aumenta mas 1 su valor                               
                cortes = cortes + 1
                #Al cumplirse la condicion la variable filauno aumenta mas 1 su valor
                columnauno = columnauno + 1
    #Regresa: el numero de cortes encontrados        
    return cortes
            
#Nombre:CortesTresCuartosVertical
#Desc:Metodo que obtiene el numero de veces que toca una linea vertical en la 
# tercer cuarta parte del numero de columnas al caracter dentro de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: el numero de cortes encontrados    
def CortesTresCuartosVertical(imagenmatriz,numfilas,numcolumnas):
    #Guarda la posicion actual                
    apuntadoractual = 0
    #Guarda una posicion adelante de apuntadoractual 
    apuntadordelantero = 0
    #Lleva el conteo de los cortes hechos por la linea    
    cortes = 0
    #Contador utilizado para la evaluacion de la fila 1 de la imagen    
    filauno = 0
    #Se realiza una operacion para obtener el numero que es igual a la tercer cuarta parte del total de columnas de la imagen  
    cuartocolumnas = int((numcolumnas/4)*3)
    #for recorre las filas de la matriz        
    for x in range(numfilas):
        #Igualamos apuntador actual a la fila actual del arreglo y justo al tercer cuarto de columnas
        apuntadoractual = imagenmatriz[x][cuartocolumnas]
        #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes
        if(x<numfilas-1):
            #Igualamos apuntadordelantero una fila adelante de la fila actual del arreglo y justo a la mitad de columnas                        
            apuntadordelantero = imagenmatriz[x+1][cuartocolumnas]
            #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes            
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (filauno==0 and imagenmatriz[0][cuartocolumnas]==1)):
                #Al cumplirse la condicion la variable cortes aumenta mas 1 su valor                                               
                cortes = cortes + 1
                #Al cumplirse la condicion la variable filauno aumenta mas 1 su valor
                filauno = filauno + 1
    #Regresa: el numero de cortes encontrados    
    return cortes
            
#Nombre:CortesTresCuartosHorizontal
#Desc:Metodo que obtiene el numero de veces que toca una linea horizontal en la 
# tercer cuarta parte del numero de columnas al caracter dentro de la imagen
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: el numero de cortes encontrados               
def CortesTresCuartosHorizontal(imagenmatriz,numfilas,numcolumnas):
    #Guarda la posicion actual                    
    apuntadoractual = 0
    #Guarda una posicion adelante de apuntadoractual 
    apuntadordelantero = 0
    #Lleva el conteo de los cortes hechos por la linea    
    cortes = 0
    #Contador utilizado para la evaluacion de la columna 1 de la imagen    
    columnauno = 0
    #Se realiza una operacion para obtener el numero que es igual a la tercer cuarta parte del total de columnas de la imagen  
    cuartofilas = int((numfilas/4)*3)
    #for recorre las columnas de la matriz            
    for x in range(numcolumnas):
        #Igualamos apuntador actual a la fila actual del arreglo y justo al tercer cuarto de columnas
        apuntadoractual = imagenmatriz[cuartofilas][x]
        #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes
        if(x<numcolumnas-1):
            #Igualamos apuntadordelantero una fila adelante de la fila actual del arreglo y justo a la mitad de columnas                        
            apuntadordelantero = imagenmatriz[cuartofilas][x+1]
            #Evalua si hay un cambio en los apuntadores y si es asi suma el cambio al contador de cortes            
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (columnauno==0 and imagenmatriz[cuartofilas][0]==1)):
                #Al cumplirse la condicion la variable cortes aumenta mas 1 su valor                                                               
                cortes = cortes + 1
                #Al cumplirse la condicion la variable filauno aumenta mas 1 su valor
                columnauno = columnauno + 1
    #Regresa: el numero de cortes encontrados    
    return cortes

#Nombre:CruzBlancosNegros
#Desc:Metodo que obtiene la razon del area de blancos respecto a la suma del área de una linea vertical y una horizontal 
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: razonescruz               
def CruzBlancosNegros(imagenmatriz,numfilas,numcolumnas):   
    #Lleva el conteo de ceros en la linea vertical que se esta evaluando    
    contadorcerosvertical = 0
    #Lleva el conteo de unos en la linea horizontal que se esta evaluando    
    contadorunosvertical = 0
    #Lleva el conteo de ceros en la linea vertical que se esta evaluando    
    contadorceroshorizontal = 0
    #Lleva el conteo de unos en la linea horizontal que se esta evaluando    
    contadorunoshorizontal = 0
    #Creacion de un arreglo que contenga la razon resultante
    razonescruz = []
    #Operación que encuentra el numero medio de filas en la imagen
    mitadfilas = int(numfilas/2)
    #Operación que encuentra el numero medio de columnas en la imagen
    mitadcolumnas = int(numcolumnas/2)
    #for recorre las filas de la matriz    
    for x in range(numfilas):
        #Busqueda de 0 en la columna vertical
        if(imagenmatriz[x][mitadcolumnas]==0):
            #Si se encuentra algun cero se aumenta uno el valor de contadorcerosvertical
            contadorcerosvertical = contadorcerosvertical + 1
        else:
            #Si se encuentra algun uno se aumenta uno el valor de contadorunosvertical
            contadorunosvertical = contadorunosvertical + 1
    #for recorre las columnas de la matriz        
    for y in range(numcolumnas):
        #Busqueda de 0 en la columna vertical
        if(imagenmatriz[mitadfilas][y]==0):
            #Si se encuentra algun cero se aumenta uno el valor de contadorceroshorizontal
            contadorceroshorizontal = contadorceroshorizontal + 1
        else:
            #Si se encuentra algun uno se aumenta uno el valor de contadorunosvertical
            contadorunoshorizontal = contadorunoshorizontal + 1
    #Se calcula la razon de pixeles blancos respecto al tamaño total de la imagen
    razonblancos = (contadorcerosvertical + contadorceroshorizontal)/(numcolumnas+numfilas)  
    #Se calcula la razon de pixeles negros respecto al tamaño total de la imagen
    razonnegros = (contadorunosvertical + contadorunoshorizontal)/(numcolumnas+numfilas)
    #Se alamcenan ambas razones en el arreglo llamado razones cruz
    razonescruz = [razonblancos,razonnegros]
    #Regresa: razonescruz              
    return razonescruz        

#Nombre:DiferenciaMitadArea
#Desc:Metodo que verifica la simetria del area de blancos del doble de la mitad izquierda 
#con respecto al area total de blancos de la imagen 
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: razon de la simetria              
def DiferenciaMitadArea(imagenmatriz,numfilas,numcolumnas):
    #Lleva el conteo de ceros en la mitad de la imagen
    contadorcerosmitad = 0
    #Lleva el conteo de unos en la mitad de la imagen
    contadorunosmitad = 0
    #Se calcula el numero medio de columnas de la imagen
    mitadcolumnas = int(numcolumnas/2)
    #Lleva el conteo de ceros 
    contadorceros = 0
    #lleva el conteo de unos
    contadorunos = 0
    #for recorre las filas de la matriz            
    for x in range(numfilas):
        #for recorre las columnas de la matriz    
        for y in range(mitadcolumnas,numcolumnas):
            #Busqueda de 0 en la imagen
            if(imagenmatriz[x][y]==0):
                #Si se encuentra algun cero se aumenta uno el valor de contadorceros
                contadorceros = contadorceros + 1
            else:
                #Si se encuentra algun cero se aumenta uno el valor de contadorunos                
                contadorunos = contadorunos + 1
    #for recorre las filas de la matriz            
    for x in range(numfilas):
        #for recorre la mitad de columnas de la matriz   
        for y in range(mitadcolumnas):
            #Busqueda de 0 en la imagen
            if(imagenmatriz[x][y]==0):
                #Si se encuentra algun cero se aumenta uno el valor de contadorcerosmitad
                contadorcerosmitad = contadorcerosmitad + 1
            else:
                 #Si se encuentra algun cero se aumenta uno el valor de contadorcerosmitad
                contadorunosmitad = contadorunosmitad + 1
    #Simetria del doble de unos de la parte izquierda con respecto al area total de blancos de laimagen
    diferenciaunos = (contadorunosmitad*2)/contadorunos
    #regresa el resultado de la operación previmamente hecha
    return diferenciaunos
    
#Nombre:DiferenciaMitadAreaHorizontal
#Desc:Metodo que verifica la simetria del area de blancos del doble de la mitad superior 
#con respecto al area total de blancos de la imagen 
#Argumentos:imagenmatriz,numfilas,numcolumnas
#Regresa: razon de la simetria              
def DiferenciaMitadAreaHorizontal(imagenmatriz,numfilas,numcolumnas):
    #Lleva el conteo de ceros en la mitad de la imagen
    contadorcerosmitad = 0
    #Lleva el conteo de unos en la mitad de la imagen
    contadorunosmitad = 0
    #Se calcula el numero medio de columnas de la imagen
    mitadfilas = int(numfilas/2)
    #Lleva el conteo de ceros 
    contadorceros = 0
    #lleva el conteo de unos
    contadorunos = 0
    #for recorre las filas de la matriz            
    for x in range(mitadfilas,numfilas):
        #for recorre las columnas de la matriz    
        for y in range(numcolumnas):
            #Busqueda de 0 en la imagen
            if(imagenmatriz[x][y]==0):
                #Si se encuentra algun cero se aumenta uno el valor de contadorceros
                contadorceros = contadorceros + 1
            else:
                #Si se encuentra algun cero se aumenta uno el valor de contadorunos                
                contadorunos = contadorunos + 1
    #for recorre las filas de la matriz            
    for x in range(mitadfilas):
        #for recorre la mitad de columnas de la matriz   
        for y in range(numcolumnas):
            #Busqueda de 0 en la imagen
            if(imagenmatriz[x][y]==0):
                #Si se encuentra algun cero se aumenta uno el valor de contadorcerosmitad
                contadorcerosmitad = contadorcerosmitad + 1
            else:
                 #Si se encuentra algun cero se aumenta uno el valor de contadorcerosmitad
                contadorunosmitad = contadorunosmitad + 1
    #Simetria del doble de unos de la parte superior con respecto al area total de blancos de laimagen
    diferenciaunos = (contadorunosmitad*2)/contadorunos
    #regresa el resultado de la operación previmamente hecha
    return diferenciaunos
    
#Nombre:LeerImagen
#Desc:Metodo para procesar la lectura de la imagen 
#Argumentos:ruta
#Regresa: parametrosimagen
def LeerImagen(ruta):
    #Se crea un arreglo para contener los parametros necesarios para el uso de la imagen    
    parametrosimagen = []
    #imagenjpg almacena la ruta de la imagen seleccionada
    imagenjpg = Image.open(ruta)
    #imagenmatriz hace que la imagen pueda ser usada como una matriz
    imagenmatriz = mpimg.imread(ruta)
    #con imagenjpg.size se obtienen las dimensiones de la imagen en este caso numcolumnas y numfilas    
    numcolumnas, numfilas = imagenjpg.size
    #En paramentrosimagen se almacena imagenmatriz,numfilas,numcolumna    
    parametrosimagen = [imagenmatriz,numfilas,numcolumnas]
    #Regresa los paramentrosimagen obtenidos previamente
    return parametrosimagen
    
#Nombre: main
#Desc:Metodo principal de funcionamiento  
def main():
    #Se crea un arreglo que almacene las caracteristicas de un numero en una fila del archivo csv
    datasetfila = []
    #Directorio principal
    rootDir= './dataset/'
    #Se crea un nuevo archivo .csv con privilegios de escritura y delimitado por comas 
    f = open('data.csv','w',newline='')
    #documento usa  la funcion csv.writer para escribir el archivo .csv delimitado por comas     
    documento = csv.writer(f,delimiter=',')
    #Ciclo que recorrera los directorios y subdirectorios para obtener cada una de las imagenes a procesar    
    for dirName, subdirList, fileList in os.walk(rootDir):
        #Impresion de mensaje que nos dice que clase se esta procesando actualmente
        print('Procesando clase: %s' % dirName)
        #Recorre la lista de ficheros localizados        
        for fname in fileList:
            #Ruta de cada fichero
            ruta = dirName + '/' + fname
            #Clase procesada
            clase = dirName[10]
            #Funciones para obtener caracteristcas
            #Nota: el nombre de las variables son las inicales de las funciones
            li = LeerImagen(ruta)
            rfc = RazonFilasColumnas(li[1],li[2])
            abc = AreaBlancosNegros(li[0],li[1],li[2])
            amsbn = AreaMitadSuperiorBlancosNegros(li[0],li[1],li[2])
            acsbn = AreaCuartoSuperiorBlancosNegros(li[0],li[1],li[2])
            atcsbn = AreaTresCuartoSuperiorBlancosNegros(li[0],li[1],li[2])
            rmh = RazonMitadHorizontal(li[0],li[1],li[2])
            rmv = RazonMitadVertical(li[0],li[1],li[2])
            rch = RazonCuartoHorizontal(li[0],li[1],li[2])
            rcv = RazonCuartoVertical(li[0],li[1],li[2])
            rtch = RazonTresCuartoHorizontal(li[0],li[1],li[2])
            rtcv = RazonTresCuartoVertical(li[0],li[1],li[2])
            cmv = CortesMitadVertical(li[0],li[1],li[2])
            cmh = CortesMitadHorizontal(li[0],li[1],li[2])
            ccv = CortesCuartoVertical(li[0],li[1],li[2])
            cch = CortesCuartoHorizontal(li[0],li[1],li[2])
            ctcv = CortesTresCuartosVertical(li[0],li[1],li[2])
            ctch = CortesTresCuartosHorizontal(li[0],li[1],li[2])
            cbn = CruzBlancosNegros(li[0],li[1],li[2])
            dma = DiferenciaMitadArea(li[0],li[1],li[2])
            dmah = DiferenciaMitadAreaHorizontal(li[0],li[1],li[2])
            #Arrelo que agrega una nueva instancia al dataset     
            datasetfila.append([rfc,abc[0],amsbn[0],acsbn[0],atcsbn[0],rmh,rmv,rch,rcv,rtch,rtcv,cmv,cmh,ccv,cch,ctcv,ctch,cbn[0],dma,dmah,clase])
    #Escritura del archivo .csv
    documento.writerows(datasetfila)
    #Cerrar archivo .csv
    f.close()
#main()


# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 16:21:44 2016

@author(s): 
Luis Alberto Muñoz Cruz
Rafael Martinez Rocha
"""
#Libreria para el manejo de archivos .csv
import csv
#Libreria para la creacion de formulas matematicas
import math
#Importacion de clase ocr_dataset para la obtencion de caracteristicas
import ocr_dataset as ocrds

#Nombre:nuevaInstanciaK
#Desc:Metodo que lee la imagen y obtiene sus caracteriscas, tambien se determina el numero de
#los k-vecinos que el usuario quiere
#Argumentos:Ninguno
#Regresa: nuevainstancia
def nuevaInstanciaK():
    #Nombre de la imagen que se desea clasificar
    imagen = str(input('\nNúmero a identificar: '))
    #Numero de intancias cercanas que se desean obtener    
    k = int(input('\nNúmero de vecinos: '))
    #Mensaje del estado del proceso
    print('\nObteniendo características de imagen...')
    #Ruta de la imagen a clasificar
    ruta = './test/' + imagen + '.png'
    #Funciones importadas de la clase ocr_dataset.py para obtener las caracteristicas
    #de la imagen a clasificar
    #Nota: el nombre de las variables son las inicales de las funciones
    li = ocrds.LeerImagen(ruta)
    rfc = ocrds.RazonFilasColumnas(li[1],li[2])
    abc = ocrds.AreaBlancosNegros(li[0],li[1],li[2])
    amsbn = ocrds.AreaMitadSuperiorBlancosNegros(li[0],li[1],li[2])
    acsbn = ocrds.AreaCuartoSuperiorBlancosNegros(li[0],li[1],li[2])
    atcsbn = ocrds.AreaTresCuartoSuperiorBlancosNegros(li[0],li[1],li[2])
    rmh = ocrds.RazonMitadHorizontal(li[0],li[1],li[2])
    rmv = ocrds.RazonMitadVertical(li[0],li[1],li[2])
    rch = ocrds.RazonCuartoHorizontal(li[0],li[1],li[2])
    rcv = ocrds.RazonCuartoVertical(li[0],li[1],li[2])
    rtch = ocrds.RazonTresCuartoHorizontal(li[0],li[1],li[2])
    rtcv = ocrds.RazonTresCuartoVertical(li[0],li[1],li[2])
    cmv = ocrds.CortesMitadVertical(li[0],li[1],li[2])
    cmh = ocrds.CortesMitadHorizontal(li[0],li[1],li[2])
    ccv = ocrds.CortesCuartoVertical(li[0],li[1],li[2])
    cch = ocrds.CortesCuartoHorizontal(li[0],li[1],li[2])
    ctcv = ocrds.CortesTresCuartosVertical(li[0],li[1],li[2])
    ctch = ocrds.CortesTresCuartosHorizontal(li[0],li[1],li[2])
    cbn = ocrds.CruzBlancosNegros(li[0],li[1],li[2])
    dma = ocrds.DiferenciaMitadArea(li[0],li[1],li[2])
    dmah = ocrds.DiferenciaMitadAreaHorizontal(li[0],li[1],li[2])
    #Arreglo que guarda las caracteristicas de la nueva intancia
    nuevainstancia = [rfc,abc[0],amsbn[0],acsbn[0],atcsbn[0],rmh,rmv,rch,rcv,rtch,rtcv,cmv,cmh,ccv,cch,ctcv,ctch,cbn[0],dma,dmah,k]
    #Regresa el arreglo nuevainstancia que contiene las caracteristicas de la nueva instancia  
    return nuevainstancia

#Nombre:cargarDataset
#Desc:Metodo que carga el dataset
#Argumentos:Ruta o nombre del archivo .csv que contiene el dataset
#Regresa: dataset
def cargarDataset(nombrearchivo):
    #Abrir el archivo csv con permisos de lectura
    with open(nombrearchivo, 'r') as csvfile:
        #Leer un archivo con reader()
        lineas = csv.reader(csvfile)
        #Obtener lista de las instancias del dataset
        dataset = list(lineas)
        #Contador que identificara el numero de instancias dentro del dataset
        contadorinstancias = 0
        #Recorrer cada instancia obtenida
        for x in range(len(dataset)):
            #Aumento de contador al detectar una instancia
            contadorinstancias = contadorinstancias + 1
            #Ciclo para recorrer cada caraacteristica de la instancia
            for y in range(21):
                #Condicion para verificar el tamaño de las caracteristicas
                if(y<20):
                    #Convierte los valores del dataset en flotantes
                    dataset[x][y] = float(dataset[x][y])
                else:
                    #Guarda el valor de la clase
                    dataset[x][y] = dataset[x][y]
        #Informacion del dataset
        print("============ Información del Dataset ============")
        print("\tNúmero de Instancias: " + str(contadorinstancias))
        print("\tNúmero de Características por Instancia: 20")
        print("\tNúmero de Clases: 10")
        print("\tNombre de Clases: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}")
    #Regresa el dataset cargado en un arreglo
    return dataset

#Nombre:calcularDistancia
#Desc:Metodo que realiza opraciones para el calculo de la distancia euclidiana a cada una
#de las instancias del dataset
#Argumentos:Dataset y nuevainstancia
#Regresa: distancias euclidianas
def calcularDistancia(dataset,ni):
    #Impresion del estado del proceso
    print('\nCalculando distancias...')
    #Arreglo para guardar las distancias calculadas
    distancias = []
    #Ciclo que recorre cada instancia del dataset y obtiene la distancia
    #euclidiana con respecto a la nueva instancia
    for x in range(len(dataset)):
        #Calculo de distancia euclidiana
        distancias.append([math.sqrt(pow((dataset[x][0] - float(ni[0])),2)+pow((dataset[x][1]-float(ni[1])),2)+pow((dataset[x][2]-float(ni[2])),2)+pow((dataset[x][3]-float(ni[3])),2)+pow((dataset[x][4]-float(ni[4])),2)+pow((dataset[x][5]-float(ni[5])),2)+pow((dataset[x][6]-float(ni[6])),2)+pow((dataset[x][7]-float(ni[7])),2)+pow((dataset[x][8]-float(ni[8])),2)+pow((dataset[x][9]-float(ni[9])),2)+pow((dataset[x][10]-float(ni[10])),2)+pow((dataset[x][11]-float(ni[11])),2)+pow((dataset[x][12]-float(ni[12])),2)+pow((dataset[x][13]-float(ni[13])),2)+pow((dataset[x][14]-float(ni[14])),2)+pow((dataset[x][15]-float(ni[15])),2)+pow((dataset[x][16]-float(ni[16])),2)+pow((dataset[x][17]-float(ni[17])),2)+pow((dataset[x][18]-float(ni[18])),2)+pow((dataset[x][19]-float(ni[19])),2)),dataset[x][20],x+1])
    #variable que contendra valores temporales
    temp = 0
    #Variable que contiene el tamaño del arreglo distancias
    tam = len(distancias)
    #Ciclo para recorrer el tamaño del arreglo
    for i in range(1, tam):
        #Ciclo para recorrer las instancias
        for j in range(0,tam-1):
            #Verifica el valor de la instancia actual y la compara con la instancia delantera
            #Si es mayor realiza las operaciones
            if(distancias[j]>distancias[j+1]):
               #Guarda el valor de la instacia posterior en la variable temporal
               temp = distancias[j+1]
               #Iguala el valor de la distancia posterior a la actual
               distancias[j+1] = distancias[j]
               #Iguala el valor de la distancia actual a la temporal
               distancias[j] = temp
    #Regresa las distancias ordenadas ascendentemente
    return distancias     

#Nombre:clasificarInstancia
#Desc:Metodo que ordena las distancias obtenidas anteriormente, y arroja las instancias que mas 
#se acercan a la nuevainstancia
#Argumentos:distancias y nuevainstancia
#Regresa: Ninguno
def clasificarInstancia(distancias,ni):
    print('\nObteniendo distancias mas cercanas...')
    #Contador de las instancias mas cercanas
    contadorinstancias = 1
    #Contadores para el numero de veces que se repite la clase
    contadorcero = 0
    contadoruno = 0
    contadordos = 0
    contadortres = 0
    contadorcuatro = 0
    contadorcinco = 0
    contadorseis= 0
    contadorsiete = 0
    contadorocho = 0
    contadornueve = 0
    #Encabezado
    print('\n')
    print('     K      |       Distancia     |Clase|Fila|')
    print('----------------------------------------------')
    #Ciclo de Impresion de las distancias mas cercanas
    for x in range(int(ni[20])):
        print('Instancia '+str(contadorinstancias)+" = "+str(distancias[x]))
        #Contador de instancias cercanas
        contadorinstancias = contadorinstancias + 1
        #Evaluacion de la clase de la instancia
        if(distancias[x][1]=='0'):
            contadorcero += 1
        if(distancias[x][1]=='1'):
            contadoruno += 1
        if(distancias[x][1]=='2'):
            contadordos += 1
        if(distancias[x][1]=='3'):
            contadortres += 1
        if(distancias[x][1]=='4'):
            contadorcuatro += 1
        if(distancias[x][1]=='5'):
            contadorcinco += 1
        if(distancias[x][1]=='6'):
            contadorseis += 1
        if(distancias[x][1]=='7'):
            contadorsiete += 1
        if(distancias[x][1]=='8'):
            contadorocho += 1
        if(distancias[x][1]=='9'):
            contadornueve += 1
    #Arreglo que contendra los contadores de las clases
    clases = []
    #Arreglo lleno con los contadores de las clases
    clases = [contadorcero,contadoruno,contadordos,contadortres,contadorcuatro,contadorcinco,contadorseis,contadorsiete,contadorocho,contadornueve]
    #Variable para comprobar los valores de las clases    
    clasemayor = 0
    #Variable para identificar la clase con mayor numero de elementos mas cercanos
    clasificacion = 0
    for x in range(len(clases)):
        #Condicion para verificar el tamañao de cada clase
        if(clases[x] > clasemayor):
            #Guarda el valor de la clase con el valor mas alto
            clasemayor = clases[x]
            #Guarda la identidad de la clase
            clasificacion = x    
    #Impresion del numero de instancias detectadas en cada clase
    #Solo se imprimiran si los contadores de clases son mayores a cero
    if(contadorcero>0):
        print('\nClase 0: '+str(contadorcero) + ' Instancias detectadas')
    if(contadoruno>0):
        print('\nClase 1: '+str(contadoruno) + ' Instancias detectadas')
    if(contadordos>0):
        print('\nClase 2: '+str(contadordos) + ' Instancias detectadas')
    if(contadortres>0):
        print('\nClase 3: '+str(contadortres) + ' Instancias detectadas')
    if(contadorcuatro>0):
        print('\nClase 4: '+str(contadorcuatro) + ' Instancias detectadas')
    if(contadorcinco>0):
        print('\nClase 5: '+str(contadorcinco) + ' Instancias detectadas')
    if(contadorseis>0):
        print('\nClase 6: '+str(contadorseis) + ' Instancias detectadas')
    if(contadorsiete>0):
        print('\nClase 7: '+str(contadorsiete) + ' Instancias detectadas')
    if(contadorocho>0):
        print('\nClase 8: '+str(contadorocho) + ' Instancias detectadas')
    if(contadornueve>0):
        print('\nClase 9: '+str(contadornueve) + ' Instancias detectadas')
    #Impresion de caracter predicho de acuerdo a las distancias mas cercanas
    print('\n\nCaracter predicho: ' + str(clasificacion))


#Funcion que carga el dataset, con el nombre o ruta del archivo como entrada
ds = cargarDataset("data.csv")
#Generacion de caracteristicas de la nueva instancia
nik = nuevaInstanciaK()    
#Calculo de las distancias mas cercanas
cd = calcularDistancia(ds,nik)
#Clasificacion de las distancias mas cercanas y determinacion de la clase de la nueva instancia
clasificarInstancia(cd,nik)

