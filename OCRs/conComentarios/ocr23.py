# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 02:44:19 2016

@author: Laura
"""

from Crear_dataset import Extraccion_de_caract #manda a llamar a la clase crear_datset & a la función Extraccion_de_caracteristicas
#from knn3 import knn #manda a traer a la clase knn llamada knn3
from ClasificacionKNN import knn

print("Menu") #mensaje que muestra en la pantalla el menu
opc = int(input("1.- Crear DataSet\n2.- Clasificar una imagen\n  Opcion: ")) #menu donde 1 es = Crear DataSet y 2 Nos da la opción de clasificar una imagen
if(opc == 1): #if que entra a la opcion 1
    extrae = Extraccion_de_caract() #se crea una variable extrae encargada de mandar a traer la función de Extraccion_de_caract
    extrae.main() # manda a tarer lo de la funcion extrae  al main para crear el dataaset
    print("ups")
if(opc == 2): ##else que nos da la otra opción de todo lo que tenga clasificación
    clasificacion = knn()  #se crea una variable clasificación encargada de mandar a traer la función knn
    clasificacion.main() #manda a traer todo lo que tiene la función extrae al main

    
import csv #libreria para escribir el archivo
import math #libreria para sacar las raices
import operator #libreria para operadores
from PIL import Image #libreria que importa una imagen
import matplotlib.image as mpimg #libreria para abrir una imagen
from Crear_dataset import Extraccion_de_caract #aqui se manda a traer a crear_datset y Extraccion de caracteres

class knn(): #clase knn

    def cargarDataset(archivo): #funcion que carga el datset
        dataset = []#lee el archivo para despues comprararla
        with open(archivo, newline='') as csvfile: #abre  el archivo
            lines = csv.reader(csvfile, delimiter= ';') # lo abre y lo va separando por comas
            dataset = list(lines) #lista las isntancias del datset
            for completo in range(len(dataset)-1): #recoore "completo" 
                for acceso in range(13): #lee las 14 caracteristicas y se le resta menos uno para que ya no tome el valor de la clase
                    #print(dataset[x][y])
                    dataset[completo][acceso] = float(dataset[completo][acceso]) # lo comvierte a entero un ejemplo seria si esta asi "1" y lo pasa a asi 1
                dataset.append(dataset[completo])
        csvfile.close() #cieera el archivo
        return dataset #regresa lo que tenga el arreglo

    def euclideanDistance(instance1, instance2, length): #funcion que calcula la distancia euclidiana
        distancia = 0 # variable que inica con cero
        for indice in range(length):
            distancia += pow((float(instance1[indice]) - float(instance2[indice])), 2)#resta los atributos de la nueva instancia con un elemnto del dataset y lo eleva 2
        return math.sqrt(distancia)#regresa la raiz de la distancia

    def getNeighbors(dataset,nuevaInstancia, k): #funcion que calcula los vecinos más cercanos       
        distancia = [] #arreglo creado para las distancias
        length = len(nuevaInstancia)-1#tamaño del arreglo
        for indice_dataset in range(len(dataset)):
            dist = knn.euclideanDistance(nuevaInstancia, dataset[indice_dataset], length)
            distancia.append((dataset[indice_dataset], dist))
        distancia.sort(key=operator.itemgetter(1))#ordena de menor a mayor
        print("\n****************************\n")
        print(distancia)
        neighbors = [] #arreglo donde se guardara los vecionos
        for indice in range(k): #recorrido hasta los vecinos a elegir
            neighbors.append(distancia[indice][0])# obtener la distancia
            print("Instancia: "+ str(distancia[indice][0][15]) + " Clase: "+ str(distancia[indice][0][14]) + " Distancia: " + str(distancia[indice][1]))
            #print("\n		Vecinos:  "+str(distancia[indice]))#nos muestra el numero de vecinos con sus caracteristicas, su clase y la linea donde se encunetra
        return neighbors # la función nos regresa a los vecinos más cercanos

    def getResponse(neighbors):  #función que hace la clasificación de los vecinos más cercanos
        classVotes = {} 
        for indice in range(len(neighbors)):
            response = neighbors[indice][-2] 
            if response in classVotes:
                classVotes[response] += 1 #hace la votación
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]

    def obtenerCaract(self,ruta): #función encargada para obtener las caracteristicas 
        data = []#se declara arreglo para guardar las caaracteristicas
        img = Image.open(ruta) #Abre imagen
        img2 = mpimg.imread(ruta) #Abre imagen
        columnas, filas = img.size #Se obtienen las filas y columnas

        #Se insertan datos en el array data
        data.extend(Extraccion_de_caract.vectoresImg(img2,filas,columnas))#manda a traer a la función de extracción de caracteristicas y al metodo de vectores
        data.extend(Extraccion_de_caract.cortes(img2,filas,columnas)) #manda a traer a la función de extracción de caracteristicas y al metodo de vectores
        data.append(Extraccion_de_caract.razonFC(columnas,filas)) #manda a traer a la función de extración de caracteristicas  y al metodo fe RazonFC
        data.append(Extraccion_de_caract.razon_1_img(columnas,filas,img2)) #manda a traer una funcion extración de caracteres y al  metodo razón
        return data

    def __init__(self): #constructor 
        pass

    def main(self):
        data =[] #arreglo declarado para sacar la clasificación de una image
        trainingSet = []#aqui se guarda el dataset
        trainingSet = knn.cargarDataset('dataset.csv') #se carga la clase cargarDataset 
        input("Se finalizo la carga de dataset, presione ENTER para continuar... : ") #mensaje en pantalla para continuar
        ruta = 'C:/Users/Paul/Desktop/OCR/ocrD/test/' #ruta donde se obtendra la imagen a clasificar
        ruta += input("Ingresa el nombre de la imagen: ") #mensaje que muestra para escribir la ruta
        data = knn.obtenerCaract(self,ruta) #en la clase knn se manda a traer al método obtener_Caract 
        k = int(input("Ingresa el numero K: ")) #mensaje que muestra en pantalla para poner cuantos vecinos queremos encontrar
        resultado = knn.getResponse(knn.getNeighbors(trainingSet,data,k))
        print("\n   La imagen es un: "+str(resultado)) #mensaje que nos devuelve que imagen es
        del trainingSet[:]#eliminar todo el contenido del arreglo trainingSet
        del data[:]
        
        
import csv #libreria para escribir el archivo
import math #libreria para sacar las raices
import operator #libreria para operadores
from PIL import Image #libreria que importa una imagen
import matplotlib.image as mpimg #libreria para abrir una imagen
from Crear_dataset import Extraccion_de_caract #aqui se manda a traer a crear_datset y Extraccion de caracteres

class knn(): #clase knn
    """
    * Metodo: cargarDataset
    * Argumentos: ruta del archivo
    * Retorno: dataset cargado
    * Funcionamiento: abre el archivo que recibe como parametro y lo guarda en un arreglo
    """
    def cargarDataset(archivo):#funcion que carga el datset
        trainingSet = []#lee el archivo para despues comprararla
        with open(archivo, newline='') as csvfile:#abre  el archivo
            lines = csv.reader(csvfile, delimiter= ';')# lo abre y lo va separando por comas
            dataset = list(lines)#lista las isntancias del datset
            for completo in range(len(dataset)-1):#recoore "completo"
                for acceso in range(13):#lee las 14 caracteristicas y se le resta menos uno para que ya no tome el valor de la clase
                    #print(dataset[x][y])
                    dataset[completo][acceso] = float(dataset[completo][acceso])# lo comvierte a entero un ejemplo seria si esta asi "1" y lo pasa a asi 1
                trainingSet.append(dataset[completo])
        csvfile.close()#cieera el archivo
        return trainingSet#regresa lo que tenga el arreglo
    """
    * Metodo: euclidianDistance
    * Argumentos: dataset, nueva instancia y el tamaño
    * Retorno: distancia entre las dos instancias recibidas
    * Funcionamiento: mide la distancia de las instancias usando las caracteristicas de cada instancia
    """
    def euclideanDistance(instance1, instance2, length): #funcion que calcula la distancia euclidiana
        distance = 0 # variable que inica con cero
        for x in range(length):
            distance += pow((instance1[x] - instance2[x]), 2)#resta los atributos de la nueva instancia con un elemnto del dataset y lo eleva 2
        return math.sqrt(distance)#regresa la raiz de la distancia
    """
    * Metodo: getNeighbors
    * Argumentos: dataset, nueva instancia, numero k
    * Retorno: los k vecinos mas cercanos
    * Funcionamiento: mide la distancia de la nueva instancia con todos los elementos del dataset y devuelve los k vecinos mas cercanos
    """
    def getNeighbors(trainingSet,testInstance, k): #funcion que calcula los vecinos más cercanos       
        distances = [] #arreglo creado para las distancias
        length = len(testInstance)-1#tamaño del arreglo
        for x in range(len(trainingSet)):
            dist = knn.euclideanDistance(testInstance, trainingSet[x], length)
            distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))#ordena de menor a mayor
        neighbors = []#arreglo donde se guardara los vecionos
        for x in range(k):#recorrido hasta los vecinos a elegir
            print("Linea(Instancia): "+str(distances[x][0][15])+ " Clase: "+str(distances[x][0][14])+" Distancia: "+str(distances[x][1]))#impresion de informacion de la clasificacion
            neighbors.append(distances[x][0])# obtener la distancia
        return neighbors# la función nos regresa a los vecinos más cercanos

    """
    * Metodo: gerResponse
    * Argumentos: k vecinos mas cercanos
    * Retorno: la clase dominante
    * Funcionamiento: recibe los k vecinos, hace un recorrido contando las clases, las ordena y regresa la clase mayor
    """
    def getResponse(neighbors):#la siguiente funcion hace la votacion de la clase que mas se repite
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-2]#se obtiene la clase
            if response in classVotes:#si se encuentra la clase, incrementa contador
                classVotes[response] += 1
            else:
                classVotes[response] = 1#si no iguala a 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)#ordena de mayor a menor
        return sortedVotes[0][0]#regresa la clase mayoria
    """
    * Metodo: obtenerCaract
    * Argumentos: ruta del archivo
    * Retorno: caracteristicas de la imagen
    * Funcionamiento: abre el archivo que recibe como parametro y obtiene las 14 caracteristicas
    """
    def obtenerCaract(self,ruta): #función encargada para obtener las caracteristicas 
        data = []#se declara arreglo para guardar las caaracteristicas
        img = Image.open(ruta) #Abre imagen
        img2 = mpimg.imread(ruta) #Abre imagen
        columnas, filas = img.size #Se obtienen las filas y columnas
        #Se insertan datos en el array data
        data.extend(Extraccion_de_caract.vectoresImg(img2,filas,columnas))#manda a traer a la función de extracción de caracteristicas y al metodo de vectores
        data.extend(Extraccion_de_caract.cortes(img2,filas,columnas)) #manda a traer a la función de extracción de caracteristicas y al metodo de vectores
        data.append(Extraccion_de_caract.razonFC(columnas,filas)) #manda a traer a la función de extración de caracteristicas  y al metodo fe RazonFC
        data.append(Extraccion_de_caract.razon_1_img(columnas,filas,img2)) #manda a traer una funcion extración de caracteres y al  metodo razón
        return data

    def __init__(self):
        pass
    """
    * Metodo: main
    * Argumentos: NoAplica
    * Retorno: NoAplica
    * Funcionamiento: controla el flujo del programa
    """
    def main(self):
        trainingSet = []#variable para el dataset
        data =[]#variable para las caracteristicas de la imagen
        trainingSet = knn.cargarDataset('dataset.csv')#se carga el dataset y se guarda en el traingset
        input("Se finalizo la carga de dataset, presione ENTER para continuar... : ")
        ruta = 'C:/Users/Paul/Desktop/OCR/ocrD/test/'#path de imagenes de prueba
        ruta += input("Ingresa el nombre de la imagen: ")#se pide nombre de imagen a usuario
        data = knn.obtenerCaract(self,ruta)#se obtienen caracteristicas de la nueva imagen
        k = int(input("Ingresa el numero K: "))#se solicita el numero K
        resultado = knn.getResponse(knn.getNeighbors(trainingSet,data,k))#se realiza la clasificación
        print("\n   La imagen es un: "+str(resultado))#se imprime resultado
        del trainingSet[:]#re borra dataset para nueva clasificación
        