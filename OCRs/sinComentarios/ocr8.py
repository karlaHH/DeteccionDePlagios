
 
from crearDataset import CreaData
from ClasificacionKNN import knn
from colorama import Fore, Back

objeto1 = CreaData()
objeto2 = knn()
opc = 0
while(opc != 3):
    print(Fore.BLUE+Back.RESET+"\n     Menu")
    opc = int(input("  1.- Crear Dataset\n  2.- Clasificar\n  3.- Salir"+Fore.GREEN+"\n    Opcion: "))
    if(opc == 1):
        objeto1.main()
    elif(opc == 2):
        objeto2.main()
    else:
        print("\n           "+Fore.MAGENTA+"Adios...!")
        



from PIL import Image
import matplotlib.image as mpimg
import csv
import os
from colorama import Fore
cont = 1

class CreaData():

    op = open('dataset2.csv','a',newline='')
    escribir = csv.writer(op,delimiter=';')
     
    def analisis(ruta,clase):
        global cont
        
        img = Image.open(ruta)
        img2 = mpimg.imread(ruta)
        col, fil = img.size
        data=[]
        data.extend(CreaData.arraysImg(img2,fil,col))
        data.extend(CreaData.cortes(img2,fil,col))
        data.append(CreaData.razonImagen(col,fil))
        data.append(CreaData.razon_1s_area(col,fil,img2))
        data.append(clase)
        data.append(cont)
        CreaData.escribir.writerow(data)
        cont += 1
        
     
    def razonImagen(col, fil):
        
        razon= col/fil
        return razon

     
    def razon_1s_area(columnas,filas,img2):
        
        c3_1 = 0
        for x in range(filas):
            for z in range(columnas):
                if(img2[x][z] == 1):
                    c3_1 += 1
        razon = c3_1/(filas*columnas)
        return razon
        
     
    def arraysImg(img,fil, col):
        vectores = [0,0,0,0,0,0]
        for x in range(fil):
            if(img[x][int(col/2)] == 1):
                vectores[0] += 1
            if(img[x][int(col/4)] == 1):
                vectores[1] += 1
            if(img[x][3*int(col/4)] == 1):
                vectores[2] += 1
    
        for x in range(col):
            if(img[int(fil/2)][x] == 1):
                vectores[3] += 1
            if(img[int(fil/4)][x] == 1):
                vectores[4] += 1
            if(img[3*int(fil/4)][x] == 1):
                vectores[5] += 1
        vec = [0.0,0.0,0.0,0.0,0.0,0.0]
        for i in range(len(vec)):
            if(i<3):
                vec[i] = vectores[i]/fil
            else:
                vec[i] = vectores[i]/col
        return vec
    
     
    def cortes(img2,fil,col):
        corte = [0,0,0,0,0,0]
        mcol = int(col/2)
        col_1_4 = int(col/4)
        col_3_4 = 3*int(col/4)
        
        for x in range(fil):
            if (x == 0 or x == (fil-1)):
                if(img2[x][mcol] == 1):
                    corte[0] += 1
                if(img2[x][col_1_4] == 1):
                    corte[1] += 1
                if(img2[x][col_3_4] == 1):
                    corte[2] += 1
            if(img2[x][mcol] != img2[x-1][mcol] and x != 0):
                corte[0] += 1
            if(img2[x][col_1_4] != img2[x-1][col_1_4] and x != 0):
                corte[1] += 1
            if(img2[x][col_3_4] != img2[x-1][col_3_4] and x != 0):
                corte[2] += 1
        mfil = int(fil/2)
        fil_1_4 = int(fil/4)
        fil_3_4 = 3*int(fil/4)
        
        for x in range(col):
            if (x == 0 or x == (col-1)):
                if(img2[mfil][x] == 1):
                    corte[3] += 1
                if(img2[fil_1_4][x] == 1):
                    corte[4] += 1
                if(img2[fil_3_4][x] == 1):
                    corte[5] += 1
            if(img2[mfil][x] != img2[mfil][x-1] and x != 0):
                corte[3] += 1
            if(img2[fil_1_4][x] != img2[fil_1_4][x-1] and x != 0):
                corte[4] += 1
            if(img2[fil_3_4][x] != img2[fil_3_4][x-1] and x != 0):
                corte[5] += 1
        return corte
    
    def main(self):
        cont = 0
        for base, dirs, files in os.walk('C:/Users/Paul/Desktop/OCR/ocrP/data'):       
            
            if cont > 0:
                print(Fore.BLUE+"    Obteniendo caracteristicas de: "+ Fore.BLACK+ str(base[len(base)-1]))
                for name in files:
                    CreaData.analisis((str(base)+'/'+name),base[len(base)-1])
            cont += 1
        CreaData.op.close()
        print(Fore.MAGENTA+"     Proceso finalizado!")
    def __init__(self):
        pass
    
    
    import csv
import math
import operator
from PIL import Image
import matplotlib.image as mpimg
from crearDataset import CreaData
from colorama import Fore, Back

trainingSet = []

class knn():
     
    def cargarDataset(archivo):
        global trainingSet
        clases = []
        with open(archivo, newline='') as csvfile:
            lines = csv.reader(csvfile, delimiter= ';')
            dataset = list(lines)
            for x in range(len(dataset)-1):
                for y in range(13):
                    dataset[x][y] = float(dataset[x][y])
                clase = dataset[x][14]
                if(x == 0):
                    clases.append(clase)
                if((clase in clases) == False):
                    clases.append(clase)
                trainingSet.append(dataset[x])
        csvfile.close()
        print(Fore.RED+"  -------------------------------------------------------")
        print(Fore.BLUE+"          Información general")
        print(Fore.BLACK+"  Caracteristicas obtenidas: "+Fore.BLUE+"14")
        print(Fore.BLACK+"  Clases: "+Fore.BLUE)
        i = 0
        for clas in clases:
            print("  "+str(clas)+", ",end='')
            if(i%5 == 0):
                print('')
            i += 1
        print(Fore.BLACK+"  Total de clases: "+Fore.BLUE+str(len(clases)))
        print(Fore.BLACK+"  Numero TOTAL de instancias: "+Fore.BLUE+ str(len(dataset)))
        print(Fore.RED+"  -------------------------------------------------------")

     
    def euclideanDistance(instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += pow((instance1[x] - instance2[x]), 2)
        return math.sqrt(distance)
     
    def getNeighbors(testInstance, k):
        global trainingSet
        distances = []
        length = len(testInstance)-1
        for x in range(len(trainingSet)):
            dist = knn.euclideanDistance(testInstance, trainingSet[x], length)
            distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
        print(Fore.RED+"  -------------------------------------------------------")
        print(Fore.BLUE+"  K vecino  "+" Linea(Instancia) "+ " Clase: "+" Distancia: ")
        for x in range(k):
            print(Fore.BLACK+"  "+str(x+1)+"              "+str(distances[x][0][15])+"           "+str(distances[x][0][14])+"       "+"%.5f" % round(distances[x][1],2))
            neighbors.append(distances[x][0])
        return neighbors
     
    def getResponse(neighbors):
        classVotes = {}
        print(Fore.RED+"  -------------------------------------------------------")
        print(Fore.BLUE+"\n       Resumen KNN")
        print("\n  Instancias de la clase   Votación")
        for x in range(len(neighbors)):
            response = neighbors[x][-2]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        for keys,values in classVotes.items():
            print("         "+Fore.BLACK+str(keys)+Fore.BLUE+"                "+str(values))
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0] 

     
    def obtenerCaract(self,ruta):
        data = []
        img = Image.open(ruta) 
        img2 = mpimg.imread(ruta) 
        columnas, filas = img.size 

        
        data.extend(CreaData.arraysImg(img2,filas,columnas))
        data.extend(CreaData.cortes(img2,filas,columnas))
        
        data.append(CreaData.razonImagen(columnas,filas))
        data.append(CreaData.razon_1s_area(columnas,filas,img2))
        return data
     
    def __init__(self):
        pass
     
    def main(self):
        global trainingSet
        data =[]
        knn.cargarDataset('dataset2.csv')
        input(Fore.BLACK+"  Se finalizo la carga de dataset, presione ENTER para continuar... : ")
        ruta = 'C:/Users/Paul/Desktop/OCR/ocrP/test/'
        ruta += input("  Ingresa el nombre de la imagen: ")
        data = knn.obtenerCaract(self,ruta)
        k = int(input("  Ingresa el numero K: "))
        resultado = knn.getResponse(knn.getNeighbors(data,k))
        print(Fore.BLACK+"\n       "+Back.CYAN+"LA IMAGEN ES UN:"+Back.RESET+Fore.RED+" "+str(resultado) +"  <-----")
        
        del trainingSet[:]
        
        
        
