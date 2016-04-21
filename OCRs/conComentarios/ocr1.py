from PIL import Image
import matplotlib.image as mpimg
import csv
import os
import math
import operator

"""
# metodo: abrirImagen
# argumentos: ruta de la imagen, clase de la imagen
# retorno: -----------
# descripcion: Recibe la ruta de las imagenes, las abre y obtiene el tamaño de las filas y las columnas
#   llama al metodo "caracteristicas" para obtener las caracteristicas de la imagen y por ultimo
#   escribe la información en un archvo CSV
"""

def escribirData(ruta,clase,Nfila):
    data = []#data arregloq que contendra las caracteristicas
    img = Image.open(ruta)#se abre imagen
    img2 = mpimg.imread(ruta)#se abre imagen
    col,fil = img.size#se obtienen filas y columnas
    
    data.extend(caracteristicas(img2,fil,col))#obtiene las caracteristicas y las inserta en el data
    data.append(clase)#inserta la clase en el data
    data.append(Nfila)#inserta el numero de fila en el dataset en data
    escribir.writerow(data)#escribe
    
"""
# metodo: caracteristicas
# argumentos: imagen, filas, columnas
# retorno: arreglo con las caracteristicas obtenidas
# descripcion: obtiene 8 razones de la imagen, columnas/filas, numero de 1s en la imagen,
#   numero de 1s en las posiciones col/2, col/4, col3/4, fil/2, fil/4, fil3/4 y el numero de cortes
#   en la posicion col/2
"""
def caracteristicas(img,fil,col):
    data = []
    #caracteristica 1
    razon_tamaño_img = col/fil#se calcula razon
    data.append(razon_tamaño_img)#se inserta la caracteristica en el arreglo data
    
    #caracteristica 2
    contador = 0#contador
    for indicex in range(fil-1):
        for indicey in range(col-1):
            if(img[indicex][indicey] == 1):#se pregunta si el pixel es == 1
                contador += 1#aumenta contador
    unos_imagen = contador/(fil*col)
    data.append(unos_imagen)#se inserta la caracteristica en el arreglo data
    
    #caracteristica3   numero de 1s en las posiciones col/2,col/4,col(3/4),fil/2,fil/4,fil(3/4)
    arreglos = [0,0,0,0,0,0]#contador
    for x in range(fil):
        if(img[x][int(col/2)] == 1):#se pregunta si el pixel es == 1
            arreglos[0] += 1#aumenta contador
        if(img[x][int(col/4)] == 1):#se pregunta si el pixel es == 1
            arreglos[1] += 1#aumenta contador
        if(img[x][int(col*3/4)] == 1):#se pregunta si el pixel es == 1
            arreglos[2] += 1#aumenta contador
    
    for x in range(col):
        if(img[int(fil/2)][x] == 1):#se pregunta si el pixel es == 1
            arreglos[3] += 1#aumenta contador
        if(img[int(fil/4)][x] == 1):#se pregunta si el pixel es == 1
            arreglos[4] += 1#aumenta contador
        if(img[int(fil*3/4)][x] == 1):#se pregunta si el pixel es == 1
            arreglos[5] += 1#aumenta contador
    vec = [0.0,0.0,0.0,0.0,0.0,0.0]#vector que guarda la razon 
    for i in range(len(vec)):
        if(i<3):
            vec[i] = arreglos[i]/fil#se calcula la razon
        else:
            vec[i] = arreglos[i]/col#se calcula la razon
    data.extend(vec)#se insertan en el data la caracterisca 3
    
    corte = [0,0,0,0,0,0]#contador
    mcol = int(col/2)
    col_1_4 = int(col/4)
    col_3_4 = int(3*col/4)
    #a continuacion se calculan los cortes en las columnas
    for x in range(fil):
        if (x == 0 or x == (fil-1)):
            if(img[x][mcol] == 1):
                corte[0] += 1#aumenta contador
            if(img[x][col_1_4] == 1):#se pregunta si el pixel es == 1
                corte[1] += 1#aumenta contador
            if(img[x][col_3_4] == 1):#se pregunta si el pixel es == 1
                corte[2] += 1#aumenta contador
        if(img[x][mcol] != img[x-1][mcol] and x != 0):
            corte[0] += 1#aumenta contador
        if(img[x][col_1_4] != img[x-1][col_1_4] and x != 0):
            corte[1] += 1#aumenta contador
        if(img[x][col_3_4] != img[x-1][col_3_4] and x != 0):
            corte[2] += 1#aumenta contador

                
    mfil = int(fil/2)
    fil_1_4 = int(fil/4)
    fil_3_4 = int(3*fil/4)
    #a continuacion se calculan los cortes en las filas
    for x in range(col):
        if (x == 0 or x == (col-1)):
            if(img[mfil][x] == 1):#se pregunta si el pixel es == 1
                corte[3] += 1#aumenta contador
            if(img[fil_1_4][x] == 1):#se pregunta si el pixel es == 1
                corte[4] += 1#aumenta contador
            if(img[fil_3_4][x] == 1):#se pregunta si el pixel es == 1
                corte[5] += 1#aumenta contador
        if(img[mfil][x] != img[mfil][x-1] and x != 0):
            corte[3] += 1#aumenta contador
        if(img[fil_1_4][x] != img[fil_1_4][x-1] and x != 0):
            corte[4] += 1#aumenta contador
        if(img[fil_3_4][x] != img[fil_3_4][x-1] and x != 0):
            corte[5] += 1#aumenta contador
    #print(corte)
                   
    data.extend(corte)#se inserta la caracteristica en el arreglo data
    return data

"""
# Metodo: principal
# Argumentos: -----
# Retorno: --------
# Descripción: Realiza el recorrido de las carpetas pasando la ruta de las imagenes al metodo
#   escribirData
"""
def principal():
    cont = 0 #contador para saber el numero de linea en el dataset
    aux = 1 #contador para saber el numero de linea en el dataset
    x = 0
    for base, dirs, files in os.walk('C:/Users/jossepablo/Desktop/ocrA/imagenes'):#path de las carpetas con las imagenes     
        if cont > 0:
            print("Calculando caracteristicas de: "+ str(files[x][0]))
            for name in files:
                escribirData( (str(base)+'/'+name),name[0],aux)#se manda la ruta y clase al
                #metodo escribirData para generar el dataset
                aux += 1
            x +=1
        cont += 1#contador que nos indica el numero de fila en el dataset
    abrir.close()#se cierra la escritura
    print("\nDataSet creado!")

"""
# Metodo: knn
# Argumentos: -----
# Retorno: --------
# Descripción: Este metodo controla las funciones de clasificar, llamando a los diferentes metodos
#            en el orden correcto para realizar la clasificación de una imagen
"""
def knn():
    dataset = []#array que guardara el dataset
    nuevaImg = []#array que guardara las caracteristicas de la imagen
    print("Clasificación KNN")
    dataset = leerDataset()#se guarda el dataset en el array
    print("Dataset cargado")
    nuevaImg = nuevaInstancia()#se guardan las caracteristicas de la nueva imagen
    k = int(input("Escribe el numero K: "))#se solicita el numero k
    resultado = votacion(getVecinos(dataset,nuevaImg,k))#se realiza la clasificación
    print("      La imagen es: "+str(resultado))
    del dataset[:]

"""
# Metodo: leerDataset
# Argumentos: -----
# Retorno: dataset cargado
# Descripción: El siguiente metodo, lee el archivo csv que contiene el dataset, y devuelve la
#         información de un array
"""
def leerDataset():
    data = []#array donde se guardara el dataset
    todas = []
    with open('dataset.csv', newline = '') as miArchivo:#se abre el archivo para lectura
        linea = csv.reader(miArchivo, delimiter= ',')
        dataset = list(linea)#se lista el dataset
        for x in range(len(dataset)-1):
            for y in range(13):
                dataset[x][y] = float(dataset[x][y])#se cambian los valores de strind a float
            clase = dataset[x][14]
            if(x == 0):
                todas.append(clase)
            if((clase in todas)== False):
                todas.append(clase)            
            data.append(dataset[x])#se guarda lainstancia en el data
        miArchivo.close()#se cierra la lectura
        print("  .........................................................")
        print("          Información general")
        print("  Caracteristicas obtenidas: 14")
        print("  Clases: ")       
        print("  "+str(todas))
        print("  Total de clases: "+str(len(todas)))
        print("  Numero TOTAL de instancias: "+ str(len(dataset)))
        print("  ..........................................................")
        
    return data;#se regresa el dataset
"""
# Metodo: euclides
# Argumentos: caracteristicas de la nueva IMG, dataset, numero de caracteristicas
# Retorno: distancia entre las dos instancias recibidas
# Descripción: El siguiente metodo, mide la distancia euclidiana entre las instancias
#         dadas
"""
def euclides(nuevaImg,data,tam):
    distancia = 0#variable donde se guardara la distancia
    for x in range(tam):
        distancia += pow((nuevaImg[x] - data[x]), 2)#se calcula la distancia
    return math.sqrt(distancia)#devuelve la distancia
"""
# Metodo: getVecinos
# Argumentos: dataset, caracteristicas de la nueva IMG y el numero k
# Retorno: arreglo con los k vecinos mas cercanos
# Descripción: El siguiente metodo, recorre el dataset midiendo la distancia
#       euclidiana, guarda la nueva información en el array 'distancias' y despues
#       guarda los k vecinos mas cercanos en el arreglo vecinos
"""
def getVecinos(dataset,nuevaImg,k):
    distancias = []#arreglo donde se guardara la instancia con la distancia con respecto de la nueva instancia
    tam = len(nuevaImg)-1#numero de caracteristicas con las que se medira la distancia
    for indice in range(len(dataset)):
        dist = euclides(nuevaImg,dataset[indice],tam)#se mide distancia
        distancias.append((dataset[indice],dist))#se inserta la instancia agregandole la distancia
    distancias.sort(key=operator.itemgetter(1))#ordena de menor a mayor
    vecinos = []#arreglo donde se guardaran los k vecinos mas cercanos
    for indice in range(k):
        vecinos.append(distancias[indice][0])#se inserta la instancia
        print("Vecino: "+ str(distancias[indice][0][14])+" Distancia: "+str(distancias[indice][1])+" Linea: "+str(distancias[indice][0][15]))#impresion informatica
    return vecinos#regresa los k vecinos más cercanos
        
"""
# Metodo: votacion
# Argumentos: array con los vecinos mas cercanos
# Retorno: retorna la clase mayoria
# Descripción: El siguiente metodo, recorre el arreglo vecinos, buscando cuantas
#       veces se repiten las clases y devulve la clase mas repetida
"""
def votacion(vecinos):
    clases = {}
    print("\n     Resumen KNN")
    for x in range(len(vecinos)):
        resp = vecinos[x][-2]#se obtiene la clase de la instancia
        if resp in clases:
            clases[resp] += 1#se hace votacion
        else:
            clases[resp] = 1
    for clase,total in clases.items():#recorrido para las impresiones
        print("   Instancia de la clase: "+str(clase)+"      Total: "+str(total))
    clasifica = sorted(clases.items(), key=operator.itemgetter(1), reverse=True)#ordena las clases de mayor a menor
    return clasifica[0][0]#regresa la clase con mas coincidencias
"""
# Metodo: nuevaInstancia
# Argumentos: ------
# Retorno: las caracteristicas de la imagen especificada por el usuario
# Descripción: El siguiente metodo, obtiene las caracteristicas de la imagen especifi-
#      cada por el usuario y las guarda en un arraglo 'data'
"""
def nuevaInstancia():
    ruta = 'C:/Users/jossepablo/Desktop/ocrA/prueba/'
    ruta += input("Ingresa el nombre de la imagen: ")
    ruta += '.png'#se concatena la extencion de la imagen
    img = Image.open(ruta)#se abre imagen
    img2 = mpimg.imread(ruta)#se abre imagen
    col,fil = img.size#se obtienen filas y columnas
    data = caracteristicas(img2,fil,col)#se guardan las caracteristicas de la imagen
    return data

#menu de ejecucion
opc = 1
while(opc != 3 ):
    print("Menu")
    opc = int(input("   1.- Crear DataSet\n   2.- KNN\n   3.- Salir\n Opción: "))
    if(opc == 1):
        abrir = open('dataset.csv','w',newline='')#se crea el archivo dataset.csv
        escribir = csv.writer(abrir,delimiter=',')#se especifica la escritura y un delimitador ','
        principal()#se ejecuta el metodo principal
    elif(opc == 2):
        knn()#clasificacion knn
    else:
        print("     Adios!")
        