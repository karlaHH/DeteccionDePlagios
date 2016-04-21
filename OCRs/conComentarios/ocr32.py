import KNN #importamos el KNN.py para realizar la clasificacion
import generarDataSet #importamos Dataset para la creacion del nuestro Dataset
import os #importamos os para usar comandos propios del Sistema Operativo
print ("Inserte un número:")#impresion del pantalla
opcion=int(input ("1.-Generar Dataset\n2.-Clasificar Imagen\n3.-Salir\n"))#se muestran las opciones del menu y se gurdan en una variable
os.system("cls")#limpia la pantalla
if(opcion<1 or opcion>3):#el número que insertemos no debera ser menor a 1 ni mayor a 3
    print("Error")#si el número insertado no es válido se mostrara esta excepción
if (opcion==1):#si la opción es igual a 1
    generarDataSet.DataSet()#se mandara a llamar la función DataSet que se encuentra en el programa generarDataSet.py
if (opcion==2):#si la opción es igual a 2 
    KNN.instancias()#se manda a llamar a la función instancias que se encuentra el programa KNN.py
if(opcion==3):#si la opción es igual a 3
    os.system("cls")#se limpiara la pantalla 

    
import matplotlib.pyplot as plt#importamos la libreria pyplot
import matplotlib.image as mpimg #importar una funcion de la libreria matplotlib y guardamos como mpimg
import os #importamos librerias de sistema operativo

def datos():#se asigna el nombre de la función
    print("Inserte el nombre de la imagen: ")#impresion de pantalla
    nombre_imagen=(input())#variable de tipo int
    os.system("cls")#limpiar pantalla
    img=mpimg.imread(nombre_imagen)#leemos la imagen y guardamos en una variable
    imgplot=plt.imshow(img)#copiamos la variable img en imgplot
    mat=img#declaramos una matriz y la igualamos a la imagen 
    tam=img.shape#obtenemos las medidas de la imagen en alto y ancho
    return img,tam,mat,imgplot #regresamos 4 variables

def RazonFilascolumnas(tam):#se asigna el nombre de la función
    razonFilasEntreColumnas=tam[0]/tam[1]#se declara una variable en donde se almacenara el resultado y posteriormente se realiza la operación
    return razonFilasEntreColumnas#regresamos el valor de la primera característica
      
def RazonPixelesBlancos(tam,mat):#se asigna el nombre de la función
    contarPixelesBlancos=0#se declara un contador y se iguala a cero
    for i in range(0,tam[0]):#Se recorre la matriz a lo alto es decir la columnas
       for j in range(0,tam[1]):#se recorre la matriz a lo ancho es decir las filas
           if(mat[i][j]!=0):#revisamos el numero de pixeles que tiene la matriz
              contarPixelesBlancos=contarPixelesBlancos+1#cada vez que los pixeles de la matriz sean blancos se iran almacenando en esta variable
    return contarPixelesBlancos#regresamos el valor de la segunda caracteristica
    
def CambiosPrimeraLineaHorizontal(tam,img):#se asigna el nombre de la función
    posicionPrimeraLineaHorizontal=int(tam[0]/4)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarCambiosPrimeraLineaHorizontal=0#Declaramos un contador que inicializamos en 0
    aux=img[posicionPrimeraLineaHorizontal][0]#declaramos una variable auxiliar a la cual asignaremos una posicion especifica en la cual queremos que se recorra nuestra matriz para encontrar los cambios efectuados ahi
    for i in range(0,tam[1]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(aux!=img[posicionPrimeraLineaHorizontal][i]):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la matriz
            aux=img[posicionPrimeraLineaHorizontal][i]#Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            contarCambiosPrimeraLineaHorizontal=contarCambiosPrimeraLineaHorizontal+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[posicionSegundaLineaHorizontal][i]=1#la siguiente linea solo mostrar el recorrido en el cual se detectaran los cambios
    return contarCambiosPrimeraLineaHorizontal#regresamos el valor de la tercera característica
    
def CambiosSegundaLineaHorizontal(tam,img):#se asigna el nombre de la función
    posicionSegundaLineaHorizontal=int(tam[0]/2)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarCambiosSegundaLineaHorizontal=0#Declaramos un contador que inicializamos en 0
    aux=img[posicionSegundaLineaHorizontal][0]#declaramos una variable auxiliar a la cual asignaremos una posicion especifica en la cual queremos que se recorra nuestra matriz para encontrar los cambios efectuados ahi
    for i in range(0,tam[1]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(aux!=img[posicionSegundaLineaHorizontal][i]):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtariz
            aux=img[posicionSegundaLineaHorizontal][i]#Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            contarCambiosSegundaLineaHorizontal=contarCambiosSegundaLineaHorizontal+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[posicionSegundaLineaHorizontal][i]=1 #la siguiente linea solo mostrar el recorrido en el cual se detectaran los cambios
    return contarCambiosSegundaLineaHorizontal#regresamos el valor de la cuarta característica
    
def CambiosTerceraLineaHorizontal(tam,img):#se asigna el nombre de la función
    posicionTerceraLineaHorizontal=int((tam[0]/4)*3)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarCambiosTerceraLineaHorizontal=0#Declaramos un contador que inicializamos en 0
    aux=img[posicionTerceraLineaHorizontal][0]#declaramos una variable auxiliar a la cual asignaremos una posicion especifica en la cual queremos que se recorra nuestra matriz para encontrar los cambios efectuados ahi
    for i in range(0,tam[1]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(aux!=img[posicionTerceraLineaHorizontal][i]):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la matriz
            aux=img[posicionTerceraLineaHorizontal][i]#Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            contarCambiosTerceraLineaHorizontal=contarCambiosTerceraLineaHorizontal+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[posicionTerceraLineaHorizontal][i]=1#la siguiente linea solo mostrar el recorrido en el cual se detectaran los cambios
    return contarCambiosTerceraLineaHorizontal#regresamos el valor de la quinta característica
    
def CambioPrimeraLineaVertical(tam,img):#se asigna el nombre de la función
    posicionPrimeraLineaVerticalal=int(tam[1]/4)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de columnas
    contarCambiosPrimeraLineaVertical=0#Declaramos un contador que inicializamos en 0
    aux=img[0][posicionPrimeraLineaVerticalal]#declaramos una variable auxiliar a la cual asignaremos una posicion especifica en la cual queremos que se recorra nuestra matriz para encontrar los cambios efectuados ahi
    for i in range(0,tam[0]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(aux!=img[i][posicionPrimeraLineaVerticalal]):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la matriz
            aux=img[i][posicionPrimeraLineaVerticalal]#Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            contarCambiosPrimeraLineaVertical=contarCambiosPrimeraLineaVertical+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[i][contarCambiosPrimeraLineaVertical]=1#la siguiente linea solo mostrar el recorrido en el cual se detectaran los cambios    
    return contarCambiosPrimeraLineaVertical#regresamos el valor de la sexta característica
    
def CambioSegundaLineaVertical(tam,img):#se asigna el nombre de la función
    posicionSegundaLineaVertical=int(tam[1]/2)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de columnas
    contarCambiosSegundaLineaVertical=0#Declaramos un contador que inicializamos en 0
    aux=img[0][posicionSegundaLineaVertical]#declaramos una variable auxiliar a la cual asignaremos una posicion especifica en la cual queremos que se recorra nuestra matriz para encontrar los cambios efectuados ahi
    for i in range(0,tam[0]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(aux!=img[i][posicionSegundaLineaVertical]):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la matriz
            aux=img[i][posicionSegundaLineaVertical]#Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            contarCambiosSegundaLineaVertical=contarCambiosSegundaLineaVertical+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[i][posicionSegundaLineaVertical]=1#la siguiente linea solo mostrar el recorrido en el cual se detectaran los cambios
    return contarCambiosSegundaLineaVertical#se regresa el  valor de la septima característica
      
def CambioTerceraLineaVertical(tam,img):#se asigna el nombre de la función
    posicionTerceraLineaVertical=int((tam[1]/4)*3)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de columnas
    contarCambiosTerceraLineaVertical=0#Declaramos un contador que inicializamos en 0
    aux=img[0][posicionTerceraLineaVertical]#declaramos una variable auxiliar a la cual asignaremos una posicion especifica en la cual queremos que se recorra nuestra matriz para encontrar los cambios efectuados ahi
    for i in range(0,tam[0]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(aux!=img[i][posicionTerceraLineaVertical]):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la matriz
            aux=img[i][posicionTerceraLineaVertical]#Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            contarCambiosTerceraLineaVertical=contarCambiosTerceraLineaVertical+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[i][posicionTerceraLineaVertical]#la siguiente linea solo mostrar el recorrido en el cual se detectaran los cambios
    return contarCambiosTerceraLineaVertical#se regresa el  valor de la octava característica
    
def ContarPixelesPrimeraLineaHorizontal(tam,img):#se asigna el nombre de la función
    posicionprimeraLineaHorizontal = int(tam[0]/4)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarPixelesPrimeraLineaHorizontal=0#Declaramos un contador que inicializamos en 0
    for i in range(0,tam[1]):#inicializamos nuestro ciclo para recorrer las filas de la matriz   
        if(img[posicionprimeraLineaHorizontal][i]!=0):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la matriz
            contarPixelesPrimeraLineaHorizontal=contarPixelesPrimeraLineaHorizontal+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[posicionprimeraLineaHorizontal][i]=1#la siguiente linea solo mostrar el recorrido en el cual se detectaran los pixeles en 1
    return contarPixelesPrimeraLineaHorizontal#se regeresa el valor de la novena caracteristica
    
def ContarPixelesSegundaLineaHorizontal(tam,img):#se asigna el nombre de la función
    posicionsegundaLineaHorizontal=int(tam[0]/2)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarPixelesSegundaLineaHorizontal=0#Declaramos un contador que inicializamos en 0
    for i in range(0,tam[1]):#inicializamos nuestro ciclo para recorrer las filas de la matriz   
        if(img[posicionsegundaLineaHorizontal][i]!=0):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz
            contarPixelesSegundaLineaHorizontal=contarPixelesSegundaLineaHorizontal+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[posicionsegundaLineaHorizontal][i]=1#la siguiente linea solo mostrar el recorrido en el cual se detectaran los pixeles en 1
    return contarPixelesSegundaLineaHorizontal#se regeresa el valor de la decima caracteristica
    
def ContarPixelesTerceraLineaHorizontal(tam,img):#se asigna el nombre de la función
    posicionterceraLineaHorizontal=int((tam[0]/4)*3)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarPixelesTerceraLineaHorizontal=0#Declaramos un contador que inicializamos en 0
    for i in range(0,tam[1]):#inicializamos nuestro ciclo para recorrer las filas de la matriz   
        if(img[posicionterceraLineaHorizontal][i]!=0):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz
            contarPixelesTerceraLineaHorizontal=contarPixelesTerceraLineaHorizontal+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[posicionterceraLineaHorizontal][i]=1#la siguiente linea solo mostrar el recorrido en el cual se detectaran los pixeles en 1
    return contarPixelesTerceraLineaHorizontal#se regeresa el valor de la onceava caracteristica
    
def ContarPixelesPrimeraLineaVertical(tam,img):#se asigna el nombre de la función
    posicionprimeraLineaVertical=int(tam[1]/4)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarPixelesPrimeraLineaVertical=0#Declaramos un contador que inicializamos en 0
    for i in range(0,tam[0]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(img[i][posicionprimeraLineaVertical]!=0):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz
            contarPixelesPrimeraLineaVertical=contarPixelesPrimeraLineaVertical+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[i][posicionprimeraLineaVertical]=0#la siguiente linea solo mostrar el recorrido en el cual se detectaran los pixeles en 1
    return contarPixelesPrimeraLineaVertical#se regeresa el valor de la doceava caracteristica
    
def ContarPixelesSegundaLineaVertical(tam,img):#se asigna el nombre de la función
    posicionsegundaLineaVertical=int(tam[1]/2)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarPixelesSegundaLineaVertical=0#Declaramos un contador que inicializamos en 0
    for i in range(0,tam[0]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(img[i][posicionsegundaLineaVertical]!=0):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz
            contarPixelesSegundaLineaVertical=contarPixelesSegundaLineaVertical+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[i][posicionsegundaLineaVertical]=0#la siguiente linea solo mostrar el recorrido en el cual se detectaran los pixeles en 1
    return contarPixelesSegundaLineaVertical#se regeresa el valor de la treceava caracteristica
    
def ContarPixelesTerceraLineaVertical(tam,img):#se asigna el nombre de la función
    posicionterceraLineaVertical=int((tam[1]/4)*3)#Declaramos una variable la cual almacenara un valor entero dado por la obtencion del tamaño del numero de filas
    contarPixelesTerceraLineaVertical=0#Declaramos un contador que inicializamos en 0
    for i in range(0,tam[0]):#inicializamos nuestro ciclo para recorrer las columnas de la matriz   
        if(img[i][posicionterceraLineaVertical]!=0):#declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz
            contarPixelesTerceraLineaVertical=contarPixelesTerceraLineaVertical+1#Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
        #img[i][posicionterceraLineaVertical]=0#la siguiente linea solo mostrar el recorrido en el cual se detectaran los pixeles en 1
    return contarPixelesTerceraLineaVertical#se regresa el valor de la característica 14


import matplotlib.image as mpimg #importar una funcion de la libreria matplotlib y guardamos como mpimg
import os #importamos librerias de sistema operativo
import csv #importamos libreria para archivos csv
import Caracteristicas #importamos el archivo Caracteristicas.py
def DataSet():#asignamos el nombre de la funcion
    root="arialSegmented"#Es la ruta de la carpeta en donde estan almacenados los números
    archivo= open ("DataSet.csv", "w",newline='')#creamos un nuevo archivo .csv con el nombre de DataSet.csv    
    salida=csv.writer(archivo)#variable que nos permite escribir en un archivo csv
    clase=-1#varialbe de tipo int
    posiciones_dataset=0#variable de tipo int
    for dirName, subdirlist, filelist in os.walk(root):#este for recorre todas la carpetas y subcarpetas de la ruta
        for fname in filelist:#aqui se leen los archivos que se encuentran en las subcarpetas
            posiciones_dataset=posiciones_dataset+1#aumentamos en uno el valor de la posicion
            nameima=dirName+'/'+fname #entramos a una nueva subcarpeta
            print("Generando DataSet....")#impresión de pantalla
            img=mpimg.imread(nameima)#leemos una imagen
            mat=img#declaramos una matriz y la igualamos a la imagen 
            tam=mat.shape#obtenemos las medidas de la imagen en alto y ancho
            #aqui representa todos los returns y manda a llamar a todas las funciones
            razonFilasEntreColumnas=Caracteristicas.RazonFilascolumnas(tam)#se obtiene la 1ra característica que es razon de filas y columnas
            contarPixelesBlancos=Caracteristicas.RazonPixelesBlancos(tam,mat)#se obtiene la 2da característica que es razon de pixeles blancos
            contarCambiosPrimeraLineaHorizontal=Caracteristicas.CambiosPrimeraLineaHorizontal(tam,img)#se obtiene la 3ra característica que es cambios en la primera linea horizontal   
            contarCambiosSegundaLineaHorizontal=Caracteristicas.CambiosSegundaLineaHorizontal(tam,img)#se obtiene la 4ta característica que es cambios en la segundaa linea horizontal 
            contarCambiosTerceraLineaHorizontal=Caracteristicas.CambiosTerceraLineaHorizontal(tam,img)#se obtiene la 5ta característica que es cambios en la tercera linea horizontal 
            contarCambiosPrimeraLineaVertical=Caracteristicas.CambioPrimeraLineaVertical(tam,img)#se obtiene la 6ta característica que es cambios en la primera linea vertical
            contarCambiosSegundaLineaVertical=Caracteristicas.CambioSegundaLineaVertical(tam,img)#se obtiene la 7ma característica que es cambios en la segundaa linea vertical
            contarCambiosTerceraLineaVertical=Caracteristicas.CambioTerceraLineaVertical(tam,img)#se obtiene la 8va característica que es cambios en la tercera linea vertical
            contarPixelesPrimeraLineaHorizontal=Caracteristicas.ContarPixelesPrimeraLineaHorizontal(tam,img)#se obtiene la 9na característica que es contar pixeles en 1 de la primera linea horizonntal
            contarPixelesSegundaLineaHorizontal=Caracteristicas.ContarPixelesSegundaLineaHorizontal(tam,img)#se obtiene la 10ma característica que es contar pixeles en 1 de la segunda linea horizonntal
            contarPixelesTerceraLineaHorizontal=Caracteristicas.ContarPixelesTerceraLineaHorizontal(tam,img)#se obtiene la 11va característica que es contar pixeles en 1 de la tercera linea horizonntal
            contarPixelesPrimeraLineaVertical=Caracteristicas.ContarPixelesPrimeraLineaVertical(tam,img)#se obtiene la 13va característica que es contar pixeles en 1 de la primera linea vertical
            contarPixelesSegundaLineaVertical=Caracteristicas.ContarPixelesSegundaLineaVertical(tam,img)#se obtiene la 14va característica que es contar pixeles en 1 de la segunda linea vertical
            contarPixelesTerceraLineaVertical=Caracteristicas.ContarPixelesTerceraLineaVertical(tam,img)#se obtiene la 9na característica que es contar pixeles en 1 de la tercera linea vertical
            #aqui se escribe el dataset en el archivo de excel 
            salida.writerow([razonFilasEntreColumnas,contarPixelesBlancos,contarCambiosPrimeraLineaHorizontal,contarCambiosSegundaLineaHorizontal,contarCambiosTerceraLineaHorizontal,contarCambiosPrimeraLineaVertical,contarCambiosSegundaLineaVertical,contarCambiosTerceraLineaVertical,contarPixelesPrimeraLineaHorizontal,contarPixelesSegundaLineaHorizontal,contarPixelesTerceraLineaHorizontal,contarPixelesPrimeraLineaVertical,contarPixelesSegundaLineaVertical,contarPixelesTerceraLineaVertical,posiciones_dataset,clase])
        clase=clase+1#aumentamos en uno al contador
        os.system("cls")#limpiamos pantalla
    print ("El DataSet esta listo....!!!!")#impresion de pantalla            
    archivo.close()#dejamos de escribir en el dataset

    
import csv#importar librerias para archivos CSV
import math#importar libreria para funciones matematicas
import os#importar libreria del sistema operativo
import Caracteristicas#importar Caracteristicas.py
def Clasificacion():#asignamos el nombre de la función
    img,tam,mat,imgplot=Caracteristicas.datos()#llamamos a la función datos que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    razonFilasEntreColumnas=Caracteristicas.RazonFilascolumnas(tam)#llamamos a la función RazonFilascolumnas que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarPixelesBlancos=Caracteristicas.RazonPixelesBlancos(tam,mat)#llamamos a la función RazonPixelesBlancos que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarCambiosPrimeraLineaHorizontal=Caracteristicas.CambiosPrimeraLineaHorizontal(tam,img)#llamamos a la función CambiosPrimeraLineaHorizontal que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarCambiosSegundaLineaHorizontal=Caracteristicas.CambiosSegundaLineaHorizontal(tam,img)#llamamos a la función CambiosSegundaLineaHorizontal que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarCambiosTerceraLineaHorizontal=Caracteristicas.CambiosTerceraLineaHorizontal(tam,img)#llamamos a la función CambiosTerceraLineaHorizontal que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno   
    contarCambiosPrimeraLineaVertical=Caracteristicas.CambioPrimeraLineaVertical(tam,img)#llamamos a la función CambioPrimeraLineaVertical que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarCambiosSegundaLineaVertical=Caracteristicas.CambioSegundaLineaVertical(tam,img)#llamamos a la función CambioSegundaLineaVertical que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarCambiosTerceraLineaVertical=Caracteristicas.CambioTerceraLineaVertical(tam,img)#llamamos a la función CambioTerceraLineaVertical que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarPixelesPrimeraLineaHorizontal=Caracteristicas.ContarPixelesPrimeraLineaHorizontal(tam,img)#llamamos a la función ContarPixelesPrimeraLineaHorizontal que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarPixelesSegundaLineaHorizontal=Caracteristicas.ContarPixelesSegundaLineaHorizontal(tam,img)#llamamos a la función ContarPixelesSegundaLineaHorizontal que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarPixelesTerceraLineaHorizontal=Caracteristicas.ContarPixelesTerceraLineaHorizontal(tam,img)#llamamos a la función ContarPixelesTerceraLineaHorizontal que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarPixelesPrimeraLineaVertical=Caracteristicas.ContarPixelesPrimeraLineaVertical(tam,img)#llamamos a la función ContarPixelesPrimeraLineaVertical que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarPixelesSegundaLineaVertical=Caracteristicas.ContarPixelesSegundaLineaVertical(tam,img)#llamamos a la función ContarPixelesSegundaLineaVertical que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    contarPixelesTerceraLineaVertical=Caracteristicas.ContarPixelesTerceraLineaVertical(tam,img)#llamamos a la función ContarPixelesTerceraLineaVertical que esta ubicada en el programa Caracteristicas.py y guardamos las variables de retorno
    
    abrir= open('DataSet.csv')#la variable abrir contendra todos los datos que se encuentran en el dataset
    leer_dataset=csv.reader(abrir)#la variable leer_dataset contriene los datos que se encuentran en abrir
    dataset=list(leer_dataset)#la variable dataset contendra el dataset en forma de lista
    print("\n\nIngrese lo que se pide a continuación")#impresión de pantalla
    print("\n\nNumero de vecinos a considerar: ",end="")#impresión de pantalla
    numeroKVecinos=int(input())#la variabl numeroKVecinos contendra el numero de vecinos que evaluaremos
    os.system("cls")#limpieza de pantalla
    contador=0#variable contado
    for i in dataset:#for que recorre el dataset en todas sus posiciones
        dataset[contador][0]=float(dataset[contador][0])#convertirmos a flotante el dataset en la posicion [contador][0]
        dataset[contador][1]=int(dataset[contador][1])#convertirmos a entero dataset en la posicion [contador][1]
        dataset[contador][2]=int(dataset[contador][2])#convertirmos a entero dataset en la posicion [contador][2]
        dataset[contador][3]=int(dataset[contador][3])#convertirmos a entero dataset en la posicion [contador][3]
        dataset[contador][4]=int(dataset[contador][4])#convertirmos a entero dataset en la posicion [contador][4]
        dataset[contador][5]=int(dataset[contador][5])#convertirmos a entero dataset en la posicion [contador][5]
        dataset[contador][6]=int(dataset[contador][6])#convertirmos a entero dataset en la posicion [contador][6]
        dataset[contador][7]=int(dataset[contador][7])#convertirmos a entero dataset en la posicion [contador][7]
        dataset[contador][8]=int(dataset[contador][8])#convertirmos a entero dataset en la posicion [contador][8]
        dataset[contador][9]=int(dataset[contador][9])#convertirmos a entero dataset en la posicion [contador][9]
        dataset[contador][10]=int(dataset[contador][10])#convertirmos a entero dataset en la posicion [contador][10]
        dataset[contador][11]=int(dataset[contador][11])#convertirmos a entero dataset en la posicion [contador][11]
        dataset[contador][12]=int(dataset[contador][12])#convertirmos a entero dataset en la posicion [contador][12]
        dataset[contador][13]=int(dataset[contador][13])#convertirmos a entero dataset en la posicion [contador][13]
        dataset[contador][14]=int(dataset[contador][14])#convertirmos a entero dataset en la posicion [contador][14]
        dataset[contador][15]=int(dataset[contador][15])#convertirmos a entero dataset en la posicion [contador][15]
        
        #Aplicamos la formula para obtener la distancia Euclidiana, es decir una sumatoria de cada caracteristica del dataset menos cada caracteristica de la imagen a clasificar       
        distancia=(((dataset[contador][0]-razonFilasEntreColumnas)**2)+
        ((dataset[contador][1]-contarPixelesBlancos)**2)+
        ((dataset[contador][2]-contarCambiosPrimeraLineaHorizontal)**2)+
        ((dataset[contador][3]-contarCambiosSegundaLineaHorizontal)**2)+
        ((dataset[contador][4]-contarCambiosTerceraLineaHorizontal)**2)+
        ((dataset[contador][5]-contarCambiosPrimeraLineaVertical)**2)+
        ((dataset[contador][6]-contarCambiosSegundaLineaVertical)**2)+
        ((dataset[contador][7]-contarCambiosTerceraLineaVertical)**2)+
        ((dataset[contador][8]-contarPixelesPrimeraLineaHorizontal)**2)+
        ((dataset[contador][9]-contarPixelesSegundaLineaHorizontal)**2)+
        ((dataset[contador][10]-contarPixelesTerceraLineaHorizontal)**2)+
        ((dataset[contador][11]-contarPixelesPrimeraLineaVertical)**2)+
        ((dataset[contador][12]-contarPixelesSegundaLineaVertical)**2)+
        ((dataset[contador][13]-contarPixelesTerceraLineaVertical)**2))
        raiz=math.sqrt(distancia)#la segunda parte de la formula es obtener la raiz cuadrada de la sumatoria
        dataset[contador].append(raiz)#agregamos una nueva fila a nuestra matriz que contendra la raiz cuadrada de cada instancia
        contador+=1#sumamos un numero al contador
    dataset.sort(key=lambda dataset: dataset[14],reverse=True)#aplicamos la funcion sort para ordenar el dataset de acuerdo al numero total de instancias
    print ("\tInformacón del DataSet")#impresión de pantalla 
    print ("No. Total de instancias: ", dataset [0][14])#se imprimen el número total de instancias    
    dataset.sort(key=lambda dataset: dataset[16])#aplicamos nuevo sort para ordenarlo de acuerdo a la distancia
    print("Instancia del K vecino mas cercano: ", dataset[0][14])#imprimimos el numero  de la instancia con la distancia mas cercana a nuestra imagen
    print ("\nK vecinos mas cercanos:")#Impresion de pantalla
    for k_Vecinos_Cercanos in range (0,numeroKVecinos):#numero de kvecinos que deberan imprimirse
        print ("Instancia:", dataset[k_Vecinos_Cercanos][14], "\tDistancia:","%.4f" %dataset[k_Vecinos_Cercanos][16], "    Clase", dataset[k_Vecinos_Cercanos][15])#impresion de los k vecinos mas cercanos
    return dataset, numeroKVecinos#valores que regresa la funcion clasificacion  
    
def instancias():#nombre de la función
    dataset,numeroKVecinos = Clasificacion()#llamamos a la funcion clasificacion y los valores de retorno son almacenados en dos variables
    clase0=0#variable de tipo int
    clase1=0#variable de tipo int
    clase2=0#variable de tipo int
    clase3=0#variable de tipo int
    clase4=0#variable de tipo int
    clase5=0#variable de tipo int
    clase6=0#variable de tipo int
    clase7=0#variable de tipo int
    clase8=0#variable de tipo int
    clase9=0#variable de tipo int
    
    numero_filas=10#variable de tipo int
    numero_columnas=2#variable de tipo int
    clase_final = []#creamos un arreglo
    for filas in range(numero_filas):#limitaremos el numero de filas a 10
        clase_final.append([])#agregaremos mas filas a nuestas matriz
        for columnas in range(numero_columnas):#limitaremos el numero de columnas a 2
            clase_final[filas].append(None)#agregamos nuevas columnas a nuestra matriz     
    
    for caracteristica in range(0,numeroKVecinos):#sumaremos el numero de vecinos que deseamos ver impresos
        if(dataset[caracteristica][15]==0):#condicion para determinar si en una posicion es igual a 0
            clase0=clase0+1#sumamos uno a nuestro contador         
        if(dataset[caracteristica][15]==1):#condicion para determinar si en una posicion es igual a 1
            clase1=clase1+1#sumamos uno a nuestro contador #sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==2):#condicion para determinar si en una posicion es igual a 2
            clase2=clase2+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==3):#condicion para determinar si en una posicion es igual a 3
            clase3=clase3+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==4):#condicion para determinar si en una posicion es igual a 4
            clase4=clase4+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==5):#condicion para determinar si en una posicion es igual a 5
            clase5=clase5+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==6):#condicion para determinar si en una posicion es igual a 6
            clase6=clase6+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==7):#condicion para determinar si en una posicion es igual a 7
            clase7=clase7+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==8):#condicion para determinar si en una posicion es igual a 8
            clase8=clase8+1#sumamos uno a nuestro contador 
        if(dataset[caracteristica][15]==9):#condicion para determinar si en una posicion es igual a 9
            clase9=clase9+1#sumamos uno a nuestro contador 
            
    clase_final[0]=clase0,0#llenamos nuestra matriz clase_final con los valores de la clase y el numero 0
    clase_final[1]=clase1,1#llenamos nuestra matriz clase_final con los valores de la clase y el numero 1
    clase_final[2]=clase2,2#llenamos nuestra matriz clase_final con los valores de la clase y el numero 2
    clase_final[3]=clase3,3#llenamos nuestra matriz clase_final con los valores de la clase y el numero 3
    clase_final[4]=clase4,4#llenamos nuestra matriz clase_final con los valores de la clase y el numero 4
    clase_final[5]=clase5,5#llenamos nuestra matriz clase_final con los valores de la clase y el numero 5
    clase_final[6]=clase6,6#llenamos nuestra matriz clase_final con los valores de la clase y el numero 7
    clase_final[7]=clase7,7#llenamos nuestra matriz clase_final con los valores de la clase y el numero 8
    clase_final[8]=clase8,8#llenamos nuestra matriz clase_final con los valores de la clase y el numero 9
    clase_final[9]=clase9,9#llenamos nuestra matriz clase_final con los valores de la clase y el numero 10
    
    clase_final.sort(key=None, reverse=True)#aplicamos sort a nuestra matriz clase_final dejando al principio el numero mayor
    print ("\nNúmero de Instancias por clase: ")#impresion de pantalla
    for conteo_instancias in range(0,10):#contaremos el numero de instancias
            print ("",clase_final[conteo_instancias][0],
            "   Instancias de la clase:",clase_final[conteo_instancias][1]) 
    print ("\n\nLa imagen es un :", clase_final[0][1]) #impresion de pantalla del numero de instancias
    
    
    