# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
#Librerias a utlizar en la aplicación
#---------------------------------------------------------------------------
#librería utilizada para abrir archivos, la cual se utilizara para leer 
#las imágenes del dataSet
import os
#libreria que permite abrir imagenes
import matplotlib.image as mpimg
from PIL import Image
import math
#libreria para crear el archivo csv donde se almacenaran las propiedades de 
#las imagenes de los numeros
import csv
#---------------------------------------------------------------------------
#Declaracion de matriz y variables globales a utilizar en la aplicación
#---------------------------------------------------------------------------
#variable para recorrer las filas de la matriz en las funciones
#alto = 0
#variable para recorrer las columnas de la matriz en las funciones
#ancho = 0
#matriz temporal donde se almacenaran las propiedades de las imagenes
matriz = []
#variable que contendra el conteo de los vecinos con respecto a 0
contadorCero = 0
#variable que contendra el conteo de los vecinos con respecto a 1
contadorUno = 0
#variable que contendra el conteo de los vecinos con respecto a 2
contadorDos = 0
#variable que contendra el conteo de los vecinos con respecto a 3
contadorTres = 0
#variable que contendra el conteo de los vecinos con respecto a 4
contadorCuatro = 0
#variable que contendra el conteo de los vecinos con respecto a 5
contadorCinco = 0
#variable que contendra el conteo de los vecinos con respecto a 6
contadorSeis = 0
#variable que contendra el conteo de los vecinos con respecto a 7
contadorSiete = 0
#variable que contendra el conteo de los vecinos con respecto a 8
contadorOcho = 0
#variable que contendra el conteo de los vecinos con respecto a 9
contadorNueve = 0
#variable de avance las filas de la matriz a llenar con los datos
x = 0
#variable de avance las columnas de la matriz a llenar con los datos
y = 0
contadorClase = 0
#---------------------------------------------------------------------------
#Llenamos la matriz con ceros que vamos a utlizar para almacenar los datos
#---------------------------------------------------------------------------
#este ciclo llena la matriz con ceros
for i in range(2369):
    #llenamos la matriz con ceros y creamos las columnas
    matriz.append([0.0]*15)

#---------------------------------------------------------------------------        
#nombre: ObtenerPropiedad1
#descripcion: Obtiene la relacion del numero de 1´s entre los pixeles 
#             de la imagen es decir relacion=#1´s/(#filas)(#columnas)
#argumentos de entrada: img, representa una imagen
#retorno: la relación = #1´s/(#filas)(#columnas) es flotante
#---------------------------------------------------------------------------
def obtenerPropiedad1(img,alto,ancho):
    #variables con las que se va a recorrer el for    
    contadorDeUnos = 0
    #este ciclo nos sirve para la cantidad de unos que existen en la imagen
    for a in range(alto):
        for b in range(ancho):
            #almacenamos en la variable num los datos de la matriz
            dato = (int(img[a][b]))
            #comparamos la variable dato si es equivalente a un 1            
            if dato!=1:
                #contador de los unos que encuentra
                contadorDeUnos = contadorDeUnos+1
    #retornamos la varible contadorUnos para ser almacenada en la matriz
    return contadorDeUnos/(alto*ancho)

#---------------------------------------------------------------------------
#nombre: obtenerPropiedad2
#descripcion: obtiene la relacion entre el numero de filas y columnas 
#             de la imagen es decir relacion=(#filas)/(#columnas)
#argumentos de entrada: img, representa una imagen
#retorno: la promedio = (#filas)/(#columnas) es flotante
#---------------------------------------------------------------------------
def obtenerPropiedad2(img,alto,ancho):
    #obtenemos un promedio de filas y columnas que almacenamos
    #en la variable prom    
    prom = ancho/alto
    #retornamos prom para ser almacenado en la matriz
    return prom

#---------------------------------------------------------------------------
#nombre: obtenerPropiedad3
#descripcion: obtiene la relacion del numero de 1´s entre los pixeles 
#             de la fila intermedia de la imagen
#argumentos de entrada: img representa una imagen, 
#retorno: promedio de 1's con respecto a la fila intermedia de la
#         matriz de la imagen
#--------------------------------------------------------------------------- 
def obtenerPropiedad3(img,alto,ancho):
    #obtenemos la fila que se encuentra en medio de la matriz de la imagen
    filaIntermedia = int(ancho/2)
    #declaramos la variable que contara los 1´s de la fila intermedia
    contadorDeUnos = 0
    #ciclo que nos ayuda a recorrer dicha fila
    for al in range(alto):
        #declaramos la variable que encuntra a los 1´s en la fila
        dato = (int(img[al][filaIntermedia]))
        #condicion para saber si es un 1 el dato de la fila
        if dato == 1:
            #contamos los 1´s que existen en la fila intermedia
            contadorDeUnos = contadorDeUnos+1
    #retornamos la cantidad de 1´s en la variable contadorDeUnos
    return contadorDeUnos/(alto*ancho)
    
#---------------------------------------------------------------------------
#nombre: ObtenerPropiedad4
#descripcion: Obtiene la relacion del numero de 1´s entre los pixeles de 
#             1/4 de fila de la imagen
#argumentos de entrada: img, representa una imagen
#retorno: cantidad de 1's en 1/4 de fila
#---------------------------------------------------------------------------
def obtenerPropiedad4(img,alto,ancho):
    #obtenemos la fila que se encuentra en 1/4 de la matriz de la imagen
    filaUnCuarto= int(ancho/4)
    #declaramos la variable que contara los 1´s de la fila 1/4
    contadorDeUnos = 0
    #ciclo que nos ayuda a recorrer dicha fila
    for al in range(alto):
        #declaramos la variable que encuentra a los 1´s en la fila
        dato = (int(img[al][filaUnCuarto]))
        #condicion para saber si es un 1 el dato de la fila
        if dato == 1:
            #contamos los 1´s que existen en la fila intermedia
           contadorDeUnos = contadorDeUnos+1
    #retornamos la cantidad de 1´s en la variable contadorDeUnos
    return contadorDeUnos/(alto*ancho)

#---------------------------------------------------------------------------
#nombre: ObtenerPropiedad5
#descripcion: Obtiene la relacion del numero de 1´s entre los pixeles 
#             a 3/4 de fila de la imagen
#argumentos de entrada: img, representa una imagen
#retorno: Cantidad de 1's en 3/4 de fila 
#---------------------------------------------------------------------------
def obtenerPropiedad5(img,alto,ancho):
    #obtenemos la fila que se encuentra a 3/4 de la matriz de la imagen
    filaTresCuartos = int((int(ancho/4))*3)
    #declaramos la variable que contara los 1´s de la fila 3/4
    contadorDeUnos = 0
    #ciclo que nos ayuda a recorrer dicha fila
    for al in range(alto):
        #declaramos la variable que encuentra a los 1´s en la fila
        dato = (int(img[al][filaTresCuartos]))
        #condicion para saber si es un 1 el dato de la fila
        if dato == 1:
            #contamos los 1´s que existen en la fila 3/4
            contadorDeUnos = contadorDeUnos+1
    #retornamos la cantidad de 1´s en la variable contadorDeUnos
    return contadorDeUnos/(alto*ancho)

#---------------------------------------------------------------------------
#nombre: ObtenerPropiedad6
#descripcion: Obtiene la relacion del numero de 1´s entre los pixeles 
#             de la columna intermedia de la imagen
#argumentos de entrada: img, representa una imagen
#retorno: Cantidad de 1's en la columna intermedia de la imagen 
#---------------------------------------------------------------------------
def obtenerPropiedad6(img,alto,ancho):
    #obtenemos la columna intermedia de la matriz de la imagen
    colItermedia = int(alto/2)
    #declaramos la variable que contara los 1´s de la columna intermedia
    contadorDeUnos = 0
    #ciclo para recorrer las filas de la matriz
    for fil in range(alto):
        #ciclo para recorrer las columas de la matriz
        for col in range(ancho):
            #condicion para saber si las columna es la del 1/4
            if fil == colItermedia:
                #alamacenamos el dato que obtenemos de la matriz
                dato = (int(img[colItermedia][col]))
                #condicion para saber si es un 1 el dato de la columna
                if dato == 1:
                    #contamos los 1´s que existen en la columna intermedia
                    contadorDeUnos = contadorDeUnos+1
    #retornamos la cantidad de 1´s en la variable contadorDeUnos
    return contadorDeUnos/(alto*ancho)

#---------------------------------------------------------------------------
#nombre: ObtenerPropiedad7
#descripcion: Obtiene la relacion del numero de 1´s entre los pixeles 
#             a 1/4 de la columna de la imagen
#argumentos de entrada: img, representa una imagen
#retorno: Cantidad de 1's a 1/4 de  columna de la imagen  
#---------------------------------------------------------------------------
def obtenerPropiedad7(img,alto,ancho):
    #obtenemos la columna que se encuentra en 1/4 de la matriz de la imagen
    columnaUnCuarto = int(alto/4)
    #declaramos la variable que contara los 1´s de la columna 1/4
    contadorDeUnos = 0
    #ciclo para recorrer las filas de la matriz
    for fil in range(alto):
        #ciclo para recorrer las columnas de la matriz
        for col in range(ancho):
            #condicion que compara la columna con la columna 1/4
            if fil == columnaUnCuarto:
                #declaramos la variable que encuentra a los 1´s en la columna
                dato = (int(img[columnaUnCuarto][col]))
                #condicion para saber si es un 1 el dato de la columna
                if dato == 1:
                    #contamos los 1´s que existen en la columna 1/4
                    contadorDeUnos = contadorDeUnos+1
    #retornamos la cantidad de 1´s en la variable contadorDeUnos
    return contadorDeUnos/(alto*ancho)

#---------------------------------------------------------------------------
#nombre: obtenerPropiedad8
#descripcion: obtiene la relacion del numero de 1´s entre los pixeles
#                     a 3/4 de la columna de la imagen
#argumentos de entrada: img, representa una imagen
#retorno: cantidad de 1's a 3/4 de  columna de la imagen
#---------------------------------------------------------------------------
def obtenerPropiedad8(img,alto,ancho):
    #obtenemos la fila que se encuentra a 3/4 de la matriz de la imagen
    colTresCuartos = int((int(alto/4))*3)
    #declaramos la variable que contara los 1´s de la columna 3/4
    contadorDeUnos = 0
    #ciclo para recorrer las filas de la matriz
    for fil in range(alto):
        #ciclo para recorrer las columnas de la matriz
        for col in range(ancho):
            #condicion que compara la columna con la columna 3/4
            if fil == colTresCuartos:
                #declaramos la variable que encuentra a los 1´s en la columna
                dato = (int(img[fil][col]))
                #condicion para saber si es un 1 el dato de la columna
                if dato == 1:
                    #contamos los 1´s que existen en la columna 1/4
                    contadorDeUnos = contadorDeUnos+1
    #retornamos la cantidad de 1´s en la variable contadorDeUnos
    return contadorDeUnos/(alto*ancho)

#---------------------------------------------------------------------------
#nombre: obtenerPropiedad9
#descripcion: obtiene la cantidad de cortes  entre 0´s y 1´s de la fila 
#             intermedia de la imagen
#argumentos de entrada: img, representa una imagen
#retorno: cantidad de cortes entre 1´s y 0´s a mitad de  fila de la imagen
#---------------------------------------------------------------------------
def obtenerPropiedad9(img,alto,ancho):
    #obtenemos la fila intermedia de la matriz de la imagen
    columnaIntermedia = int(ancho/2)
    #obtenemos el numero de cortes de la matriz de la imagen
    contadorDeCortes = 0
    #variable de referencia para hacer el corte
    corte = 0
    #ciclo que recorre la matriz para obtener los cortes
    for fil in range(alto):
        #obtenemos el dato de la matriz
        dato = (int(img[fil][columnaIntermedia]))
        #comparamos el dato con el corte
        if dato!=corte:
            #contamos el corte que se produjo
            contadorDeCortes = contadorDeCortes+1
            #corte = (int(img[fil][columnaIntermedia]))
    #retorna el numero de cortes de la imagen (matriz)
    return contadorDeCortes/(alto*ancho)

#---------------------------------------------------------------------------
#nombre: obtenerPropiedad10
#descripcion: obtiene la cantidad de cortes  entre 0´s y 1´s en 1/4 de fila  
#             de la imagen
#argumentos de entrada: img, representa una imagen
#retorno: cantidad de cortes entre 1´s y 0´s a 1/4 de  fila de la imagen 
#---------------------------------------------------------------------------
def obtenerPropiedad10(img,alto,ancho):
    #obtenemos la fila que se encuentra en 1/4 de la matriz de la imagen
    filaUnCuarto = int(ancho/4)
    #obtenemos el numero de cortes de la matriz de la imagen
    contadorDeCortes = 0
    #variable de referencia para hacer el corte
    corte = 0
    #ciclo que recorre la matriz para obtener los cortes
    for fil in range(alto):
        #obtenemos el dato de la matriz
        dato = (int(img[fil][filaUnCuarto]))
        #comparamos el dato con el corte
        if dato!=corte:
            #contamos el corte que se produjo
            contadorDeCortes = contadorDeCortes+1
            #corte=(int(img[fil][filaUnCuarto]))
    #retorna el numero de cortes de la imagen (matriz)
    return contadorDeCortes/(alto*ancho)

#---------------------------------------------------------------------------
#nombre: obtenerPropiedad11
#descripcion: obtiene la cantidad de cortes  entre 0´s y 1´s en 3/4 de fila  
#             de la imagen
#argumentos de entrada: img, representa una imagen
#retorno: cantidad de cortes entre 1´s y 0´s a 3/4 de  fila de la imagen
#---------------------------------------------------------------------------
def obtenerPropiedad11(img,alto,ancho):
    #obtenemos la columna que se encuentra a 3/4 de la matriz de la imagen
    col = int((int(ancho/4))*3)
    #obtenemos el numero de cortes de la matriz de la imagen
    contadorDeCortes = 0
    #variable de referencia para hacer el corte
    corte = 0
    #ciclo que recorre la matriz para obtener los cortes
    for al in range(alto):
        #obtenemos el dato de la matriz
        dato = (int(img[al][col]))
        #comparamos el dato con el corte
        if dato!=corte:
            #contamos el corte que se produjo
            contadorDeCortes = contadorDeCortes+1
            #corte = (int(img[al][col]))
    #retorna el numero de cortes de la imagen (matriz)
    return contadorDeCortes/(alto*ancho)

#---------------------------------------------------------------------------
#nombre: obtenerPropiedad12
#descripcion: obtiene la cantidad de cortes  entre 0´s y 1´s de la columna
#             intermedia de la imagen
#argumentos de entrada: img, representa una imagen
#retorno: cantidad de cortes entre 1´s y 0´s a mitad de la columna de la imagen
#---------------------------------------------------------------------------
def obtenerPropiedad12(img,alto,ancho):
    #obtenemos la fila intermedia de la matriz de la imagen
    columaIntermedia = int(alto/2)
    #obtenemos el numero de cortes de la matriz de la imagen
    contadorDeCortes = 0
    #variable de referencia para hacer el corte
    corte = 0
    #ciclo para recorrer las filas de la matriz
    for an in range(alto):
        #ciclo para recorrer las columnas de la matriz
        for an2 in range(ancho):
            #condicion para encontrar la columna intermedia
            if an==columaIntermedia:
                #obtenemos el dato de la matriz
                dato = (int(img[columaIntermedia][an2]))
                #comparamos el dato con el corte
                if dato!=corte:
                    #contamos el corte que se produjo
                    contadorDeCortes = contadorDeCortes+1
                    #corte = (int(img[columaIntermedia][an2]))
    #retorna el numero de cortes de la imagen (matriz)
    return contadorDeCortes/(alto*ancho)

#---------------------------------------------------------------------------
#nombre: obtenerPropiedad13
#descripcion: obtiene la cantidad de cortes  entre 0´s y 1´s en 1/4 de la 
#             columna de la imagen
#argumentos de entrada: img, representa una imagen
#retorno: cantidad de cortes entre 1´s y 0´s a 1/4 de la columna de la imagen
#---------------------------------------------------------------------------
def obtenerPropiedad13(img,alto,ancho):
    #obtenemos la fila que se encuentra en 1/4 de la matriz de la imagen
    columnaUnCuarto = int(alto/4)
    #obtenemos el numero de cortes de la matriz de la imagen
    contadorDeCortes = 0
    #variable de referencia para hacer el corte
    corte = 0
    #ciclo para recorrer las filas de la matriz
    for fil in range(alto):
        #ciclo para recorrer las columnas de la matriz
        for col in range(ancho):
            #condicion para encontrar la columna 1/4
            if fil == columnaUnCuarto:
                #obtenemos el dato de la matriz
                dato = (int(img[columnaUnCuarto][col]))
                #comparamos el dato con el corte
                if dato!=corte:
                    #contamos el corte que se produjo
                    contadorDeCortes = contadorDeCortes+1
                    #corte = (int(img[al][an2]))
    #retorna el numero de cortes de la imagen (matriz)
    return contadorDeCortes/(alto*ancho)

#---------------------------------------------------------------------------
#nombre: obtenerPropiedad14
#descripcion: obtiene la cantidad de cortes  entre 0´s y 1´s en 3/4 de la 
#             columna de la imagen
#argumentos de entrada: img, representa una imagen, alto y ancho
#retorno: cantidad de cortes entre 1´s y 0´s a 3/4 de la columna de la imagen
#---------------------------------------------------------------------------
def obtenerPropiedad14(img,alto,ancho):
    #obtenemos la columna que se encuentra a 3/4 de la matriz de la imagen
    columnaTresCuartos = int((int(alto/4))*3)
    #obtenemos el numero de cortes de la matriz de la imagen
    contadorDeCortes = 0
    #variable de referencia para hacer el corte
    corte = 0
    #ciclo para recorrer las filas de la matriz
    for fil in range(alto):
        #ciclo para recorrer las columnas de la matriz
        for col in range(ancho):
            #condicion para encontrar la columna 3/4
            if fil == columnaTresCuartos:
                #obtenemos el dato de la matriz
                dato = (int(img[columnaTresCuartos][col]))
                #comparamos el dato con el corte
                if dato!=corte:
                    #contamos el corte que se produjo
                    contadorDeCortes = contadorDeCortes+1
                    #corte = (int(img[columnaTresCuartos][col]))
    #retorna el numero de cortes de la imagen (matriz)   
    return contadorDeCortes/(alto*ancho)

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
def kNN(img, numVeci):
   #leemos la imagen de entrada 
    imgc = mpimg.imread(img)
    #creamos la matriz de para almacenar los datos de la imagen de entrada
    mat = []
    #matriz para los vecinos mas cercanos
    knn = []
    #contador para recorrer las columnas
    cont = 0

    #obtenemos informacion de la imagen
    imgCoFi = Image.open(img)
    #obtenemos filas y columnas de la imagen
    (fil,col) = imgCoFi.size
    #ciclo que recorre la matriz
    for x in range(2369+1):
        #llenamos la matriz con ''
        mat.append(['']*15)
    #ciclo que recorre la matriz de knn 
    for x in range(2369):
        #llenamos la matriz con '' para almacenar la distancia y la clase
        knn.append(['']*3)
    #leemos el archivo del dataSet
    reader = csv.reader(open('dataSet.csv'))
    #ciclo que llena la matriz con los datos del dataSet
    for index,row in enumerate(reader):
        #cliclo que recorre las columnas 
        for cont in range(15):
            #llenado de matriz con el archivo
            mat[index][cont] = row[cont]
    #Aqui se llama a la funcion obtenerPropiedad1 para que nos devuelva 
    #la propiedad1 de la nueva instancia
    i2P1 = obtenerPropiedad1(imgc,col,fil)
    #Aqui se llama a la funcion obtenerPropiedad2 para que nos devuelva 
    #la propiedad2 de la nueva instancia
    i2P2=obtenerPropiedad2(imgc, col,fil)               
    #Aqui se llama a la funcion obtenerPropiedad3 para que nos devuelva 
    #la propiedad3 de la nueva instancia
    i2P3=obtenerPropiedad3(imgc, col,fil)               
    #Aqui se llama a la funcion obtenerPropiedad4 para que nos devuelva 
    #la propiedad4 de la nueva instancia
    i2P4=obtenerPropiedad4(imgc, col,fil)               
    #Aqui se llama a la funcion obtenerPropiedad5 para que nos devuelva 
    #la propiedad5 de la nueva instancia
    i2P5=obtenerPropiedad5(imgc, col,fil)               
    #Aqui se llama a la funcion obtenerPropiedad6 para que nos devuelva 
    #la propiedad6 de la nueva instancia
    i2P6=obtenerPropiedad6(imgc, col,fil)               
    #Aqui se llama a la funcion obtenerPropiedad7 para que nos devuelva 
    #la propiedad7 de la nueva instancia
    i2P7=obtenerPropiedad7(imgc, col,fil)               
    #Aqui se llama a la funcion obtenerPropiedad8 para que nos devuelva 
    #la propiedad8 de la nueva instancia
    i2P8=obtenerPropiedad8(imgc, col,fil)              
    #Aqui se llama a la funcion obtenerPropiedad9 para que nos devuelva 
    #la propiedad9 de la nueva instancia
    i2P9=obtenerPropiedad9(imgc, col,fil)               
    #Aqui se llama a la funcion obtenerPropiedad10 para que nos devuelva 
    #la propiedad10 de la nueva instancia
    i2P10=obtenerPropiedad10(imgc, col,fil)             
    #Aqui se llama a la funcion obtenerPropiedad11 para que nos devuelva 
    #la propiedad11 de la nueva instancia
    i2P11=obtenerPropiedad11(imgc, col,fil)             
    #Aqui se llama a la funcion obtenerPropiedad12 para que nos devuelva 
    #la propiedad12 de la nueva instancia
    i2P12=obtenerPropiedad12(imgc, col,fil)             
    #Aqui se llama a la funcion obtenerPropiedad13 para que nos devuelva 
    #la propiedad13 de la nueva instancia
    i2P13=obtenerPropiedad13(imgc, col,fil)            
    #Aqui se llama a la funcion obtenerPropiedad14 para que nos devuelva 
    #la propiedad14 de la nueva instancia
    i2P14=obtenerPropiedad14(imgc, col,fil)             
    #ciclo para recorrer y obtener las caracteristicas del dataSet 
    for val in range(2369):
        #obtenemos propiedad 1 del dataSet
        p1 = float(mat[val+1][0])
        #obtenemos propiedad 2 del dataSet        
        p2 = float(mat[val+1][1])
        #obtenemos propiedad 3 del dataSet
        p3 = float(mat[val+1][2])
        #obtenemos propiedad 4 del dataSet
        p4 = float(mat[val+1][3])
        #obtenemos propiedad 5 del dataSet
        p5 = float(mat[val+1][4])
        #obtenemos propiedad 6 del dataSet
        p6 = float(mat[val+1][5])
        #obtenemos propiedad 7 del dataSet
        p7 = float(mat[val+1][6])
        #obtenemos propiedad 8 del dataSet
        p8 = float(mat[val+1][7])
        #obtenemos propiedad 9 del dataSet
        p9 = float(mat[val+1][8])
        #obtenemos propiedad 10 del dataSet        
        p10 = float(mat[val+1][9])
        #obtenemos propiedad 11 del dataSet
        p11 = float(mat[val+1][10])
        #obtenemos propiedad 12 del dataSet
        p12 = float(mat[val+1][11])
        #obtenemos propiedad 13 del dataSet
        p13 = float(mat[val+1][12])
        #obtenemos propiedad 14 del dataSet
        p14 = float(mat[val+1][13])
        #aplicamos la formula euclidiana
        dist = math.sqrt(((p1-i2P1)**2)+((p2-i2P2)**2)+((p3-i2P3)**2)+((p4-i2P4)**2)+((p5-i2P5)**2)+((p6-i2P6)**2)+((p7-i2P7)**2)+((p8-i2P8)**2)+((p9-i2P9)**2)+((p10-i2P10)**2)+((p11-i2P11)**2)+((p12-i2P12)**2)+((p13-i2P13)**2)+((p14-i2P14)**2))
        #almacenamos la distancia de la formula y lo almacenamos en la matriz knn        
        knn[val][0] = val+1
        knn[val][1] = dist
        #almacena la clase a la que pertenece
        knn[val][2] = mat[val+1][14]
    #matriz para datos del knn
    res=[]
    #ciclo que crea la matriz con ceros
    for x in range(numVeci):
        #llenado de matriz con ceros decimales
        res.append([0.0]*3)
    #obtenemos el numero de elementos de knn la cual contiene la distancia y
    #la posicion en el dataSet
    elementos = knn
    #apuntador para alamacenar distancia, posicion dataSet y la clase 
    apun = 0
    for i in range(numVeci):
        temp = elementos[0][1]
        numero = len(elementos)
        for j in range(numero):
            if(elementos[j][1] < temp):
                temp = elementos[j][1]
                apun = j 
            if (j+1==numero):
                res[i][0] = elementos[apun][0]
                res[i][1] = elementos[apun][1]
                res[i][2] = elementos[apun][2]
                elementos.pop(apun)
    #regresamos el conjunto de elementos que son distancia, posicion y clase
    return res
#---------------------------------------------------------------------------
#Inicio del main de la aplicación
#---------------------------------------------------------------------------
#obtenemos el directorio (carpeta) de los archivos
rootDir = 'dataSet'
#variable para concatenar la direccion de los archivos
name=''
#ciclo para recorrer los directorios de los archivos que se utilizaran 
#para la obtencion de sus caracteristicas 
for directorio, subDir, listaArchivos in os.walk(rootDir):
    #imprimimos el prosicionamiento de las carpetas    
    #print('Directorio encontrado: %s' % directorio)
    #ciclo que obtiene los archivos (imagenes) en la lista de fileList    
    for archivo in listaArchivos:
        #almacenamos en la variable name la ruta del archivo        
        rutaArchivo = directorio+"/"+archivo
        #leemos los datos de la imagen y lo almacenamos en la variable img
        imgCF = Image.open(rutaArchivo)
        #lemos las filas y columnas de imagen
        img = mpimg.imread(rutaArchivo)
        
        #obtenemos el tamaño de la imagen y almacenamos en la variable tam
        (ancho,alto) = imgCF.size
        #almacenamos los datos en la matriz que devuelve la 
        #funcion obtenerPropiedad1         
        matriz[x][y] = obtenerPropiedad1(img,alto,ancho)
        #con esta linea avanzamos entre las columnas de la matriz
        y = y+1
        #almacenamos los datos en la matriz que devuelve la 
        #funcion obtenerPropiedad2
        matriz[x][y] = obtenerPropiedad2(img,alto,ancho)
        #con esta linea avanzamos entre las columnas de la matriz
        y = y+1
        #almacenamos los datos en la matriz que devuelve la 
        #funcion obtenerPropiedad3
        matriz[x][y] = obtenerPropiedad3(img,alto,ancho)
        #con esta lienea avancamos entre las columnas de la matriz
        y = y+1
        #almacenamos los datos en la matriz que devuelve la 
        #funcion obtenerPropiedad4
        matriz[x][y] = obtenerPropiedad4(img,alto,ancho)
        #con esta linea avanzamos entre las columnas de la matriz
        y = y+1
        #almacenamos los datos en la matriz que devuelve la 
        #funcion obtenerPropiedad5
        matriz[x][y] = obtenerPropiedad5(img,alto,ancho)
        #con esta linea avanzamos entre las columnas de la matriz
        y = y+1
        #almacenamos los datos en la matriz que devuelve la 
        #funcion obtenerPropiedad6
        matriz[x][y] = obtenerPropiedad6(img,alto,ancho)
        #con esta linea avanzamos entre las columnas de la matriz
        y = y+1
        #almacenamos los datos en la matriz que devuelve la 
        #funcion obtenerPropiedad7
        matriz[x][y] = obtenerPropiedad7(img,alto,ancho)
        #con esta linea avanzamos entre las columnas de la matriz
        y = y+1
        #almacenamos los datos en la matriz que devuelve la 
        #funcion obtenerPropiedad8
        matriz[x][y] = obtenerPropiedad8(img,alto,ancho)
        #con esta linea avanzamos entre las columnas de la matriz
        y = y+1
        #almacenamos los datos en la matriz que devuelve la 
        #funcion obtenerPropiedad9
        matriz[x][y] = obtenerPropiedad9(img,alto,ancho)
        #con esta linea avanzamos entre las columnas de la matriz
        y = y+1
        #almacenamos los datos en la matriz que devuelve la 
        #funcion obtenerPropiedad10
        matriz[x][y] = obtenerPropiedad10(img,alto,ancho)
       #con esta linea avanzamos entre las columnas de la matriz
        y = y+1
        #almacenamos los datos en la matriz que devuelve la 
        #funcion obtenerPropiedad11
        matriz[x][y] = obtenerPropiedad11(img,alto,ancho)
        #con esta linea avanzamos entre las columnas de la matriz
        y = y+1
        #almacenamos los datos en la matriz que devuelve la 
        #funcion obtenerPropiedad12
        matriz[x][y] = obtenerPropiedad12(img,alto,ancho)
        #con esta linea avanzamos entre las columnas de la matriz
        y = y+1
        #almacenamos los datos en la matriz que devuelve la 
        #funcion obtenerPropiedad13
        matriz[x][y] = obtenerPropiedad13(img,alto,ancho)
        #con esta linea avanzamos entre las columnas de la matriz
        y = y+1
        #almacenamos los datos en la matriz que devuelve la 
        #funcion obtenerPropiedad14
        matriz[x][y] = obtenerPropiedad14(img,alto,ancho)
        #con esta lienea avancamos entre las columnas de la matriz+
        y = y+1
        matriz[x][y] = contadorClase-1
        #incrementamos x para saltar de fila
        x = x+1
        #volvemos a cero y para volver a recorrer las columnas de la matriz
        y = 0
    contadorClase = contadorClase+1
    
#---------------------------------------------------------------------------
#Generacón del dataSet de la aplicación (Archivo csv)
#---------------------------------------------------------------------------
#pasamos los datos de la matriz a la variable datosMatriz
datosMatriz = matriz
#creamos el documento en donde escribiremos los datos 
csvOut = open('dataSet.csv','w',newline='')
#mandamos a escribir los datos como parametro de la libreria csv
out = csv.writer(csvOut)
#escribimos en el documento las celdas con los nombres (titulos de propiedades)
out.writerow(["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P11","P12",
              "P13","P14","Clase"])
#finalmente escribimos la matriz de datos en el documento csv
out.writerows(datosMatriz)
#eliminamos la salida del documento
del out
#cerramos el archivo que escribimos con los datos
csvOut.close()
#----------------------------------------------------------------------------
#Lectura del dataSet y solicitud de imagen para encontrar su vencidad con knn
#----------------------------------------------------------------------------
#ingresamos el nombre de la imagen 
nomImg = input('Nombre de la imagen a buscar: ')
#ingresamos el numero de vecinos
numVeci = int(input('Número de vecinos: '))
#almacenamos el nombre de la imagen
nomImg = nomImg+".png"
#mandamos el nobre de la imagen a la funcion knn
mat = kNN(nomImg, numVeci)
#----------------------------------------------------------------------------
#Se muestran los datos que se genran en el dataSet como: Propiedades, numero
#de clases, total de vecinos, etc.
#----------------------------------------------------------------------------
print("******************************************************************")
#imprimimos numero de instancias en el dataSet
print("Numero de instancias en el dataSet: "+str(2369))
#Imprimimos el numero de propiedades generadas para las instancias del dataSet
print("Numero de propiedades (Caracteristicas): "+str(14))
#Se imprime el total de las clases
print("Numero de clases: "+str(10))
#Mostramos el las clases que existen e en el dataSet
print("Clases; 0, 1, 2, 3, 4, 5, 6, 7, 8, 9")
print("******************************************************************")
print("")
print("******************************************************************")
#imprimimos vesino ,as cercano, posición del dataSet, Clase a la que pertenece
#distancia de la formula euclidiana
print("Vecino: \t"+"Posición dataSet: \t"+"Clase: \t"+"Distancia:\t")
#ciclo que imprime lo ya mencionado del dataSet
for va in range(numVeci):
#imprimimos vesino ,as cercano, posición del dataSet, Clase a la que pertenece
#distancia de la formula euclidiana    
    print(str(va+1)+"\t"+str(mat[va][0])+" \t\t"+str(mat[va][2])+
           "\t"+"%.10f"%mat[va][1])
    #comparamos el dato para generar el conteo de vesinos de 0
    if(mat[va][2]=='0'):
        contadorCero = contadorCero+1
    #comparamos el dato para generar el conteo de vesinos de  1   
    elif(mat[va][2]=='1'):
        contadorUno = contadorUno+1
    #comparamos el dato para generar el conteo de vesinos de 2
    elif(mat[va][2]=='2'):
        contadorDos = contadorDos+1
    #comparamos el dato para generar el conteo de vesinos de 3
    elif(mat[va][2]=='3'):
        contadorTres = contadorTres+1
    #comparamos el dato para generar el conteo de vesinos de 4
    elif(mat[va][2]=='4'):
        contadorCuatro = contadorCuatro+1
    #comparamos el dato para generar el conteo de vesinos de 5
    elif(mat[va][2]=='5'):
        contadorCinco = contadorCinco+1
    #comparamos el dato para generar el conteo de vesinos de 6
    elif(mat[va][2]=='6'):
        contadorSeis = contadorSeis+1
    #comparamos el dato para generar el conteo de vesinos de 7
    elif(mat[va][2]=='7'):
        contadorSiete = contadorSiete+1
    #comparamos el dato para generar el conteo de vesinos de 8
    elif(mat[va][2]=='8'):
        contadorOcho = contadorOcho+1
    #comparamos el dato para generar el conteo de vesinos de 9 
    elif(mat[va][2]=='9'):
        contadorNueve = contadorNueve+1        
print("******************************************************************")
print("")
print("******************************************************************")
#se imprime el total de instancias en el dataSet, la clase y la cantidad de
#vecinos que previamente contamos para cada clase
print("Instancias:\t "+"Clase:\t"+"Vecinos encontrados: ")
#se improme la clase y contador de 0
print(str(237)+"\t "+"0"+"\t"+str(contadorCero))
#se improme la clase y contador de 1
print(str(237)+"\t "+"1"+"\t"+str(contadorUno))
#se improme la clase y contador de 2
print(str(236)+"\t "+"2"+"\t"+str(contadorDos))
#se improme la clase y contador de 3
print(str(237)+"\t "+"3"+"\t"+str(contadorTres))
#se improme la clase y contador de 4
print(str(237)+"\t "+"4"+"\t"+str(contadorCuatro))
#se improme la clase y contador de 5
print(str(237)+"\t "+"5"+"\t"+str(contadorCinco))
#se improme la clase y contador de 6
print(str(237)+"\t "+"6"+"\t"+str(contadorSeis))
#se improme la clase y contador de 7
print(str(237)+"\t "+"7"+"\t"+str(contadorSiete))
#se improme la clase y contador de 8
print(str(237)+"\t "+"8"+"\t"+str(contadorOcho))
#se improme la clase y contador de 9
print(str(237)+"\t "+"9"+"\t"+str(contadorNueve))
print("******************************************************************")
print("")
print("******************************************************************")
#imprimimos el numero a la que pertenece de la imagen que reconocio
print('La Imagen es de clase: ',mat[0][2])
print("******************************************************************")
