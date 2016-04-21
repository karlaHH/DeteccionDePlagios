# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 00:36:09 2016

@author: Cocoletzi
"""
import KNN_funciones #importamos KNN_funciones para el manejo de las función KNN que programamos con anterioridad
import Dataset #importamos Dataset para la creacion del nuestro Dataset
import os #importamos os para usar comandos propios del Sistema Operativo
print ("Qué deseas realizar:")#impresion del menú para realizar la primera acción
opcion=int(input ("\t1.-Generar Dataset\n\t2.-Clasificar Imagen\n\t3.-Salir\n"))#Menú de opciones que contiene la variable opcion de tipo int que servira para evaluar lo que hara el programa
os.system("cls")#función para limpiar la pantalla una vez que se halla seleccionado una opción
opcion_dos=0#variable de tipo entero que alamcenara un valor para evaluar la segunda parte del menú
while(opcion!=3):#ciclo while que evaluara la varialbe opcion que fuera ingresada por el usuario
    if(opcion<1 or opcion>3):#la variable opcion es validada con la finalidad de el usuario solo pueda saleccionar un rango de numero que debera estar entre el 1 y el 3
        print("Error")#si el numero seleccionado por el usuario no se encuentra dentro de rango 1:3 se mostrara en pantalla un mesaneje de error
    if (opcion==1):#se evalalua que el numero ingresado por el usuario sea igual a 1
        Dataset.dataset()#si el numero ingresado por el usuario es igual entonce invocamos al metodo Dataset y a la funcion dataset con la finalidad de generar un nuevo dataset
    if (opcion==2):#se evalua si el numero ingresado por el usuario es igual a 2 
        KNN_funciones.instancias()#se aplica la funcion de clasificacion del metodo KNN
    input("\n\nPulsa una tecla para continuar...")#impresion de pantalla para retrasar la limpieza de la pantalla
    os.system("cls")#limpieza de pantalla
    opcion_dos=int(input("Deseas Realizar algo mas?\n\t1.-SI\n\t2.-Salir\n"))#impresion de pantalla de nuevas acciones y guardamos en variable opcion_dos 
    os.system("cls")#limpieza de pantalla
    if (opcion_dos==1):#validamos que el valor que ingreso el usuario sea igual a uno 
        print ("Qué deseas realizar:")#impresion preguntando nuevamente que desea hacer
        opcion=int(input ("\t1.-Generar Dataset\n\t2.-Clasificar Imagen\n\t3.-Salir\n"))#mostramos opciones al usuario de las acciones que puede realizar y guardamos en la variable opcion
        os.system("cls")#limpiamos pantalla
    else:# que haremos en caso de que el usuario elija una opcion distinta al  1
        opcion=3#la variable opcion sera igual a 3 lo que finalizara el programa
if(opcion==3):#se evalua que el usuario haya escrito el numero 3 
    os.system("cls")#en caso de que se haya tecleado el numero 3 se limpiara la pantalla
    print("Adios")#se imprime mensaje de despedida


# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 13:53:29 2016

@author: verticalCarlos
"""
import matplotlib.image as mpimg#importar una funcion de la libreria matplotlib y guardamos como mpimg
import os#importamos librerias de sistema operativo
"""
Nombre:      datos_imagen
Descripción: Leemos imagenes y las guardamos en un arreglo
Parámetros de entrada: Ninguno
Parámetros de Salida: img
"""
def datos_imagen():
    print("Nombre de la imagen: ")#impresion de pantalla
    nombre_imagen=(input())#variable de tipo int
    os.system("cls")#limpiar pantalla
    img=mpimg.imread(nombre_imagen)#leemos la imagen y guardamos en una variable
    #img_dos=img
    #img_dos=plt.imshow(img_dos)
    return img#regresamos un arreglo con los datos de la imagen
"""
Nombre:      lectura
Descripción: leemos los valores de la imagen tales como tamaño de lo alto y ancho
Parámetros de entrada: Ninguno
Parámetros de retorno: limx,limy, imgplot, div_x,div_y
"""    
def lectura():
    img=datos_imagen()#llamamos a la funcion datos imagen y la almacenamos en la variable img
    imgplot=img#copiamos la variable img en imgplot
    imagen=imgplot.shape#obtenemos las medidas de la imagen en alto y ancho
    limx= imagen[1]#obtenemos las medidas de lo ancho
    limy= imagen[0]#obtenemos las medidas de lo alto
    div_x=int(limx/2)#dividimos el ancho entre dos y lo guardamos en div_x
    div_y=int(limy/2)#dividimos el alto entre dos y lo guardamos en div_y
    return limx,limy, imgplot, div_x,div_y#regresamos 4 datos y un arreglo
"""
Nombre:      primera_segunda_carac
Descripción: obtenemos las dos primeras caracteristicas de la imagen, la primera consiste en la relacion que existe
            entre el alto y el acho de la imagen, la segunda es respecto al numero de pixeles blancos de la totalidad de pixeles
Parámetros de entrada: tamaño de alto y ancho, iamgen
Parámetros de retorno: relacion_1, relacion_2
"""    
def primera_segunda_carac(limx, limy,imgplot):
    relacion_1=limy/limx#dividimos el alto entre el ancho para saber la relacion de la imagen
    fila=0#variable de tipo entero
    columna=0#variable de tipo entero
    relacion_2=0#variable de tipo entero
    aux=0#variable de tipo entero
    for fila in range (0, limy):#recorreremos la imagen hasta el limite de lo alto
        for columna in range (0,limx):#recorremos la imagen hasta el limite de lo ancho
            if (imgplot[fila,columna]==1):#revisamos el numero que contiene la matriz en cada posicion
                aux=aux+1#si es un 1 aumentamos en 1 el contador
    relacion_2=(limx*limy)/aux#multiplicamos el tamoño de la imagen para saber la totalidad de pixeles y luego la dividimos entre el total de auxiliares
    return relacion_1, relacion_2#regresamos las primeras dos caracteristicas
"""
Nombre:      tercera_cuarta_carac
Descripción: obtenemos caracteristicas tres(el numero de cambios de color en la parte media de la imagen) y cuatro (el numero
            total de pixeles blancos en la parte media de la imagen)
Parámetros de entrada: tamaño de alto y ancho, iamgen y la mitad de la imagen en lo alto y lo ancho
Parámetros de retorno: vertical_cambios,vertical_numero
"""    
def tecera_cuarta_carac(limx,limy,imgplot,div_x,div_y):
    fila=0#variable de tipo entero 
    vertical_cambios=0#variable de tipo entero 
    vertical_numero=0#variable de tipo entero 
    aux=imgplot[fila,div_x]#variable de tipo entero 
    for fila in range (0, limy):#for que recorre la fila hasta la ultima posicion de la imagen
        if (imgplot[fila, div_x]!=aux):#condicion para detectar los cambios de color
            vertical_cambios=vertical_cambios+1#aumentamos en uno el contador si se cumple la condicion
            aux=imgplot[fila,div_x]#el auxiliar toma el valor del pixel anterior
        if (imgplot[fila, div_x]==1):#condicion para detectar la totalida de blancos a la mitad de la imagen
            vertical_numero=vertical_numero+1#aumentamos en uno el contador
    return vertical_cambios,vertical_numero#regresamos las dos caracteristicas

"""
Nombre:      quinta_sexta_carac
Descripción: obtenemos caracteristicas cinco (el numero de cambios de color de la mitad de la imagen trazando una linea horizontal) 
            y seis (el numero de pixeles blancos de la mitad de la imagen trazando una linea horizontal) de la imagen
Parámetros de entrada: tamaño de alto y ancho, iamgen y la mitad de la imagen en lo alto y lo ancho
Parámetros de retorno: horizontal_cambios, horizontal_numero
"""    
def quinta_sexta_carac(limx,limy,imgplot,div_x,div_y):
    columna=0#variable de tipo entero
    horizontal_cambios=0#variable de tipo entero
    horizontal_numero=0#variable de tipo entero
    aux=imgplot[div_y,columna]#variable de tipo entero
    for columna in range (0, limx):#for que recorre la columna hasta la ultima posicion de la imagen
        if (imgplot[div_y, columna]!=aux):#condicion para detectar los cambios de color
            horizontal_cambios=horizontal_cambios+1#aumentamos en uno el contador si se cumple la condicion
            aux=imgplot[div_y,columna] #el auxiliar toma el valor del pixel anterior               
        if (imgplot[div_y, columna]==1):#condicion para detectar la totalida de blancos en la mitad de la imagen en linea horizontal
            horizontal_numero=horizontal_numero+1#aumentamos en uno el contador
    return horizontal_cambios, horizontal_numero#regresamos las dos caracteristicas
"""
Nombre:     septima_octava_carac
Descripción: obtenemos caracteristicas siete(el numero de cambios de color de la primera cuarta parte de la imagen trazando una linea vertical) 
            ocho (el numero de pixeles blancos de la primera cuarta parte de la imagen trazando una linea vertical) de la imagen
Parámetros de entrada: tamaño de alto y ancho, iamgen y la mitad de la imagen en lo alto y lo ancho
Parámetros de retorno: vertical_cambios_izquierda,vertical_cambios_numeros_izquierda
"""        
def septima_octava_carac(limx,limy,imgplot,div_x,div_y):
    fila=0#variable de tipo entero
    vertical_cambios_izquierda=0#variable de tipo entero
    vertical_cambios_numeros_izquierda=0#variable de tipo entero
    division=int(limx/4)#variable de tipo entero en la que dividimos el ancho de la imagen en 4 
    aux=imgplot[fila,division]#variable de tipo entero
    for fila in range (0, limy):#for que recorre la fila hasta la ultima posicion de la imagen
        if (imgplot[fila, division]!=aux):#condicion para detectar los cambios de color en la parte izquierda de la imagen
            vertical_cambios_izquierda=vertical_cambios_izquierda+1#aumentamos en uno el contador si se cumple la condicion
            aux=imgplot[fila,division]#el auxiliar toma el valor del pixel anterior
        if (imgplot[fila, division]==1):#condicion para detectar la totalida de blancos en cuartpa parte izquierda de la imagen en linea horizontal
            vertical_cambios_numeros_izquierda=vertical_cambios_numeros_izquierda+1#aumentamos en uno el contador       
    return vertical_cambios_izquierda,vertical_cambios_numeros_izquierda#regresamos las dos caracteristicas
"""
Nombre:     novena_decima_carac
Descripción: obtenemos caracteristicas nueve(el numero de cambios de color de la ultima cuarta parte de la imagen trazando una linea vertical) 
            decima (el numero de pixeles blancos de la ultima cuarta parte de la imagen trazando una linea vertical) de la imagen
Parámetros de entrada: tamaño de alto y ancho, iamgen y la mitad de la imagen en lo alto y lo ancho
Parámetros de retorno: vertical_cambios_derecha,vertical_cambios_numeros_derecha
"""       
def novena_decima_carac(limx,limy,imgplot,div_x,div_y):
    fila=0#variable de tipo entero
    vertical_cambios_derecha=0#variable de tipo entero
    vertical_cambios_numeros_derecha=0#variable de tipo entero
    division=int (limx/4)#variable de tipo entero en la que dividimos el alto de la imagen en 4 
    division=limx-division#al tamaño del ancho de la imagen le restaremos el resultado de la division
    aux=imgplot[fila,division]#variable de tipo entero
    for fila in range (0, limy):#for que recorre la fila hasta la ultima posicion de la imagen
        if (imgplot[fila, division]!=aux):#condicion para detectar los cambios de color en la parte derecha de la imagen
            vertical_cambios_derecha=vertical_cambios_derecha+1#aumentamos en uno el contador si se cumple la condicion
            aux=imgplot[fila,division]#el auxiliar toma el valor del pixel anterior
        if (imgplot[fila, division]==1):#condicion para detectar la totalida de blancos en cuartpa parte derecha de la imagen en linea horizontal
            vertical_cambios_numeros_derecha=vertical_cambios_numeros_derecha+1  #aumentamos en uno el contador      
    return vertical_cambios_derecha,vertical_cambios_numeros_derecha#regresamos las dos caracteristicas
"""
Nombre:     once_doce_carac
Descripción: obtenemos caracteristicas once(el numero de cambios de color de la primera cuarta parte de la imagen trazando una linea horizontal, es decir parte de arriba) 
            doce (el numero de pixeles blancos de la primera cuarta parte de la imagen trazando una linea horizontal, parte arriba) de la imagen
Parámetros de entrada: tamaño de alto y ancho, iamgen y la mitad de la imagen en lo alto y lo ancho
Parámetros de retorno:  horizontal_cambios_arriba, horizontal_numero_arriba
"""     
def once_doce_carac(limx,limy,imgplot,div_x,div_y):
    columna=0#variable de tipo entero
    horizontal_cambios_arriba=0#variable de tipo entero
    horizontal_numero_arriba=0#variable de tipo entero
    division=int (limy/4)#variable de tipo entero en la que dividimos el ancho de la imagen en 4 
    aux=imgplot[division,columna]#variable de tipo entero
    for columna in range (0, limx):#for que recorre la columna hasta la ultima posicion de la imagen
        if (imgplot[division, columna]!=aux):#condicion para detectar los cambios de color en la parte de arriba de la imagen
            horizontal_cambios_arriba=horizontal_cambios_arriba+1#aumentamos en uno el contador si se cumple la condicion
            aux=imgplot[division,columna]#el auxiliar toma el valor del pixel anterior                
        if (imgplot[division, columna]==1):#condicion para detectar la totalida de blancos en cuartpa parte de arriba de la imagen en linea horizontal
            horizontal_numero_arriba=horizontal_numero_arriba+1#aumentamos en uno el contador    
    return horizontal_cambios_arriba, horizontal_numero_arriba#regresamos las dos caracteristicas
"""
Nombre:     trece_catorce_carac
Descripción: obtenemos caracteristicas trece(el numero de cambios de color de la ultima cuarta parte de la imagen trazando una linea horizontal, parte baja de la imagen) 
            catorce (el numero de pixeles blancos de la ultima cuarta parte de la imagen trazando una linea horizontal) de la imagen
Parámetros de entrada: tamaño de alto y ancho, iamgen y la mitad de la imagen en lo alto y lo ancho
Parámetros de retorno:  horizontal_cambios_abajo,horizontal_numero_abajo
"""    
def trece_catorce_caract(limx,limy,imgplot,div_x,div_y):
    columna=0#variable de tipo entero
    horizontal_cambios_abajo=0#variable de tipo entero
    horizontal_numero_abajo=0#variable de tipo entero
    division=int (limy/4)#variable de tipo entero en la que dividimos el ancho de la imagen en 4 
    division=limy-division#variable de tipo entero en la que restamos la divison al alto de la imagen 
    aux=imgplot[division,columna]#variable de tipo entero
    for columna in range (0, limx):#for que recorre la columna hasta la ultima posicion de la imagen
        if (imgplot[division, columna]!=aux):#condicion para detectar los cambios de color en la parte de abajo de la imagen
            horizontal_cambios_abajo=horizontal_cambios_abajo+1#aumentamos en uno el contador si se cumple la condicion
            aux=imgplot[division,columna]#el auxiliar toma el valor del pixel anterior                    
        if (imgplot[division, columna]==1):#condicion para detectar la totalida de blancos en cuartpa parte de abajo de la imagen en linea horizontal
            horizontal_numero_abajo=horizontal_numero_abajo+1#aumentamos en uno el contador    
    return horizontal_cambios_abajo,horizontal_numero_abajo#regresamos las dos caracteristicas


# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 10:06:02 2016

@author: JuanCarlos
"""
import matplotlib.image as mpimg#importar una funcion de la libreria matplotlib y guardamos como mpimg
import csv#importamos libreria para archivos csv
import os#importamos librerias de sistema operativo
import Caracteristicas#importamos caracteristicas.py
"""
Nombre:      dataset()
Descripción:Generamos un dataset en un archivo.csv que contiene 14 caracteristicas, una clase
Parámetros de entrada: Ninguno
Parámetros de Salida: dataset.csv
"""
def dataset():
    root='Numeros'#Es el nombre de la carpeta en donde se encuentra nuestos numeros
    archivo= open('DataSet_Final.csv', 'w', newline='')#creamos un nuevo archivo .csv con el nombre de DataSet_final.csv
    salida = csv.writer(archivo)#variable que nos permite escribir en un archivo csv 
    porcentaje=''#variable de tipo str
    clase=0#varialbe de tipo int
    posiciones_dataset=0#variable de tipo int
    for dirName, subdirList, fileList in os.walk(root):#podremos recorrer todas las carpetas y subcarpetas de una ruta
        print("Estamos trabajando en el dataset\n",porcentaje)#impresion de pantalla
        porcentaje=porcentaje+'.#'#escribimos una cadena con .#        
        for fname in fileList:#leemos todos los archivos que se encuentran en las subcarpetas
            posiciones_dataset=posiciones_dataset+1#aumentamos en uno el valor de la posicion
            nameima=dirName+'/'+fname#entramos a una nueva subcarpeta
            imgplot=mpimg.imread(nameima)#leemos una imagen
            imagen=imgplot.shape#obtenemos las medidas de las imagenes
            limx= imagen[1]#guardamos enuna variable de tipo entero el la poscion de imagen
            limy= imagen[0]#guardamos enuna variable de tipo entero el la poscion de imagen
            div_x=int(limx/2)#obtenemos la mitad del tamaño de lo ancho de la imagen 
            div_y=int(limy/2)#obtenemos la mitad del tamaño de lo alto de la imagen
            relacion_1,relacion_2=Caracteristicas.primera_segunda_carac(limx, limy,imgplot)#obtenrmos las primeras dos caracteristicas de la imagen
            recta_cambios,recta_numero=Caracteristicas.tecera_cuarta_carac(limx,limy,imgplot,div_x,div_y)#caracteristicas tres y cuatro
            perpendicular_cambios,perpendicular_numero=Caracteristicas.quinta_sexta_carac(limx,limy,imgplot,div_x,div_y)##caracteristicas cinco y seis
            recta_cambios_izquierda,recta_cambios_numeros=Caracteristicas.septima_octava_carac(limx,limy,imgplot,div_x,div_y)#caracteristicas siete y ocho
            recta_cambios_derecha,recta_cambios_derecha_numeros=Caracteristicas.novena_decima_carac(limx,limy,imgplot,div_x,div_y)#caracteristicas nueve y diez
            perpendicular_cambios_arriba, perpendicular_numero_arriba=Caracteristicas.once_doce_carac(limx,limy,imgplot,div_x,div_y)#caracteristicas once y doce
            perpendicular_cambios_abajo, perpendicular_numero_abajo=Caracteristicas.trece_catorce_caract(limx,limy,imgplot,div_x,div_y)#caracteristicas trece y catorce                 
            salida.writerow([relacion_1,relacion_2, recta_cambios,recta_numero,perpendicular_cambios, 
                             perpendicular_numero, recta_cambios_izquierda,recta_cambios_numeros, recta_cambios_derecha,
                             recta_cambios_derecha_numeros, perpendicular_cambios_arriba, perpendicular_numero_arriba,
                             perpendicular_cambios_abajo, perpendicular_numero_abajo,posiciones_dataset,clase-1])#escribimos todas las caracteristicas en un archivo.csv
        clase=clase+1#aumentamos en uno al contador 
        os.system("cls")#limpiamos pantalla
    print ("Dataset Terminado")#impresion de pantalla    
    archivo.close()#dejamos de escribir en el dataset
    
    
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:27:01 2016

@author: JuanCarlos
"""

import csv#importar librerias para archivos CSV
import math#importar libreria para funciones matematicas
import Caracteristicas#importar caracteristicas.py
import os#importar libreria del sistema operativo
"""
Nombre:      KNN_funciones
Descripción:Clasificamos una imagen utilizando knn para clasificacion de
            acuerdo a 14 caracteristicas previamente definidas y almacenadas
            en un archivo .csv
Parámetros de entrada: Ninguno
Parámetros de Salida: dataset, numero de vecinos
"""
def Clasificacion():#nombre de la funcion para clasificar la imagen
    limx,limy, imgplot, div_x,div_y=Caracteristicas.lectura()
    """llamamos a la funcion lectura que se encuetra en Caracteristicas.py
    y guardamos los valores de retorno en limx=limites en eje de las x
    limy=limite en el eje de las y, imgplot= contenido de la imagen, div_x= la
    mitad del tamaño de la imagen en el eje de las x, div_y=la mitad del tamaño de la imagen en el eje de las y"""
    relacion_1,relacion_2=Caracteristicas.primera_segunda_carac(limx, limy,imgplot)
    """llamamos a la funcion que contiene a las dos primeras caracterisiticas
    y las guardamos en las variables relacion_1=relacion del tamaño de la imagen, 
    relación_2= relacion del numero de pixeles blancos con negros """
    vertical_cambios,vertical_numero=Caracteristicas.tecera_cuarta_carac(limx,limy,imgplot,div_x,div_y)
    """llamamos a la funcion que contiene a las caracterisiticas tres y cuatro
    y las guardamos en las variables vertical_cambios= los cambios de color que existen 
    a mitad de la imagen con respecto a los pixeles que se encuentran en esa posicion, 
    vertical_numero= al numero de pixeles blancos que se encuentran a mitad de la imagen 
    con respecto a los pixeles en esa posicion"""
    horizontal_cambios,horizontal_numero=Caracteristicas.quinta_sexta_carac(limx,limy,imgplot,div_x,div_y)
    """llamamos a la funcion que contiene a las caracterisiticas cinco y seis
    y las guardamos en las variables horizontal_cambios=a los cambios de color que existen 
    a mitad de la imagen con respecto a los pixeles que se encuentran en esa posicion de las x , 
    horizontal_numero= al numero de pixeles blancos que se encuentran a mitad de la imagen 
    con respecto a los pixeles en esa posicion del eje x"""
    vertical_cambios_izquierda,vertical_cambios_numeros=Caracteristicas.septima_octava_carac(limx,limy,imgplot,div_x,div_y)
    """llamamos a la funcion que contiene a las caracterisiticas siete y ocho
    y las guardamos en las variables vertical_cambios_izquierda= los cambios de color que existen 
    del lado izquierdo de la primera cuarta parte de la imagen con respecto a los pixeles que se encuentran en esa posicion de las y, 
    vertical_cambios_numeros= al numero de pixeles blancos que se encuentran en la primera cuarta parte de la imagen 
    con respecto a los pixeles en esa posicion del eje y"""
    vertical_cambios_derecha,vertical_cambios_derecha_numeros=Caracteristicas.novena_decima_carac(limx,limy,imgplot,div_x,div_y)
    """llamamos a la funcion que contiene a las caracterisiticas nueve y diez
    y las guardamos en las variables vertical_cambios_derecha= los cambios de color que existen 
    del lado derecha de la ultima cuarta parte de la imagen con respecto a los pixeles que se encuentran en esa posicion de las y, 
    vertical_cambios_derecha_numeros= al numero de pixeles blancos que se encuentran en la ultima cuarta parte de la imagen 
    con respecto a los pixeles en esa posicion del eje y"""    
    horizontal_cambios_arriba, horizontal_numero_arriba=Caracteristicas.once_doce_carac(limx,limy,imgplot,div_x,div_y)
    """llamamos a la funcion que contiene a las caracterisiticas once y doce
    y las guardamos en las variables horizontal_cambios_arriba=a los cambios de color que existen 
    a  en la primera cuarta parte de arriba de la imagen con respecto a los pixeles que se encuentran en esa posicion de las x, 
    horizontal_numero_arriba= al numero de pixeles blancos que se encuentran a en la primera cuarta parte de la imagen 
    con respecto a los pixeles en esa posicion del eje x"""    
    horizontal_cambios_abajo, horizontal_numero_abajo=Caracteristicas.trece_catorce_caract(limx,limy,imgplot,div_x,div_y)    
    """llamamos a la funcion que contiene a las caracterisiticas trece y catorce
    y las guardamos en las variables horizontal_cambios_abajo=a los cambios de color que existen 
     en la ultima cuarta parte de abajo de la imagen con respecto a los pixeles que se encuentran en esa posicion de las x, 
    horizontal_numero_abajo= al numero de pixeles blancos que se encuentran a en la ultima cuarta parte de la imagen 
    con respecto a los pixeles en esa posicion del eje x"""       
    abrir= open('DataSet_Final.csv')#la variable abrir contendra todos los datos que se encuentran en el dataset
    leer_dataset=csv.reader(abrir)#la variable leer_dataset contriene los datos que se encuentran en abrir
    dataset=list(leer_dataset)#la variable dataset contendra el dataset en forma de lista
    print ("Por favor ingrese los datos solicitados")#impresion con instrucciones
    print("Numero de vecinos a considerar: ",end="")#impresion con intrucciones
    numero_vecinos=int(input())#la variabl numero_vecinos contendra el numero de vecinos que evaluaremos
    os.system("cls")#limpieza de pantalla
    contador=0#variable contador     
    for i in dataset:#for que recorre el dataset en todas sus posiciones
        dataset[contador][0]=float(dataset[contador][0])#convertirmos a flotante dataset en la posicion [contador][0]
        dataset[contador][1]=float(dataset[contador][1])#convertirmos a flotante dataset en la posicion [contador][1]
        dataset[contador][2]=int(dataset[contador][2])#convertirmos a entero dataset en la posicion [contador][2]
        dataset[contador][3]=int(dataset[contador][3])#convertirmos a entero dataset en la posicion [contador][3]
        dataset[contador][4]=int(dataset[contador][4])#convertirmos a entero dataset en la posicion [contador][4]
        dataset[contador][5]=int(dataset[contador][5])#convertirmos a entero dataset en la posicion [contador][5]
        dataset[contador][6]=int(dataset[contador][6])#convertirmos a entero dataset en la posicion [contador][6]
        dataset[contador][7]=int(dataset[contador][7])#convertirmos a entero dataset en la posicion [contador][7]
        dataset[contador][8]=int(dataset[contador][8])#convertirmos a entero dataset en la posicion [contador][8]
        dataset[contador][9]=int(dataset[contador][9])#convertirmos a entero dataset en la posicion [contador][9]
        dataset[contador][10]=int(dataset[contador][10])#convertirmos a entero dataset en la posicion [contador][10]
        dataset[contador][11]=int(dataset[contador][11])#convertirmos a entero dataset en la posicion [contador][11]
        dataset[contador][12]=int(dataset[contador][12])#convertirmos a entero dataset en la posicion [contador][12]
        dataset[contador][13]=int(dataset[contador][13])#convertirmos a entero dataset en la posicion [contador][13]
        dataset[contador][14]=int(dataset[contador][14])#convertirmos a entero dataset en la posicion [contador][14]
        dataset[contador][15]=int(dataset[contador][15])#convertirmos a entero dataset en la posicion [contador][15]         
        distancia_previa=(((dataset[contador][0]-relacion_1)**2)+((dataset[contador][1]-relacion_2)**2)
        +((dataset[contador][2]-vertical_cambios)**2)+((dataset[contador][3]-vertical_numero)**2)+
        ((dataset[contador][4]-horizontal_cambios)**2)+((dataset[contador][5]-horizontal_numero)**2)+
        ((dataset[contador][6]-vertical_cambios_izquierda)**2)+((dataset[contador][7]-vertical_cambios_numeros)**2)+
        ((dataset[contador][8]-vertical_cambios_derecha)**2)+((dataset[contador][9]-vertical_cambios_derecha_numeros)**2)+
        ((dataset[contador][10]-horizontal_cambios_arriba)**2)+((dataset[contador][11]-horizontal_numero_arriba)**2)+
        ((dataset[contador][12]-horizontal_cambios_abajo)**2)+((dataset[contador][13]-horizontal_numero_abajo)**2))
        """Aplicamos la formula para obtener la distancia Euclidiana, es decir una sumatoria de cada caracteristica del dataset
        menos cada caracteristica de la imagen a clasificar"""
        raiz=math.sqrt(distancia_previa)#la segunda parte de la formula es obtener la raiz cuadrada de la sumatoria
        dataset[contador].append(raiz)#agregamos una nueva fila a nuestra matriz que contendra la raiz cuadrada de cada instancia
        contador+=1#sumamos un numero al contador    
    dataset.sort(key=lambda dataset: dataset[14],reverse=True)#aplicamos la funcion sort para ordenar el dataset de acuerdo al numero total de instancias
    print ("\t\tDataset info:\nNúmero total de instancias:", dataset [0][14],"\nTotal de caracteristicas por instancia: 14 \nTotal de clases: 10\nNombre de las clases:{0,1,2,3,4,5,6,7,8,9}")#imprimimos el numoro de primera instancia despues del sort
    dataset.sort(key=lambda dataset: dataset[16])#aplicamos nuevo sort para ordenarlo de acuerdo a la distancia  
    print("Instancia del K vecino mas cercano:", dataset[0][14])#imprimimos el numero  de la instancia con la distancia mas cercana a nuestra imagen
    print ("\nk vecinos mas cercanos:")#Impresion de pantalla
    for K_vecinos in range (0,numero_vecinos):#numero de kvecinos que deberan imprimirse
        print ("\tInstancia:", dataset[K_vecinos][14], "\tDistancia:",
               "%.5f" %dataset[K_vecinos][16], "\tClase", dataset[K_vecinos][15])#impresion de los k vecinos mas cercanos
    return dataset, numero_vecinos#valores que regresa la funcion clasificacion

"""
Nombre:      instancias
Descripción:Ordenamos e imprimimos las instancias, así como un resumen del dataset
Parámetros de entrada: Ninguno
Parámetros de Salida: Ninguno
Variables:
"""
def instancias():
    dataset,numero_vecinos=Clasificacion()#llamamos a la funcion clasificacion y los valores de retorno son almacenados en dos variables
    clase_0=0#variable de tipo int
    clase_1=0#variable de tipo int
    clase_2=0#variable de tipo int
    clase_3=0#variable de tipo int
    clase_4=0#variable de tipo int
    clase_5=0#variable de tipo int
    clase_6=0#variable de tipo int
    clase_7=0#variable de tipo int
    clase_8=0#variable de tipo int
    clase_9=0#variable de tipo int
    
    numero_filas=10#variable de tipo int
    numero_columnas=2#variable de tipo int
    clase_final = []#creamos un arreglo
    for filas in range(numero_filas):#limitaremos el numero de filas a 10
        clase_final.append([])#agregaremos mas filas a nuestas matriz
        for columnas in range(numero_columnas):#limitaremos el numero de columnas a 2
            clase_final[filas].append(None)#agregamos nuevas columnas a nuestra matriz         
    
    for caracteristica in range(0,numero_vecinos):#sumaremos el numero de vecinos que deseamos ver impresos
        if(dataset[caracteristica][15]==0):#condicion para determinar si en una posicion es igual a 0
            clase_0=clase_0+1#sumamos uno a nuestro contador         
        if(dataset[caracteristica][15]==1):#condicion para determinar si en una posicion es igual a 1
            clase_1=clase_1+1#sumamos uno a nuestro contador #sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==2):#condicion para determinar si en una posicion es igual a 2
            clase_2=clase_2+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==3):#condicion para determinar si en una posicion es igual a 3
            clase_3=clase_3+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==4):#condicion para determinar si en una posicion es igual a 4
            clase_4=clase_4+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==5):#condicion para determinar si en una posicion es igual a 5
            clase_5=clase_5+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==6):#condicion para determinar si en una posicion es igual a 6
            clase_6=clase_6+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==7):#condicion para determinar si en una posicion es igual a 7
            clase_7=clase_7+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==8):#condicion para determinar si en una posicion es igual a 8
            clase_8=clase_8+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==9):#condicion para determinar si en una posicion es igual a 9
            clase_9=clase_9+1#sumamos uno a nuestro contador 
            
    clase_final[0]=clase_0,0#llenamos nuestra matriz clse_final con los valores de la clase y el numero 0
    clase_final[1]=clase_1,1#llenamos nuestra matriz clse_final con los valores de la clase y el numero 1
    clase_final[2]=clase_2,2#llenamos nuestra matriz clse_final con los valores de la clase y el numero 2
    clase_final[3]=clase_3,3#llenamos nuestra matriz clse_final con los valores de la clase y el numero 3
    clase_final[4]=clase_4,4#llenamos nuestra matriz clse_final con los valores de la clase y el numero 4
    clase_final[5]=clase_5,5#llenamos nuestra matriz clse_final con los valores de la clase y el numero 5
    clase_final[6]=clase_6,6#llenamos nuestra matriz clse_final con los valores de la clase y el numero 7
    clase_final[7]=clase_7,7#llenamos nuestra matriz clse_final con los valores de la clase y el numero 8
    clase_final[8]=clase_8,8#llenamos nuestra matriz clse_final con los valores de la clase y el numero 9
    clase_final[9]=clase_9,9#llenamos nuestra matriz clse_final con los valores de la clase y el numero 10
    
    clase_final.sort(key=None, reverse=True)#aplicamos sort a nuestra matriz clase_final dejando al principio el numero mayor
    print ("\nNúmero de Instancias por clase:")#impresion de pantalla
    for conteo_instancias in range(0,10):#contaremos el numero de instancias
            print ("\t",clase_final[conteo_instancias][0],
            "\tInstancias de la clase:",clase_final[conteo_instancias][1]) 
    print ("\nLa imagen es el numero:", clase_final[0][1]) #impresion de pantalla del numero de instancias
