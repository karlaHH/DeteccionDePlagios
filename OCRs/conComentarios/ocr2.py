#snake_case todas las funciones son camelCase
#Jose Javier Muñoz Cabrera
#descripcion:este codigo obtiene caracteristicas de imagenes segmentadas para despues poder tomar una prueba de estas y poder clasificarla segun sus caracteristicas

#importa el objeto para recorrer las carpetas
import os 
#Este objeto se importa para recorrer los archivos                            
import matplotlib.image as mpimg 
#Esté es el objeto ocupado para los archivos csv     
import csv
#Importamos la libreria math                            
import math                           

#Declaracion de la matriz que almacenara todos los datos
data=[]                               
                      

#Nombre: caracteristica1
#Descripcion: Esta funcion nos regresa la relacion entre unos con respecto al tamaño de la imagen (total de unos/tamaño total de la imagen)
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tamImg)
#return: Retorna la relacion #1´s/#pixeles total, es flotante

#Creamos la funcion
def caracteristica1(img, tamImg): 
#Declaracion de la variable que sera el contador de los unos    
    resu=0
#Se declara la variable que contiene el alto de la imagen                           
    alto=len(img)                    
#Se declara la variable que contiene el ancho de la imagen
    ancho=int(tamImg/alto)
#For que recorre las filas de la imagen           
    for al in range(alto):
#For que recorre las columnas           
        for an in range(ancho): 
#Obtiene el valor de cada pixel para ser comparado
            num=(int(img[al][an])) 
#Se compara cada pixel para validar si es un 1
            if num==1:               
#Si el pixel es 1 se almacena al contador
                resu=resu+1          
#Se divide el número de pixeles sobre el total de la imagen, para obtener la relacion
    resu=(resu/tamImg)               
#Se regresa la relacion 1's/total de pixeles
    return resu                      


#Nombre: caracteristica2
#Descripcion: Esta funcion nos regresa la relacion entre el ancho sobre el alto 
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tImTo)
#return: Retorna la relacion ancho/alto

#Creación de la función
def caracteristica2(img, tamImg):
#Creamos la variable que contiene el alto de la imagen
    alto=len(img) 
#Creamos la variable con el ancho de la imagen               
    ancho=int(tamImg/alto)
#Realizamos la operacion para obtener la relacion deseada        
    resu=ancho/alto
#Retornamos la relacion ancho/alto               
    return resu                  


#Nombre: caracteristica3
#Descripcion: Esta funcion nos regresa la relacion de 1´s que en encuentran a la mitad de la imagen de forma vertical con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tamImg)
#return: Retorna la relacion total de pixeles en linea vertical/tamaño total de la imagen

#Creacion de la funcion
def caracteristica3(img, tamImg):
#Creamos la variable que contiene el alto de la imagen            
    alto=len(img)
#Creamos la variable con el ancho de la imagen                           
    ancho=int(tamImg/alto)
#Obtenemos la distancia en la cual haremos la busqueda de 1´s                   
    dista=int(ancho/2)
#Inicializaremos la variable que contendra el numero de 1´s                       
    numuns=0 
#For encargado de recorrer las filas de la imagen                               
    for al in range(alto):
#Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente                  
        compara=(int(img[al][dista]))
#En esta linea comparamos si el valor actual es 1 o no
        if compara==1:
#Se hace la sobrecarga del numero de 1´s encontrado en la linea de busqueda                      
            numuns=numuns+1 
#Retornamos el numero de 1´s encontrados en la mitad de la imagen/tamaño total de la imagen                
    return numuns/alto                      
    

#Nombre: caracteristica4
#Descripcion: Esta funcion nos regresa la relacion de 1´s que en encuentran a 1/4 de la imagen de forma vertical con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tamImg)
#return: Retorna la relacion total de pixeles en linea vertical/tamaño total de la imagen

#Creacion de la funciones
def caracteristica4(img, tamImg):
 #Creamos la variable que contiene el alto de la imagen            
    alto=len(img)
#Creamos la variable con el ancho de la imagen                          
    ancho=int(tamImg/alto) 
#Obtenemos la distancia en la cual haremos la busqueda de 1´s                  
    dista=int(ancho/4)
#Inicializaremos la variable que contendra el numero de 1´s                       
    numuns=0    
 #For encargado de recorrer las filas de la imagen                            
    for al in range(alto):
#Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente                 
        compara=(int(img[al][dista]))   
#En esta linea comparamos si el valor actual es 1 o no
        if compara==1:
#Se hace la sobrecarga del numero de 1´s encontrado en la linea de busqueda                      
            numuns=numuns+1 
#Retornamos el numero de 1´s encontrados en 1/4 de la imagen/tamaño total de la imagen
                    
    return numuns/alto                      

#Nombre: caracteristica5
#Descripcion: Esta funcion nos regresa la relacion de 1´s que en encuentran a 3/4 de la imagen de forma vertical con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tamImg)
#return: Retorna la relacion total de pixeles en linea vertical/tamaño total de la imagen

#Creacion de la funcion
def caracteristica5(img, tamImg):            
#Creamos la variable que contiene el alto de la imagen
    alto=len(img)
 #Creamos la variable con el ancho de la imagen                           
    ancho=int(tamImg/alto)  
#Obtenemos la distancia en la cual haremos la busqueda de 1´s                
    dista=int((int(ancho/4))*3)
#Inicializaremos la variable que contendra el numero de 1´s              
    numuns=0
 #For encargado de recorrer las filas de la imagen                                
    for al in range(alto):
#Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente                 
        compara=(int(img[al][dista]))
#En esta linea comparamos si el valor actual es 1 o no
        if compara==1:
#Se hace la sobrecarga del numero de 1´s encontrado en la linea de busqueda                     
            numuns=numuns+1 
#Retornamos el numero de 1´s encontrados en 3/4 de la imagen/tamaño total de la imagen                
    return numuns/alto                      

       
#Nombre: caracteristica6
#Descripcion: Esta funcion nos regresa la relacion de 1´s que en encuentran a 1/2 de la imagen de forma horizontal con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tamImg)
#return: Retorna la relacion total de pixeles en linea horizontal/tamaño total de la imagen
 
#Creacion de la funcion      
def caracteristica6(img, tamImg): 
#Creamos la variable que contiene el alto de la imagen                   
    alto=len(img)
 #Creamos la variable con el ancho de la imagen                                   
    ancho=int(tamImg/alto)
 #Obtenemos la distancia en la cual haremos la busqueda de 1´s                          
    altu=int(alto/2) 
#Inicializaremos la variable que contendra el numero de 1´s                               
    numuns=0
 #For encargado de recorrer las filas de la imagen                                        
    for alt in range(alto):
#For encargado de recorrer las columnas de la imagen                        
        for anch in range(ancho):
#Verificamos que nuestro buscador se encuentre en la columna la cual seleccionamos para realizar la busqueda                   
            if alt==altu:
#Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente                           
                compara=(int(img[altu][anch]))
#En esta linea comparamos si el valor actual es 1 o no
                if compara==1:
#Se hace la sobrecarga del numero de 1´s encontrado en la linea de busqueda                      
                    numuns=numuns+1
#Retornamos el numero de 1´s encontrados en 1/2 de la imagen/tamaño total de la imagen
    return numuns/ancho                            


#Nombre: caracteristica7
#Descripcion: Esta funcion nos regresa la relacion de 1´s que en encuentran a 1/4 de la imagen de forma horizontal con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tamImg)
#return: Retorna la relacion total de pixeles en linea horizontal/tamaño total de la imagen

#Creacion de la funcion        
def caracteristica7(img, tamImg):
#Creamos la variable que contiene el alto de la imagen                    
    alto=len(img)
#Creamos la variable con el ancho de la imagen                                  
    ancho=int(tamImg/alto)
#Obtenemos la distancia en la cual haremos la busqueda de 1´s                          
    altu=int(alto/4)
#Inicializaremos la variable que contendra el numero de 1´s                                 
    numuns=0
#For encargado de recorrer las filas de la imagen                                       
    for alt in range(alto):
#For encargado de recorrer las columnas de la imagen                         
        for anch in range(ancho):
#Verificamos que nuestro buscador se encuentre en la columna la cual seleccionamos para realizar la busqueda                  
            if alt==altu:   
#Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente                        
                compara=(int(img[altu][anch]))
#En esta linea comparamos si el valor actual es 1 o no
                if compara==1:
#Se hace la sobrecarga del numero de 1´s encontrado en la linea de busqueda                      
                    numuns=numuns+1
#Retornamos el numero de 1´s encontrados en q/4 de la imagen/tamaño total de la imagen
    return numuns/ancho                             

#Nombre: caracteristica8
#Descripcion: Esta funcion nos regresa la relacion de 1´s que en encuentran a 3/4 de la imagen de forma horizontal con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tamImg)
#return: Retorna la relacion total de pixeles en linea horizontal/tamaño total de la imagen

#Creacion de la funcion
def caracteristica8(img, tamImg):
#Creamos la variable que contiene el alto de la imagen                   
    alto=len(img)
#Creamos la variable con el ancho de la imagen                                  
    ancho=int(tamImg/alto)
#Obtenemos la distancia en la cual haremos la busqueda de 1´s                           
    altu=int((int(alto/4))*3)
#Inicializaremos la variable que contendra el numero de 1´s                        
    numuns=0 
#For encargado de recorrer las filas de la imagen                                      
    for alt in range(alto):
#For encargado de recorrer las columnas de la imagen                        
        for anch in range(ancho):
#Verificamos que nuestro buscador se encuentre en la columna la cual seleccionamos para realizar la busqueda                   
            if alt==altu:
#Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente                           
                compara=(int(img[altu][anch]))
#En esta linea comparamos si el valor actual es 1 o no
                if compara==1:
#Se hace la sobrecarga del numero de 1´s encontrado en la linea de busqueda                      
                    numuns=numuns+1
#Retornamos el numero de 1´s encontrados en q/4 de la imagen/tamaño total de la imagen
    return numuns/ancho                             


#Nombre: caracteristica9
#Descripcion: Esta funcion nos regresa la relacion de cortes que en encuentran a 1/2 de la imagen de forma vertical osea los cambios que hace entre 1´s y 0´s con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tamImg)
#return: Retorna la relacion de cortes que hay entre la imagen/tamaño total de la imagen

#Creacion de la funcion
def caracteristica9(img, tamImg):
#Creamos la variable que contiene el alto de la imagen                
    alto=len(img)
#Creamos la variable con el ancho de la imagen                               
    ancho=int(tamImg/alto)
#Obtenemos la distancia en la cual haremos los cortes de la imagen                       
    dista=int(ancho/2)
#Inicializaremos la variable que contendra el numero de cortes                          
    numuns=0
#Inicializaremos la variable que contendra el valor que sera comparado despues para obtenes el numero de cortes                                    
    val=0
#For encargado de recorrer las filas de la imagen                                       
    for al in range(alto):
#Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente                     
        compara=(int(img[al][dista]))
#Comparamos si el valor del pixel actual es diferente a la asignacion anterior, asi sabemos si hay cortes en la imagen          
        if compara!=val:
#Se hace la sobrecarga del numero de cortes encontrados en la linea de busqueda                       
            numuns=numuns+1
#Si hay un corte en la imagen asignamos el valor a nuestra variable para seguir buscando cortes despues                    
            val=(int(img[al][dista]))
#Retornams el numero de cortes encontrados a 1/2 de la imagen de forma vertical
    return numuns                               


#Nombre: caracteristica10
#Descripcion: Esta funcion nos regresa la relacion de cortes que en encuentran a 1/4 de la imagen de forma vertical osea los cambios que hace entre 1´s y 0´s con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tamImg)
#return: Retorna la relacion de cortes que hay entre la imagen/tamaño total de la imagen

#Creacion de la funcion    
def caracteristica10(img, tamImg):
#Creamos la variable que contiene el alto de la imagen               
    alto=len(img)
#Creamos la variable que contiene el ancho de la imagen                               
    ancho=int(tamImg/alto)
#Obtenemos la distancia en la cual haremos los cortes de la imagen                       
    dista=int(ancho/4)
#Inicializaremos la variable que contendra el numero de cortes                          
    numuns=0
#Inicializaremos la variable que contendra el valor que sera comparado despues para obtenes el numero de cortes                                    
    val=0 
#For encargado de recorrer las filas de la imagen                                     
    for al in range(alto):
#Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente                      
        compara=(int(img[al][dista]))
#Comparamos si el valor del pixel actual es diferente a la asignacion anterior, asi sabemos si hay cortes en la imagen           
        if compara!=val:
#Se hace la sobrecarga del numero de cortes encontrados en la linea de busqueda                        
            numuns=numuns+1
#Si hay un corte en la imagen asignamos el valor a nuestra variable para seguir buscando cortes despues                     
            val=(int(img[al][dista]))
#Retornams el numero de cortes encontrados a 1/4 de la imagen de forma vertical
    return numuns                               

#Nombre: caracteristica11
#Descripcion: Esta funcion nos regresa la relacion de cortes que en encuentran a 3/4 de la imagen de forma vertical osea los cambios que hace entre 1´s y 0´s con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tamImg)
#return: Retorna la relacion de cortes que hay entre la imagen/tamaño total de la imagen

#Creacion de la funcion
def caracteristica11(img, tamImg):
#Creamos la variable que contiene el alto de la imagen               
    alto=len(img)
#Creamos la variable con el ancho de la imagen                               
    ancho=int(tamImg/alto)
#Obtenemos la distancia en la cual haremos los cortes de la imagen                       
    dista=int((int(ancho/4))*3)
#Inicializaremos la variable que contendra el numero de cortes                 
    numuns=0
#Inicializaremos la variable que contendra el valor que sera comparado despues para obtenes el numero de cortes                                    
    val=0
#For encargado de recorrer las filas de la imagen                                       
    for al in range(alto):
#Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente                      
        compara=(int(img[al][dista]))
#Comparamos si el valor del pixel actual es diferente a la asignacion anterior, asi sabemos si hay cortes en la imagen           
        if compara!=val:
#Se hace la sobrecarga del numero de cortes encontrados en la linea de busqueda                        
            numuns=numuns+1
#Si hay un corte en la imagen asignamos el valor a nuestra variable para seguir buscando cortes despues                     
            val=(int(img[al][dista]))
#Retornams el numero de cortes encontrados a 3/4 de la imagen de forma vertical
    return numuns                               


#Nombre: caracteristica12
#Descripcion: Esta funcion nos regresa la relacion de cortes que en encuentran a 1/2 de la imagen de forma horizontal osea los cambios que hace entre 1´s y 0´s con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tamImg)
#return: Retorna la relacion de cortes que hay entre la imagen/tamaño total de la imagen

#Creacion de la funcion
def caracteristica12(img, tamImg):
#Creamos la variable que contiene el alto de la imagen                   
    alto=len(img)
#Creamos la variable con el ancho de la imagen                                   
    ancho=int(tamImg/alto)
#Obtenemos la distancia en la cual haremos los cortes de la imagen                           
    altu=int(alto/2)
#Inicializaremos la variable que contendra el numero de cortes                                
    numuns=0
#Inicializaremos la variable que contendra el valor que sera comparado despues para obtenes el numero de cortes                                        
    val=0 
#For encargado de recorrer las filas de la imagen                                          
    for alt in range(alto):
#For encargado de recorrer las columnas de la imagen                         
        for anch in range(ancho):
#Aquí verificamos que nuestro buscador se encuentre en la columna que necesitamos analizar                   
            if alt==altu:
#Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente                          
                compara=(int(img[altu][anch]))
#Comparamos si el valor del pixel actual es diferente a la asignacion anterior, asi sabemos si hay cortes en la imagen
                if compara!=val:  
#Se hace la sobrecarga del numero de cortes encontrados en la linea de busqueda
                    numuns=numuns+1
#Si hay un corte en la imagen asignamos el valor a nuestra variable para seguir buscando cortes despues
                    val=(int(img[altu][anch]))
#Retornams el numero de cortes encontrados a 1/2 de la imagen de forma horizontal
    return numuns                                   


#Nombre: caracteristica13
#Descripcion: Esta funcion nos regresa la relacion de cortes que en encuentran a 1/4 de la imagen de forma horizontal osea los cambios que hace entre 1´s y 0´s con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tamImg)
#return: Retorna la relacion de cortes que hay entre la imagen/tamaño total de la imagen    

#Creacion de la funcion
def caracteristica13(img, tamImg):
#Creamos la variable que contiene el alto de la imagen                   
    alto=len(img)
#Creamos la variable con el ancho de la imagen                                   
    ancho=int(tamImg/alto)
#Obtenemos la distancia en la cual haremos los cortes de la imagen                           
    altu=int(alto/4)
#Inicializaremos la variable que contendra el numero de cortes                                
    numuns=0 
#Inicializaremos la variable que contendra el valor que sera comparado despues para obtenes el numero de cortes                                       
    val=0
#For encargado de recorrer las filas de la imagen                                         
    for alt in range(alto):
#For encargado de recorrer las columnas de la imagen                         
        for anch in range(ancho):
#Aquí verificamos que nuestro buscador se encuentre en la columna que necesitamos analizar                   
            if alt==altu:
#Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente                           
                compara=(int(img[altu][anch]))
#Comparamos si el valor del pixel actual es diferente a la asignacion anterior, asi sabemos si hay cortes en la imagen
                if compara!=val:
#Se hace la sobrecarga del numero de cortes encontrados en la linea de busqueda                    
                    numuns=numuns+1
#Si hay un corte en la imagen asignamos el valor a nuestra variable para seguir buscando cortes despues
                    val=(int(img[altu][anch]))
#Retornams el numero de cortes encontrados a 1/4 de la imagen de forma horizontal
    return numuns                                   


#Nombre: caracteristica14
#Descripcion: Esta funcion nos regresa la relacion de cortes que en encuentran a 3/4 de la imagen de forma horizontal osea los cambios que hace entre 1´s y 0´s con respecto al tamaño total de la imagen
#Argumentos entrada: Recibe una imagen (img) y el tamaño total de la imagen (tamImg)
#return: Retorna la relacion de cortes que hay entre la imagen/tamaño total de la imagen

#Creacion de la funcion
def caracteristica14(img, tamImg):
#Creamos la variable que contiene el alto de la imagen                   
    alto=len(img)
#Creamos la variable con el ancho de la imagen                                   
    ancho=int(tamImg/alto)
#Obtenemos la distancia en la cual haremos los cortes de la imagen                           
    altu=int((int(alto/4))*3)
#Inicializaremos la variable que contendra el numero de cortes                       
    numuns=0
#Inicializaremos la variable que contendra el valor que sera comparado despues para obtenes el numero de cortes                                        
    val=0
#For encargado de recorrer las filas de la imagen                                           
    for alt in range(alto):
#For encargado de recorrer las columnas de la imagen                         
        for anch in range(ancho):
#Aquí verificamos que nuestro buscador se encuentre en la columna que necesitamos analizar                   
            if alt==altu:
#Aquí asignamos el valor del pixel a una variable para ser comparada posteriormente                          
                compara=(int(img[altu][anch]))
#Comparamos si el valor del pixel actual es diferente a la asignacion anterior, asi sabemos si hay cortes en la imagen
                if compara!=val:
#Se hace la sobrecarga del numero de cortes encontrados en la linea de busqueda                    
                    numuns=numuns+1
#Si hay un corte en la imagen asignamos el valor a nuestra variable para seguir buscando cortes despues
                    val=(int(img[altu][anch]))
#Retornams el numero de cortes encontrados a 1/4 de la imagen de forma horizontal
    return numuns                                   

#Nombre: generarArchivo
#Descripcion: En esta funcion llenamos el data set (archivo csv) con los datos de la matriz ya antes llenada
#Argumentos de entrada: Recibe la matriz datset la cual contiene todas las propiedades de todos los numeros analizados previamente
#Retorno: No hay retorno

#Declaracion de la funcion
def generarArchivo(datset):
#Asignamos los datos de datset a dataset para meter nos los mismos al archivo csv                         
    dataSet=datset
#Abrimos el archivo csv en el cual meteremos las propiedades                                  
    csvsalida=open('DataSet.csv','w',newline='')
#Se le indica a la variable salida que archivo sera escrito    
    salida=csv.writer(csvsalida)
#Se agregan los datos de la matriz a el archivo csv en cada celda 
#Se agrega la cabecera al archivo csv                                          
    salida.writerow(["Caracteristica 1","Caracteristica 2","Caracteristica 3","Caracteristica 4","Caracteristica 5","Caracteristica 6","Caracteristica 7","Caracteristica 8","Caracteristica 9","Caracteristica 10","Caracteristica 11","Caracteristica 12","Caracteristica 13","Caracteristica 14","Número"])      
#En esta parte se elimina la variable para que no ocupe espacio en memoria    
    salida.writerows(dataSet)    
    del salida
#Una vez que el archivo fue grabado lo cerramos                                      
    csvsalida.close()
#Imprimimos un mensaje indicando que el proceso a concluido                               
    print('El dataset se genero exitosamente')      
    

#Nombre: kNN
#Descripcion: Esta funcion realiza el algoritmo KNN y nos devuelve los K vecinos más cercanos
#Argumentos de entrada: Recibe la imagen de la nueva instancia y el número de vecinos a obtener
#Retorno: Los K vecinos más cercanos

#Declaración de la función
def kNN(img, numVeci):
#Leemos nuestra nueva instancia                     
    img=mpimg.imread(img) 
#Declaramos la matriz mat                  
    mat=[]
#Declaramos la matriz knn                                  
    knn=[] 
#Obtenemos el tamaño total de la imagen                                
    tamImg=img.size
#indica de que tamaño debemos crear la matriz en la cual meteremos los datos del dataSet                                                  
    for x in range(1736+1):
#Llenamos la matriz mat de 0´s para sustituir cada dato después               
        mat.append(['']*15)
#Esta matriz contendra solo los datos de cada distancia Euclidiana de cada clase con el nombre de la clase                 
    for x in range(1736):  
#Llenamos la matriz mat de 0´s para sustituir cada dato después               
        knn.append(['']*3)
#Leemos el dataSet                  
    reader = csv.reader(open('DataSet.csv'))
#Vaciamos el dataSet (csv) en nuestra matriz knn
    for index,row in enumerate(reader): 
#Recorremos cada columna del csv
        for cont in range(15):
#Colocamos cada dato de cada celda en un espacio de la matriz              
            mat[index][cont]=row[cont]      
#se llama a cada funcion para que nos devuelva cada propiedad de la nueva instancia    
    i2P1=caracteristica1(img, tamImg)              
    i2P2=caracteristica2(img, tamImg)              
    i2P3=caracteristica3(img, tamImg)               
    i2P4=caracteristica4(img, tamImg)              
    i2P5=caracteristica5(img, tamImg)              
    i2P6=caracteristica6(img, tamImg)               
    i2P7=caracteristica7(img, tamImg)               
    i2P8=caracteristica8(img, tamImg)               
    i2P9=caracteristica9(img, tamImg)               
    i2P10=caracteristica10(img, tamImg)             
    i2P11=caracteristica11(img, tamImg)             
    i2P12=caracteristica12(img, tamImg)             
    i2P13=caracteristica13(img, tamImg)             
    i2P14=caracteristica14(img, tamImg)             
    
#Aqui hacemos asignacion de cada propiedad de una clase a las variables de la ecuacion Euclidiana
#Este for recorre todos los datos del dataSet
    for val in range(1736):
#Se le asigna el valor de cada propiedad a cada variable                
        p1=float(mat[val+1][0])              
        p2=float(mat[val+1][1])              
        p3=float(mat[val+1][2])              
        p4=float(mat[val+1][3])              
        p5=float(mat[val+1][4])              
        p6=float(mat[val+1][5])              
        p7=float(mat[val+1][6])              
        p8=float(mat[val+1][7])              
        p9=float(mat[val+1][8])              
        p10=float(mat[val+1][9])             
        p11=float(mat[val+1][10])            
        p12=float(mat[val+1][11])            
        p13=float(mat[val+1][12])            
        p14=float(mat[val+1][13])            
        
#Aplicamos la distancia Euclidiana para cada clase de el dataset comparada con la nueva instancia
        dist= math.sqrt(((p1-i2P1)**2)+((p2-i2P2)**2)+((p3-i2P3)**2)+((p4-i2P4)**2)+((p5-i2P5)**2)+((p6-i2P6)**2)+((p7-i2P7)**2)+((p8-i2P8)**2)+((p9-i2P9)**2)+((p10-i2P10)**2)+((p11-i2P11)**2)+((p12-i2P12)**2)+((p13-i2P13)**2)+((p14-i2P14)**2))
#Asignacion de la posicion del resultado de la distancia entre dato e instancia nueva       
        knn[val][0]=val+1
#Asignacion de la distancia de nada dato con la nueva instancia                   
        knn[val][1]=dist 
#Asignacion de el nombre de la clase de cada dato                   
        knn[val][2]=mat[val+1][14]          
     
#Aqui se obtienen los K vecinos más cercanos 
#Declaramos una matriz para ingresarle nos k vecinos más cercanos
    res=[]  
#Llenamos de 0´s la matriz                                 
    for x in range(numVeci):
#Llenamos de 0´s la matriz para sustituir cada campo despues                
        res.append([0.0]*3)                 
#Se recorre la matriz las K veces    
    for i in range(numVeci):
#Asignamos el valor del primer datos a la variable temp                
        temp = knn[0][1]
#Obtenemos el tamaño de la matriz                    
        numero = len(knn) 
#Se recorre la matriz completa                  
        for j in range(numero):
#Se compra cada dato para ver si es el menor de todos             
            if(knn[j][1] < temp): 
#Si el dato es el menor re asigna a la variable temp
                temp = knn[j][1]
#Guardamos la posicion de la variable de menor valor
                apun=j
#Validamos si estamos en la ultima posicion                      
            if (j+1==numero):
#Asignamos la posicion en la matriz res
                res[i][0] = knn[apun][0]
#Asignamos la distancia en la matriz res
                res[i][1] = knn[apun][1]
#Asignamos la clase en la matriz res
                res[i][2] = knn[apun][2]
#Borramos el elemento para no repetir datos
                knn.pop(apun)
#Retornamos la matriz de los k vecinos mas cercanos
    return res                              
        
    
#Nombre: crearDataSet
#Descripcion: En esta funcion llenamos la matriz datS previamente declarada de puros 0´s para despues sustituir cada valor por cada una de las propiedades de todas las imagenes
#parametros: no
#retorno: La matriz con las propiedades
    
def crearDataSet():                                         #Declaracion de la funcion
    for i in range(1736):                                 #En este for se controlan el numero de filas de nuestra matriz
        data.append([0.0]*15)                               #Aqui asignamos el numero de columnas que llevara nuestra matriz y llenaremos cada espacio de 0´s
    rootDir = 'DatosPrueba'                                 #Declaramos la variable rootDir la cual contiene el nombre de la carpeta en la cual se encuentran las carpetas de nuestras imagenes
    nameima=''                                              #Declaramos esta variable la cual contendra la ruta completa de cada imagen
    x=0                                                     #Declaramos e inicializamos la variable que controlara la posicion de las filas de nuestra matriz
    y=0                                                     #Declaramos e inicializamos la variable que controlara la posicion de las columnas de nuestra matriz
    for dirName, subdirList, fileList in os.walk(rootDir):  #Este for recorrera las carpetas que contienen nuestras imagenes en la ruta especificada por "rootDir"
        num=str(dirName)+'  '                               #Obtenemos el nombre de la ruta actual para indicar en que carpeta nos encontramos
        for fname in fileList:                              #Este for controla cada imagen dentro de cada carpeta para que cada una sea abierta y analizada
            nameima=dirName+"/"+fname                       #Concatenamos las variables para obtener la ruta exacta de cada imagen
            img = mpimg.imread(nameima)                     #Leemos cada imagen de cada carpeta
            tamImg=img.size                                  #Asignamos el tamaño de cada imagen para su posterior uso
            data[x][y]=caracteristica1(img, tamImg)               #se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #incrementamos la variable "y" para poner cada propiedad en la columna correcta
            data[x][y]=caracteristica2(img, tamImg)               #se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #incrementamos la variable "y" para poner cada propiedad en la columna correcta
            data[x][y]=caracteristica3(img, tamImg)               #se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #incrementamos la variable "y" para poner cada propiedad en la columna correcta
            data[x][y]=caracteristica4(img, tamImg)               #se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #incrementamos la variable "y" para poner cada propiedad en la columna correcta
            data[x][y]=caracteristica5(img, tamImg)               #se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #incrementamos la variable "y" para poner cada propiedad en la columna correcta
            data[x][y]=caracteristica6(img, tamImg)               #se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #incrementamos la variable "y" para poner cada propiedad en la columna correcta
            data[x][y]=caracteristica7(img, tamImg)               #llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #incrementamos la variable "y" para poner cada propiedad en la columna correcta
            data[x][y]=caracteristica8(img, tamImg)               #se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #incrementamos la variable "y" para poner cada propiedad en la columna correcta
            data[x][y]=caracteristica9(img, tamImg)               #se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #incrementamos la variable "y" para poner cada propiedad en la columna correcta
            data[x][y]=caracteristica10(img, tamImg)              #se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #incrementamos la variable "y" para poner cada propiedad en la columna correcta
            data[x][y]=caracteristica11(img, tamImg)              #se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #incrementamos la variable "y" para poner cada propiedad en la columna correcta
            data[x][y]=caracteristica12(img, tamImg)              #se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #incrementamos la variable "y" para poner cada propiedad en la columna correcta
            data[x][y]=caracteristica13(img, tamImg)              #se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #incrementamos la variable "y" para poner cada propiedad en la columna correcta
            data[x][y]=caracteristica14(img, tamImg)              #se llama a cada funcion para que nos devuelva cada propiedad de cada imagen
            y=y+1                                           #incrementamos la variable "y" para poner cada propiedad en la columna correcta
            data[x][y]=num[12]                         #se llama a la funcion que nos devolvera el nombre de la clase
            y=0                                             #En esta parte regresamos "y" a cero para volver a la primera columna y llenar las propiedades de la siguiente imagen
            x=x+1                                           #Aqui incrementamos la variable "x" para indicar que estamos en la siguiente imagen
        if num[12]!=' ':                                    #Validamos si el caracter no es ' '
            print('Carpeta/ %s' % num[12])     #Aquí indicamos que carpeta exactamente estamos analizando
    return data                                             #En esta parte retornamos la matriz la llenada
    

#Nombre: Main
#Descripcion: Es la funcion principal la cual manda a llamar las demas funciones
#Parametros: No
#Return: No

#Aqui indicamos la funcion main
if __name__ == "__main__":
#En esta parte mandamos a llamar la funcion encargada de llenar la matriz con las propiedades de cada imagen                                                   
            #data=crearDataSet() 
#Aqui mandamos a llamar a la funcion encargada de generar el archivo csv                                             
            #generarArchivo(data) 
#Solicitamos el nombre de la imagen a clasificar                                            
            nomImg=input('Ingrese el nombre de la imagen a buscar: ')
#Solicitamos el numero de vecinos
            numVeci=int(input('Ingrese el número de vecinos: ')) 
#Llamamos a la funcion kNN y su valor de retorno se lo damos a mat            
            mat=kNN(nomImg, numVeci) 
#For para imprimir los K vecinos                                        
            for va in range(numVeci):
#variable que imprime el vecino                                        
                vecino=va+1 
# se imprimen el vecino
                print("\n Vecino # ", vecino)
#se imprime la pocision del vecino la distancia euclidiana y la clase a la que pertenece
                print( " Posición en DataSet: \n", mat[va][0],"\n Distancia euclidiana: \n",mat[va][1],"\n Clase: \n",mat[va][2])  
                print("-----------------------")
            print("La imagen pertenece a la clase :",mat[va][2])
            
            