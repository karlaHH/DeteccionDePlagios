# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 21:52:55 2016

@author: crush
"""



import matplotlib.image as mpimg
import os
import csv
#  ///////// /////    ////////     ///////////    ///////////    ///////
#Nombre:Area 
#Descripcion: calcula el area de la imagen 
#Argumentos:img= imagen que se esta analizando 
#Retorno: area= filas*columnas
def Area (img):
    [filas,columnas]=img.shape #img.shape sirve para obtener los valores de la imgen
    area=filas*columnas
    return area
#Nombre:Relacion 
#Descripcion: calcula la razon entre filas y columnas de la imagen 
#Argumentos:img= imagen que se esta analizando 
#Retorno: razon = filas/columnas
def Relacion(img):
    [numero_filas,numero_columnas]=img.shape
    razon=numero_filas/numero_columnas
    return razon
#Nombre: LineasVerticales5
#Descripcion: crea 5 lineas verticales en la imagen y cuentas veces se cortaron las 5 lineas 
#Argumentos: img = imagen a procesar 
#Retorno: cortado= total de cortes en las 5 lineas 
def lineasVerticales5 (img):
    [numero_filas,numero_columnas]=img.shape 
    movimiento_filas=numero_filas/5
    movimiento_filas=int(movimiento_filas)
    cortado=0

    for j in range(0,numero_filas,movimiento_filas):
        for i in range(0,numero_columnas):
            if img[j,i]!=img[j-1,i]:
                cortado+=1
    return cortado
    
#Nombre: LineasVerticales3
#Descripcion:Creo 3 lineas Verticales y cuento cuantos cortes hubo en las lineas creadas 
#Argumentos: img=imagen a procesar
#Retorno:    cortado= total de cortes que se encontraron 
def lineasVerticales3 (img):
    [filas,columnas]=img.shape 
    movimiento_filas=filas/3
    movimiento_filas=int(movimiento_filas)
    cortado=0

    for j in range(0,filas,movimiento_filas):
        for i in range(0,columnas):
            if img[j,i]!=img[j-1,i]:
                cortado+=1
    return cortado

#Nombre: LineasHorizontales5
#Descripcion: crea 5 lineas horizontales en la imagen y cuenta cuantas veces se encontr un corte en la linea 
#Argumentos:img=imagen a procesar 
#Retorno:cortado= total de cortes en las lineas 
def lineasHorizontales5 (img):
    [filas,columnas]=img.shape
    movimiento_columnas=columnas/5
    movimiento_columnas=int(movimiento_columnas)
    cortado=0
    for j in range(0,columnas,movimiento_columnas):
        for i in range(0,filas):
            if img[i,j]!=img[i-1,j]:
                cortado+=1 
    return cortado

#Nombre: LineasHorizontales3
#Descripcion:crea 3 lineas horizontales en la imagen y cuenta cuantas veces se encontr un corte en la linea 
#Argumentos:img=imagen a procesar 
#Retorno:  cortado= total de cortes en las lineas  
def lineasHorizontales3 (img):
    [filas,columnas]=img.shape
    movimiento_columnas=columnas/3
    movimiento_columnas=int(movimiento_columnas)
    cortado=0
    for j in range(0,columnas,movimiento_columnas):
        for i in range(0,filas):
            if img[i,j]!=img[i-1,j]:
                cortado+=1 
    return cortado
    
    
# Nombre:LineaHorizontal
#Descripcion: crea una linea horizontal en el centro de la imagen y cuento cuantas veces cambio su valor, de 0 a 1 o de 1 a 0
#Argumentos: fila=el numero de filas de la imagen,columna=numero de columnas, img= la imagen en matriz 
#Retorno :cortado= el numero de cambios que detecto la funcion, puntos1= total de "1" en la imagen 
def lineaHorizontal(filas,columnas,img):
    mitad=filas/2
    mitad=int(mitad)
    cortado=0
    puntos1=0
    for i in range(0,columnas):
    #print(img[d2,contador])
        if img[mitad,i]==1:
            puntos1+=1
        if img[mitad,i]!=img[mitad,i-1]:
            cortado+=1
    #print("lineas horizontales"+str(cortado))
   # print(mitad)
   # print("lo logre!")
    return cortado,puntos1
    
#Nombre:LineaVertical
#Descripcion: Crea una linea vertical en el centro de la imagen, y cuanta cuantas veces cambio su valor de 0 a 1 o de 1 a 0
#Argumentos:fila=el numero de filas de la imagen,columna=numero de columnas, img= la imagen en matriz 
#Retrono:cortado=numero de cambios que detecto la funcion  puntos1= total de "1" en la imagen
def lineaVertical(filas,columnas,img):
    
    mitad=0
    cortado=0
    mitad=columnas/2
    mitad=int(mitad)
    puntos1=0
    for i in range(0,filas):
    #print(img[d2,contador])
        if img[i,mitad]==1:
            puntos1+=1
        if img[i,mitad]!=img[i-1,mitad]:
            cortado+=1
    #print("cortes verticales: "+str(cortado))
    #print(mitad)
    return cortado,puntos1
    
#Nombre:PixelesNegrosyBlancos
#Descripcion:cuento cuantos pixeles son 0 y cuantos son 1
#Argumentos:fila=el numero de filas de la imagen,columna=numero de columnas, img= la imagen en matriz 
#Retrono:  blancos=numero de pixeles que son 1 negros= numero de pixeles que son 0   
def pixelesNegrosYBlancos(filas,columnas,img):
    
    negros=0
    blancos=0
    for l in range(0,filas):
        for m in range(0,columnas):
            if img[l,m]==1:
                blancos+=1
            else:
                negros+=1
    return blancos,negros

#Nombre:BuscarArchivo
#Descripcion:busca y guarda el nombre de los archivos que tenga en el directorio con terminacion PNG
#Argumentos:ruta= es la ruta donde voy a buscar los archivos PNG
#Retrono:lstFiles=lista con todos los nombres que encontro con terminacion PNG
def BuscarArchivos(ruta): 
    path =ruta
    #Lista vacia para incluir los ficheros
    lstFiles = []
 
     #Lista con todos los ficheros del directorio:
    lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
#Crea una lista de los ficheros png que existen en el directorio y los incluye a la lista.
    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if(extension == ".png"):
                lstFiles.append(nombreFichero+extension)
                        
    #print(lstFiles)            
    #print ("LISTADO FINALIZADO")
    #print (len(lstFiles))
                        
    return lstFiles

#Nombre: LineasHorizontales2
#Descripcion:
#Argumentos:
#Retorno:    
def lineasVerticalesyHorizontales2(img):
    
    [filas,columnas]=img.shape   # obtengo el numero de filas y columnas de la imagen  
    mitadfila=filas/2 # encuentro la mitad de la imagen(largo)
    mitadcolumna=columnas/2#33 encutro la mitad de la imagen (ancho)
    mitadfila=int(mitadfila) # se castean en caso de obtener algun valor decimal
    mitadcolumna=int(mitadcolumna) # se castean en caso de obtener algun valor decimal

    aux1=mitadfila+(filas/10)
    aux2=mitadfila-(filas/10)
    aux3=mitadcolumna+(columnas/10)
    aux4=mitadcolumna-(columnas/10)
    blancos1=0 #cuantos "1" encontre en la primera linea
    blancos2=0 # cuantos "1" encontre en la segunda linea 
    cortado1=0 # cuantos cortes detecte en la primera linea 
    cortado2=0 # cuntos cortes deetecte en la segunda linea 
    
     #pinta rayas horizontales
    for i in range(0,columnas):
        # este bloque encuentra los "1"
        if img[aux1,i]==1:
            blancos1+=1
        if img[aux2,i]==1:
            blancos1+=1
        # Este bloque encuentra los cortes 
        if img[aux1,i]!=img[aux1,i-1]:
            cortado1+=1
        if img[aux2,i]!=img[aux2,i-1]:
            cortado1+=1
    #pinta rayas verticales  
    for i in range (0,filas):
         # este bloque encuentra los "1"
        if img[i,aux3]!=img[i-1,aux3]:
            cortado2+=1
        if img[i,aux4]!=img[i-1,aux4]:
            cortado2+=1
        # Este bloque encuentra los cortes     
        if img[i,aux3]==1:
            blancos2+=1
        if img[i,aux4]==1:
            blancos2+=1
    return blancos1,blancos2,cortado1,cortado2
        

#  /////////////////////////////////////////////////////////////////////////////////////////////////

def main(opc):
    
    if opc=="si":
        ruta='numeros/'
        archivo= open('dataset.csv', 'w', newline='')
        salida = csv.writer(archivo)
        contador=1
        for i in range(0,10):
            print(" obteniendo caracteristicas de "+str(i))
            ruta=ruta+str(i) # agrego el nombre de la carpeta a la ruta 
            ls=BuscarArchivos(ruta) # creo la lista con los nombres de los archivos que encontre 
            
            for j in range(0,len(ls)):
                rutaimagen=ruta+'/'+ls[j] #creo la ruta de la imagen 
                img=mpimg.imread(rutaimagen)
                [fila,columna]=img.shape
                dato1=Relacion(img)
                dato2=Area(img)
                [dato3,negro1]=lineaVertical(fila,columna,img)
                [dato4,negro2]=lineaHorizontal(fila,columna,img)
                [x1,x2,x3,x4]=lineasVerticalesyHorizontales2(img)
                dato5=lineasHorizontales5(img)
                dato6=lineasVerticales5(img)
                dato7=lineasHorizontales3(img)
                dato8=lineasVerticales3(img)
                dato9=x1+x2 #cuantos "1" encontre en los dos cortes 
                dato10=x3+x4# cuantos cambios de valor encontre en los dos cortes 
                dato11=negro1
                dato12=negro2
                dato13=(dato3+dato4)/fila # relacion entre los cambios quedetecte en una cruz en la imagen entre las filas 
                [dato14,dato15]=pixelesNegrosYBlancos(fila,columna,img)
                salida.writerow([dato1,dato2,dato3,dato4,dato5,dato6,dato7,dato8,dato9,dato10,dato11,dato12,dato13,dato14,dato15,i,contador])
                #print(str(d1)+","+str(d2)+","+str(d3)+","+str(d4)+","+str(d5)+","+str(d6)+","+str(d7)+" Clase "+str(i))
                contador+=1
            ruta='numeros/'#reinicio la ruta para un nuevo numero
        print("termino de crear las caracteristicas")   
        archivo.close()

print("desea crear un nuevo dataset?")
opcion=input()

main(opcion)

    
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 21:56:32 2016

@author: crush
"""

import csv
import math
import OCR
import matplotlib.image as mpimg
f= open('dataset.csv')
lns=csv.reader(f)
print("Cual es el nombre de la imagen que se va clasificar: ",end="")
rutaImagen=input()
img=mpimg.imread(rutaImagen)
dataset=list(lns)

distancias=[0,0]
beca=[0,0]
contador=0

for i in dataset:
    
    dataset[contador][0]=float(dataset[contador][0])
    dataset[contador][1]=float(dataset[contador][1])
    dataset[contador][2]=float(dataset[contador][2])
    dataset[contador][3]=float(dataset[contador][3])
    dataset[contador][4]=float(dataset[contador][4])
    dataset[contador][5]=float(dataset[contador][5])
    dataset[contador][6]=float(dataset[contador][6])
    dataset[contador][7]=float(dataset[contador][7])
    dataset[contador][8]=float(dataset[contador][8])
    dataset[contador][9]=float(dataset[contador][9])
    dataset[contador][10]=float(dataset[contador][10])
    dataset[contador][11]=float(dataset[contador][11])
    dataset[contador][12]=float(dataset[contador][12])
    dataset[contador][13]=float(dataset[contador][13])
    dataset[contador][14]=float(dataset[contador][14])
    dataset[contador][15]=float(dataset[contador][15])
    dataset[contador][16]=float(dataset[contador][16])
    contador+=1
    
Matrix=dataset
[fila,columna]=img.shape
dato1=OCR.Relacion(img)
dato2=OCR.Area(img)
[dato3,negro1]=OCR.lineaVertical(fila,columna,img)
[dato4,negro2]=OCR.lineaHorizontal(fila,columna,img)
[x1,x2,x3,x4]=OCR.lineasVerticalesyHorizontales2(img)
dato5=OCR.lineasHorizontales5(img)
dato6=OCR.lineasVerticales5(img)
dato7=OCR.lineasHorizontales3(img)
dato8=OCR.lineasVerticales3(img)
dato9=x1+x2 #cuantos "1" encontre en los dos cortes 
dato10=x3+x4# cuantos cambios de valor encontre en los dos cortes 
dato11=negro1
dato12=negro2
dato13=(dato3+dato4)/fila # relacion entre los cambios quedetecte en una cruz en la imagen entre las filas 
[dato14,dato15]=OCR.pixelesNegrosYBlancos(fila,columna,img)


prediccion=[dato1,dato2,dato3,dato4,dato5,dato6,dato7,dato8,dato9,dato10,dato11,dato12,dato13,dato14,dato15] 
contador=0



for i in Matrix:# realizo la distancia euclidiana
    aux=0
    aux=(pow((Matrix[contador][0]-dato1),2))+ (pow((Matrix[contador][1]-dato2),2))+ (pow((Matrix[contador][2]-dato3),2))+ (pow((Matrix[contador][3]-dato4),2))+(pow((Matrix[contador][4]-dato5),2)) +(pow((Matrix[contador][5]-dato6),2))
    aux=aux+(pow((Matrix[contador][6]-dato7),2))+ (pow((Matrix[contador][7]-dato8),2))+ (pow((Matrix[contador][8]-dato9),2))+ (pow((Matrix[contador][9]-dato10),2))+(pow((Matrix[contador][10]-dato11),2)) +(pow((Matrix[contador][11]-dato12),2))
    aux=aux+(pow((Matrix[contador][12]-dato13),2))+ (pow((Matrix[contador][13]-dato14),2))+ (pow((Matrix[contador][14]-dato15),2))     
    aux=math.sqrt(aux)
    Matrix[contador].append(aux)
    contador+=1
print(Matrix[0])
Matrix.sort(key=lambda Matrix: Matrix[17])


print("Ingrese el numero de K vecinos: ",end="")
k=input()
k=int(k)
contador0=0
contador1=0
contador2=0
contador3=0
contador4=0
contador5=0
contador6=0
contador7=0
contador8=0
contador9=0

print("\tInformacion del dataset ************************\n\n")
print("Numero de instancias: "+str(len(Matrix)))
print("Numero de clases: 10")
print("Nombre de las clases: 0,1,2,3,4,5,6,7,8,9 ")
print("Numero de propiedades por instancia: "+str(len(dataset[0])-2))
print(len(Matrix))
print("\t\tresultados de la clasificacion|||||||||||||||||||||||||\n")
for i in range(0,k):
    print("\n")
    print("Vecino #"+str(i+1))
    print ("\tDistancia euclidiana: "+str(Matrix[i][17])+"\tClase a la que pertenece: "+str(Matrix[i][15])+"Numero de instancia: "+str(Matrix[i][16]))
print("\n")    


for i in range  (k):
    
    #print(Matrix[contador][4])
    if Matrix[i][15]==1:
        contador1+=1
    if Matrix[i][15]==2:
        contador2+=1
    if Matrix[i][15]==3:
        contador3+=1
    if Matrix[i][15]==4:
        contador4+=1
    if Matrix[i][15]==5:
        contador5+=1
    if Matrix[i][15]==6:
        contador6+=1
    if Matrix[i][15]==7:
        contador7+=1
    if Matrix[i][15]==8:
        contador8+=1
    if Matrix[i][15]==9:
        contador9+=1
    if Matrix[i][15]==0:
        contador0+=1

totales=[[contador0," es un cero"],[contador1,"El numero es un uno "],[contador2,"El numero es un dos"],[contador3,"El numero es un tres"],[contador4,"El numero es un cuatro"],[contador5,"El numero es un cinco"],[contador6,"El numero es un seis"],[contador7,"El numero es un siete"],[contador8,"El numero es un ocho"],[contador9,"El numero es un nueve"],]

print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n")
for i in range(0,len(totales)):
    print("Se encontraron "+str(totales[i][0])+" resigistros de la clase "+str(i))
totales.sort(key=lambda totales: totales[0])
print("\n\n\resultado de la clasificacion\n\n")
print (totales[9][1])
