# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 18:31:39 2016

@author: Marko
"""

import os                             #Aquí se importa el objeto para recorrer las carpetas
import matplotlib.image as mpimg      #Este objeto se importa para recorrer los archivos
import csv                            #Esté es el objeto ocupado para los archivos csv
import math                           #Importamos la libreria math


datS=[]                               #Declaracion de la matriz que almacenara todos los datos
tamMat=2380                          #Asignamos el tamaño que tendran las matrices de acuerdo a el numero de imagenes


#Nombre: propiedad1
#Descripcion: Esta funcion nos regresa la relacion entre 1´s con respecto al tamaño de la imagen (total de 1´s/tamaño total de la imagen)
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion #1´s/#pixeles total, es flotante
def propiedad1(img, tImTo):          #Creacion de la funcion
    resu=0                           #Declaracion de la variable contador de 1´s
    alto=len(img)                    #Esta variable contiene el alto de la imagen
    ancho=int(tImTo/alto)            #Esta variable tiene el ancho de la imagen
    for al in range(alto):           #For que recorre las filas de la imagen
        for an in range(ancho):      #For que recorre las columnas
            num=(int(img[al][an]))   #Obtiene el valor de cada pixel para ser comparado
            if num==1:               #Se compara cada pixel para validar si es un 1
                resu=resu+1          #Si el pixel es 1 se almacena al contador
    resu=(resu/tImTo)                #Se divide el número de pixeles sobre el total de la imagen, para obtener la relacion
    return resu                      #Se regresa la relacion 1's/total de pixeles


#Nombre: propiedad2
#Descripcion: Esta funcion nos regresa la relacion entre el ancho sobre el alto 
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion ancho/alto
def propiedad2(img, tImTo):    #Creación de la función
    alto=len(img)              #Creamos la variable que contiene el alto de la imagen
    ancho=int(tImTo/alto)      #Creamos la variable con el ancho de la imagen
    resu=ancho/alto            #Realizamos la operacion para obtener la relacion deseada
    return resu                #Retornamos la relacion ancho/alto 


#Nombre: propiedad3
#Descripcion: Esta funcion nos regresa la relacion de 1´s que en encuentran a la mitad de la imagen de forma vertical con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion total de pixeles en linea vertical/tamaño total de la imagen
def propiedad3(img, tImTo):                 #Creacion de la funcion
    alto=len(img)                           #Creamos la variable que contiene el alto de la imagen
    ancho=int(tImTo/alto)                   #Creamos la variable con el ancho de la imagen
    dista=int(ancho/2)                      #Obtenemos la distancia en la cual haremos la busqueda de 1´s
    numuns=0                                #Inicializaremos la variable que contendra el numero de 1´s 
    for al in range(alto):                  #For encargado de recorrer las filas de la imagen
        compara=(int(img[al][dista]))       #Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente
        if compara==1:                      #En esta linea comparamos si el valor actual es 1 o no
            numuns=numuns+1                 #Se hace la sobrecarga del numero de 1´s encontrado en la linea de busqueda
    return numuns/alto                      #Retornamos el numero de 1´s encontrados en la mitad de la imagen/tamaño total de la imagen
    

#Nombre: propiedad4
#Descripcion: Esta funcion nos regresa la relacion de 1´s que en encuentran a 1/4 de la imagen de forma vertical con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion total de pixeles en linea vertical/tamaño total de la imagen
def propiedad4(img, tImTo):                 #Creacion de la funcion
    alto=len(img)                           #Creamos la variable que contiene el alto de la imagen
    ancho=int(tImTo/alto)                   #Creamos la variable con el ancho de la imagen
    dista=int(ancho/4)                      #Obtenemos la distancia en la cual haremos la busqueda de 1´s
    numuns=0                                #Inicializaremos la variable que contendra el numero de 1´s 
    for al in range(alto):                  #For encargado de recorrer las filas de la imagen
        compara=(int(img[al][dista]))       #Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente
        if compara==1:                      #En esta linea comparamos si el valor actual es 1 o no
            numuns=numuns+1                 #Se hace la sobrecarga del numero de 1´s encontrado en la linea de busqueda
    return numuns/alto                      #Retornamos el numero de 1´s encontrados en 1/4 de la imagen/tamaño total de la imagen
    

#Nombre: propiedad5
#Descripcion: Esta funcion nos regresa la relacion de 1´s que en encuentran a 3/4 de la imagen de forma vertical con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion total de pixeles en linea vertical/tamaño total de la imagen
def propiedad5(img, tImTo):                 #Creacion de la funcion
    alto=len(img)                           #Creamos la variable que contiene el alto de la imagen
    ancho=int(tImTo/alto)                   #Creamos la variable con el ancho de la imagen
    dista=int((int(ancho/4))*3)             #Obtenemos la distancia en la cual haremos la busqueda de 1´s
    numuns=0                                #Inicializaremos la variable que contendra el numero de 1´s 
    for al in range(alto):                  #For encargado de recorrer las filas de la imagen
        compara=(int(img[al][dista]))       #Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente
        if compara==1:                      #En esta linea comparamos si el valor actual es 1 o no
            numuns=numuns+1                 #Se hace la sobrecarga del numero de 1´s encontrado en la linea de busqueda
    return numuns/alto                      #Retornamos el numero de 1´s encontrados en 3/4 de la imagen/tamaño total de la imagen

       
#Nombre: propiedad6
#Descripcion: Esta funcion nos regresa la relacion de 1´s que en encuentran a 1/2 de la imagen de forma horizontal con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion total de pixeles en linea horizontal/tamaño total de la imagen
def propiedad6(img, tImTo):                         #Creacion de la funcion
    alto=len(img)                                   #Creamos la variable que contiene el alto de la imagen
    ancho=int(tImTo/alto)                           #Creamos la variable con el ancho de la imagen
    altu=int(alto/2)                                #Obtenemos la distancia en la cual haremos la busqueda de 1´s
    numuns=0                                        #Inicializaremos la variable que contendra el numero de 1´s 
    for alt in range(alto):                         #For encargado de recorrer las filas de la imagen
        for anch in range(ancho):                   #For encargado de recorrer las columnas de la imagen
            if alt==altu:                           #Verificamos que nuestro buscador se encuentre en la columna la cual seleccionamos para realizar la busqueda
                compara=(int(img[altu][anch]))      #Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente
                if compara==1:                      #En esta linea comparamos si el valor actual es 1 o no
                    numuns=numuns+1                 #Se hace la sobrecarga del numero de 1´s encontrado en la linea de busqueda
    return numuns/ancho                             #Retornamos el numero de 1´s encontrados en 1/2 de la imagen/tamaño total de la imagen


#Nombre: propiedad7
#Descripcion: Esta funcion nos regresa la relacion de 1´s que en encuentran a 1/4 de la imagen de forma horizontal con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion total de pixeles en linea horizontal/tamaño total de la imagen        
def propiedad7(img, tImTo):                         #Creacion de la funcion
    alto=len(img)                                   #Creamos la variable que contiene el alto de la imagen
    ancho=int(tImTo/alto)                           #Creamos la variable con el ancho de la imagen
    altu=int(alto/4)                                #Obtenemos la distancia en la cual haremos la busqueda de 1´s
    numuns=0                                        #Inicializaremos la variable que contendra el numero de 1´s 
    for alt in range(alto):                         #For encargado de recorrer las filas de la imagen
        for anch in range(ancho):                   #For encargado de recorrer las columnas de la imagen
            if alt==altu:                           #Verificamos que nuestro buscador se encuentre en la columna la cual seleccionamos para realizar la busqueda
                compara=(int(img[altu][anch]))      #Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente
                if compara==1:                      #En esta linea comparamos si el valor actual es 1 o no
                    numuns=numuns+1                 #Se hace la sobrecarga del numero de 1´s encontrado en la linea de busqueda
    return numuns/ancho                             #Retornamos el numero de 1´s encontrados en q/4 de la imagen/tamaño total de la imagen


#Nombre: propiedad8
#Descripcion: Esta funcion nos regresa la relacion de 1´s que en encuentran a 3/4 de la imagen de forma horizontal con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion total de pixeles en linea horizontal/tamaño total de la imagen
def propiedad8(img, tImTo):                         #Creacion de la funcion
    alto=len(img)                                   #Creamos la variable que contiene el alto de la imagen
    ancho=int(tImTo/alto)                           #Creamos la variable con el ancho de la imagen
    altu=int((int(alto/4))*3)                       #Obtenemos la distancia en la cual haremos la busqueda de 1´s
    numuns=0                                        #Inicializaremos la variable que contendra el numero de 1´s 
    for alt in range(alto):                         #For encargado de recorrer las filas de la imagen
        for anch in range(ancho):                   #For encargado de recorrer las columnas de la imagen
            if alt==altu:                           #Verificamos que nuestro buscador se encuentre en la columna la cual seleccionamos para realizar la busqueda
                compara=(int(img[altu][anch]))      #Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente
                if compara==1:                      #En esta linea comparamos si el valor actual es 1 o no
                    numuns=numuns+1                 #Se hace la sobrecarga del numero de 1´s encontrado en la linea de busqueda
    return numuns/ancho                             #Retornamos el numero de 1´s encontrados en q/4 de la imagen/tamaño total de la imagen


#Nombre: propiedad9
#Descripcion: Esta funcion nos regresa la relacion de cortes que en encuentran a 1/2 de la imagen de forma vertical osea los cambios que hace entre 1´s y 0´s con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion de cortes que hay entre la imagen/tamaño total de la imagen
def propiedad9(img, tImTo):                     #Creacion de la funcion
    alto=len(img)                               #Creamos la variable que contiene el alto de la imagen
    ancho=int(tImTo/alto)                       #Creamos la variable con el ancho de la imagen
    dista=int(ancho/2)                          #Obtenemos la distancia en la cual haremos los cortes de la imagen
    numuns=0                                    #Inicializaremos la variable que contendra el numero de cortes
    val=0                                       #Inicializaremos la variable que contendra el valor que sera comparado despues para obtenes el numero de cortes
    for al in range(alto):                      #For encargado de recorrer las filas de la imagen
        compara=(int(img[al][dista]))           #Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente
        if compara!=val:                        #Comparamos si el valor del pixel actual es diferente a la asignacion anterior, asi sabemos si hay cortes en la imagen
            numuns=numuns+1                     #Se hace la sobrecarga del numero de cortes encontrados en la linea de busqueda
            val=(int(img[al][dista]))           #Si hay un corte en la imagen asignamos el valor a nuestra variable para seguir buscando cortes despues
    return numuns                               #Retornams el numero de cortes encontrados a 1/2 de la imagen de forma vertical


#Nombre: propiedad10
#Descripcion: Esta funcion nos regresa la relacion de cortes que en encuentran a 1/4 de la imagen de forma vertical osea los cambios que hace entre 1´s y 0´s con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion de cortes que hay entre la imagen/tamaño total de la imagen    
def propiedad10(img, tImTo):                    #Creacion de la funcion
    alto=len(img)                               #Creamos la variable que contiene el alto de la imagen
    ancho=int(tImTo/alto)                       #Creamos la variable con el ancho de la imagen
    dista=int(ancho/4)                          #Obtenemos la distancia en la cual haremos los cortes de la imagen
    numuns=0                                    #Inicializaremos la variable que contendra el numero de cortes
    val=0                                       #Inicializaremos la variable que contendra el valor que sera comparado despues para obtenes el numero de cortes
    for al in range(alto):                      #For encargado de recorrer las filas de la imagen
        compara=(int(img[al][dista]))           #Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente
        if compara!=val:                        #Comparamos si el valor del pixel actual es diferente a la asignacion anterior, asi sabemos si hay cortes en la imagen
            numuns=numuns+1                     #Se hace la sobrecarga del numero de cortes encontrados en la linea de busqueda
            val=(int(img[al][dista]))           #Si hay un corte en la imagen asignamos el valor a nuestra variable para seguir buscando cortes despues
    return numuns                               #Retornams el numero de cortes encontrados a 1/4 de la imagen de forma vertical


#Nombre: propiedad11
#Descripcion: Esta funcion nos regresa la relacion de cortes que en encuentran a 3/4 de la imagen de forma vertical osea los cambios que hace entre 1´s y 0´s con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion de cortes que hay entre la imagen/tamaño total de la imagen
def propiedad11(img, tImTo):                    #Creacion de la funcion
    alto=len(img)                               #Creamos la variable que contiene el alto de la imagen
    ancho=int(tImTo/alto)                       #Creamos la variable con el ancho de la imagen
    dista=int((int(ancho/4))*3)                 #Obtenemos la distancia en la cual haremos los cortes de la imagen
    numuns=0                                    #Inicializaremos la variable que contendra el numero de cortes
    val=0                                       #Inicializaremos la variable que contendra el valor que sera comparado despues para obtenes el numero de cortes
    for al in range(alto):                      #For encargado de recorrer las filas de la imagen
        compara=(int(img[al][dista]))           #Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente
        if compara!=val:                        #Comparamos si el valor del pixel actual es diferente a la asignacion anterior, asi sabemos si hay cortes en la imagen
            numuns=numuns+1                     #Se hace la sobrecarga del numero de cortes encontrados en la linea de busqueda
            val=(int(img[al][dista]))           #Si hay un corte en la imagen asignamos el valor a nuestra variable para seguir buscando cortes despues
    return numuns                               #Retornams el numero de cortes encontrados a 3/4 de la imagen de forma vertical


#Nombre: propiedad12
#Descripcion: Esta funcion nos regresa la relacion de cortes que en encuentran a 1/2 de la imagen de forma horizontal osea los cambios que hace entre 1´s y 0´s con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion de cortes que hay entre la imagen/tamaño total de la imagen
def propiedad12(img, tImTo):                        #Creacion de la funcion
    alto=len(img)                                   #Creamos la variable que contiene el alto de la imagen
    ancho=int(tImTo/alto)                           #Creamos la variable con el ancho de la imagen
    altu=int(alto/2)                                #Obtenemos la distancia en la cual haremos los cortes de la imagen
    numuns=0                                        #Inicializaremos la variable que contendra el numero de cortes
    val=0                                           #Inicializaremos la variable que contendra el valor que sera comparado despues para obtenes el numero de cortes
    for alt in range(alto):                         #For encargado de recorrer las filas de la imagen
        for anch in range(ancho):                   #For encargado de recorrer las columnas de la imagen
            if alt==altu:                           #Aquí verificamos que nuestro buscador se encuentre en la columna que necesitamos analizar
                compara=(int(img[altu][anch]))      #Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente
                if compara!=val:                    #Comparamos si el valor del pixel actual es diferente a la asignacion anterior, asi sabemos si hay cortes en la imagen
                    numuns=numuns+1                 #Se hace la sobrecarga del numero de cortes encontrados en la linea de busqueda
                    val=(int(img[altu][anch]))      #Si hay un corte en la imagen asignamos el valor a nuestra variable para seguir buscando cortes despues
    return numuns                                   #Retornams el numero de cortes encontrados a 1/2 de la imagen de forma horizontal


#Nombre: propiedad13
#Descripcion: Esta funcion nos regresa la relacion de cortes que en encuentran a 1/4 de la imagen de forma horizontal osea los cambios que hace entre 1´s y 0´s con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion de cortes que hay entre la imagen/tamaño total de la imagen    
def propiedad13(img, tImTo):                        #Creacion de la funcion
    alto=len(img)                                   #Creamos la variable que contiene el alto de la imagen
    ancho=int(tImTo/alto)                           #Creamos la variable con el ancho de la imagen
    altu=int(alto/4)                                #Obtenemos la distancia en la cual haremos los cortes de la imagen
    numuns=0                                        #Inicializaremos la variable que contendra el numero de cortes
    val=0                                           #Inicializaremos la variable que contendra el valor que sera comparado despues para obtenes el numero de cortes
    for alt in range(alto):                         #For encargado de recorrer las filas de la imagen
        for anch in range(ancho):                   #For encargado de recorrer las columnas de la imagen
            if alt==altu:                           #Aquí verificamos que nuestro buscador se encuentre en la columna que necesitamos analizar
                compara=(int(img[altu][anch]))      #Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente
                if compara!=val:                    #Comparamos si el valor del pixel actual es diferente a la asignacion anterior, asi sabemos si hay cortes en la imagen
                    numuns=numuns+1                 #Se hace la sobrecarga del numero de cortes encontrados en la linea de busqueda
                    val=(int(img[altu][anch]))      #Si hay un corte en la imagen asignamos el valor a nuestra variable para seguir buscando cortes despues
    return numuns                                   #Retornams el numero de cortes encontrados a 1/4 de la imagen de forma horizontal


#Nombre: propiedad14
#Descripcion: Esta funcion nos regresa la relacion de cortes que en encuentran a 3/4 de la imagen de forma horizontal osea los cambios que hace entre 1´s y 0´s con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion de cortes que hay entre la imagen/tamaño total de la imagen
def propiedad14(img, tImTo):                        #Creacion de la funcion
    alto=len(img)                                   #Creamos la variable que contiene el alto de la imagen
    ancho=int(tImTo/alto)                           #Creamos la variable con el ancho de la imagen
    altu=int((int(alto/4))*3)                       #Obtenemos la distancia en la cual haremos los cortes de la imagen
    numuns=0                                        #Inicializaremos la variable que contendra el numero de cortes
    val=0                                           #Inicializaremos la variable que contendra el valor que sera comparado despues para obtenes el numero de cortes
    for alt in range(alto):                         #For encargado de recorrer las filas de la imagen
        for anch in range(ancho):                   #For encargado de recorrer las columnas de la imagen
            if alt==altu:                           #Aquí verificamos que nuestro buscador se encuentre en la columna que necesitamos analizar
                compara=(int(img[altu][anch]))      #Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente
                if compara!=val:                    #Comparamos si el valor del pixel actual es diferente a la asignacion anterior, asi sabemos si hay cortes en la imagen
                    numuns=numuns+1                 #Se hace la sobrecarga del numero de cortes encontrados en la linea de busqueda
                    val=(int(img[altu][anch]))      #Si hay un corte en la imagen asignamos el valor a nuestra variable para seguir buscando cortes despues
    return numuns                                   #Retornams el numero de cortes encontrados a 1/4 de la imagen de forma horizontal

#Nombre: generarArchivo
#Descripcion: En esta funcion llenamos el data set (archivo csv) con los datos de la matriz ya antes llenada
#Argumentos de entrada: Recibe la matriz datset la cual contiene todas las propiedades de todos los numeros analizados previamente
#Retorno: No hay retorno
def generarArchivo(datset):                         #Declaracion de la funcion
    dataSet=datset                                  #Asignamos los datos de datset a dataset para meter nos los mismos al archivo csv
    csvsalida=open('DataSet.csv','w',newline='')    #Abrimos el archivo csv en el cual meteremos las propiedades
    salida=csv.writer(csvsalida)                    #Se le indica a la variable salida que archivo sera escrito
    salida.writerow(["Caracteristica 1","Caracteristica 2","Caracteristica 3","Caracteristica 4","Caracteristica 5","Caracteristica 6","Caracteristica 7","Caracteristica 8","Caracteristica 9","Caracteristica 10","Caracteristica 11","Caracteristica 12","Caracteristica 13","Caracteristica 14","Número"])      #Se agrega la cabecera al archivo csv
    salida.writerows(dataSet)                       #Se agregan los datos de la matriz a el archivo csv en cada celda
    del salida                                      #En esta parte se elimina la variable para que no ocupe espacio en memoria
    csvsalida.close()                               #Una vez que el archivo fue grabado lo cerramos
  
  
#Nombre: kNN
#Descripcion: Esta funcion realiza el algoritmo KNN y nos devuelve los K vecinos más cercanos
#Argumentos de entrada: Recibe la imagen de la nueva instancia y el número de vecinos a obtener
#Retorno: Los K vecinos más cercanos
def kNN(img, numVeci):                      #Declaración de la función
    img=mpimg.imread(img)                   #Leemos nuestra nueva instancia
    mat=[]                                  #Declaramos la matriz mat
    knn=[]                                  #Declaramos la matriz knn
    tImTo=img.size                          #Obtenemos el tamaño total de la imagen                        
    for x in range(tamMat+1):               #Esta variable tamMat nos indica de que tamaño debemos crear la matriz en la cual meteremos los datos del dataSet
        mat.append(['']*15)                 #Llenamos la matriz mat de 0´s para sustituir cada dato después
    for x in range(tamMat):                 #Esta matriz contendra solo los datos de cada distancia Euclidiana de cada clase con el nombre de la clase
        knn.append(['']*3)                  #Llenamos la matriz mat de 0´s para sustituir cada dato después
    reader = csv.reader(open('DataSet.csv')) #Leemos el dataSet
    for index,row in enumerate(reader):      #Vaciamos el dataSet (csv) en nuestra matriz knn
        for cont in range(15):              #Recorremos cada columna del csv
            mat[index][cont]=row[cont]      #Colocamos cada dato de cada celda en un espacio de la matriz
    
    i2P1=propiedad1(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia
    i2P2=propiedad2(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia
    i2P3=propiedad3(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia
    i2P4=propiedad4(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia
    i2P5=propiedad5(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia
    i2P6=propiedad6(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia
    i2P7=propiedad7(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia
    i2P8=propiedad8(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia
    i2P9=propiedad9(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia
    i2P10=propiedad10(img, tImTo)             #Aqui se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia
    i2P11=propiedad11(img, tImTo)             #Aqui se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia
    i2P12=propiedad12(img, tImTo)             #Aqui se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia
    i2P13=propiedad13(img, tImTo)             #Aqui se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia
    i2P14=propiedad14(img, tImTo)             #Aqui se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia
    
    #Aqui hacemos asignacion de cada propiedad de una clase a las variables de la ecuacion Euclidiana
    for val in range(tamMat):                #Este for recorre todos los datos del dataSet
        p1=float(mat[val+1][0])              #Se le asigna el valor de cada propiedad a cada variable
        p2=float(mat[val+1][1])              #Se le asigna el valor de cada propiedad a cada variable
        p3=float(mat[val+1][2])              #Se le asigna el valor de cada propiedad a cada variable
        p4=float(mat[val+1][3])              #Se le asigna el valor de cada propiedad a cada variable
        p5=float(mat[val+1][4])              #Se le asigna el valor de cada propiedad a cada variable
        p6=float(mat[val+1][5])              #Se le asigna el valor de cada propiedad a cada variable
        p7=float(mat[val+1][6])              #Se le asigna el valor de cada propiedad a cada variable
        p8=float(mat[val+1][7])              #Se le asigna el valor de cada propiedad a cada variable
        p9=float(mat[val+1][8])              #Se le asigna el valor de cada propiedad a cada variable
        p10=float(mat[val+1][9])             #Se le asigna el valor de cada propiedad a cada variable
        p11=float(mat[val+1][10])            #Se le asigna el valor de cada propiedad a cada variable
        p12=float(mat[val+1][11])            #Se le asigna el valor de cada propiedad a cada variable
        p13=float(mat[val+1][12])            #Se le asigna el valor de cada propiedad a cada variable
        p14=float(mat[val+1][13])            #Se le asigna el valor de cada propiedad a cada variable
        
        #Aplicamos la distancia Euclidiana para cada clase de el dataset comparada con la nueva instancia
        dist= math.sqrt(((p1-i2P1)**2)+((p2-i2P2)**2)+((p3-i2P3)**2)+((p4-i2P4)**2)+((p5-i2P5)**2)+((p6-i2P6)**2)+((p7-i2P7)**2)+((p8-i2P8)**2)+((p9-i2P9)**2)+((p10-i2P10)**2)+((p11-i2P11)**2)+((p12-i2P12)**2)+((p13-i2P13)**2)+((p14-i2P14)**2))
        knn[val][0]=val+1                   #Asignacion de la posicion del resultado de la distancia entre dato e instancia nueva
        knn[val][1]=dist                    #Asignacion de la distancia de nada dato con la nueva instancia
        knn[val][2]=mat[val+1][14]          #Asignacion de el nombre de la clase de cada dato
     
    #Aqui se obtienen los K vecinos más cercanos   
    res=[]                                  #Declaramos una matriz para ingresarle nos k vecinos más cercanos
    for x in range(numVeci):                #Llenamos de 0´s la matriz 
        res.append([0.0]*3)                 #Llenamos de 0´s la matriz para sustituir cada campo despues
    
    for i in range(numVeci):                #Se recorre la matriz las K veces
        temp = knn[0][1]                    #Asignamos el valor del primer datos a la variable temp
        numero = len(knn)                   #Obtenemos el tamaño de la matriz
        for j in range(numero):             #Se recorre la matriz completa
            if(knn[j][1] < temp):           #Se compra cada dato para ver si es el menor de todos
                temp = knn[j][1]            #Si el dato es el menor re asigna a la variable temp
                apun=j                      #Guardamos la posicion de la variable de menor valor
            if (j+1==numero):               #Validamos si estamos en la ultima posicion
                res[i][0] = knn[apun][0]    #Asignamos la posicion en la matriz res
                res[i][1] = knn[apun][1]    #Asignamos la distancia en la matriz res
                res[i][2] = knn[apun][2]    #Asignamos la clase en la matriz res
                knn.pop(apun)               #Borramos el elemento para no repetir datos
    return res                              #Retornamos la matriz de los k vecinos mas cercanos
        
    
#Nombre: crearDataSet
#Descripcion: En esta funcion llenamos la matriz datS previamente declarada de puros 0´s para despues sustituir cada valor por cada una de las propiedades de todas las imagenes
#parametros: no
#retorno: La matriz con las propiedades
def crearDataSet():                                         #Declaracion de la funcion
    for i in range(tamMat):                                 #En este for se controlan el numero de filas de nuestra matriz
        datS.append([0.0]*15)                               #Aqui asignamos el numero de columnas que llevara nuestra matriz y llenaremos cada espacio de 0´s
    rootDir = 'DatosPrueba'                                 #Declaramos la variable rootDir la cual contiene el nombre de la carpeta en la cual se encuentran las carpetas de nuestras imagenes
    nameima=''                                              #Declaramos esta variable la cual contendra la ruta completa de cada imagen
    x=0                                                     #Declaramos e inicializamos la variable que controlara la posicion de las filas de nuestra matriz
    y=0                                                     #Declaramos e inicializamos la variable que controlara la posicion de las columnas de nuestra matriz
    for dirName, subdirList, fileList in os.walk(rootDir):  #Este for recorrera las carpetas que contienen nuestras imagenes en la ruta especificada por "rootDir"
        num=str(dirName)+'  '                               #Obtenemos el nombre de la ruta actual para indicar en que carpeta nos encontramos
        for fname in fileList:                              #Este for controla cada imagen dentro de cada carpeta para que cada una sea abierta y analizada
            nameima=dirName+"/"+fname                       #Concatenamos las variables para obtener la ruta exacta de cada imagen
            img = mpimg.imread(nameima)                     #Leemos cada imagen de cada carpeta
            tImTo=img.size                                  #Asignamos el tamaño de cada imagen para su posterior uso
            datS[x][y]=propiedad1(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #Aqui incrementamos la variable "y" para poner cada propiedad en la columna correcta
            datS[x][y]=propiedad2(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #Aqui incrementamos la variable "y" para poner cada propiedad en la columna correcta
            datS[x][y]=propiedad3(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #Aqui incrementamos la variable "y" para poner cada propiedad en la columna correcta
            datS[x][y]=propiedad4(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #Aqui incrementamos la variable "y" para poner cada propiedad en la columna correcta
            datS[x][y]=propiedad5(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #Aqui incrementamos la variable "y" para poner cada propiedad en la columna correcta
            datS[x][y]=propiedad6(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #Aqui incrementamos la variable "y" para poner cada propiedad en la columna correcta
            datS[x][y]=propiedad7(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #Aqui incrementamos la variable "y" para poner cada propiedad en la columna correcta
            datS[x][y]=propiedad8(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #Aqui incrementamos la variable "y" para poner cada propiedad en la columna correcta
            datS[x][y]=propiedad9(img, tImTo)               #Aqui se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #Aqui incrementamos la variable "y" para poner cada propiedad en la columna correcta
            datS[x][y]=propiedad10(img, tImTo)              #Aqui se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #Aqui incrementamos la variable "y" para poner cada propiedad en la columna correcta
            datS[x][y]=propiedad11(img, tImTo)              #Aqui se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #Aqui incrementamos la variable "y" para poner cada propiedad en la columna correcta
            datS[x][y]=propiedad12(img, tImTo)              #Aqui se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #Aqui incrementamos la variable "y" para poner cada propiedad en la columna correcta
            datS[x][y]=propiedad13(img, tImTo)              #Aqui se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #Aqui incrementamos la variable "y" para poner cada propiedad en la columna correcta
            datS[x][y]=propiedad14(img, tImTo)              #Aqui se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #Aqui incrementamos la variable "y" para poner cada propiedad en la columna correcta
            datS[x][y]=num[12]+'´s'                         #Aqui se llama a la funcion que nos devolvera el nombre de la clase
            y=0                                             #En esta parte regresamos "y" a cero para volver a la primera columna y llenar las propiedades de la siguiente imagen
            x=x+1                                           #Aqui incrementamos la variable "x" para indicar que estamos en la siguiente imagen
        #if num[12]!=' ':                                   #Validamos si el caracter no es ' '
          # print('Leyendo carpeta: %s' % num[12])          #Aquí indicamos que carpeta exactamente estamos analizando
    return datS                                             #En esta parte retornamos la matriz la llenada
    
     

#Nombre: Main
#Descripcion: Es la funcion principal la cual manda a llamar las demas funciones
#Parametros: No
#Return: No
if __name__ == "__main__":                                              #Aqui indicamos la funcion main
    os.system('cls')                                                    #Limpiamos la pantala    
    while True:                                                         #Hacemos un while que se repita hasta que el usuario lo detenga
        print('\n****   Menu de opciones   ****')                       #Imprimimos el menu principal
        print('1.-Crear DataSet')                                       #Imprimimos el menu principal
        print('2.-Buscar numero por KNN')                               #Imprimimos el menu principal
        print('3.-Salir')                                               #Imprimimos el menu principal
        opcion=int(input('¿Qué opción eliges?: '))                      #Ingresamos la opcion deseada
        if opcion==1:                                                   #Validamos si seleccionamos la opcion 1
            print('Procesando informacion ...')                         #Mandamos mensaje de procesamiento 
            data=crearDataSet()                                         #En esta parte mandamos a llamar la funcion encargada de llenar la matriz con las propiedades de cada imagen
            generarArchivo(data)                                        #Aqui mandamos a llamar a la funcion encargada de generar el archivo csv
            print ('Se leyeron: ',tamMat,' datos\nSe definieron 14 instancias\nSe definieron 10 clases\nLas clases son: 0,1,2,3,4,5,6,7,8,9' )  #Mandamos mensaje con las caracteristicas de la ejecucion
        elif opcion==2:                                                #Validamos si seleccionamos la opcion 2
            nomImg=input('Ingrese el nombre de la imagen a comparar sin extension: ') #Solicitamos el nombre de la imagen a clasificar
            numVeci=int(input('Ingrese el número de vecinos K: '))     #Solicitamos el numero de vecinos
            nomImg=nomImg+".png"                                       #Agregamos la extención a la imagen 
            mat=kNN(nomImg, numVeci)                                   #Llamamos a la funcion kNN y su valor de retorno se lo damos a mat
            for va in range(numVeci):                                  #For para imprimir los K vecinos
                print("Num. vecino: ",va+1,"\n Posición en DataSet: ", mat[va][0]+1,"\n Clase: ",mat[va][2],"\n Distancia: ",mat[va][1])  #Se imprimen solamente los vecinos más cercanos indicados anteriormente
            print('\nTu imagen es de clase',mat[va][2])
            print('Proceso finalizado\n')                              #Mandamos mensaje de proceso finalizado
        elif opcion==3:                                                #Validamos si seleccionamos la opcion 2
            print('Programa finalizado\n')                             #Mandamos mensaje de despedida
            break                                                      #Detenemos el while
        else:                                                          #Validamos si seleccionamos una opcion invalida
            print('No has ingresado una opcion valida\n')              #Mandamos un mensaje de error
            