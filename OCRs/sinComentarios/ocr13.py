

from PIL import Image 
import matplotlib.image as mpimg
import csv 
import os
import math
import operator

  
def recorrerArchivos():
    x = 0
    N_linea = 0
    for ruta, dirs, files in os.walk('C:/Users/Dashen/Documents/OCR_/images'):
        if(x > 0):
            print("Escribiendo caracteristicas de: "+ str(files[x][0]))
            for archivo in files:
                escribir((ruta+"/"+archivo),archivo[0],N_linea)
                N_linea += 1
        x += 1
    
   
def escribir(ruta,clase,linea):
    caracteristicas = []
    img = Image.open(ruta)
    img2 = mpimg.imread(ruta)
    c,f = img.size
    caracteristicas.append(caracteristica1(c,f))
    caracteristicas.append(caracteristica2(img2,c,f))
    caracteristicas.append(caracteristica3(img2,c,f))
    caracteristicas.append(caracteristica4(img2,c,f))
    caracteristicas.append(caracteristica5(img2,c,f))
    caracteristicas.append(caracteristica6(img2,c,f))
    caracteristicas.append(caracteristica7(img2,c,f))
    caracteristicas.append(caracteristica8(img2,c,f))
    caracteristicas.extend(caracteristica_cortes(img2,c,f))
    caracteristicas.append(clase)
    caracteristicas.append(linea)
    write.writerow(caracteristicas)
    
   
def caracteristica1(col,fil):
    return col/fil
 
def caracteristica2(img,col,fil):
    unos = 0
    for indice_x in range(fil-1):
        for indice_y in range(col-1):
            if(img[indice_x][indice_y] == 1):
                unos += 1
    return unos/(fil*col)
 
def caracteristica3(img,col,fil):
    unos = 0
    for x in range(fil):
        if(img[x][int(col/2)] == 1):
            unos += 1
    return unos/fil
 
def caracteristica4(img,col,fil):
    unos = 0
    for x in range(fil):
        if(img[x][int(col/4)] == 1):
            unos += 1
    return unos/fil
 
def caracteristica5(img,col,fil):
    unos = 0
    for x in range(fil):
        if(img[x][int(3*col/4)] == 1):
            unos += 1
    return unos/fil
 
def caracteristica6(img,col,fil):
    unos = 0
    for x in range(col):
        if(img[int(fil/2)][x] == 1):
            unos += 1
    return unos/col
 
def caracteristica7(img,col,fil):
    unos = 0
    for x in range(col):
        if(img[int(fil/4)][x] == 1):
            unos += 1
    return unos/col
 
def caracteristica8(img,col,fil):
    unos = 0
    for x in range(col):
        if(img[int(3*fil/4)][x] == 1):
            unos += 1
    return unos/col

 
def caracteristica_cortes(img2,col,fil):
    corte = [0,0,0,0,0,0]
    mcol = int(col/2)
    col_1_4 = int(col/4)
    col_3_4 = int(3*col/4)
    
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
    fil_3_4 = int(3*fil/4)
    
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

 
def obtenerDataset():
    data = []
    clases = []
    with open('dataset.csv', newline = '') as archivo:
        lineas = csv.reader(archivo, delimiter= ',')
        dataset = list(lineas)
        for x in range(len(dataset)-1):
            for y in range(13):
                dataset[x][y] = float(dataset[x][y])
            clase = dataset[x][14]
            if(x == 0):
                clases.append(clase)
            if((clase in clases) == False):
                clases.append(clase)            
            data.append(dataset[x])
        archivo.close()
        print("\n          Información general")
        print("  Caracteristicas obtenidas: 14")
        print("  Clases: ")
        print(clases)
        print("  Total de clases: "+str(len(clases)))
        print("  Numero TOTAL de instancias: "+ str(len(dataset)))
    return data
 
def distancia(nuevaIMG, dataset, tam):
    distancia = 0
    for indice in range(tam):
        distancia += pow((nuevaIMG[indice] - dataset[indice]), 2)
    return math.sqrt(distancia)

 
def vecinos(dataset, nuevaIMG, k):
    instancia_dist = []
    tam = len(nuevaIMG)-1
    for indice in range(len(dataset)):
        dist = distancia(nuevaIMG,dataset[indice],tam)
        instancia_dist.append((dataset[indice],dist))
    instancia_dist.sort(key=operator.itemgetter(1))
    vecinos = []
    for indice in range(k):
        vecinos.append(instancia_dist[indice][0])
        print("Distancia: "+str(instancia_dist[indice][1])+" Linea: "+str(instancia_dist[indice][0][15])+" Vecino: "+ str(instancia_dist[indice][0][14]))
    return vecinos
 
def votacion(vecinos):
    instancias = {}
    print("\n       Resumen KNN")
    for x in range(len(vecinos)):
        resp = vecinos[x][-2]
        if resp in instancias:
            instancias[resp] += 1
        else:
            instancias[resp] = 1
        
    print("    Instancia de la clase       Total")
    for keys,values in instancias.items():
        print("         "+str(keys)+"                        "+str(values))
    result = sorted(instancias.items(), key=operator.itemgetter(1), reverse=True)
    
    return result[0][0]
 
def imgClasificar(ruta):
    caracteristicas = []
    img = Image.open(ruta)
    img2 = mpimg.imread(ruta)
    c,f = img.size
    caracteristicas.append(caracteristica1(c,f))
    caracteristicas.append(caracteristica2(img2,c,f))
    caracteristicas.append(caracteristica3(img2,c,f))
    caracteristicas.append(caracteristica4(img2,c,f))
    caracteristicas.append(caracteristica5(img2,c,f))
    caracteristicas.append(caracteristica6(img2,c,f))
    caracteristicas.append(caracteristica7(img2,c,f))
    caracteristicas.append(caracteristica8(img2,c,f))
    caracteristicas.extend(caracteristica_cortes(img2,c,f))
    return caracteristicas
    
opc = 0
while(opc != 3):
    print("\n     Menu")
    opc = int(input("1.- Generar dataset\n2.- Clasificación KNN\n3.- Salir\n    Opcion: "))
    if(opc == 1):
        crear = open('dataset.csv','w',newline='')
        write = csv.writer(crear,delimiter=',')
        recorrerArchivos()
        crear.close()
    elif(opc == 2):
        data =[]
        dataset =[]
        dataset = obtenerDataset()
        rutaIMG = 'C:/Users/Dashen/Documents/OCR_/pruebas/'
        rutaIMG += input('Ingresa el nombre de la imagen a clasificar: ')
        rutaIMG +='.png'
        data = imgClasificar(rutaIMG)
        k = int(input("Ingresa el número k: "))
        clase = votacion(vecinos(dataset, data, k))
        print("\nLa imagen es un simbolo: "+str(clase))
        del dataset[:]
        
