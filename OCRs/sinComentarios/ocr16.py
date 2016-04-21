
 

from Crear_dataset import Extraccion_de_caract 

from ClasificacionKNN import knn

print("Menu") 
opc = int(input("1.- Crear DataSet\n2.- Clasificar una imagen\n  Opcion: ")) 
if(opc == 1): 
    extrae = Extraccion_de_caract() 
    extrae.main() 
    print("ups")
if(opc == 2): 
    clasificacion = knn()  
    clasificacion.main() 

    
import csv 
import math 
import operator 
from PIL import Image 
import matplotlib.image as mpimg 
from Crear_dataset import Extraccion_de_caract 

class knn(): 

    def cargarDataset(archivo): 
        dataset = []
        with open(archivo, newline='') as csvfile: 
            lines = csv.reader(csvfile, delimiter= ';') 
            dataset = list(lines) 
            for completo in range(len(dataset)-1): 
                for acceso in range(13): 
                    
                    dataset[completo][acceso] = float(dataset[completo][acceso]) 
                dataset.append(dataset[completo])
        csvfile.close() 
        return dataset 

    def euclideanDistance(instance1, instance2, length): 
        distancia = 0 
        for indice in range(length):
            distancia += pow((float(instance1[indice]) - float(instance2[indice])), 2)
        return math.sqrt(distancia)

    def getNeighbors(dataset,nuevaInstancia, k): 
        distancia = [] 
        length = len(nuevaInstancia)-1
        for indice_dataset in range(len(dataset)):
            dist = knn.euclideanDistance(nuevaInstancia, dataset[indice_dataset], length)
            distancia.append((dataset[indice_dataset], dist))
        distancia.sort(key=operator.itemgetter(1))
        print("\n****************************\n")
        print(distancia)
        neighbors = [] 
        for indice in range(k): 
            neighbors.append(distancia[indice][0])
            print("Instancia: "+ str(distancia[indice][0][15]) + " Clase: "+ str(distancia[indice][0][14]) + " Distancia: " + str(distancia[indice][1]))
            
        return neighbors 

    def getResponse(neighbors):  
        classVotes = {} 
        for indice in range(len(neighbors)):
            response = neighbors[indice][-2] 
            if response in classVotes:
                classVotes[response] += 1 
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]

    def obtenerCaract(self,ruta): 
        data = []
        img = Image.open(ruta) 
        img2 = mpimg.imread(ruta) 
        columnas, filas = img.size 

        
        data.extend(Extraccion_de_caract.vectoresImg(img2,filas,columnas))
        data.extend(Extraccion_de_caract.cortes(img2,filas,columnas)) 
        data.append(Extraccion_de_caract.razonFC(columnas,filas)) 
        data.append(Extraccion_de_caract.razon_1_img(columnas,filas,img2)) 
        return data

    def __init__(self): 
        pass

    def main(self):
        data =[] 
        trainingSet = []
        trainingSet = knn.cargarDataset('dataset.csv') 
        input("Se finalizo la carga de dataset, presione ENTER para continuar... : ") 
        ruta = 'C:/Users/Paul/Desktop/OCR/ocrD/test/' 
        ruta += input("Ingresa el nombre de la imagen: ") 
        data = knn.obtenerCaract(self,ruta) 
        k = int(input("Ingresa el numero K: ")) 
        resultado = knn.getResponse(knn.getNeighbors(trainingSet,data,k))
        print("\n   La imagen es un: "+str(resultado)) 
        del trainingSet[:]
        del data[:]
        
        
import csv 
import math 
import operator 
from PIL import Image 
import matplotlib.image as mpimg 
from Crear_dataset import Extraccion_de_caract 

class knn(): 
     
    def cargarDataset(archivo):
        trainingSet = []
        with open(archivo, newline='') as csvfile:
            lines = csv.reader(csvfile, delimiter= ';')
            dataset = list(lines)
            for completo in range(len(dataset)-1):
                for acceso in range(13):
                    
                    dataset[completo][acceso] = float(dataset[completo][acceso])
                trainingSet.append(dataset[completo])
        csvfile.close()
        return trainingSet
     
    def euclideanDistance(instance1, instance2, length): 
        distance = 0 
        for x in range(length):
            distance += pow((instance1[x] - instance2[x]), 2)
        return math.sqrt(distance)
     
    def getNeighbors(trainingSet,testInstance, k): 
        distances = [] 
        length = len(testInstance)-1
        for x in range(len(trainingSet)):
            dist = knn.euclideanDistance(testInstance, trainingSet[x], length)
            distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for x in range(k):
            print("Linea(Instancia): "+str(distances[x][0][15])+ " Clase: "+str(distances[x][0][14])+" Distancia: "+str(distances[x][1]))
            neighbors.append(distances[x][0])
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
     
    def obtenerCaract(self,ruta): 
        data = []
        img = Image.open(ruta) 
        img2 = mpimg.imread(ruta) 
        columnas, filas = img.size 
        
        data.extend(Extraccion_de_caract.vectoresImg(img2,filas,columnas))
        data.extend(Extraccion_de_caract.cortes(img2,filas,columnas)) 
        data.append(Extraccion_de_caract.razonFC(columnas,filas)) 
        data.append(Extraccion_de_caract.razon_1_img(columnas,filas,img2)) 
        return data

    def __init__(self):
        pass
     
    def main(self):
        trainingSet = []
        data =[]
        trainingSet = knn.cargarDataset('dataset.csv')
        input("Se finalizo la carga de dataset, presione ENTER para continuar... : ")
        ruta = 'C:/Users/Paul/Desktop/OCR/ocrD/test/'
        ruta += input("Ingresa el nombre de la imagen: ")
        data = knn.obtenerCaract(self,ruta)
        k = int(input("Ingresa el numero K: "))
        resultado = knn.getResponse(knn.getNeighbors(trainingSet,data,k))
        print("\n   La imagen es un: "+str(resultado))
        del trainingSet[:]
        
