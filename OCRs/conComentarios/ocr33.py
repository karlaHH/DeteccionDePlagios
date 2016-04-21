# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 16:21:44 2016

@author: Oscar
"""

#Biblioteca para escribir datos en un archivo csv
import csv
#Biblioteca para funciones matemáticas
import math
#Importacion de el archivo ocr_dataset
import ocr_dataset as caracteristicasimg

#Nombre: nuevaInstancia
#Desc: Metodo para obtener caracteristicas de la nueva instancia
#Párametro: ruta de la imagen
#Regresa: Regresa las caracteristicas de la nueva instancia
def nuevaInstanciaK(ruta, k):
    
    #Llamar la funcion de matriz imagen para obtener el numero de filas y columnas
    (img2, filas, columnas) = caracteristicasimg.matrizimagen(ruta)
    #LLamar la funcion de Razon filas columnas
    razonfilascolumnas = caracteristicasimg.razon_filascolumnas(filas, columnas)
    #Llamar la funcion unoscerosimagen para calcula cuantos 1s hay respecto al área del imagen
    razonunos = caracteristicasimg.unosimagen(img2, filas, columnas)
    #Llamar la funcion vectorcuartovertical para calcular la razon del numero de unos / tamaño del vector1/4 vertical
    razonunoscuartovertical = caracteristicasimg.vectorcuartovertical(img2, filas, columnas)
    #Llamar la funcion vectorcuartohorizontal para calcular la razon del numero de unos / tamaño del vector1/4 horizontal
    razonunoscuartohorizontal = caracteristicasimg.vectorcuartohorizontal(img2, filas, columnas)
    #Llamar la funcion vectormitadvertical para calcular la razon del numero de unos / tamaño del vector1/2 vertical
    razonunosmitadvertical = caracteristicasimg.vectormitadvertical(img2, filas, columnas)
    #Llamar la funcion vectormitadhorizontal para calcular la razon del numero de unos / tamaño del vector1/2 horizontal
    razonunosmitadhorizontal = caracteristicasimg.vectormitadhorizontal(img2, filas, columnas)
    #Llamar la funcion vectortrescuartosvertical para calcular la razon del numero de unos / tamaño del vector3/4 vertical
    razonunostrescuartosvertical = caracteristicasimg.vectortrescuartosvertical(img2, filas, columnas)
    #Llamar la funcion vectortrescuartoshorizontal para calcular la razon del numero de unos / tamaño del vector3/4 horizontal
    razonunostrescuartoshorizontal = caracteristicasimg.vectortrescuartoshorizontal(img2, filas, columnas)
    #Llamar la funcion cortesvertical para calcula cuantas veces corta al número la línea a un cuarto vertical
    cortescuartovertical = caracteristicasimg.lineacuartovertical(img2, filas, columnas)
    #Llamar la funcion lineacuartohorizontal para calcula cuantas veces corta al número la línea a un cuarto horizontal
    cortescuartohorizontal = caracteristicasimg.lineacuartohorizontal(img2, filas, columnas)
    #Llamar la funcion lineamitadvertical para calcula cuantas veces corta al número la línea a la mitad vertical
    cortesmitadvertical = caracteristicasimg.lineamitadvertical(img2, filas, columnas)
    #Llamar la funcion lineamitadhorizontal para calcula cuantas veces corta al número la línea a la mitad horizontal
    cortesmitadhorizontal = caracteristicasimg.lineamitadhorizontal(img2, filas, columnas)
    #Llamar la funcion lineatrescuartosvertical para calcula cuantas veces corta al número la línea a 3/4 vertical
    cortestrescurtovertical = caracteristicasimg.lineatrescuartosvertical(img2, filas, columnas)
    #Llamar la funcion lineatrescuartoshorizontal para calcula cuantas veces corta al número la línea a 3/4 horizontal
    cortestrescuertohorizontal = caracteristicasimg.lineatrescuartoshorizontal(img2, filas, columnas)
    #Llamar la funcion cerosunoscruz para calcula cuantos 1s y 0s hay en forma de cruz respecto al área de la imagen
    razonunoscruz = caracteristicasimg.cerosunoscruz(img2, filas, columnas)
    
    #Arreglo con las caracteristicas calculadas
    nuevainstancia = [razonfilascolumnas,razonunos,razonunoscuartovertical,razonunoscuartohorizontal,razonunosmitadvertical,razonunosmitadhorizontal,razonunostrescuartosvertical,razonunostrescuartoshorizontal,cortescuartovertical,cortescuartohorizontal,cortesmitadvertical,cortesmitadhorizontal,cortestrescurtovertical,cortestrescuertohorizontal,razonunoscruz,k]
    
    #Regresa las caracteristicas obtenidas de la nueva instacia
    return nuevainstancia

#Nombre: cargarDataset
#Desc: Metodo para cargar el archivo dataset
#Párametro: nombrearchivo
#Regresa: Regresa el dataset
def cargarDataset(nombrearchivo):
	#Abrir el archivo csv con permisos de leer
    with open(nombrearchivo, 'r') as csvfile:
    	#Leer un archivo con reader()
        lineas = csv.reader(csvfile)
        #Obtener lista de de cada instancia
        dataset = list(lineas)
        #Recorrer cada instancia obtenida
        for x in range(len(dataset)):
        	#Ciclo para recorrer cada caraacteristica de la instancia
            for y in range(16):
            	#Condicion para verificar el tamaño de las caracteristicas
                if(y<15):
                	#Convierte los valores del dataset en flotantes
                    dataset[x][y] = float(dataset[x][y])
                else:
                	#Guarda el valor de la clase
                    dataset[x][y] = dataset[x][y]
                #print(dataset[x][y])
    #Regresa el dataset cargado en un arreglo
    return dataset

#Nombre: calcularDistancia
#Desc: Metodo para calcular la distancia eucladiana de la nueva instancia con el dataset
#Párametro: dataset y la nueva instancia
#Regresa: Regresa la distancia calculada
def calcularDistancia(dataset,nuevainstancia):
	#Arreglo para guardar las distancias calculadas
    distancias = []
    #Ciclo para 
    for x in range(len(dataset)):
        distancias.append([math.sqrt(pow((dataset[x][0] - float(nuevainstancia[0])),2)+pow((dataset[x][1]-float(nuevainstancia[1])),2)+pow((dataset[x][2]-float(nuevainstancia[2])),2)+pow((dataset[x][3]-float(nuevainstancia[3])),2)+pow((dataset[x][4]-float(nuevainstancia[4])),2)+pow((dataset[x][5]-float(nuevainstancia[5])),2)+pow((dataset[x][6]-float(nuevainstancia[6])),2)+pow((dataset[x][7]-float(nuevainstancia[7])),2)+pow((dataset[x][8]-float(nuevainstancia[8])),2)+pow((dataset[x][9]-float(nuevainstancia[9])),2)+pow((dataset[x][10]-float(nuevainstancia[10])),2)+pow((dataset[x][11]-float(nuevainstancia[11])),2)+pow((dataset[x][12]-float(nuevainstancia[12])),2)+pow((dataset[x][13]-float(nuevainstancia[13])),2)+pow((dataset[x][14]-float(nuevainstancia[14])),2)),dataset[x][15],(x+1)])
    #print(distancias)
    #Variable auxiliar para guardar el valor de la distancia
    auxiliar = 0
    #Variable para almacenar el tamaño del arreglo distancias
    tamaño = len(distancias)
    #Ciclo para recorrer el tamaño del arreglo
    for i in range(1, tamaño):
    	#Ciclo para recorrer las instancias
        for j in range(0,tamaño-1):
        	#Verifica el tmaño de la instancia actual
            if(distancias[j]>distancias[j+1]):
            	#Guarda el valor de la instacia posterior
               	auxiliar = distancias[j+1]
               	#Iguala el valor de la distancia posterior a la actual
               	distancias[j+1] = distancias[j]
               	#Iguala el valor de la distancia actual a la auxiliar
               	distancias[j] = auxiliar
    #Regresa las distancias ordenadas ascendentes
    return distancias     

#Nombre: clasificarInstancia
#Desc: Metodo para clasificar la nueva instancia
#Párametro: distancias y la nueva instancia
#Regresa: Regresa la distancia calculada
def clasificarInstancia(distancias,nuevainstancia):
    #Contadores para el numero de veces que se repite la clase
    clase0 = 0
    clase1 = 0
    clase2 = 0
    clase3 = 0
    clase4 = 0
    clase5 = 0
    clase6 = 0
    clase7 = 0
    clase8 = 0
    clase9 = 0
    #Arreglo para guardar los contadores
    totalclase = []
    print('\n')
    #Mensaje en pantalla de las columnas...
    print("\t  K\t     Distancias      Clase  Id") 
    print("\t___________________________________________")
    #Variable para contsar el numero de k vecinos
    contador = 1
    #Ciclo para recorrer el arreglo de la nueva instancia
    for x in range(int(nuevainstancia[15])):
    	#Imprime en pantalla las distancias k vecinas más cercanas
        print('\tI - '+str(contador)+' =\t'+str(distancias[x]))
        #Verifica si la clase es igual a 0
        if(distancias[x][1] == '0'):
            #Aumenta la clase 0 en uno
            clase0 += 1
        #Verifica si la clase es igual a 1
        if(distancias[x][1] == '1'):
            #Aumenta la clase 1 en uno
            clase1 += 1
        #Verifica si la clase es igual a 2
        if(distancias[x][1] == '2'):
            #Aumenta la clase 2 en uno
            clase2 += 1
        #Verifica si la clase es igual a 3
        if(distancias[x][1] == '3'):
            #Aumenta la clase 3 en uno
            clase3 += 1
        #Verifica si la clase es igual a 4
        if(distancias[x][1] == '4'):
            #Aumenta la clase 4 en uno
            clase4 += 1
        #Verifica si la clase es igual a 5
        if(distancias[x][1] == '5'):
            #Aumenta la clase 5 en uno
            clase5 += 1
        #Verifica si la clase es igual a 6
        if(distancias[x][1] == '6'):
            clase6 += 1
        #Verifica si la clase es igual a 7
        if(distancias[x][1] == '7'):
            #Aumenta la clase 7 en uno
            clase7 += 1
        #Verifica si la clase es igual a 8
        if(distancias[x][1] == '8'):
            #Aumenta la clase 8 en uno
            clase8 += 1
        #Verifica si la clase es igual a 9
        if(distancias[x][1] == '9'):
            #Aumenta la clase 9 en uno
            clase9 += 1
        #Aumenta el contador de k vecinos
        contador += 1
    #Guarda los contadores de las clases en un arreglo
    totalclase = [clase0, clase1,clase2,clase3,clase4,clase5,clase6,clase7,clase8,clase9]
    print("\n")
    #Variable auxiliar para valor de la clase
    auxiliar = 0
    #Ciclo para recorrer el arreglo totalclase
    for x in range(len(totalclase)):
        #Mensaje en pantalla de cuants veces se repite la clase
        print('\t\tTotal de la Clase '+str(x)+' = '+str(totalclase[x]))
        #Condicion para verificar las veces que se repite la clase
        if(auxiliar <= totalclase[x]):
            #Guarda el valor de la clase que mas se repite
            auxiliar = totalclase[x]
            #Guarda la identidad de la clase
            claseidentidad = x
    #Mensaje en pantalla del caracter identificado
    print('\n\t\tCaracter Identificado: ' + str(claseidentidad))

#Nombre: main
#Desc: Metodo principal del programa
#Argumentos: No tiene argumentos de netrada
def main():
    #Mensaje en pantalla
    k=int(input("\t        Escribe el numero de k: "))
    imagen = str(input("\t     Escribe el numero de la imagen: "))
    print("\n\n\t      Identificando caracteristicas!")
    #Se define la ruta de la imagen
    ruta = 'C:/Users/user/Documents/8 cuatrimestre/Mineria de Datos/ocr/test/' + imagen + '.png'
    #Llama al metodo nuevainstancia y le manda como parametro la ruta de la imagen
    nuevainstancia = nuevaInstanciaK(ruta, k)
    #Llama al metodo cargarDataset y le manda como parametro el nombre del dataset
    dataset = cargarDataset('dataset.csv')
    #Se obtiene el tamaño de instancias en el dataset
    tam = len(dataset)
    print("\t\tInformacion General")
    #Mensaje en pantalla total de instancias
    print("\n\t        Total de intancias: "+str(tam))
    #Mensaje en pantalla de total de caracteristicas
    print("\tTotal de caracteristicas por Instancia: 14")
    print("\tTotal de clases: 10")
    print("\tNombres de las clases {0,1,2,3,4,5,6,7,8,9}")
    #Llama al metodo calcularDistancia para calcular la distancia entre el dataset y la nueva instancia
    distancia = calcularDistancia(dataset,nuevainstancia)
    #Llamar al metodo clasificarInstancia para clasificar la nueva instancia 
    clasificarInstancia(distancia,nuevainstancia)

#clasificarInstancia(calcularDistancia(cargarDataset('dataset.csv'),nuevainstancia),nuevainstancia)
main()


# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 10:45:11 2016

@author: Oscar
"""
#Biblioteca de imagenes en Python
from PIL import Image
#Biblioteca para generar matriz de la imagen
import matplotlib.image as mpimg
#Biblioteca para recorrer archivos en un árbol de directorios
import os
#Biblioteca para escribir datos en un archivo csv
import csv

#Nombre: matrizimagen
#Desc: Metodo para obtener la matriz de la imagen
#Argumentos: nombre de la imagen
#Regresa: matriz y tamaño de las filas y columnas
def matrizimagen(nombre):
    #Carga la imagen en la variable img
    img = Image.open(nombre)
    #Carga la imagen en forma de matriz
    img2 = mpimg.imread(nombre)
    #Se optiene el tamaño de la imagen
    columnas, filas = img.size
    #regresa matriz de la imagen y filas y columnas
    return img2, filas, columnas

#Nombre: razon_filascolumnas
#Desc: Metodo para calcular la razon entre filas y columnas
#Argumentos: filas y columnas
#Regresa: razon filas/columnas
def razon_filascolumnas(filas, columnas):
    #Variable para guardar la razon de filas y columnas
    razonfilascolumnas = 0
    #Caracteristica 1.. Calcula la razón de Filas/Columnas
    razonfilascolumnas = filas/columnas
    #Regresa razon  de las filas entre las columnas
    return razonfilascolumnas

#Nombre: unoscerosimagen
#Desc: Metodo para calcula cuantos 1s y 0s hay respecto al área del imagen
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos y razon de ceros respecto al area
def unosimagen(img2, filas, columnas):
    #Contadores de unos
    contadoruno = 0
    #Contadores de razon de unos y ceros respecto al área
    razonunos = 0
    #Ciclo para recorer las filas de la matriz
    for x in range(filas):
        #Ciclo para recorer las columnas de la matriz
        for y in range(columnas):
            #Condición para verificar el pixel igual a 0
            if(img2[x][y] == 1):
                contadoruno = contadoruno + 1
    #Guarda la razón entre el numero de 1s respecto al área de la imagen
    razonunos = contadoruno/(filas*columnas)
#            print(razon1)
    #Regresa la razon de unos y ceros
    return razonunos

#Nombre: vectorcuartovertical
#Desc: Metodo para calcula cuantos unos hay en el vector 1/4 vertical respecto asu tamaño 
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos / tamaño del vector
def vectorcuartovertical(img2, filas, columnas):
    #Contador para el numero de unos en el vector
    contadorunos = 0
    #Variable par el tamaño del vector
    sizevector = 0
    #Variable para guardar la razon del numero de unos / tamaño del vector
    razonunoscuartovertical = 0
    #Calcula la línea a 1/4 vertical de la imagen
    cuartovectorvertical = int(columnas/4)
    #Ciclo para recorre la linea vertical calculada
    for x in range(filas):
        #Condición para verificar el pixel igual a 0 
        if(img2[x][cuartovectorvertical] == 1):
            #Aumenta el contador de los 1s
            contadorunos += 1
    #Obtiene el tamaño del vector
    sizevector = filas
    #Guarda la razon de el numero de unos / el tamaño del vector
    razonunoscuartovertical = contadorunos/sizevector
#    print(razonunoscuartovertical)
    #Regresa el numero de cortes en a 1/4 vertical
    return razonunoscuartovertical

#Nombre: vectorcuartohorizontal
#Desc: Metodo para calcular el numero de unos en el vector 1/4 horizontal respecto asu tamaño
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos / tamaño del vector
def vectorcuartohorizontal(img2, filas, columnas):
    #Contador del numero de unos en el vector
    contadorunos = 0
    #Varible para guadar el tamaño del vector
    sizevector = 0
    #Variable para guadar la razon del numero de unos / tamaño del vector
    razonunoscuartohorizontal = 0
    #Calcula la línea a 1/4 horizaontal de la imagen
    cuartovectorhorizontal = int(filas/4)
    #Recorre la línea horizontal de la imagen
    #Ciclo para recorre la linea horizontal calculada
    for x in range(columnas):
        #Condición para verificar el pixel igual a 0
        if(img2[cuartovectorhorizontal][x]==1):
            #Aumenta el contador de los 1s
            contadorunos += 1
#            print(corteshc)
    sizevector = columnas
    #Guarda la razon de el numero de unos / el tamaño del vector
    razonunoscuartohorizontal = contadorunos/sizevector
    #Regresa el numero de cortes en a 1/4 horizontal
    return razonunoscuartohorizontal

#Nombre: vectormitadvertical
#Desc: Metodo para calcula la razon de numero de unos que hay en el vector 1/2 / el vector
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos / tamaño del vector
def vectormitadvertical(img2, filas, columnas):
    #Contador para el numero de unos en el vector
    contadorunos = 0
    #Variable par el tamaño del vector
    sizevector = 0
    #Variable para guardar la razon del numero de unos / tamaño del vector
    razonunosmitadvertical = 0
    #Calcula la línea a 1/2 vertical de la imagen
    mitadvectorvertical = int(columnas/2)
    #Ciclo para recorre la linea vertical calculada
    for x in range(filas):
        #Condición para verificar el pixel igual a 0 
        if(img2[x][mitadvectorvertical] == 1):
            #Aumenta el contador de los 1s
            contadorunos += 1
    #Obtiene el tamaño del vector
    sizevector = filas
    #Guarda la razon de el numero de unos / el tamaño del vector
    razonunosmitadvertical = contadorunos/sizevector
#    print(razonunoscuartovertical)
    #Regresa el numero de cortes en a 1/2 vertical
    return razonunosmitadvertical
    
#Nombre: vectormitadhorizontal
#Desc: Metodo para calcula cuantas veces corta al número la línea a la mitad horizontal
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos / tamaño del vector
def vectormitadhorizontal(img2, filas, columnas):
    #Contador del numero de unos en el vector
    contadorunos = 0
    #Varible para guadar el tamaño del vector
    sizevector = 0
    #Variable para guadar la razon del numero de unos / tamaño del vector
    razonunosmitadhorizontal = 0
    #Calcula la línea a 1/4 horizaontal de la imagen
    mitadvectorhorizontal = int(filas/2)
    #Recorre la línea horizontal de la imagen
    #Ciclo para recorre la linea horizontal calculada
    for x in range(columnas):
        #Condición para verificar el pixel igual a 0
        if(img2[mitadvectorhorizontal][x]==1):
            #Aumenta el contador de los 1s
            contadorunos += 1
#            print(corteshc)
    sizevector = columnas
    #Guarda la razon de el numero de unos / el tamaño del vector
    razonunosmitadhorizontal = contadorunos/sizevector
    #Regresa el numero de cortes en a 1/2 horizontal
    return razonunosmitadhorizontal

#Nombre: vectortrescuartosvertical
#Desc: Metodo para calcula el numero de unos en el vector 3/4 / el tamaño del vector
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos / tamaño del vector
def vectortrescuartosvertical(img2, filas, columnas):
    #Contador para el numero de unos en el vector
    contadorunos = 0
    #Variable par el tamaño del vector
    sizevector = 0
    #Variable para guardar la razon del numero de unos / tamaño del vector
    razonunostrescuartosvertical = 0
    #Calcula la línea a 1/2 vertical de la imagen
    trescuartosvectorvertical = int(columnas/2)
    #Ciclo para recorre la linea vertical calculada
    for x in range(filas):
        #Condición para verificar el pixel igual a 0 
        if(img2[x][trescuartosvectorvertical] == 1):
            #Aumenta el contador de los 1s
            contadorunos += 1
    #Obtiene el tamaño del vector
    sizevector = filas
    #Guarda la razon de el numero de unos / el tamaño del vector
    razonunostrescuartosvertical = contadorunos/sizevector
#    print(razonunoscuartovertical)
    #Regresa el numero de cortes en a 3/4 vertical
    return razonunostrescuartosvertical

#Nombre: vectortrescuartoshorizontal
#Desc: Metodo para calcula el numero de unos en le vector 3/4 / el tamaño del vector
#Argumentos: matriz, filas y columnas
#Regresa: razon de unos / tamaño del vector
def vectortrescuartoshorizontal(img2, filas, columnas):
   #Contador del numero de unos en el vector
    contadorunos = 0
    #Varible para guadar el tamaño del vector
    sizevector = 0
    #Variable para guadar la razon del numero de unos / tamaño del vector
    razonunostrescuartoshorizontal = 0
    #Calcula la línea a 1/4 horizaontal de la imagen
    trescuartosvectorhorizontal = int(filas/2)
    #Recorre la línea horizontal de la imagen
    #Ciclo para recorre la linea horizontal calculada
    for x in range(columnas):
        #Condición para verificar el pixel igual a 0
        if(img2[trescuartosvectorhorizontal][x]==1):
            #Aumenta el contador de los 1s
            contadorunos += 1
#            print(corteshc)
    sizevector = columnas
    #Guarda la razon de el numero de unos / el tamaño del vector
    razonunostrescuartoshorizontal = contadorunos/sizevector
    #Regresa el numero de cortes en a 3/4 horizontal
    return razonunostrescuartoshorizontal

#Nombre: lineacuartovertical
#Desc: Metodo para calcula cuantas veces corta al número la línea a un cuarto vertical
#Argumentos: matriz, filas y columnas
#Regresa: numero de cortes
def lineacuartovertical(img2, filas, columnas):
    #Contadores para numero de cortes
    contadorcortes1 = 0
    contadorcortes0 = 0
    cortescuartovertical = 0
    fila = 0
    #Calcula la línea a 1/4 vertical de la imagen
    cc = int(columnas/4)
    #Recorre la linea vertical seleccionada
    for x in range(filas):
        #Guarda el valor del pixel actual
        contadorcortes1 = img2[x][cc]
        #Condición para verificar el rango de la fila
        if(x<filas-1):
            #Guarda el valor del pixel posterior
            contadorcortes0 = img2[x+1][cc]
            #Condición para verificar el corte de la imagen
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (fila==0 and img2[0][cc]==1)):
                #Aumenta el número de cortes a la imagen
                cortescuartovertical = cortescuartovertical + 1
                #Aumenta el número de la fila
                fila = fila + 1
#            print(cortesvc)
    #Regresa el numero de cortes en a 1/4 vertical
    return cortescuartovertical

#Nombre: lineacuartohorizontal
#Desc: Metodo para calcula cuantas veces corta al número la línea a un cuarto horizontal
#Argumentos: matriz, filas y columnas
#Regresa: numero de cortes
def lineacuartohorizontal(img2, filas, columnas):
    #Contadores de numero de cortes
    contadorcortes1 = 0
    contadorcortes0 = 0
    #Contador de numero de cortes en la imagen
    cortescuartohorizontal = 0
    #Contador de columna
    columna = 0
    #Calcula la línea a 1/4 horizaontal de la imagen
    cr = int(filas/4)
    #Recorre la línea horizontal de la imagen
    for x in range(columnas):
        #Guarda el valor del pixel actual
        contadorcortes1 = img2[cr][x]
        #Condición para verificar el rango de la columna
        if(x<columnas-1):
            #Guarda el valor del pixel posterior
            contadorcortes0 = img2[cr][x+1]
            #Condición para verificar el corte de la imagen
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (columna==0 and img2[cr][0]==1)):
                #Aumenta el número de cortes a la imagen
                cortescuartohorizontal = cortescuartohorizontal + 1
                #Aumenta el número de la columna
                columna = columna + 1
#            print(corteshc)
    #Regresa el numero de cortes en a 1/4 horizontal
    return cortescuartohorizontal

#Nombre: lineamitadvertical
#Desc: Metodo para calcula cuantas veces corta al número la línea a la mitad vertical
#Argumentos: matriz, filas y columnas
#Regresa: numero de cortes
def lineamitadvertical(img2, filas, columnas):
    #Contadores de numeros de cortes
    contadorcortes1 = 0
    contadorcortes0 = 0
    #Contador de numero de cortes en la imagen
    cortesmitadvertical = 0
    #Contador de numero de fila
    fila = 0
    #Calcula la línea a 1/2 vertical de la imagen
    medc = int(columnas/2)
    #Recorre la linea vertical seleccionada
    for x in range(filas):
        #Guarda el valor del pixel actual
        contadorcortes1 = img2[x][medc]
        #Condición para verificar el rango de la fila
        if(x<filas-1):
            #Guarda el valor del pixel posterior
            contadorcortes0 = img2[x+1][medc]
            #Condición para verificar el corte de la imagen
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (fila==0 and img2[0][medc]==1)):
                #Aumenta el número de cortes a la imagen
                cortesmitadvertical = cortesmitadvertical + 1
                #Aumenta el número de la fila
                fila = fila + 1
#            print(cortesvmit)
    #Regresa el numero de cortes en a 1/2 vertical
    return cortesmitadvertical

#Nombre: lineamitadhorizontal
#Desc: Metodo para calcula cuantas veces corta al número la línea a la mitad horizontal
#Argumentos: matriz, filas y columnas
#Regresa: numero de cortes
def lineamitadhorizontal(img2, filas, columnas):
    #Contadores de los cortes de unos y ceros
    contadorcortes1 = 0
    contadorcortes0 = 0
    #Contador de numero de cortes en la imagen
    cortesmitadhorizontal = 0
    #Contador de la columna 
    columna = 0
    #Calcula la línea a 1/2 horizaontal de la imagen
    medr = int(filas/2)
    #Recorre la linea horizontal seleccionada
    for x in range(columnas):
        #Guarda el valor del pixel actual
        contadorcortes1 = img2[medr][x]
        #Condición para verificar el rango de la columna
        if(x<columnas-1):
            #Guarda el valor del pixel posterior
            contadorcortes0 = img2[medr][x+1]
            #Condición para verificar el corte de la imagen
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (columna==0 and img2[medr][0]==1)):
                #Aumenta el número de cortes a la imagen
                cortesmitadhorizontal = cortesmitadhorizontal + 1
                #Aumenta el número de la columna
                columna = columna + 1
#            print(corteshmit)
    #Regresa el numero de cortes en a 1/2 horizontal
    return cortesmitadhorizontal

#Nombre: lineatrescuartosvertical
#Desc: Metodo para calcula cuantas veces corta al número la línea a 3/4 vertical
#Argumentos: matriz, filas y columnas
#Regresa: numero de cortes
def lineatrescuartosvertical(img2, filas, columnas):
    ##Contadores de los cortes de unos y ceros
    contadorcortes1 = 0
    contadorcortes0 = 0
    #Contador de cortes en la imagen
    cortestrescurtovertical = 0
    #Contador de la fila
    fila = 0
    #Calcula la línea a 3/4 vertical de la imagen
    cc = int((columnas/4)*3)
    #Recorre la linea vertical seleccionada
    for x in range(filas):
        #Guarda el valor del pixel actual
        contadorcortes1 = img2[x][cc]
        #Condición para verificar el rango de la fila
        if(x<filas-1):
            #Guarda el valor del pixel posterior
            contadorcortes0 = img2[x+1][cc]
            #Condición para verificar el corte de la imagen
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (fila==0 and img2[0][cc]==1)):
                #Aumenta el número de cortes a la imagen
                cortestrescurtovertical = cortestrescurtovertical + 1
                #Aumenta el número de la fila
                fila = fila + 1
#            print(cortesv3c)
    #Regresa el numero de cortes en a 3/4 vertical
    return cortestrescurtovertical

#Nombre: lineatrescuartoshorizontal
#Desc: Metodo para calcula cuantas veces corta al número la línea a 3/4 horizontal
#Argumentos: matriz, filas y columnas
#Regresa: numero de cortes
def lineatrescuartoshorizontal(img2, filas, columnas):
    #Contadores de cortes de unos y ceros
    contadorcortes1 = 0
    contadorcortes0 = 0
    #Contador de numero de cortes en la imagen
    cortestrescuertohorizontal = 0
    #Contador de la columna
    columna = 0
    #Calcula la línea a 3/4 horizaontal de la imagen
    cr = int((filas/4)*3)
    #Recorre la linea horizontal seleccionada
    for x in range(columnas):
        #Guarda el valor del pixel actual
        contadorcortes1 = img2[cr][x]
        #Condición para verificar el rango de la columna
        if(x<columnas-1):
            #Guarda el valor del pixel posterior
            contadorcortes0 = img2[cr][x+1]
            #Condición para verificar el corte de la imagen
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (columna==0 and img2[cr][0]==1)):
                #Aumenta el número de cortes a la imagen
                cortestrescuertohorizontal = cortestrescuertohorizontal + 1
                #Aumenta el número de la columna
                columna = columna + 1
#            print(cortesh3c)
    #Regresa el numero de cortes en a 3/4 horizontal
    return cortestrescuertohorizontal

#Nombre: cerosunoscruz
#Desc: Metodo para calcula cuantos 1s hay en forma de cruz respecto al área de la imagen
#Argumentos: matriz, filas y columnas
#Regresa: numero de unos
def cerosunoscruz(img2, filas, columnas):
    #Contadore de ceros
    contadoruno1 = 0
    contadoruno2 = 0
    #Calcula la línea a 1/2 vertical de la imagen
    medr = int(filas/2)
    #Calcula la línea a 1/2 horizaontal de la imagen
    medc = int(columnas/2)
#            print(medr)
#            print(medc)
    #Ciclo para recorre la linea vertical calculada
    for x in range(filas):
        #Condición para verificar el pixel igual a 0 
        if(img2[x][medc]==1):
            #Aumenta el contador de los 1s
            contadoruno1 = contadoruno1 + 1
    #Ciclo para recorre la linea horizontal calculada
    for y in range(columnas):
        #Condición para verificar el pixel igual a 0
        if(img2[medr][y]==1):
            #Aumenta el contador de los 1s
            contadoruno2 = contadoruno2 + 1
    #Guarda la razón entre el numero de 1s en forma de cruz respecto al área de la imagen 
    razonunoscruz = (contadoruno1 + contadoruno2)/(filas * columnas)
#            print(numt0)
#            print(numt1)
    #Regresa el el total de unos y ceros
    return razonunoscruz
    
#Nombre: Dataset
#Desc: Metodo leer los directorios y crear dataset
#Argumentos: no tiene argumentos de entrada
def Dataset():

    #Arreglo para juntar datos para el dataset
    dataset = []

    #Ruta de directorio de las imagenes
    rootDir= './dataset/'
    #Creación del archivo csv
    f = open('dataset.csv','w',newline='')
    #Delimitación del archivo cvs a traves de una coma.
    obj = csv.writer(f,delimiter=',')    

    #Recorer los directorios dentro de rootDir
    #dirName: El siguiente directorio en el que se encontró
    #subdirList: Una lista de los subdirectorios en el directorio actual
    #fileList: Una lista de los subdirectorios en el directorio actual.
    for dirName, subdirList, fileList in os.walk(rootDir):
        #Imprime la direccion del directorio actual
        print('Identificando clase: %s' % dirName)

        #Recore cada subdirectorio
        for fname in fileList:
            #concatena y guarda en una variable la ruta de la imagen
            nombre = dirName + '/' + fname
            #Guarda el nombre de la clase actual
            numeroclase = dirName[10]
#            print(clasenum)
            
            #Llamar la funcion de matriz imagen para obtener el numero de filas y columnas
            (img2, filas, columnas) = matrizimagen(nombre)
            #LLamar la funcion de Razon filas columnas
            razonfilascolumnas = razon_filascolumnas(filas, columnas)
            #Llamar la funcion unoscerosimagen para calcula cuantos 1s hay respecto al área del imagen
            razonunos = unosimagen(img2, filas, columnas)
            #Llamar la funcion vectorcuartovertical para calcular la razon del numero de unos / tamaño del vector1/4 vertical
            razonunoscuartovertical = vectorcuartovertical(img2, filas, columnas)
            #Llamar la funcion vectorcuartohorizontal para calcular la razon del numero de unos / tamaño del vector1/4 horizontal
            razonunoscuartohorizontal = vectorcuartohorizontal(img2, filas, columnas)
            #Llamar la funcion vectormitadvertical para calcular la razon del numero de unos / tamaño del vector1/2 vertical
            razonunosmitadvertical = vectormitadvertical(img2, filas, columnas)
            #Llamar la funcion vectormitadhorizontal para calcular la razon del numero de unos / tamaño del vector1/2 horizontal
            razonunosmitadhorizontal = vectormitadhorizontal(img2, filas, columnas)
            #Llamar la funcion vectortrescuartosvertical para calcular la razon del numero de unos / tamaño del vector3/4 vertical
            razonunostrescuartosvertical = vectortrescuartosvertical(img2, filas, columnas)
            #Llamar la funcion vectortrescuartoshorizontal para calcular la razon del numero de unos / tamaño del vector3/4 horizontal
            razonunostrescuartoshorizontal = vectortrescuartoshorizontal(img2, filas, columnas)
            #Llamar la funcion cortesvertical para calcula cuantas veces corta al número la línea a un cuarto vertical
            cortescuartovertical = lineacuartovertical(img2, filas, columnas)
            #Llamar la funcion lineacuartohorizontal para calcula cuantas veces corta al número la línea a un cuarto horizontal
            cortescuartohorizontal = lineacuartohorizontal(img2, filas, columnas)
            #Llamar la funcion lineamitadvertical para calcula cuantas veces corta al número la línea a la mitad vertical
            cortesmitadvertical = lineamitadvertical(img2, filas, columnas)
            #Llamar la funcion lineamitadhorizontal para calcula cuantas veces corta al número la línea a la mitad horizontal
            cortesmitadhorizontal = lineamitadhorizontal(img2, filas, columnas)
            #Llamar la funcion lineatrescuartosvertical para calcula cuantas veces corta al número la línea a 3/4 vertical
            cortestrescurtovertical = lineatrescuartosvertical(img2, filas, columnas)
            #Llamar la funcion lineatrescuartoshorizontal para calcula cuantas veces corta al número la línea a 3/4 horizontal
            cortestrescuertohorizontal = lineatrescuartoshorizontal(img2, filas, columnas)
            #Llamar la funcion cerosunoscruz para calcula cuantos 1s y 0s hay en forma de cruz respecto al área de la imagen
            razonunoscruz = cerosunoscruz(img2, filas, columnas)
            #append añade un elemento a la final de la lista dataset
            dataset.append([razonfilascolumnas,razonunos,razonunoscuartovertical,razonunoscuartohorizontal,razonunosmitadvertical,razonunosmitadhorizontal,razonunostrescuartosvertical,razonunostrescuartoshorizontal,cortescuartovertical,cortescuartohorizontal,cortesmitadvertical,cortesmitadhorizontal,cortestrescurtovertical,cortestrescuertohorizontal,razonunoscruz,numeroclase])
#        print(dataset)

    #Agrega una nueva línea despues de cada línea
    obj.writerows(dataset)
    #Cierra el archivo csv
    f.close()
    
#Llamar la función Dataset
#Dataset()
