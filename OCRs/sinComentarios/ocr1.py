from PIL import Image
import matplotlib.image as mpimg
import csv
import os
import math
import operator

None"caracteristicas" para obtener las caracteristicas de la imagen y por ultimo

 






 





None"Calculando caracteristicas de: "+ str(files[x][0]))
            for name in files:
                escribirData( (str(base)+'/'+name),name[0],aux)
                
                aux += 1
            x +=1
        cont += 1
    abrir.close()
    print("\nDataSet creado!")

 
def knn():
    dataset = []
    nuevaImg = []
    print("Clasificación KNN")
    dataset = leerDataset()
    print("Dataset cargado")
    nuevaImg = nuevaInstancia()
    k = int(input("Escribe el numero K: "))
    resultado = votacion(getVecinos(dataset,nuevaImg,k))
    print("      La imagen es: "+str(resultado))
    del dataset[:]

 
def leerDataset():
    data = []
    todas = []
    with open('dataset.csv', newline = '') as miArchivo:
        linea = csv.reader(miArchivo, delimiter= ',')
        dataset = list(linea)
        for x in range(len(dataset)-1):
            for y in range(13):
                dataset[x][y] = float(dataset[x][y])
            clase = dataset[x][14]
            if(x == 0):
                todas.append(clase)
            if((clase in todas)== False):
                todas.append(clase)            
            data.append(dataset[x])
        miArchivo.close()
        print("  .........................................................")
        print("          Información general")
        print("  Caracteristicas obtenidas: 14")
        print("  Clases: ")       
        print("  "+str(todas))
        print("  Total de clases: "+str(len(todas)))
        print("  Numero TOTAL de instancias: "+ str(len(dataset)))
        print("  ..........................................................")
        
    return data;
 
def euclides(nuevaImg,data,tam):
    distancia = 0
    for x in range(tam):
        distancia += pow((nuevaImg[x] - data[x]), 2)
    return math.sqrt(distancia)
 
def getVecinos(dataset,nuevaImg,k):
    distancias = []
    tam = len(nuevaImg)-1
    for indice in range(len(dataset)):
        dist = euclides(nuevaImg,dataset[indice],tam)
        distancias.append((dataset[indice],dist))
    distancias.sort(key=operator.itemgetter(1))
    vecinos = []
    for indice in range(k):
        vecinos.append(distancias[indice][0])
        print("Vecino: "+ str(distancias[indice][0][14])+" Distancia: "+str(distancias[indice][1])+" Linea: "+str(distancias[indice][0][15]))
    return vecinos
        
 
def votacion(vecinos):
    clases = {}
    print("\n     Resumen KNN")
    for x in range(len(vecinos)):
        resp = vecinos[x][-2]
        if resp in clases:
            clases[resp] += 1
        else:
            clases[resp] = 1
    for clase,total in clases.items():
        print("   Instancia de la clase: "+str(clase)+"      Total: "+str(total))
    clasifica = sorted(clases.items(), key=operator.itemgetter(1), reverse=True)
    return clasifica[0][0]
 
def nuevaInstancia():
    ruta = 'C:/Users/jossepablo/Desktop/ocrA/prueba/'
    ruta += input("Ingresa el nombre de la imagen: ")
    ruta += '.png'
    img = Image.open(ruta)
    img2 = mpimg.imread(ruta)
    col,fil = img.size
    data = caracteristicas(img2,fil,col)
    return data


opc = 1
while(opc != 3 ):
    print("Menu")
    opc = int(input("   1.- Crear DataSet\n   2.- KNN\n   3.- Salir\n Opción: "))
    if(opc == 1):
        abrir = open('dataset.csv','w',newline='')
        escribir = csv.writer(abrir,delimiter=',')
        principal()
    elif(opc == 2):
        knn()
    else:
        print("     Adios!")
        
