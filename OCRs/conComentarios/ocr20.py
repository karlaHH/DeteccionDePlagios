# -*- coding: utf-8 -*-

from PIL import Image #libreria de manejo de imagenes
import matplotlib.image as mpimg#libreria de manejo de imagenes
import csv #libreria para escritura
import os#libreria para recorrido de directorios
import math
import operator

"""
    * Método recorrerArchivos
    * Parametros: No Aplica
    * Retorna: No Aplica
    * Funcionamiento:
    *   Su funcion consiste en recorrer los directorios del path que tiene especificado,
    *   mandando la ruta de cada imagen contenida en los directorios, con su clase y lleva el
    *   contador del numero de linea en el dataset
""" 
def recorrerArchivos():
    x = 0#evita abrir el directorio raiz
    N_linea = 0#control del numero de linea en el archivo CSV
    for ruta, dirs, files in os.walk('C:/Users/Dashen/Documents/OCR_/images'):
        if(x > 0):#evita abrir el directorio raiz
            print("Escribiendo caracteristicas de: "+ str(files[x][0]))
            for archivo in files:#for que recorre todas las imagenes en la carpeta
                escribir((ruta+"/"+archivo),archivo[0],N_linea)#metodo escribir
                N_linea += 1#se incrementa el numero de linea
        x += 1#evita abrir el directorio raiz
    
"""
    * Método escribir
    * Parametros: ruta de la imagen, clase, numero de linea
    * Retorna: No Aplica
    * Funcionamiento:
    *    Abre la imagen que se le pasa como argumento,
    *    llama a los diferentes metodos para obtener las 14 caracteristicas,
    *    y escribe las caracteristicas obtenidas de cada imagen
"""  
def escribir(ruta,clase,linea):
    caracteristicas = []#arreglo que contendra las caracteristicas de la imagen
    img = Image.open(ruta)#se abre imagen
    img2 = mpimg.imread(ruta)#se abre imagen
    c,f = img.size#se obtienen filas y columnas
    caracteristicas.append(caracteristica1(c,f))#llamada para obtener caracteristica 1
    caracteristicas.append(caracteristica2(img2,c,f))#llamada para obtener caracteristica 2
    caracteristicas.append(caracteristica3(img2,c,f))#llamada para obtener caracteristica 3
    caracteristicas.append(caracteristica4(img2,c,f))#llamada para obtener caracteristica 4
    caracteristicas.append(caracteristica5(img2,c,f))#llamada para obtener caracteristica 5
    caracteristicas.append(caracteristica6(img2,c,f))#llamada para obtener caracteristica 6
    caracteristicas.append(caracteristica7(img2,c,f))#llamada para obtener caracteristica 7
    caracteristicas.append(caracteristica8(img2,c,f))#llamada para obtener caracteristica 8
    caracteristicas.extend(caracteristica_cortes(img2,c,f))#llamada para obtener caracteristica 9,10,11,12,13
    caracteristicas.append(clase)#se inserta la clase
    caracteristicas.append(linea)#se inserta el numero de linea
    write.writerow(caracteristicas)#se escriben las caracteristicas
    
"""
    * Método caracteristica1
    * Parametros: numero de filas, numero de columnas
    * Retorna: la razon de columnas entre filas
    * Funcionamiento:
    *    divide columnas entre filas y devuelve el valor
"""  
def caracteristica1(col,fil):
    return col/fil
"""
    * Método caracteristica2
    * Parametros: Imagen iterable, numero de filas, numero de columnas
    * Retorna: la razon de 1s en toda la imagen
    * Funcionamiento:
    *    Recorre la imagen contando los 1s y divide el total entre el area de la imagen
"""
def caracteristica2(img,col,fil):
    unos = 0#contador de 1s
    for indice_x in range(fil-1):
        for indice_y in range(col-1):
            if(img[indice_x][indice_y] == 1):#se hace la comparacion
                unos += 1#incrementa contador de 1s
    return unos/(fil*col)#retorno de la razon
"""
    * Método caracteristica3
    * Parametros: Imagen iterable, numero de filas, numero de columnas
    * Retorna: la razon de 1s en el vector col/2
    * Funcionamiento:
    *    Recorre el vector col/2 contando los 1s y retorna la razon de los 1s en ese vector
"""
def caracteristica3(img,col,fil):
    unos = 0#contador de 1s
    for x in range(fil):
        if(img[x][int(col/2)] == 1):#se hace la comparacion
            unos += 1#incrementa contador
    return unos/fil#retorno de la razon
"""
    * Método caracteristica4
    * Parametros: Imagen iterable, numero de filas, numero de columnas
    * Retorna: la razon de 1s en el vector col/4
    * Funcionamiento:
    *    Recorre el vector col/4 contando los 1s y retorna la razon de los 1s en ese vector
"""
def caracteristica4(img,col,fil):
    unos = 0#contador de 1s
    for x in range(fil):
        if(img[x][int(col/4)] == 1):#se hace la comparacion
            unos += 1#incrementa contador
    return unos/fil#retorno de la razon
"""
    * Método caracteristica5
    * Parametros: Imagen iterable, numero de filas, numero de columnas
    * Retorna: la razon de 1s en el vector col3/4
    * Funcionamiento:
    *    Recorre el vector col3/4 contando los 1s y retorna la razon de los 1s en ese vector
"""
def caracteristica5(img,col,fil):
    unos = 0#contador de 1s
    for x in range(fil):
        if(img[x][int(3*col/4)] == 1):#se hace la comparacion
            unos += 1#incrementa contador
    return unos/fil#retorno de la razon
"""
    * Método caracteristica6
    * Parametros: Imagen iterable, numero de filas, numero de columnas
    * Retorna: la razon de 1s en el vector fil/2
    * Funcionamiento:
    *    Recorre el vector fil/2 contando los 1s y retorna la razon de los 1s en ese vector
"""
def caracteristica6(img,col,fil):
    unos = 0#contador de 1s
    for x in range(col):
        if(img[int(fil/2)][x] == 1):#se hace la comparacion
            unos += 1#incrementa contador
    return unos/col#retorno de la razon
"""
    * Método caracteristica7
    * Parametros: Imagen iterable, numero de filas, numero de columnas
    * Retorna: la razon de 1s en el vector fil/4
    * Funcionamiento:
    *    Recorre el vector fil/4 contando los 1s y retorna la razon de los 1s en ese vector
"""
def caracteristica7(img,col,fil):
    unos = 0#contador de 1s
    for x in range(col):
        if(img[int(fil/4)][x] == 1):#se hace la comparacion
            unos += 1#incrementa contador
    return unos/col#retorno de la razon
"""
    * Método caracteristica8
    * Parametros: Imagen iterable, numero de filas, numero de columnas
    * Retorna: la razon de 1s en el vector fil3/4
    * Funcionamiento:
    *    Recorre el vector fil3/4 contando los 1s y retorna la razon de los 1s en ese vector
"""
def caracteristica8(img,col,fil):
    unos = 0#contador de 1s
    for x in range(col):
        if(img[int(3*fil/4)][x] == 1):#se hace la comparacion
            unos += 1#incrementa contador
    return unos/col#retorno de la razon

"""
    * Método caracteristica_cortes
    * Parametros: Imagen iterable, numero de filas, numero de columnas
    * Retorna: El numero de cortes de 1/2 de la imagen, 1/4 de la imagen y 3/4 de la imagen
    *    verticalmente y horizontalmente
    * Funcionamiento:
    *    Recorre la imagen en las columnas (col/2), (col/4),(col3/4),(fil/2),(fil/4) y (fil3/4)
    *    y cuenta los cambios de 1's y 0's
"""
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

"""
    * Método obtenerDataset
    * Parametros: ------
    * Retorna: dataset cargado en un arreglo
    * Funcionamiento:
    *    Lee el archivo CSV, convierte los valores string a float y guarda los datos en
    *    un arreglo
"""
def obtenerDataset():
    data = []#array donde se guardara el dataset
    clases = []#arreglo que contara el numero de clases en el dataset
    with open('dataset.csv', newline = '') as archivo:#se abre el archivo para lectura
        lineas = csv.reader(archivo, delimiter= ',')
        dataset = list(lineas)#se lista el dataset
        for x in range(len(dataset)-1):
            for y in range(13):
                dataset[x][y] = float(dataset[x][y])#se cambian los valores de strind a float
            clase = dataset[x][14]
            if(x == 0):
                clases.append(clase)
            if((clase in clases) == False):
                clases.append(clase)            
            data.append(dataset[x])#se guarda lainstancia en el data
        archivo.close()#se cierra la lectura
        print("\n          Información general")
        print("  Caracteristicas obtenidas: 14")
        print("  Clases: ")
        print(clases)
        print("  Total de clases: "+str(len(clases)))
        print("  Numero TOTAL de instancias: "+ str(len(dataset)))
    return data#se regresa el dataset
"""
    * Método distancia
    * Parametros: caracteristicas de la nueva IMG, instancia del dataset, tamaño de las caracteristicas
    * Retorna: distancia entre la nueva IMG y la instancia del dataset
    * Funcionamiento:
    *    Mide la distancia euclidiana entre las dos instancias dadas
"""
def distancia(nuevaIMG, dataset, tam):
    distancia = 0#variable donde se guardara la distancia
    for indice in range(tam):
        distancia += pow((nuevaIMG[indice] - dataset[indice]), 2)#se calcula la distancia
    return math.sqrt(distancia)#devuelve la distancia

"""
    * Método vecinos
    * Parametros: dataset, caracteristicas de la nueva IMG, numero K
    * Retorna: los k vecinos mas cercanos a la nueva img
    * Funcionamiento:
    *    Mide la distancia euclidiana entre la nueva imagen y todo el dataset, ordena los valores de
    *    menor a mayor y guarda los k vecinos mas cercanos en el arreglo
"""
def vecinos(dataset, nuevaIMG, k):
    instancia_dist = []#arreglo donde se guardara la instancia con la distancia con respecto de la nueva instancia
    tam = len(nuevaIMG)-1#numero de caracteristicas con las que se medira la distancia
    for indice in range(len(dataset)):
        dist = distancia(nuevaIMG,dataset[indice],tam)#se mide distancia
        instancia_dist.append((dataset[indice],dist))#se inserta la instancia agregandole la distancia
    instancia_dist.sort(key=operator.itemgetter(1))#ordena de menor a mayor
    vecinos = []#arreglo donde se guardaran los k vecinos mas cercanos
    for indice in range(k):
        vecinos.append(instancia_dist[indice][0])#se inserta la instancia
        print("Distancia: "+str(instancia_dist[indice][1])+" Linea: "+str(instancia_dist[indice][0][15])+" Vecino: "+ str(instancia_dist[indice][0][14]))#impresion informatica
    return vecinos#regresa los k vecinos más cercanos
"""
    * Método votacion
    * Parametros: k vecinos mas cercanos
    * Retorna: la clase a la cual pertenece la nueva imagen
    * Funcionamiento:
    *    Cuenta las insidencias de las clases para votar la que sea mayor
"""
def votacion(vecinos):
    instancias = {}
    print("\n       Resumen KNN")
    for x in range(len(vecinos)):
        resp = vecinos[x][-2]#se obtiene la clase de la instancia
        if resp in instancias:
            instancias[resp] += 1#se hace votacion
        else:
            instancias[resp] = 1
        #print(clases)
    print("    Instancia de la clase       Total")
    for keys,values in instancias.items():
        print("         "+str(keys)+"                        "+str(values))
    result = sorted(instancias.items(), key=operator.itemgetter(1), reverse=True)#ordena las clases de mayor a menor
    #print(clasifica[0][0])
    return result[0][0]#regresa la clase con mas coincidencias
"""
    * Método imgClasificar
    * Parametros: ruta de la imagen a procesar
    * Retorna: arreglo con las caracteristicas de la nueva img
    * Funcionamiento:
    *    Obtiene las 14 caracteristicas de la imagen
"""
def imgClasificar(ruta):
    caracteristicas = []#arreglo que contendra las caracteristicas de la imagen
    img = Image.open(ruta)#se abre imagen
    img2 = mpimg.imread(ruta)#se abre imagen
    c,f = img.size#se obtienen filas y columnas
    caracteristicas.append(caracteristica1(c,f))#llamada para obtener caracteristica 1
    caracteristicas.append(caracteristica2(img2,c,f))#llamada para obtener caracteristica 2
    caracteristicas.append(caracteristica3(img2,c,f))#llamada para obtener caracteristica 3
    caracteristicas.append(caracteristica4(img2,c,f))#llamada para obtener caracteristica 4
    caracteristicas.append(caracteristica5(img2,c,f))#llamada para obtener caracteristica 5
    caracteristicas.append(caracteristica6(img2,c,f))#llamada para obtener caracteristica 6
    caracteristicas.append(caracteristica7(img2,c,f))#llamada para obtener caracteristica 7
    caracteristicas.append(caracteristica8(img2,c,f))#llamada para obtener caracteristica 8
    caracteristicas.extend(caracteristica_cortes(img2,c,f))#llamada para obtener caracteristica 9,10,11,12,13
    return caracteristicas
    
opc = 0
while(opc != 3):
    print("\n     Menu")
    opc = int(input("1.- Generar dataset\n2.- Clasificación KNN\n3.- Salir\n    Opcion: "))
    if(opc == 1):
        crear = open('dataset.csv','w',newline='')#se crea el archivo dataset.csv
        write = csv.writer(crear,delimiter=',')#se especifica la escritura y un delimitador ';'
        recorrerArchivos()#llamada al metodo para recorrer archivos
        crear.close()#cierra la escritura
    elif(opc == 2):
        data =[]
        dataset =[]
        dataset = obtenerDataset()
        rutaIMG = 'C:/Users/Dashen/Documents/OCR_/pruebas/'#ruta por default de la img
        rutaIMG += input('Ingresa el nombre de la imagen a clasificar: ')
        rutaIMG +='.png'#concatena la extension de la imagen
        data = imgClasificar(rutaIMG)#obtiene las caracteristicas de la img
        k = int(input("Ingresa el número k: "))#pide el numero k
        clase = votacion(vecinos(dataset, data, k))#se realiza la clasificacion
        print("\nLa imagen es un simbolo: "+str(clase))#se imprime el resultado
        del dataset[:]#elimina el dataset
        