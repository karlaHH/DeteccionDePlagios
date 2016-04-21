# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:44:54 2016

@author: Hector HP
"""
from OCR import DataSet
from KNNFinal import knn

Data = DataSet()
KnnFinal = knn()
opc = 0
while(opc != 3):
    print("Menu")
    opc = int(input("1.- Crear Dataset\n2.- Clasificar con KNN\n3.- Salir\n  Opcion:"))
    if(opc == 1):
        Data.main()
    elif(opc == 2):
        print ("entra")
        KnnFinal.main()
    else:
        print("Programa Finalizado")
        
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:47:16 2016

@author: Hector HP
"""
from PIL import Image
import csv
import os
import matplotlib.image as mpimg
cont = 0
class DataSet():
    
    op = open('dataset.csv','a',newline='')
    escribir = csv.writer(op,delimiter=';')
    
    def Conjunto(ruta,clase):
        global cont
        #abrimos imagen
        imgPrincipal = Image.open(ruta)
        img = mpimg.imread(ruta)
        columnas, filas = imgPrincipal.size
        data=[]#arreglo para insertar en el data
        data.append(DataSet.Propiedad_1(filas,columnas))
        data.append(DataSet.Propiedad_2(img,filas,columnas))
        data.append(DataSet.Propiedad_3(img,filas,columnas))
        data.append(DataSet.Propiedad_4(img,filas,columnas))
        data.append(DataSet.Propiedad_5(img,filas,columnas))
        data.append(DataSet.Propiedad_6(img,filas,columnas))
        data.append(DataSet.Propiedad_7(img,filas,columnas))
        data.append(DataSet.Propiedad_8(img,filas,columnas))
        data.append(DataSet.Propiedad_9(img,filas,columnas))
        data.append(DataSet.Propiedad_10(img,filas,columnas))
        data.append(DataSet.Propiedad_11(img,filas,columnas))
        data.append(DataSet.Propiedad_12(img,filas,columnas))
        data.append(DataSet.Propiedad_13(img,filas,columnas))
        data.append(DataSet.Propiedad_14(img,filas,columnas))
        data.append(clase)
        data.append(cont)
        DataSet.escribir.writerow(data)#se escribe en el data
        cont += 1
        
    def Propiedad_1(filas,columnas):
        P_1=columnas/filas
        return P_1
    
    def Propiedad_2(img,filas,columnas):
        numunos=0
        for a in range(filas):
            for b in range(columnas):
                nu=(int(img[a][b]))
                if nu==1:
                    numunos=numunos+1
        unos=numunos/(filas*columnas)
        
        return unos
    
    def Propiedad_3(img,filas,columnas):
        numunos=0
        b=int(columnas/2)
        for a in range (filas):            
             nu=(int(img[a][b]))
             if nu==1:
                 numunos=numunos+1
        p3=numunos/filas
        
        return p3
    
    def Propiedad_4(img,filas,columnas):
        numunos=0
        for a in range (filas):
             b=int(columnas/4)             
             nu=(int(img[a][b]))             
             if nu==1:
                 numunos=numunos+1
        p4=numunos/filas
        
        return p4
    
    def Propiedad_5(img,filas,columnas):
        numunos=0
        for a in range (filas):
             b=int(3*(columnas/4))
             nu=(int(img[a][b]))             
             if nu==1:
                 numunos=numunos+1
        p5=numunos/filas
        
        return p5
    
    def Propiedad_6(img,filas,columnas):
        numunos=0
        numceros=0
        a=int(filas/2)
        for b in range(columnas):            
             nu=(int(img[a][b]))             
             if nu==1:
                 numunos=numunos+1
             else:
                numceros=numceros+1
        p6=numunos/columnas
        
        return p6
    
    def Propiedad_7(img,filas,columnas):
        numunos=0
        numceros=0
        a=int(filas/4)
        for b in range(columnas):             
             nu=(int(img[a][b]))             
             if nu==1:
                 numunos=numunos+1
             else:
                numceros=numceros+1
        p7=numunos/columnas
        
        return p7
    
    def Propiedad_8(img,filas,columnas):
        numunos=0
        numceros=0
        a=int(3*(filas/4))
        for b in range(columnas):
            nu=(int(img[a][b]))             
            if nu==1:
                numunos=numunos+1
            else:
                numceros=numceros+1
        p8=numunos/columnas
        
        return p8
    
    def Propiedad_9(img,filas,columnas):
        nc_1=0
        b=int(columnas/2)
        for a in range (filas):
            if (img[a][b] != img[a-1][b] and a != filas-2 and a != 0):
                nc_1+=1
            if (a==0 or a==(filas-1)):
                if (img[a][b] == 1):
                    nc_1+=1
            
        return nc_1
    
    def Propiedad_10(img,filas,columnas):
        nc=0
        b=int(columnas/4)
        for a in range (filas):
            if (img[a][b] != img[a-1][b] and a != filas-2 and a != 0):
                nc+=1
            if (a==0 or a==(filas-1)):
                if (img[a][b] == 1):
                    nc+=1
            
        return nc
    
    def Propiedad_11(img,filas,columnas):
        nc=0
        a=int(3*(filas/4))
        for b in range (columnas):
            if (img[a][b] != img[a][b-1] and b != columnas-1):
                nc+=1
            if (b==0 or b==(columnas-1)):
                if (img[a][b] == 1):
                    nc+=1
            
        return nc
        
    def Propiedad_12(img,filas,columnas):
        nc=0
        a=int(filas/2)
        for b in range (columnas):
            if (img[a][b] != img[a][b-1] and b != columnas-1 and b!=0):
                nc+=1
            if (b==0 or b==(columnas-1)):
                if (img[a][b] == 1):
                    nc+=1
            
        return nc
    
    def Propiedad_13(img,filas,columnas):
        nc=0
        a=int(filas/4)
        for b in range (columnas):
            if (img[a][b] != img[a][b-1] and b != columnas-1 and b!=0):
                nc+=1
            if (b==0 or b==(columnas-1)):
                if (img[a][b] == 1):
                    nc+=1
            
        return nc
    
    def Propiedad_14(img,filas,columnas):
        nc=0
        a=int(3*(filas/4))
        for b in range (columnas):
            if (img[a][b] != img[a][b-1] and b != columnas-1 and b!=0):
                nc+=1
            if (b==0 or b==(columnas-1)):
                if (img[a][b] == 1):
                    nc+=1
            
        return nc
        
    
    def main(self):
        rootDir='arialSegmented'
        cont=0
        
        for base, dirs, files in os.walk(rootDir):
            if cont > 0:
                print("Obteniendo caracteristicas de: " + str(base[len(base)-1]))
                for name in files:
                    DataSet.Conjunto((str(base)+'/'+name),base[len(base)-1])
            cont += 1
        print ("Numero de imagenes examinados: 14,914")
        print ("clases: 0 1 2 3 4 5 6 7 8 9 a b c d e f g h i j k l m n o p q r s t u v w x y z")
        DataSet.op.close()#se cierra la escritura
        print("     Proceso finalizado!")
        
        def __init__(self):
            pass
        
        
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 22:49:42 2016

@author: Hector HP
"""
import csv
import math
import operator
from PIL import Image
import matplotlib.image as mpimg
from OCR import DataSet

trainingSet=[]#creamos un arreglo
class knn():#creamos una clases 
    def cargarDataset(archivo):#metodo de cargara data set
        global trainingSet#variable de un arreglo
        with open(archivo, newline='') as csvfile:#abre el archivo y recorre linea por lines
            lines = csv.reader(csvfile, delimiter= ';')#se almacena una linea y se cepara por el punto y coma
            dataset = list(lines)#lee linea por linea y lo almacena
            for x in range(len(dataset)-1):#recoere nuestra matriz
                for y in range(13):#recorre nuestra matriz
                    dataset[x][y] = float(dataset[x][y])#se almacena en la matriz dataset 
                trainingSet.append(dataset[x])
        csvfile.close()#se cierra e; archivo csv
        
    def euclideanDistance(instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((instance1[x] - instance2[x]), 2)
        return math.sqrt(distance)

    def getNeighbors(testInstance, k):
        global trainingSet
        distances=[]
        neighbors = []
        uno=0
        cero=0
        dos=0
        tres=0
        cuatro=0
        ci=0
        seis=0
        siete=0
        ocho=0
        nuevu=0
        a=0
        be=0
        c=0
        d=0
        e=0
        f=0
        g=0
        h=0
        i=0
        j=0
        ka=0
        l=0
        m=0
        n=0
        o=0
        p=0
        q=0
        r=0
        s=0
        t=0
        u=0
        v=0
        w=0
        y=0
        xe=0
        z=0

        length = len(testInstance)-1
        for x in range(len(trainingSet)):
            dist = knn.euclideanDistance(testInstance, trainingSet[x], length)
            distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))#ordena de menor a mayor
        for x in range(k):
            print("Linea(Instancia): "+str(distances[x][0][15])+ " Clase: "+str(distances[x][0][14])+" Distancia: "+str(distances[x][1]))            
            neighbors.append(distances[x][0])
            cadena=str(distances[x][0][14])
            if (cadena=='0'):
                cero+=1
                print("entra")
            elif (cadena=='1'):
                uno+=1
            elif (cadena=='2'):
                dos+=1
            elif (cadena=='3'):
                tres+=1
            elif (cadena=='4'):
                cuatro+=1
            elif (cadena=='5'):
                ci+=1
            elif (cadena=='6'):
                seis+=1
            elif (cadena=='7'):
                siete+=1
            elif (cadena=='8'):
                ocho+=1
            elif (cadena=='9'):
                nuevu+=1
            elif (cadena=='A'):
                a+=1
            elif (cadena=='B'):
                be+=1
            elif (cadena=='C'):
                c+=1
            elif (cadena=='D'):
                d+=1
            elif (cadena=='E'):
                e+=1
            elif (cadena=='F'):
                f+=1
            elif (cadena=='G'):
                g+=1
            elif (cadena=='H'):
                h+=1
            elif (cadena=='I'):
                i+=1
            elif (cadena=='J'):
                j+=1
            elif (cadena=='K'):
                ka+=1
            elif (cadena=='L'):
                l+=1
            elif (cadena=='M'):
                m+=1
            elif (cadena=='N'):
                n+=1
            elif (cadena=='O'):
                o+=1
            elif (cadena=='P'):
                p+=1
            elif (cadena=='Q'):
                q+=1
            elif (cadena=='R'):
                r+=1
            elif (cadena=='S'):
                s+=1
            elif (cadena=='T'):
                t+=1
            elif (cadena=='U'):
                u+=1
            elif (cadena=='V'):
                v+=1
            elif (cadena=='W'):
                w+=1
            elif (cadena=='Y'):
                y+=1
            elif (cadena=='X'):
                xe+=1
            elif (cadena=='Z'):
                z+=1
        print ("============================================")
        print ("Resumen de la clasificacion KNN")
        print ("============================================")
        print ("Numero de ceros encontrados:")
        print (cero)
        print ("Numero de unos encontrados:")
        print (uno)
        print ("Numero de dos encontrados:")
        print (dos)        
        print ("Numero de tres encontrados:")
        print (tres)
        print ("Numero de cuatro encontrados:")
        print (cuatro)
        print ("Numero de cinco encontrados:")
        print (ci)
        print ("Numero de seis encontrados:")
        print (seis)
        print ("Numero de siete encontrados:")
        print (siete)
        print ("Numero de ocho encontrados:")
        print (ocho)
        print ("Numero de nuevo encontrados:")
        print (nuevu)  
        print ("Numero de 'a' encontrados:")
        print (a)
        print ("Numero de 'b' encontrados:")
        print (be)
        print ("Numero de 'c' encontrados:")
        print (c)        
        print ("Numero de 'd' encontrados:")
        print (d)
        print ("Numero de 'e' encontrados:")
        print (e)
        print ("Numero de 'f' encontrados:")
        print (f)
        print ("Numero de 'g' encontrados:")
        print (g)
        print ("Numero de 'h' encontrados:")
        print (h)
        print ("Numero de 'i' encontrados:")
        print (i)
        print ("Numero de 'j' encontrados:")
        print (j)
        print ("Numero de 'k' encontrados:")
        print (ka)
        print ("Numero de 'l' encontrados:")
        print (l)
        print ("Numero de 'm' encontrados:")
        print (m)        
        print ("Numero de 'n' encontrados:")
        print (n)
        print ("Numero de 'o' encontrados:")
        print (o)
        print ("Numero de 'p' encontrados:")
        print (p)
        print ("Numero de 'q' encontrados:")
        print (q)
        print ("Numero de 'r' encontrados:")
        print (r)
        print ("Numero de 's' encontrados:")
        print (s)
        print ("Numero de 't' encontrados:")
        print (t)
        print ("Numero de 'u' encontrados:")
        print (u)
        print ("Numero de 'v' encontrados:")
        print (v)
        print ("Numero de 'w' encontrados:")
        print (w)        
        print ("Numero de 'x' encontrados:")
        print (xe)
        print ("Numero de 'y' encontrados:")
        print (y)
        print ("Numero de 'z' encontrados:")
        print (z)
        return neighbors

    def getResponse(neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-2]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]
    
    def obtenerCaract(self,ruta):#Resive 
        data = []#se declara arreglo para guardar las caaracteristicas
        imgPrincipal = Image.open(ruta) #Abre imagne
        img = mpimg.imread(ruta) #Abre imagen
        columnas, filas = imgPrincipal.size #Se obtienen las filas y columnas
    
        #Se insertan datos en el array data
        data.append(DataSet.Propiedad_1(filas,columnas))#Se acquiere la propiedad 1 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_2(img,filas,columnas))#Se adquiere la propiedad 2 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_3(img,filas,columnas))#Se adquiere la propiedad 3 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_4(img,filas,columnas))#Se adquiere la propiedad 4 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_5(img,filas,columnas))#Se adquiere la propiedad 5 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_6(img,filas,columnas))#Se adquiere la propiedad 6 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_7(img,filas,columnas))#Se adquiere la propiedad 7 de la imagen que se llama a llamar de la clase OCR        
        data.append(DataSet.Propiedad_8(img,filas,columnas))#Se adquiere la propiedad 8 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_9(img,filas,columnas))#Se adquiere la propiedad 9 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_10(img,filas,columnas))#Se adquiere la propiedad 10 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_11(img,filas,columnas))#Se adquiere la propiedad 11 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_12(img,filas,columnas))#Se adquiere la propiedad 12 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_13(img,filas,columnas))#Se adquiere la propiedad 13 de la imagen que se llama a llamar de la clase OCR
        data.append(DataSet.Propiedad_14(img,filas,columnas))#Se adquiere la propiedad 14 de la imagen que se llama a llamar de la clase OCR

        return data#Retorna el arreglo que se almacenaron las propiedades
        
    def __init__(self):
        pass
    
    def main(self):#metodo main
        global trainingSet#se declara el arreglo que almacena
        knn.cargarDataset('dataset.csv')#abre el data set que deseamos comparar
        #print(trainingSet)
        ruta = 'C:/Users/Hector HP/Desktop/OCR FINAL/comparar/'#Ruta donde estan las imagenes donde se tomaran sus caracteristicas
        ruta += input("Ingresa el nombre de la imagen: ")#Pide el nombre de la imagen con su estancion PNG
        data =knn.obtenerCaract(self,ruta)#Manda a llamar el metodo donde se odtiene las caracteristicas de la imagen
        k = int(input("Ingresa el numero K: "))#ingresa el numero de vecinos que tiene que comparar
        resultado=knn.getResponse(knn.getNeighbors(data,k))#El metodo regresa con la comparacion con los vecinos mas cercanos
        print ("============================================================")
        print("\n   La imagen es un: "+str(resultado))#Imprime la clase que se repitio mas veces
        print ("============================================================")
        del trainingSet[:]
        #print (data)
        
        
