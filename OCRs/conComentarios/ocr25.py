# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 14:43:04 2016

@author: Gerardo Lara Rojas
"""
import temp#importamos nuestro otro programa
import knn#importamos el progrmama knn para clasificacion

opcion=0#se asigna el valor de 0 para trabajar con la imagen

while(opcion!=3):
    print("Selecciona una opcion ")#impresion de pantalla
    opcion=int(input ("\t1.-Generar Dataset\n\t2.-Clasificar Imagen\n\t3.-Salir\n"))#Menú de opciones que contiene la variable opcion de tipo int que servira para evaluar lo que hara el programa

    if(opcion<1 or opcion>3):#la variable opcion es validada con la finalidad de el usuario solo pueda saleccionar un rango de numero que debera estar entre el 1 y el 3
        print("Error")#si el numero seleccionado por el usuario no se encuentra dentro de rango 1:3 se mostrara en pantalla un mesaneje de error
    if (opcion==1):#se evalalua que el numero ingresado por el usuario sea igual a 1
        temp.creardataset()#si el numero ingresado por el usuario es igual entonce invocamos al metodo Dataset y a la funcion dataset con la finalidad de generar un nuevo dataset
    if (opcion==2):#se evalua si el numero ingresado por el usuario es igual a 2 
        knn.instancias_de_la_clase()#se aplica la funcion de clasificacion del metodo KNN
        
print("Adios")#mensaje de despedida


import matplotlib.image as mpimg#libreria usada para trbajar con la imgane
import os#libreria para trabajar con el data set
import csv#extendcion de el resultado


#Nombre:Area
#Descripcion:saca el area de las imagenes 
#Argumentos:img que es la imagen
#Retorno: la area de la imagen
def Area(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    area=filas*columnas#son multiplicadas para sacar el area de la imagen
    return area#regresa la variable area que es la que usaremos
    
#Nombre:tamaño
#Descripcion:funcion que saca el tamaño de la imgagen en pixeles
#Argumentos:img que es la imagen
#Retorno: retorna el tamaño
def Tamaño(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    tamaño=filas/columnas#son divididas para 
    return tamaño#regresa el tamaño

#Bombre:Horizontal
#Descripcion:Metodo que cuenta los cortes de una linea horizontal trasada a la mitad
#Argumento:img es la variable donde se guarda la imagen
#Retorno:retorna el contador
def Linea1Horizontal(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    columnas=columnas/2#dividimos el tamaño total de las columnas entre dos
    columnas=columnas/2#dividimos el tamaño medio de las columnas entre dos
    columnas=int(columnas)#en dado de salir decimales las pasamos a numeros enteros
    cortador=0#contador de los cortes que hace la linea
    contadorblanco=0#cuenta el numero de pixeles blancos que tiene la imgane
    for i in range (filas):#ciclo que usamos para recorrer las columnas en base al tamaño de las filas
        #print(img[columnas,i])#Imprime el numero de columnas que hay
        #img[columnas,i]=253;# en dado caso de querer ver la impresion de la linea desmarcar 
        if img[columnas,i]!= img[columnas,i-1]:#usamos la conducion para if para contar el numero de pixes blancos
            cortador+=1#se le va aumentando un uno para tener los cortes optenidos 
        if img[columnas,i] == 1:#condicion if para contar los pixeles blancos
            contadorblanco+=1#wn caso de encotrar pixeles blancos son contados
    #print("linea 1 horizontal",cortador)#usado para mostrar el valor del coortador
    contadorblanco=(columnas/filas)/contadorblanco#se saca la proporcion en caso de imagenes grandes
    return cortador, contadorblanco#retorna el cortador y contador


#Bombre:Horizontal
#Descripcion:Metodo que cuenta los cortes de una linea horizontal trasada a la mitad
#Argumento:img es la variable donde se guarda la imagen
#Retorno:retorna el contador
def Linea2Horizontal(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    columnas=columnas/2#dividimos el tamaño total de las columnas entre dos
    columnas=int(columnas)#en dado de salir decimales las pasamos a numeros enteros
    cortador=0#contador de los cortes que hace la linea
    contadorblanco=0#cuenta el numero de pixeles blancos que tiene la imgane
    for i in range (filas):#ciclo que usamos para recorrer las columnas en base al tamaño de las filas
        #print(img[columnas,i])#Imprime el numero de columnas que hay
        #img[columnas,i]=253;# en dado caso de querer ver la impresion de la linea desmarcar   
        if img[columnas,i]!= img[columnas,i-1]:#usamos la conducion para if para contar el numero de pixes blancos
            cortador+=1#se le va aumentando un uno para tener los cortes optenidos  
        if img[columnas,i] == 1:#condicion if para contar los pixeles blancos
            contadorblanco+=1#wn caso de encotrar pixeles blancos son contados
   # print(cortador)
    contadorblanco=(columnas/filas)/contadorblanco#se saca la proporcion en caso de imagenes grandes
    return cortador, contadorblanco#retorna el cortador y contador


#Bombre:Horizontal
#Descripcion:Metodo que cuenta los cortes de una linea horizontal trasada a la mitad
#Argumento:img es la variable donde se guarda la imagen
#Retorno:retorna el contador blanco y el cortador
def Linea3Horizontal(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    columnas=columnas/2#dividimos el tamaño total de las columnas entre dos
    columnas=columnas/2#dividimos el tamaño medio de las columnas entre dos
    columnas=columnas*3#se multiplica por 3 para que la linea este a 3 cuartos de la imagen
    columnas=int(columnas)#en dado de salir decimales las pasamos a numeros enteros
    cortador=0#contador de los cortes que hace la linea
    contadorblanco=0#cuenta el numero de pixeles blancos que tiene la imgane
    for i in range (filas):#ciclo que usamos para recorrer las columnas en base al tamaño de las filas
        #print(img[columnas,i])#Imprime el numero de columnas que hay
        #img[columnas,i]=253;# en dado caso de querer ver la impresion de la linea desmarcar     
        if img[columnas,i]!= img[columnas,i-1]:#usamos la conducion para if para contar el numero de pixes blancos
            cortador+=1#se le va aumentando un uno para tener los cortes optenidos   
        if img[columnas,i] == 1:#condicion if para contar los pixeles blancos
            contadorblanco+=1#wn caso de encotrar pixeles blancos son contados
    #print(cortador)
    contadorblanco=(columnas/filas)/contadorblanco#se saca la proporcion en caso de imagenes grandes
    return cortador,contadorblanco#retorna el cortador y contador

#Nombre:Linea1vertical
#Descripcion:trasa una linea a una cuarta parte
#Argumentos:img es a variable donde se cuarda la imgen
#Retorno:retorna el contador blanco y el cortador
def Linea1Vertical(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    filas=filas/2#dividimos el tamaño total de las filas entre dos    
    filas=filas/2#dividimos el tamaño medio de las filas entre dos    
    filas=int(filas)#en dado de salir decimales las pasamos a numeros enteros
    cortador=0#contador de los cortes que hace la linea
    contadorblanco=0#cuenta el numero de pixeles blancos que tiene la imgane
    for i in range (columnas):#ciclo que usamos para recorrer las columnas en base al tamaño de las filas       
        #print(img[i,filas])#Imprime el numero de columnas que hay
        #img[i,filas]=253;# en dado caso de querer ver la impresion de la linea desmarcar       
        if img[i,filas]!= img[i-1,filas]:#usamos la conducion para if para contar el numero de pixes blancos
            cortador+=1#se le va aumentando un uno para tener los cortes optenidos     
        if img[i,filas] == 1:#condicion if para contar los pixeles blancos
            contadorblanco+=1#wn caso de encotrar pixeles blancos son contados
    #print("linea 1 vertical",cortador)
    contadorblanco=(columnas/filas)/contadorblanco#se saca la proporcion en caso de imagenes grandes
    return cortador, contadorblanco#retorna el cortador y contador
    

#Nombre:Linea2Vertical
#Descripcion:trasa una linea a mitad de la imgen
#Argumentos:img es a variable donde se cuarda la imgen
#Retorno:retorna el contador blanco y el cortador
def Linea2Vertical(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    filas=filas/2#dividimos el tamaño total de las filas entre dos    
    filas=int(filas)#en dado de salir decimales las pasamos a numeros enteros
    cortador=0#contador de los cortes que hace la linea
    contadorblanco=0#cuenta el numero de pixeles blancos que tiene la imgane
    for i in range (columnas):#ciclo que usamos para recorrer las columnas en base al tamaño de las filas       
        #print(img[i,filas])#Imprime el numero de columnas que hay
        #img[i,filas]=253;# en dado caso de querer ver la impresion de la linea desmarcar         
        if img[i,filas]!= img[i-1,filas]:#usamos la conducion para if para contar el numero de pixes blancos
            cortador+=1#se le va aumentando un uno para tener los cortes optenidos     
        if img[i,filas] == 1:#condicion if para contar los pixeles blancos
            contadorblanco+=1#condicion if para contar los pixeles blancos
    #print("linea 2 vertical",cortador)
    contadorblanco=(columnas/filas)/contadorblanco#se saca la proporcion en caso de imagenes grandes
    return cortador, contadorblanco#retorna el cortador y contador

#Nombre:Buscar archivos
#Descripcion:busca los archivos de un fichero
#Argumentos:ruta
#Retorno:retorna el contador blanco y el cortador    
def BuscarArchivos(ruta): 
    path =ruta
    #Lista vacia para incluir los ficheros
    lstFiles = []
 
     #Lista con todos los ficheros del directorio:
    lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
#Crea una lista de los ficheros png que existen en el directorio y los incluye a la lista.
    for root, dirs, files in lstDir:#ciclo usado para recorrer todos los archivos
        for fichero in files:#recorrera de fichechero en cichero los archivos
            (nombreFichero, extension) = os.path.splitext(fichero)#en caso de cso de encontrar archivos
            if(extension == ".png"):#si la extension del archivo es .png
                lstFiles.append(nombreFichero+extension)#se guarda el nombre del fichero con su extencion
                        
                        
    return lstFiles#retorna la imagen y extencion

    
#Nombre:Linea3vertical
#Descripcion:saca la 3 lineaen la imagen
#Argumentos:img nombre la variable que guarda la imgaen
#Retorno:contador blanco y cortador
def Linea3Vertical(img):
    [columnas,filas]=img.shape#se guardan las caracteriscas de columnas y filas
    filas=filas/2#dividimos el tamaño total de las filas entre dos    
    filas=filas/2#dividimos el tamaño medio de las filas entre dos    
    filas=filas*3#multiplicamos por 3 las filas para obtener 3 cuartos
    filas=int(filas)#en dado de salir decimales las pasamos a numeros enteros
    cortador=0#contador de los cortes que hace la linea
    contadorblanco=0#cuenta el numero de pixeles blancos que tiene la imgane
    for i in range (columnas):#ciclo que usamos para recorrer las columnas en base al tamaño de las filas       
        #print(img[i,filas])#Imprime el numero de columnas que hay
        #img[i,filas]=253;# en dado caso de querer ver la impresion de la linea desmarcar         
        if img[i,filas]!= img[i-1,filas]:#usamos la conducion para if para contar el numero de pixes blancos
            cortador+=1 #se le va aumentando un uno para tener los cortes optenidos       
        if img[i,filas] == 1:#condicion if para contar los pixeles blancos
            contadorblanco+=1#se le va aumentando un uno para tener los blancos optenidos       
   # print("Linea 3 vertical",cortador)
    contadorblanco=(columnas/filas)/contadorblanco#se saca la proporcion en caso de imagenes grandes
    return cortador,contadorblanco#retorna el cortador y contador


#Nombre:Creardataset
#DescripcionCrea el data set con todos los archivos
#Argumentos:null
#Retorna: la salida que tiene los datos
def creardataset():
    ruta='prueba/'#asignamos el nombre de la carpeta a la ruta
    archivo= open('resultado.csv', 'w', newline='')#abrimos el dataset y lo guardamos en archivo
    salida = csv.writer(archivo)#asignamos  una salida con extenxion csv
    numero=0#inicializamos numero
    for i in range(10):#se asigna un 10 por ser el numero de carpetasexistentes
        print("trabajando data set caracteristica del: "+str(i))#se imprime el msj de en que numero de carpeta va
        ruta=ruta+str(i)#se va asignando la ruta de cada una de las carpetas la caprta 10
        ls=BuscarArchivos(ruta)#se asgina la busqueda de los archivos
        
        
        for j in range(0,len(ls)):#se recorrera asta terminar los archivos dentro de las carpetas
            numero+=1#se agrega una variable que sera la contadora de las instancias
            rutaimagen=ruta+'/'+ls[j]#se asigna el contednido de las carpetas
            img=mpimg.imread(rutaimagen)#Ni idea de que pase aca
            caracteristica1=Linea1Horizontal(img)#obtenemos la caracteristica1     
            caracteristica2=Linea2Horizontal(img)#obtenemos la caracteristica2
            caracteristica3=Linea3Horizontal(img)##obtenemos la caracteristica3
            caracteristica4=Linea1Vertical(img)#obtenemos la caracteristica4
            caracteristica5=Linea2Vertical(img)#obtenemos la caracteristica5
            caracteristica6=Linea3Vertical(img)#obtenemos la caracteristica6
            caracteristica7=Area(img)#obtenemos la caracteristica7
            caracteristica8=Tamaño(img)#obtenemos la caracteristica8
            #la salida obtenida sera los valores guardados en nuestras caracteristticas al contener dos valores se asigna 0 que es el primer valor y 1 sienfo el segundo valor
            salida.writerow([caracteristica1[0],caracteristica1[1],caracteristica2[0],caracteristica2[1],caracteristica3[0],caracteristica3[1],caracteristica4[0],caracteristica4[1],caracteristica5[0],caracteristica5[1],caracteristica6[0],caracteristica6[1],caracteristica7,caracteristica8,numero,i])
        ruta='prueba/'#la salida de csv
    
    archivo.close()#una vez terminado el archivo se cierra para su visualizacion
    return salida #se retornal la salida

#def escribirArchivosCSV(n,m):#funcion que escribe, ny m son parametros para definir las fulas y columnas a escribir
 #  archivo=open("archivo.csv","a")
  # for filas in range(0, m):
   #print(")
    
    
    
import csv#lbreria utilizada para trabajar con csv
import math#funciones matematicas
import temp#importamos nuestro otro programa
import matplotlib.image as mpimg#libreria utilizada para trabajar con imagenes
    
#Nombre:Clasificacion
#Descripcion:hace la clasificacion de la imagen
#Argumentos:null
#Retorno:la prediccion, MAtrix,Mumeros_vecinos
def clasificacion():
    contador=0#inicializamos un contador en 0
    print("Nombre de la imagen: ")#impresion de pantalla
    nombre_imagen=(input())#variable de tipo int
    img=mpimg.imread(nombre_imagen)#se asigna el nombre de la imgen y se guarda en la vairable img
    dato1=temp.Linea1Horizontal(img)#cargamos las caracteristicas de la imagen a un nuevo dato1    
    dato2=temp.Linea2Horizontal(img)#cargamos las caracteristicas de la imagen a un nuevo dato1
    dato3=temp.Linea3Horizontal(img)#cargamos las caracteristicas de la imagen a un nuevo dato1
    dato4=temp.Linea1Vertical(img)#cargamos las caracteristicas de la imagen a un nuevo dato1
    dato5=temp.Linea2Vertical(img)#cargamos las caracteristicas de la imagen a un nuevo dato1
    dato6=temp.Linea3Vertical(img)#cargamos las caracteristicas de la imagen a un nuevo dato1
    dato7=temp.Area(img)#cargamos las caracteristicas de la imagen a un nuevo dato1
    dato8=temp.Tamaño(img)#cargamos las caracteristicas de la imagen a un nuevo dato1

    abrir= open('resultado.csv')#asignamos la dataset llamada resultado a una variable de nombre abrir
    lectura_de_dataset=csv.reader(abrir)#abrimos en data set previamente establecido
    dataset=list(lectura_de_dataset)#se guarda en una nueva instaciacion
    print("Numero de vecinos a considerar: ",end="")#impresion con intrucciones
    numero_vecinos=int(input())#la variabl numero_vecinos contendra el numero de vecinos que evaluaremos
    
    for i in dataset:#recorremos la dataset
    
        dataset[contador][0]=float(dataset[contador][0])#es reasignada un nueva variable
        dataset[contador][1]=float(dataset[contador][1])#es reasignada un nueva variable
        dataset[contador][2]=float(dataset[contador][2])#es reasignada un nueva variable
        dataset[contador][3]=float(dataset[contador][3])#es reasignada un nueva variable
        dataset[contador][4]=float(dataset[contador][4])#es reasignada un nueva variable
        dataset[contador][5]=float(dataset[contador][5])#es reasignada un nueva variable
        dataset[contador][6]=float(dataset[contador][6])#es reasignada un nueva variable
        dataset[contador][7]=float(dataset[contador][7])#es reasignada un nueva variable
        dataset[contador][8]=float(dataset[contador][8])#es reasignada un nueva variable
        dataset[contador][9]=float(dataset[contador][9])#es reasignada un nueva variable
        dataset[contador][10]=float(dataset[contador][10])#es reasignada un nueva variable
        dataset[contador][11]=float(dataset[contador][11])#es reasignada un nueva variable
        dataset[contador][12]=float(dataset[contador][12])#es reasignada un nueva variable
        dataset[contador][13]=float(dataset[contador][13])#es reasignada un nueva variable
        dataset[contador][14]=int(dataset[contador][14])#es reasignada un nueva variable
        dataset[contador][15]=int(dataset[contador][15])#es reasignada un nueva variable
        #que contiene el numero de valoes de el dataset
        contador+=1#se le asigna una suma para poder recorrer todos las casillas
        
        Matrix=dataset#cada valor es asignador a una nueva matrix que contiene el dataset
        #la prediccion son los valores obtenidos de la nueva imagen
        prediccion=[dato1[0],dato1[1],dato2[0],dato2[1],dato3[0],dato3[1],dato4[0],dato4[1],dato5[0],dato5[1],dato6[0],dato6[1],dato7,dato8]
    contador=0#una ves terminado el ciclo se devuelve a 0 el contador
    
    
    
    for i in Matrix:# realizo la distancia euclidiana
            aux=0#inicializamos la aux en 0
            aux=(pow((Matrix[contador][0]-dato1[0]),2))+ (pow((Matrix[contador][1]-dato1[1]),2))+ (pow((Matrix[contador][2]-dato2[0]),2))+ (pow((Matrix[contador][3]-dato2[1]),2))+(pow((Matrix[contador][4]-dato3[0]),2)) +(pow((Matrix[contador][5]-dato3[1]),2))#se hace la suma de los daots
            aux=aux+(pow((Matrix[contador][6]-dato4[0]),2))+ (pow((Matrix[contador][7]-dato4[1]),2))+ (pow((Matrix[contador][8]-dato5[0]),2))+ (pow((Matrix[contador][9]-dato5[1]),2))+(pow((Matrix[contador][10]-dato6[0]),2)) +(pow((Matrix[contador][11]-dato6[1]),2))#con la formula ya establecida
            aux=aux+(pow((Matrix[contador][12]-dato7),2))+ (pow((Matrix[contador][13]-dato8),2))#obtenido la distancia euclidiana
            aux=math.sqrt(aux)#sees asignada una raiz 
            dataset[contador].append(aux)#se guarga el resultado en la parte de dataset
            contador+=1#el contador se le aumenta un mas uno 
            
            
    Matrix.sort(key=lambda Matrix: Matrix[14],reverse=True)#se le aplica la reversa
    print ("\t\tDataset info:\nNúmero total de instancias:", Matrix[0][14])#imprimimos el numoro de primera instancia despues del sort
    Matrix.sort(key=lambda Matrix: Matrix[16])#aplicamos nuevo sort para ordenarlo de acuerdo a la distancia
    print("Instancia del K vecino mas cercano:", Matrix[0][14])#imprimimos el numero  de la instancia con la distancia mas cercana a nuestra imagen
    print ("\nk vecinos mas cercanos:")#Impresion de pantalla
    for K_vecinos in range (0,numero_vecinos):#numero de kvecinos que deberan imprimirse
        print ("\tInstancia:", Matrix[K_vecinos][14], "\tDistancia:",
               "%.5f" %Matrix[K_vecinos][16], "\tClase", Matrix[K_vecinos][15])#impresion de los k vecinos mas cercanos
           
    return prediccion, Matrix, numero_vecinos#valores de retorno de la imgane
def instancias_de_la_clase():
    prediccion,Matrix,numero_vecinos=clasificacion()#asemos un llamado de la funcion pasada
    k=numero_vecinos#guardamos los valores de numero vecinos en ca
    contador0=0#es el valor de las claces
    contador1=0#es el valor de las claces
    contador2=0#es el valor de las claces
    contador3=0#es el valor de las claces
    contador4=0#es el valor de las claces
    contador5=0#es el valor de las claces
    contador6=0#es el valor de las claces
    contador7=0#es el valor de las claces
    contador8=0#es el valor de las claces
    contador9=0#es el valor de las claces
    
    numero_filas=10#variable de tipo int
    numero_columnas=2#variable de tipo int
    clase_final = []#creamos un arreglo
    for filas in range(numero_filas):#limitaremos el numero de filas a 10
        clase_final.append([])#agregaremos mas filas a nuestas matriz
        for columnas in range(numero_columnas):#limitaremos el numero de columnas a 2
            clase_final[filas].append(None)#agregamos nuevas columnas a nuestra matriz       
            
    for caracateristica in range(k):#realizamos el siclo dependediendo de los valores de k 
    
            #print(Matrix[contador][4])
            if Matrix[caracateristica][15]==1:#condicional para sacar el valpores corresponsal
                contador1+=1#en dado caso que sea un 1
            if Matrix[caracateristica][15]==2:#condicional para sacar el valpores corresponsal
                contador2+=1#en dado caso que sea un 2
            if Matrix[caracateristica][15]==3:#condicional para sacar el valpores corresponsal
                contador3+=1#en dado caso que sea un 3
            if Matrix[caracateristica][15]==4:#condicional para sacar el valpores corresponsal
                contador4+=1#en dado caso que sea un 4
            if Matrix[caracateristica][15]==5:#condicional para sacar el valpores corresponsal
                contador5+=1#en dado caso que sea un 5
            if Matrix[caracateristica][15]==6:#condicional para sacar el valpores corresponsal
                contador6+=1#en dado caso que sea un 6
            if Matrix[caracateristica][15]==7:#condicional para sacar el valpores corresponsal
                contador7+=1#en dado caso que sea un 7
            if Matrix[caracateristica][15]==8:#condicional para sacar el valpores corresponsal
                contador8+=1#en dado caso que sea un 8
            if Matrix[caracateristica][15]==9:#condicional para sacar el valpores corresponsal
                contador9+=1#en dado caso que sea un 9
            if Matrix[caracateristica][15]==0:#condicional para sacar el valpores corresponsal
                contador0+=1#en dado caso que sea un 0
                
    clase_final[0]=contador0,0#llenamos nuestra matriz clse_final con los valores de la clase y el numero 0
    clase_final[1]=contador1,1#llenamos nuestra matriz clse_final con los valores de la clase y el numero 1
    clase_final[2]=contador2,2#llenamos nuestra matriz clse_final con los valores de la clase y el numero 2
    clase_final[3]=contador3,3#llenamos nuestra matriz clse_final con los valores de la clase y el numero 3
    clase_final[4]=contador4,4#llenamos nuestra matriz clse_final con los valores de la clase y el numero 4
    clase_final[5]=contador5,5#llenamos nuestra matriz clse_final con los valores de la clase y el numero 5
    clase_final[6]=contador6,6#llenamos nuestra matriz clse_final con los valores de la clase y el numero 7
    clase_final[7]=contador7,7#llenamos nuestra matriz clse_final con los valores de la clase y el numero 8
    clase_final[8]=contador8,8#llenamos nuestra matriz clse_final con los valores de la clase y el numero 9
    clase_final[9]=contador9,9#llenamos nuestra matriz clse_final con los valores de la clase y el numero 10
    
    clase_final.sort(key=None, reverse=True)#aplicamos sort a nuestra matriz clase_final dejando al principio el numero mayor
    print ("\nNúmero de Instancias por clase:")#impresion de pantalla
    for conteo_instancias in range(0,10):#contaremos el numero de instancias
            print ("\t",clase_final[conteo_instancias][0],#se imprime la clase u la instancia
            "\tInstancias de la clase:",clase_final[conteo_instancias][1]) 
    print ("\nLa imagen es el numero:", clase_final[0][1]) #impresion de pantalla del numero de instancias

    