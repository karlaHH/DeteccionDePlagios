
 


import csv

import math

import ocr_dataset as caracteristicasimg





def nuevaInstanciaK(ruta, k):
    
    
    (img2, filas, columnas) = caracteristicasimg.matrizimagen(ruta)
    
    razonfilascolumnas = caracteristicasimg.razon_filascolumnas(filas, columnas)
    
    razonunos = caracteristicasimg.unosimagen(img2, filas, columnas)
    
    razonunoscuartovertical = caracteristicasimg.vectorcuartovertical(img2, filas, columnas)
    
    razonunoscuartohorizontal = caracteristicasimg.vectorcuartohorizontal(img2, filas, columnas)
    
    razonunosmitadvertical = caracteristicasimg.vectormitadvertical(img2, filas, columnas)
    
    razonunosmitadhorizontal = caracteristicasimg.vectormitadhorizontal(img2, filas, columnas)
    
    razonunostrescuartosvertical = caracteristicasimg.vectortrescuartosvertical(img2, filas, columnas)
    
    razonunostrescuartoshorizontal = caracteristicasimg.vectortrescuartoshorizontal(img2, filas, columnas)
    
    cortescuartovertical = caracteristicasimg.lineacuartovertical(img2, filas, columnas)
    
    cortescuartohorizontal = caracteristicasimg.lineacuartohorizontal(img2, filas, columnas)
    
    cortesmitadvertical = caracteristicasimg.lineamitadvertical(img2, filas, columnas)
    
    cortesmitadhorizontal = caracteristicasimg.lineamitadhorizontal(img2, filas, columnas)
    
    cortestrescurtovertical = caracteristicasimg.lineatrescuartosvertical(img2, filas, columnas)
    
    cortestrescuertohorizontal = caracteristicasimg.lineatrescuartoshorizontal(img2, filas, columnas)
    
    razonunoscruz = caracteristicasimg.cerosunoscruz(img2, filas, columnas)
    
    
    nuevainstancia = [razonfilascolumnas,razonunos,razonunoscuartovertical,razonunoscuartohorizontal,razonunosmitadvertical,razonunosmitadhorizontal,razonunostrescuartosvertical,razonunostrescuartoshorizontal,cortescuartovertical,cortescuartohorizontal,cortesmitadvertical,cortesmitadhorizontal,cortestrescurtovertical,cortestrescuertohorizontal,razonunoscruz,k]
    
    
    return nuevainstancia





def cargarDataset(nombrearchivo):
	
    with open(nombrearchivo, 'r') as csvfile:
    	
        lineas = csv.reader(csvfile)
        
        dataset = list(lineas)
        
        for x in range(len(dataset)):
        	
            for y in range(16):
            	
                if(y<15):
                	
                    dataset[x][y] = float(dataset[x][y])
                else:
                	
                    dataset[x][y] = dataset[x][y]
                
    
    return dataset





def calcularDistancia(dataset,nuevainstancia):
	
    distancias = []
    
    for x in range(len(dataset)):
        distancias.append([math.sqrt(pow((dataset[x][0] - float(nuevainstancia[0])),2)+pow((dataset[x][1]-float(nuevainstancia[1])),2)+pow((dataset[x][2]-float(nuevainstancia[2])),2)+pow((dataset[x][3]-float(nuevainstancia[3])),2)+pow((dataset[x][4]-float(nuevainstancia[4])),2)+pow((dataset[x][5]-float(nuevainstancia[5])),2)+pow((dataset[x][6]-float(nuevainstancia[6])),2)+pow((dataset[x][7]-float(nuevainstancia[7])),2)+pow((dataset[x][8]-float(nuevainstancia[8])),2)+pow((dataset[x][9]-float(nuevainstancia[9])),2)+pow((dataset[x][10]-float(nuevainstancia[10])),2)+pow((dataset[x][11]-float(nuevainstancia[11])),2)+pow((dataset[x][12]-float(nuevainstancia[12])),2)+pow((dataset[x][13]-float(nuevainstancia[13])),2)+pow((dataset[x][14]-float(nuevainstancia[14])),2)),dataset[x][15],(x+1)])
    
    
    auxiliar = 0
    
    tamaño = len(distancias)
    
    for i in range(1, tamaño):
    	
        for j in range(0,tamaño-1):
        	
            if(distancias[j]>distancias[j+1]):
            	
               	auxiliar = distancias[j+1]
               	
               	distancias[j+1] = distancias[j]
               	
               	distancias[j] = auxiliar
    
    return distancias     





def clasificarInstancia(distancias,nuevainstancia):
    
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
    
    totalclase = []
    print('\n')
    
    print("\t  K\t     Distancias      Clase  Id") 
    print("\t___________________________________________")
    
    contador = 1
    
    for x in range(int(nuevainstancia[15])):
    	
        print('\tI - '+str(contador)+' =\t'+str(distancias[x]))
        
        if(distancias[x][1] == '0'):
            
            clase0 += 1
        
        if(distancias[x][1] == '1'):
            
            clase1 += 1
        
        if(distancias[x][1] == '2'):
            
            clase2 += 1
        
        if(distancias[x][1] == '3'):
            
            clase3 += 1
        
        if(distancias[x][1] == '4'):
            
            clase4 += 1
        
        if(distancias[x][1] == '5'):
            
            clase5 += 1
        
        if(distancias[x][1] == '6'):
            clase6 += 1
        
        if(distancias[x][1] == '7'):
            
            clase7 += 1
        
        if(distancias[x][1] == '8'):
            
            clase8 += 1
        
        if(distancias[x][1] == '9'):
            
            clase9 += 1
        
        contador += 1
    
    totalclase = [clase0, clase1,clase2,clase3,clase4,clase5,clase6,clase7,clase8,clase9]
    print("\n")
    
    auxiliar = 0
    
    for x in range(len(totalclase)):
        
        print('\t\tTotal de la Clase '+str(x)+' = '+str(totalclase[x]))
        
        if(auxiliar <= totalclase[x]):
            
            auxiliar = totalclase[x]
            
            claseidentidad = x
    
    print('\n\t\tCaracter Identificado: ' + str(claseidentidad))




def main():
    
    k=int(input("\t        Escribe el numero de k: "))
    imagen = str(input("\t     Escribe el numero de la imagen: "))
    print("\n\n\t      Identificando caracteristicas!")
    
    ruta = 'C:/Users/user/Documents/8 cuatrimestre/Mineria de Datos/ocr/test/' + imagen + '.png'
    
    nuevainstancia = nuevaInstanciaK(ruta, k)
    
    dataset = cargarDataset('dataset.csv')
    
    tam = len(dataset)
    print("\t\tInformacion General")
    
    print("\n\t        Total de intancias: "+str(tam))
    
    print("\tTotal de caracteristicas por Instancia: 14")
    print("\tTotal de clases: 10")
    print("\tNombres de las clases {0,1,2,3,4,5,6,7,8,9}")
    
    distancia = calcularDistancia(dataset,nuevainstancia)
    
    clasificarInstancia(distancia,nuevainstancia)


main()



 

from PIL import Image

import matplotlib.image as mpimg

import os

import csv





def matrizimagen(nombre):
    
    img = Image.open(nombre)
    
    img2 = mpimg.imread(nombre)
    
    columnas, filas = img.size
    
    return img2, filas, columnas





def razon_filascolumnas(filas, columnas):
    
    razonfilascolumnas = 0
    
    razonfilascolumnas = filas/columnas
    
    return razonfilascolumnas





def unosimagen(img2, filas, columnas):
    
    contadoruno = 0
    
    razonunos = 0
    
    for x in range(filas):
        
        for y in range(columnas):
            
            if(img2[x][y] == 1):
                contadoruno = contadoruno + 1
    
    razonunos = contadoruno/(filas*columnas)

    
    return razonunos





def vectorcuartovertical(img2, filas, columnas):
    
    contadorunos = 0
    
    sizevector = 0
    
    razonunoscuartovertical = 0
    
    cuartovectorvertical = int(columnas/4)
    
    for x in range(filas):
        
        if(img2[x][cuartovectorvertical] == 1):
            
            contadorunos += 1
    
    sizevector = filas
    
    razonunoscuartovertical = contadorunos/sizevector

    
    return razonunoscuartovertical





def vectorcuartohorizontal(img2, filas, columnas):
    
    contadorunos = 0
    
    sizevector = 0
    
    razonunoscuartohorizontal = 0
    
    cuartovectorhorizontal = int(filas/4)
    
    
    for x in range(columnas):
        
        if(img2[cuartovectorhorizontal][x]==1):
            
            contadorunos += 1

    sizevector = columnas
    
    razonunoscuartohorizontal = contadorunos/sizevector
    
    return razonunoscuartohorizontal





def vectormitadvertical(img2, filas, columnas):
    
    contadorunos = 0
    
    sizevector = 0
    
    razonunosmitadvertical = 0
    
    mitadvectorvertical = int(columnas/2)
    
    for x in range(filas):
        
        if(img2[x][mitadvectorvertical] == 1):
            
            contadorunos += 1
    
    sizevector = filas
    
    razonunosmitadvertical = contadorunos/sizevector

    
    return razonunosmitadvertical
    




def vectormitadhorizontal(img2, filas, columnas):
    
    contadorunos = 0
    
    sizevector = 0
    
    razonunosmitadhorizontal = 0
    
    mitadvectorhorizontal = int(filas/2)
    
    
    for x in range(columnas):
        
        if(img2[mitadvectorhorizontal][x]==1):
            
            contadorunos += 1

    sizevector = columnas
    
    razonunosmitadhorizontal = contadorunos/sizevector
    
    return razonunosmitadhorizontal





def vectortrescuartosvertical(img2, filas, columnas):
    
    contadorunos = 0
    
    sizevector = 0
    
    razonunostrescuartosvertical = 0
    
    trescuartosvectorvertical = int(columnas/2)
    
    for x in range(filas):
        
        if(img2[x][trescuartosvectorvertical] == 1):
            
            contadorunos += 1
    
    sizevector = filas
    
    razonunostrescuartosvertical = contadorunos/sizevector

    
    return razonunostrescuartosvertical





def vectortrescuartoshorizontal(img2, filas, columnas):
   
    contadorunos = 0
    
    sizevector = 0
    
    razonunostrescuartoshorizontal = 0
    
    trescuartosvectorhorizontal = int(filas/2)
    
    
    for x in range(columnas):
        
        if(img2[trescuartosvectorhorizontal][x]==1):
            
            contadorunos += 1

    sizevector = columnas
    
    razonunostrescuartoshorizontal = contadorunos/sizevector
    
    return razonunostrescuartoshorizontal





def lineacuartovertical(img2, filas, columnas):
    
    contadorcortes1 = 0
    contadorcortes0 = 0
    cortescuartovertical = 0
    fila = 0
    
    cc = int(columnas/4)
    
    for x in range(filas):
        
        contadorcortes1 = img2[x][cc]
        
        if(x<filas-1):
            
            contadorcortes0 = img2[x+1][cc]
            
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (fila==0 and img2[0][cc]==1)):
                
                cortescuartovertical = cortescuartovertical + 1
                
                fila = fila + 1

    
    return cortescuartovertical





def lineacuartohorizontal(img2, filas, columnas):
    
    contadorcortes1 = 0
    contadorcortes0 = 0
    
    cortescuartohorizontal = 0
    
    columna = 0
    
    cr = int(filas/4)
    
    for x in range(columnas):
        
        contadorcortes1 = img2[cr][x]
        
        if(x<columnas-1):
            
            contadorcortes0 = img2[cr][x+1]
            
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (columna==0 and img2[cr][0]==1)):
                
                cortescuartohorizontal = cortescuartohorizontal + 1
                
                columna = columna + 1

    
    return cortescuartohorizontal





def lineamitadvertical(img2, filas, columnas):
    
    contadorcortes1 = 0
    contadorcortes0 = 0
    
    cortesmitadvertical = 0
    
    fila = 0
    
    medc = int(columnas/2)
    
    for x in range(filas):
        
        contadorcortes1 = img2[x][medc]
        
        if(x<filas-1):
            
            contadorcortes0 = img2[x+1][medc]
            
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (fila==0 and img2[0][medc]==1)):
                
                cortesmitadvertical = cortesmitadvertical + 1
                
                fila = fila + 1

    
    return cortesmitadvertical





def lineamitadhorizontal(img2, filas, columnas):
    
    contadorcortes1 = 0
    contadorcortes0 = 0
    
    cortesmitadhorizontal = 0
    
    columna = 0
    
    medr = int(filas/2)
    
    for x in range(columnas):
        
        contadorcortes1 = img2[medr][x]
        
        if(x<columnas-1):
            
            contadorcortes0 = img2[medr][x+1]
            
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (columna==0 and img2[medr][0]==1)):
                
                cortesmitadhorizontal = cortesmitadhorizontal + 1
                
                columna = columna + 1

    
    return cortesmitadhorizontal





def lineatrescuartosvertical(img2, filas, columnas):
    
    contadorcortes1 = 0
    contadorcortes0 = 0
    
    cortestrescurtovertical = 0
    
    fila = 0
    
    cc = int((columnas/4)*3)
    
    for x in range(filas):
        
        contadorcortes1 = img2[x][cc]
        
        if(x<filas-1):
            
            contadorcortes0 = img2[x+1][cc]
            
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (fila==0 and img2[0][cc]==1)):
                
                cortestrescurtovertical = cortestrescurtovertical + 1
                
                fila = fila + 1

    
    return cortestrescurtovertical





def lineatrescuartoshorizontal(img2, filas, columnas):
    
    contadorcortes1 = 0
    contadorcortes0 = 0
    
    cortestrescuertohorizontal = 0
    
    columna = 0
    
    cr = int((filas/4)*3)
    
    for x in range(columnas):
        
        contadorcortes1 = img2[cr][x]
        
        if(x<columnas-1):
            
            contadorcortes0 = img2[cr][x+1]
            
            if((contadorcortes0!=contadorcortes1 and contadorcortes0==1) or (columna==0 and img2[cr][0]==1)):
                
                cortestrescuertohorizontal = cortestrescuertohorizontal + 1
                
                columna = columna + 1

    
    return cortestrescuertohorizontal





def cerosunoscruz(img2, filas, columnas):
    
    contadoruno1 = 0
    contadoruno2 = 0
    
    medr = int(filas/2)
    
    medc = int(columnas/2)


    
    for x in range(filas):
        
        if(img2[x][medc]==1):
            
            contadoruno1 = contadoruno1 + 1
    
    for y in range(columnas):
        
        if(img2[medr][y]==1):
            
            contadoruno2 = contadoruno2 + 1
    
    razonunoscruz = (contadoruno1 + contadoruno2)/(filas * columnas)


    
    return razonunoscruz
    



def Dataset():

    
    dataset = []

    
    rootDir= './dataset/'
    
    f = open('dataset.csv','w',newline='')
    
    obj = csv.writer(f,delimiter=',')    

    
    
    
    
    for dirName, subdirList, fileList in os.walk(rootDir):
        
        print('Identificando clase: %s' % dirName)

        
        for fname in fileList:
            
            nombre = dirName + '/' + fname
            
            numeroclase = dirName[10]

            
            
            (img2, filas, columnas) = matrizimagen(nombre)
            
            razonfilascolumnas = razon_filascolumnas(filas, columnas)
            
            razonunos = unosimagen(img2, filas, columnas)
            
            razonunoscuartovertical = vectorcuartovertical(img2, filas, columnas)
            
            razonunoscuartohorizontal = vectorcuartohorizontal(img2, filas, columnas)
            
            razonunosmitadvertical = vectormitadvertical(img2, filas, columnas)
            
            razonunosmitadhorizontal = vectormitadhorizontal(img2, filas, columnas)
            
            razonunostrescuartosvertical = vectortrescuartosvertical(img2, filas, columnas)
            
            razonunostrescuartoshorizontal = vectortrescuartoshorizontal(img2, filas, columnas)
            
            cortescuartovertical = lineacuartovertical(img2, filas, columnas)
            
            cortescuartohorizontal = lineacuartohorizontal(img2, filas, columnas)
            
            cortesmitadvertical = lineamitadvertical(img2, filas, columnas)
            
            cortesmitadhorizontal = lineamitadhorizontal(img2, filas, columnas)
            
            cortestrescurtovertical = lineatrescuartosvertical(img2, filas, columnas)
            
            cortestrescuertohorizontal = lineatrescuartoshorizontal(img2, filas, columnas)
            
            razonunoscruz = cerosunoscruz(img2, filas, columnas)
            
            dataset.append([razonfilascolumnas,razonunos,razonunoscuartovertical,razonunoscuartohorizontal,razonunosmitadvertical,razonunosmitadhorizontal,razonunostrescuartosvertical,razonunostrescuartoshorizontal,cortescuartovertical,cortescuartohorizontal,cortesmitadvertical,cortesmitadhorizontal,cortestrescurtovertical,cortestrescuertohorizontal,razonunoscruz,numeroclase])


    
    obj.writerows(dataset)
    
    f.close()
    



