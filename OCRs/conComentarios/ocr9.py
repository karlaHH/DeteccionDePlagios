# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 01:25:30 2016

@authores:Itzel&Daniel 
"""
#librerias ocupadas en el programa
import os
import matplotlib.image as im
from PIL import Image as IM
import csv,math

# funcion main                                                                       #
#  es la primera en ejecutarse y llama a la funcion proceso                          #

def inicio():

  
    repetir = 1
    while(repetir == 1):
        print("\nMenu de opciones\n1 Cargar Archivos \n2 Reconocer imagen")
        opcion = int(input('>>>>>>>>>  '))
        if(opcion == 1):    
            path = 'DatosPrueba'
            cargar(path)#llamamos al metodo cargar pasando como parametro la ruta del directorio
        elif(opcion == 2):
            knn()
        else:
            print("Ha ingresado una opcion incorrecta")
            menu()
        print("Realizar otra operaion\n1 >>>> Si\n2 >>>> No")
        repetir = int(input('>>>>>>  '))
        os.system ("cls")
#funcion cargar                                                                        #
# recolectar las carpetas y los archivos dentro de la carpeta padre                    #
# este metodo recibe string padre, es la ruta del directorio padre                     #

def cargar(padre):

    #lista donde se almacenaran cada una de las rutas del directorio padre
    rutas = []
    #recorrermos todos los archivos que hay dentro de la carpeta padre
    for (path, carpetas, archivos) in os.walk(padre):
        #recorremos las carpetas existentes en el directorio y accedemos a sus archivos
        for name in archivos:
            #concatenamos la el nombre de la carpeta con el nombre de la imagen
            ruta = path+"/"+name#
            rutas.append(ruta)#agreamos la ruta a la lista de rutas
    recolectar(rutas)#llamamos al metodo recolectar pasando como parametros las rutas ordenadas


# funcion recolectar                                                                       #
# abre todas las imagenes con las rutas obtenidas anteriormente                      #
# esta funcion recibe lista de todas las rutas de las imagenes                       #

def recolectar(rutas):

    #para saber el tiempo en que inicio el proceso
    n_archivo = "Caracteristicas.csv"
    #para escribir el el archivo csv
    csvsalida = open(n_archivo, 'w', newline='')
    escribir = csv.writer(csvsalida)
    #recorremos todas las imagenes para sacar sus atributos
    print("Escribiendo el dataset, el proceso puede tardar un rato")
    t = 0#variable total de lineas escritas
    carpeta = 0#para indicar el proceso    
    for i in range(len(rutas)):
        lineas = []#lista para los atributos por cada instancia
        img=im.imread(rutas[i])#abrir la imagen con este metodo para tener acceso a la matriz
        img1 = IM.open(rutas[i])#abrir la imagen con este metodo para tener acceso al metodo para calcular filas y columnas
        col, filas = img1.size#obtenemos el tamanio de cada imagen
        lineas.append(i+1)#atributo 0
        lineas.append(filascolumnas(filas,col))#atributo 1
        lineas.append(unostamanio(img,filas,col))#atributo 2
        #lista con los resultados de los atributos de las columnas
        r_col = cortecolum(img, filas, col)
        #lista con los resultados de los atributos de las filas
        r_filas = cortesfilas(img, filas, col)
        lineas.append(r_col[0])#atributo 3
        lineas.append(r_col[1])#atributo 4
        lineas.append(r_col[2])#atributo 5
        lineas.append(r_filas[0])#atributo 6
        lineas.append(r_filas[1])#atributo 7
        lineas.append(r_filas[2])#atributo 8
        lineas.append(r_col[3])#atributo 9
        lineas.append(r_col[4])#atributo 10
        lineas.append(r_col[5])#atributo 11
        lineas.append(r_filas[3])#atributo 12
        lineas.append(r_filas[4])#atributo 13
        lineas.append(r_filas[5])#atributo 14
        #del numbre de la ruta, tomamos el nombre de la carpeta
        #que este caso esta en la posicion 6
        #y este es la clase a la que pertenece
        lineas.append (str(rutas[i][12]))#atributo 15
        #guardamos en una lista nueva los renglones a escribir en el archivo
        data = [(lineas[0],lineas[1],lineas[2],lineas[3],lineas[4],lineas[5],lineas[6],lineas[7],lineas[8],lineas[9],lineas[10],lineas[11],lineas[12],lineas[13],lineas[14],lineas[15])]
        escribir.writerows(data)
        t = i+1
        #mostramos el proceso actual de la operacion
        if(carpeta != str(rutas[i][12])):
            os.system ("cls")
            carpeta +=0.007
            print("\nCarpeta >>> "+str(rutas[i][12]))
            print("Total de carga >>> "+str(carpeta)+str("%"))
        #fin del for total
    csvsalida.close()
    os.system ("cls")
    print("Total de carga >>> 100%")
    print("\nProceso terminado, se han escrito\nNumero de Intancias "+str(t)+"\nNumero de CLases 36\nNumero de Caracteristicas 14\n")

# funcion filascolumnas                                                                       #
# calcula el valor de las filas entre las columnas de cada imagen                    #
# Esta funcion recibe las filas y columnas (int col, int filas)                      #
# Y regresa la divicion de filas entre columas (float filas/columnas)                #

def filascolumnas(filas, col):

    return float(filas)/float(col)#se divide las filas de las columnas

# funcion unostamanio                                                                       #
# calcula la cantidad de 1´s entre el tamanio de la imagen                           #
# Esta funcion recibe los siguientes parametros array img, int filas, int col        #
# regresa el numero de unos entre el tamaño de la imagen                             #

def unostamanio(img, filas, col):
    
    unos = 0
    for i in range(filas):#se recoren las filas
        for j in range(col):#se recolen lascolumnas
            if(img[i][j] == 1):#se compara la matriz si alguno es uno
                unos+=1#se cuentan los unos
    return unos/(filas*col)#se divide el numero de unos por el tamaño


# funcion cortecolum                                                                  #
# calcula los atributos indicados en las columnas                                      #
# Esta funcion recibe los siguientes parametros array img, int filas, int col          #
# retorna el numero de unos entre el tamaño y los cortes de las columnas               #
# (atri3, atri4, atri5, atri 9, atri10, filascolumnas1)                                         #

def cortecolum(img, filas, col):

    #contadores de cada atributo
    atri3 = atri4 = atri5 = 0
    #condiciones de cada atributo
    condicion_atri3 = int(col/2)
    condicion_atri4 = int(col/4)
    condicion_atri5 = int((col/4)*3)
    #listas para calcular los cortes
    lista1 = []
    lista2 = []
    lista3 = []
    #recorremos toda la imagen y comparamos
    for i in range(filas):
        for j in range(col):
            if(j == condicion_atri3):
                lista1.append(img[i][j])#agregamos el valor en una lista, dependiendo la condicion
                if(img[i][j] == 1):
                    atri3+=1
                    atri3=atri3/(filas*col)
            if(j == condicion_atri4):
                lista2.append(img[i][j])
                if(img[i][j] == 1):
                    atri4+=1
                    atri4=atri4/(filas*col)
            if(j == condicion_atri5):
                lista3.append(img[i][j])
                if(img[i][j] == 1):
                    atri5+=1
                    atri5=atri5/(filas*col)
    #valor inicial para calcular los cortes
    inicio1 = lista1[0]
    inicio2 = lista2[0]
    inicio3 = lista3[0]
    #contadores de cada corte
    c_corte1 = 0
    c_corte2 = 0
    c_corte3 = 0
    #condicion para los cortes
    if(lista1[0] == 1):
        c_corte1+=1
    if(lista2[0] == 1):
        c_corte2+=1
    if(lista3[0] == 1):
        c_corte3+=1
    if(lista1[len(lista1)-1] == 1):
        c_corte1+=1
    if(lista2[len(lista1)-1] == 1):
        c_corte2+=1
    if(lista3[len(lista1)-1] == 1):
        c_corte3+=1
    #recorremos la lista de las columna y calculamos los cortes
    for l in range(len(lista1)):
        if(inicio1 != lista1[l]):
            inicio1 = lista1[l]
            c_corte1+=1
        if(inicio2 != lista2[l]):
            inicio2 = lista2[l]
            c_corte2+=1
        if(inicio3 != lista3[l]):
            inicio3 = lista3[l]
            c_corte3+=1
    atributos_col = [atri3, atri4, atri5, c_corte1, c_corte2, c_corte3]
    return atributos_col

#  funcion cortesfilas                                                                  #
#  calcula los atributos indicados en las filas                                      #
#  recibe los siguientes parametros array img, int filas, int col                    #
#  retorna el numero de unos eltre el tamaño y los cortes de las filas               #
#  (int atri6, atri7, atri8, atri12, atri13, atri4)                                  #

def cortesfilas(img, filas, col):

    #contadores de cada atributo
    atri6 = atri7 = atri8 = atri12 = atri13 = atri14 = 0
    #condiciones de cada atributo
    condicion_atri6 = int(filas/2)
    condicion_atri7 = int(filas/4)
    condicion_atri8 = int((filas/4)*3)
    #listas para calcular los cortes
    lista1 = []
    lista2 = []
    lista3 = []
    #recorremos toda la imagen y comparamos
    for i in range(filas):
        for j in range(col):
            if(i == condicion_atri6):
                lista1.append(img[i][j])#agregamos el valor en una lista, dependiendo la condicion
                if(img[i][j] == 1):
                    atri6+=1
                    atri6=atri6/(filas*col)
            if(i == condicion_atri7):
                lista2.append(img[i][j])#agregamos el valor en una lista, dependiendo la condicion
                if(img[i][j] == 1):
                    atri7+=1
                    atri7=atri7/(filas*col)
            if(i == condicion_atri8):
                lista3.append(img[i][j])#agregamos el valor en una lista, dependiendo la condicion
                if(img[i][j] == 1):
                    atri8+=1
                    atri8=atri8/(filas*col)
    #valor inicial para calcular los cortes
    inicio1 = lista1[0]
    inicio2 = lista2[0]
    inicio3 = lista3[0]
    #contadores de cada corte
    c_corte1 = c_corte2 = c_corte3 = 0
    #condicion para los cortes
    if(float(lista1[0]) == 1.0):
        c_corte1+=1
    if(float(lista2[0]) == 1.0):
        c_corte2+=1
    if(float(lista3[0]) == 1.0):
        c_corte3+=1
    if(float(lista1[len(lista1)-1]) == 1.0):
        c_corte1+=1
    if(float(lista2[len(lista1)-1]) == 1.0):
        c_corte2+=1
    if(float(lista3[len(lista1)-1]) == 1.0):
        c_corte3+=1
    #recorremos la lista de las columna y calculamos los cortes
    for l in range(len(lista1)):
        if(inicio1 != lista1[l]):
            inicio1 = lista1[l]
            c_corte1+=1
        if(inicio2 != lista2[l]):
            inicio2 = lista2[l]
            c_corte2+=1
        if(inicio3 != lista3[l]):
            inicio3 = lista3[l]
            c_corte3+=1
    atributos_filas = [atri6, atri7, atri8, c_corte1, c_corte2, c_corte3]
    return atributos_filas

# funcion knn                                                                        #
# calcular el metodo KNN                                                             #

def knn():

    ruta = "Caracteristicas.csv"
    print("Ingrese la ruta de la imagen que desea reconocer")
    r = input(' ')+".png"
    nueva = dataset(r)
    recolectar_data(ruta,nueva)

# funcion dataset                                                               #
# calcular los atributos de la imagen nueva                                          #
# Aqui se recibe la ruta de la imagen string r_imagen                                #
# y se retorna la list datos(datos de la imagen nueva)                               #
def dataset(r_imagen):

    datos = []
    img=im.imread(r_imagen)#abrir la imagen con este metodo para tener acceso a la matriz
    img1 = IM.open(r_imagen)#abrir la imagen con este metodo para tener acceso al metodo 
    col, filas = img1.size#obtenemos el tamanio de cada imagene
    datos.append(filascolumnas(filas,col))#atributo 1
    datos.append(unostamanio(img,filas,col))#atributo 2
    #lista con los resultados de los atributos de las columnas
    r_col = cortecolum(img, filas, col)
    #lista con los resultados de los atributos de las filas
    r_filas = cortesfilas(img, filas, col)
    datos.append(r_col[0])#atributo 3
    datos.append(r_col[1])#atributo 4
    datos.append(r_col[2])#atributo 5
    datos.append(r_filas[0])#atributo 6
    datos.append(r_filas[1])#atributo 7
    datos.append(r_filas[2])#atributo 8
    datos.append(r_col[3])#atributo 9
    datos.append(r_col[4])#atributo 10
    datos.append(r_col[5])#atributo 11
    datos.append(r_filas[3])#atributo 12
    datos.append(r_filas[4])#atributo 13
    datos.append(r_filas[5])#atributo 14
    return datos

# funcion recolectar_data                                                                      #
# lee el archivo csv y llama al metodo para calcular sus distanciass                      #
# recibimos los siguientes parametros string ruta, list x(datos de la imagen a calcular) #
# regresamos la lista distancias(la distancias de todas las lineas)                    #

def recolectar_data(ruta,x):

    read = csv.reader(open(ruta,'r'))
    datos_distancias = []
    dis = 0
    for index,row in enumerate(read):
        #aqui sacamos los datos de cada renglon y los pasamos como parametros para la funcion de calcular distancias
        y = [float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7]),float(row[8]),float(row[9]),float(row[10]),float(row[11]),float(row[12]),float(row[13]),float(row[14])]
        dis = distancias(x,y)
        atri = []
        atri.append(int(index+1))
        atri.append(dis)
        atri.append(row[15])
        datos_distancias.append(atri)
    vecinos(datos_distancias,ruta)

# funcion distancias                                                                  #
# calcula las distanciass de una instancia                                            #
# recibimos la lista x(instancia a calcular), lista y(instancia de cada renglon)     #
# regresamos la distancias (float distancias)                                          #

def distancias(x,y):

    total = 0.0
    for i in range(len(x)):
        total+=((float(x[i])-float(y[i]))**2)
    return math.sqrt(total)

# funcion vecinos                                                                    #
# calcula los vecinos mas cercanos y obtiene su clase                                #
# recibimos los parametros list datos_distancias, string ruta                         #


def vecinos(datos_distancias,ruta):
    print("Ingrese el valor de K")
    k = int(input('>>>>>  '))
    solo_distanciass = []#solo almacenara las distancias
    for x in range(len(datos_distancias)):
        solo_distanciass.append(datos_distancias[x][1])
    #solo obtener las distanciass ordenadas dependiendo de k
    veci = []
    distan = sorted(solo_distanciass)
    for i in range(len(distan)):
        if(i == int(k)):
            break
        else:
            veci.append(distan[i])
    print("Numero de Intancias 14264\nNumero de CLases 36 \nNumero de Caracteristicas 14\n")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>") 
    print("\nValor de K ="+str(k)+"\nNo Instancia     distancias          Clase")
    for z in range(len(datos_distancias)):
        for y in range(len(veci)):
            if(veci[y] == datos_distancias[z][1]):
                print(" "+str(datos_distancias[z][0])+"        "+str(datos_distancias[z][1])+"   "+str(datos_distancias[z][2]))
    #contadores de cada clase
    carac0 = carac1 = carac2 = carac3 = carac4 = carac5 = carac6 = carac7 = carac8 = carac9 = cA = cB = cC = cD = cE = cF = cG = cH = cI = cJ = cK = cL = cM = cN = cO = cP = cQ = cR = cS = cT = cU = cV = cW = cX = cY = cZ = 0
    c=-1
    read = csv.reader(open(ruta,'r'))#abrimos el archivo
    for index,row in enumerate(read):#recorremos el archivo del dataset
        for j in range(k):#comparamos con cada valor de la lista de vecinos
            if(solo_distanciass[c] == veci[j]):#comparaciones para cada clase
                if(row[15] == '0'):
                    carac0+=1
                elif(row[15] == '1'):
                    carac1+=1
                elif(row[15] == '2'):
                    carac2+=1
                elif(row[15]== '3'):
                    carac3+=1
                elif(row[15] == '4'):
                    carac4+=1
                elif(row[15] == '5'):
                    carac5+=1
                elif(row[15] == '6'):
                    carac6+=1
                elif(row[15] == '7'):
                    carac7+=1
                elif(row[15] == '8'):
                    carac8+=1
                elif(row[15] == '9'):
                    carac9+=1
                elif(row[15] == 'A'):
                    cA+=1
                elif(row[15] == 'B'):
                    cB+=1
                elif(row[15] == 'C'):
                    cC+=1
                elif(row[15] == 'D'):
                    cD+=1
                elif(row[15] == 'E'):
                    cE+=1
                elif(row[15] == 'F'):
                    cF+=1
                elif(row[15] == 'G'):
                    cG+=1
                elif( row[15] == 'H'):
                    cH+=1
                elif(row[15] == 'I'):
                    cI+=1
                elif(row[15] == 'J'):
                    cJ+=1
                elif(row[15] == 'K'):
                    cK+=1
                elif(row[15]== 'L'):
                    cL+=1
                elif(row[15] == 'M'):
                    cM+=1
                elif(row[15] == 'N'):
                    cN+=1
                elif(row[15] == 'O'):
                    cO+=1
                elif(row[15] == 'P'):
                    cP+=1
                elif(row[15] == 'Q'):
                    cQ+=1
                elif(row[15] == 'R'):
                    cR+=1
                elif(row[15] == 'S'):
                    cS+=1
                elif(row[15] == 'T'):
                    cT+=1
                elif(row[15] == 'U'):
                    cU+=1
                elif(row[15] == 'V'):
                    cV+=1
                elif(row[15] == 'W'):
                    cW+=1
                elif(row[15] == 'X'):
                    cX+=1
                elif(row[15] == 'Y'):
                    cY+=1
                elif( row[15] == 'Z'):
                    cZ+=1
        c+=1
    
    #comparaciones para cada clase por medio de los contadores, el que sea mayor es al que le pertenece la clase
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")   
    print("Clase  total distancias  Clase  total distancias")
    print('  0           '+str(carac0)+'            A       '+str(cA))
    print('  1           '+str(carac1)+'            B       '+str(cB))
    print('  2           '+str(carac2)+'            C       '+str(cC))
    print('  3           '+str(carac3)+'            D       '+str(cD))
    print('  4           '+str(carac4)+'            E       '+str(cE))
    print('  5           '+str(carac5)+'            F       '+str(cF))
    print('  6           '+str(carac6)+'            G       '+str(cG))
    print('  7           '+str(carac7)+'            H       '+str(cH))
    print('  8           '+str(carac8)+'            I       '+str(cI))
    print('  9           '+str(carac9)+'            J       '+str(cJ))
    print('                           K       '+str(cK))
    print('                           L       '+str(cL))
    print('                           M       '+str(cM))
    print('                           N       '+str(cN))
    print('                           O       '+str(cO))
    print('                           P       '+str(cP))
    print('                           Q       '+str(cQ))
    print('                           R       '+str(cR))
    print('                           S       '+str(cS))
    print('                           T       '+str(cT))
    print('                           U       '+str(cU))
    print('                           V       '+str(cV))
    print('                           W       '+str(cW))
    print('                           X       '+str(cX))
    print('                           Y       '+str(cY))
    print('                           Z       '+str(cZ))
    
    if(carac0 > carac1 and carac0 > carac2 and carac0 > carac3 and carac0 > carac4 and carac0 > carac5 and carac0 > carac6 and carac0 > carac7 and carac0 > carac8 and carac0 > carac9 and carac0 > cA and carac0 > cB and carac0 > cC and carac0 > cD and carac0 > cE and carac0 > cF and carac0 > cG and carac0 > cH and carac0 > cI and carac0 > cJ and carac0 > cK and carac0 > cL and carac0 > cM and carac0 > cN and carac0 > cO and carac0 > cP and carac0 > cQ and carac0 > cR and carac0 > cS and carac0 > cT and carac0 > cU and carac0 > cV and carac0 > cW and carac0 > cX and carac0 > cY and carac0 > cZ):
        print("La imagen es ---> 0")
    elif(carac1 > carac0 and carac1 > carac2 and carac1 > carac3 and carac1 > carac4 and carac1 > carac5 and carac1 > carac6 and carac1 > carac7 and carac1 > carac8 and carac1 > carac9 and carac1 > cA and carac1 > cB and carac1 > cC and carac1 > cD and carac1 > cE and carac1 > cF and carac1 > cG and carac1 > cH and carac1 > cI and carac1 > cJ and carac1 > cK and carac1 > cL and carac1 > cM and carac1 > cN and carac1 > cO and carac1 > cP and carac1 > cQ and carac1 > cR and carac1 > cS and carac1 > cT and carac1 > cU and carac1 > cV and carac1 > cW and carac1 > cX and carac1 > cY and carac1 > cZ):
        print("La imagen es ---> 1")
    elif(carac2 > carac0 and carac2 > carac1 and carac2 > carac3 and carac2 > carac4 and carac2 > carac5 and carac2 > carac6 and carac2 > carac7 and carac2 > carac8 and carac2 > carac9 and carac2 > cA and carac2 > cB and carac2 > cC and carac2 > cD and carac2 > cE and carac2 > cF and carac2 > cG and carac2 > cH and carac2 > cI and carac2 > cJ and carac2 > cK and carac2 > cL and carac2 > cM and carac2 > cN and carac2 > cO and carac2 > cP and carac2 > cQ and carac2 > cR and carac2 > cS and carac2 > cT and carac2 > cU and carac2 > cV and carac2 > cW and carac2 > cX and carac2 > cY and carac2 > cZ):
        print("La imagen es ---> 2")
    elif(carac3 > carac0 and carac3 > carac1 and carac3 > carac2 and carac3 > carac4 and carac3 > carac5 and carac3 > carac6 and carac3 > carac7 and carac3 > carac8 and carac3 > carac9 and carac3 > cA and carac3 > cB and carac3 > cC and carac3 > cD and carac3 > cE and carac3 > cF and carac3 > cG and carac3 > cH and carac3 > cI and carac3 > cJ and carac3 > cK and carac3 > cL and carac3 > cM and carac3 > cN and carac3 > cO and carac3 > cP and carac3 > cQ and carac3 > cR and carac3 > cS and carac3 > cT and carac3 > cU and carac3 > cV and carac3 > cW and carac3 > cX and carac3 > cY and carac3 > cZ):
        print("La imagen es ---> 3")
    elif(carac4 > carac0 and carac4 > carac1 and carac4 > carac2 and carac4 > carac3 and carac4 > carac5 and carac4 > carac6 and carac4 > carac7 and carac4 > carac8 and carac4 > carac9 and carac4 > cA and carac4 > cB and carac4 > cC and carac4 > cD and carac4 > cE and carac4 > cF and carac4 > cG and carac4 > cH and carac4 > cI and carac4 > cJ and carac4 > cK and carac4 > cL and carac4 > cM and carac4 > cN and carac4 > cO and carac4 > cP and carac4 > cQ and carac4 > cR and carac4 > cS and carac4 > cT and carac4 > cU and carac4 > cV and carac4 > cW and carac4 > cX and carac4 > cY and carac4 > cZ):
        print("La imagen es ---> 4")
    elif(carac5 > carac0 and carac5 > carac1 and carac5 > carac2 and carac5 > carac3 and carac5 > carac4 and carac5 > carac6 and carac5 > carac7 and carac5 > carac8 and carac5 > carac9 and carac5 > cA and carac5 > cB and carac5 > cC and carac5 > cD and carac5 > cE and carac5 > cF and carac5 > cG and carac5 > cH and carac5 > cI and carac5 > cJ and carac5 > cK and carac5 > cL and carac5 > cM and carac5 > cN and carac5 > cO and carac5 > cP and carac5 > cQ and carac5 > cR and carac5 > cS and carac5 > cT and carac5 > cU and carac5 > cV and carac5 > cW and carac5 > cX and carac5 > cY and carac5 > cZ):
        print("La imagen es ---> 5")
    elif(carac6 > carac0 and carac6 > carac1 and carac6 > carac2 and carac6 > carac3 and carac6 > carac4 and carac6 > carac5 and carac6 > carac7 and carac6 > carac8 and carac6 > carac9 and carac6 > cA and carac6 > cB and carac6 > cC and carac6 > cD and carac6 > cE and carac6 > cF and carac6 > cG and carac6 > cH and carac6 > cI and carac6 > cJ and carac6 > cK and carac6 > cL and carac6 > cM and carac6 > cN and carac6 > cO and carac6 > cP and carac6 > cQ and carac6 > cR and carac6 > cS and carac6 > cT and carac6 > cU and carac6 > cV and carac6 > cW and carac6 > cX and carac6 > cY and carac6 > cZ):
        print("La imagen es ---> 6")
    elif(carac7 > carac0 and carac7 > carac1 and carac7 > carac2 and carac7 > carac3 and carac7 > carac4 and carac7 > carac5 and carac7 > carac6 and carac7 > carac8 and carac7 > carac9 and carac7 > cA and carac7 > cB and carac7 > cC and carac7 > cD and carac7 > cE and carac7 > cF and carac7 > cG and carac7 > cH and carac7 > cI and carac7 > cJ and carac7 > cK and carac7 > cL and carac7 > cM and carac7 > cN and carac7 > cO and carac7 > cP and carac7 > cQ and carac7 > cR and carac7 > cS and carac7 > cT and carac7 > cU and carac7 > cV and carac7 > cW and carac7 > cX and carac7 > cY and carac7 > cZ):
        print("La imagen es ---> 7")
    elif(carac8 > carac0 and carac8 > carac1 and carac8 > carac2 and carac8 > carac3 and carac8 > carac4 and carac8 > carac5 and carac8 > carac6 and carac8 > carac7 and carac8 > carac9 and carac8 > cA and carac8 > cB and carac8 > cC and carac8 > cD and carac8 > cE and carac8 > cF and carac8 > cG and carac8 > cH and carac8 > cI and carac8 > cJ and carac8 > cK and carac8 > cL and carac8 > cM and carac8 > cN and carac8 > cO and carac8 > cP and carac8 > cQ and carac8 > cR and carac8 > cS and carac8 > cT and carac8 > cU and carac8 > cV and carac8 > cW and carac8 > cX and carac8 > cY and carac8 > cZ):
        print("La imagen es  ---> 8")
    elif(carac9 > carac0 and carac9 > carac1 and carac9 > carac2 and carac9 > carac3 and carac9 > carac4 and carac9 > carac5 and carac9 > carac6 and carac9 > carac9 and carac7 > carac9 and carac8 > cA and carac9 > cB and carac9 > cC and carac9 > cD and carac9 > cE and carac9 > cF and carac9 > cG and carac9 > cH and carac9 > cI and carac9 > cJ and carac9 > cK and carac9 > cL and carac9 > cM and carac9 > cN and carac9 > cO and carac9 > cP and carac9 > cQ and carac9 > cR and carac9 > cS and carac9 > cT and carac9 > cU and carac9 > cV and carac9 > cW and carac9 > cX and carac9 > cY and carac9 > cZ):
        print("La imagen es ---> 9") 
    elif(cA > carac0 and cA > carac2 and cA > carac3 and cA > carac4 and cA > carac5 and cA > carac6 and cA > carac7 and cA > carac8 and cA > carac9 and cA > carac1 and cA > cB and cA > cC and cA > cD and cA > cE and cA > cF and cA > cG and cA > cH and cA > cI and cA > cJ and cA > cK and cA > cL and cA > cM and cA > cN and cA > cO and cA > cP and cA > cQ and cA > cR and cA > cS and cA > cT and cA > cU and cA > cV and cA > cW and cA > cX and cA > cY and cA > cZ):
        print("La imagen es  ---> A") 
    elif(cB > carac0 and cB > carac2 and cB > carac3 and cB > carac4 and cB > carac5 and cB > carac6 and cB > carac7 and cB > carac8 and cB > carac9 and cB > cA and cB > carac1 and cB > cC and cB > cD and cB > cE and cB > cF and cB > cG and cB > cH and cB > cI and cB > cJ and cB > cK and cB > cL and cB > cM and cB > cN and cB > cO and cB > cP and cB > cQ and cB > cR and cB > cS and cB > cT and cB > cU and cB > cV and cB > cW and cB > cX and cB > cY and cB > cZ):
        print("La imagen es  ---> B")
    elif(cC > carac0 and cC > carac2 and cC > carac3 and cC > carac4 and cC > carac5 and cC > carac6 and cC > carac7 and cC > carac8 and cC > carac9 and cC > cA and cC > carac1 and cC > cB and cC > cD and cC > cE and cC > cF and cC > cG and cC > cH and cC > cI and cC > cJ and cC > cK and cC > cL and cC > cM and cC > cN and cC > cO and cC > cP and cC > cQ and cC > cR and cC > cS and cC > cT and cC > cU and cC > cV and cC > cW and cC > cX and cC > cY and cC > cZ):
        print("La imagen es  ---> C")
    elif(cD > carac0 and cD > carac2 and cD > carac3 and cD > carac4 and cD > carac5 and cD > carac6 and cD > carac7 and cD > carac8 and cD > carac9 and cD > cA and cD > carac1 and cD > cB and cD > cC and cD > cE and cD > cF and cD > cG and cD > cH and cD > cI and cD > cJ and cD > cK and cD > cL and cD > cM and cD > cN and cD > cO and cD > cP and cD > cQ and cD > cR and cD > cS and cD > cT and cD > cU and cD > cV and cD > cW and cD > cX and cD > cY and cD > cZ):
        print("La imagen es  ---> D")
    elif(cE > carac0 and cE > carac2 and cE > carac3 and cE > carac4 and cE > carac5 and cE > carac6 and cE > carac7 and cE > carac8 and cE > carac9 and cE > cA and cE > carac1 and cE > cB and cE > cC and cE > cD and cE > cF and cE > cG and cE > cH and cE > cI and cE > cJ and cE > cK and cE > cL and cE > cM and cE > cN and cE > cO and cE > cP and cE > cQ and cE > cR and cE > cS and cE > cT and cE > cU and cE > cV and cE > cW and cE > cX and cE > cY and cE > cZ):
        print("La imagen es  ---> E")
    elif(cF > carac0 and cF > carac2 and cF > carac3 and cF > carac4 and cF > carac5 and cF > carac6 and cF > carac7 and cF > carac8 and cF > carac9 and cF > cA and cF > carac1 and cF > cB and cF > cC and cF > cD and cF > cE and cF > cG and cF > cH and cF > cI and cF > cJ and cF > cK and cF > cL and cF > cM and cF > cN and cF > cO and cF > cP and cF > cQ and cF > cR and cF > cS and cF > cT and cF > cU and cF > cV and cF > cW and cF > cX and cF > cY and cF > cZ):
        print("La imagen es  ---> F")
    elif(cG > carac0 and cG > carac2 and cG > carac3 and cG > carac4 and cG > carac5 and cG > carac6 and cG > carac7 and cG > carac8 and cG > carac9 and cG > cA and cG > carac1 and cG > cB and cG > cC and cG > cD and cG > cE and cG > cF and cG > cH and cG > cI and cG > cJ and cG > cK and cG > cL and cG > cM and cG > cN and cG > cO and cG > cP and cG > cQ and cG > cR and cG > cS and cG > cT and cG > cU and cG > cV and cG > cW and cG > cX and cG > cY and cG > cZ):
        print("La imagen es  ---> G")
    elif(cH > carac0 and cH > carac2 and cH > carac3 and cH > carac4 and cH > carac5 and cH > carac6 and cH > carac7 and cH > carac8 and cH > carac9 and cH > cA and cH > carac1 and cH > cB and cH > cC and cH > cD and cH > cE and cH > cF and cH > cG and cH > cI and cH > cJ and cH > cK and cH > cL and cH > cM and cH > cN and cH > cO and cH > cP and cH > cQ and cH > cR and cH > cS and cH > cT and cH > cU and cH > cV and cH > cW and cH > cX and cH > cY and cH > cZ):
        print("La imagen es  ---> H")
    elif(cI > carac0 and cI > carac2 and cI > carac3 and cI > carac4 and cI > carac5 and cI > carac6 and cI > carac7 and cI > carac8 and cI > carac9 and cI > cA and cI > carac1 and cI > cB and cI > cC and cI > cD and cI > cE and cI > cF and cI > cG and cI > cH and cI > cJ and cI > cK and cI > cL and cI > cM and cI > cN and cI > cO and cI > cP and cI > cQ and cI > cR and cI > cS and cI > cT and cI > cU and cI > cV and cI > cW and cI > cX and cI > cY and cI > cZ):
        print("La imagen es  ---> I")
    elif(cJ > carac0 and cJ > carac2 and cJ > carac3 and cJ > carac4 and cJ > carac5 and cJ > carac6 and cJ > carac7 and cJ > carac8 and cJ > carac9 and cJ > cA and cJ > carac1 and cJ > cB and cJ > cC and cJ > cD and cJ > cE and cJ > cF and cJ > cG and cJ > cH and cJ > cI and cJ > cK and cJ > cL and cJ > cM and cJ > cN and cJ > cO and cJ > cP and cJ > cQ and cJ > cR and cJ > cS and cJ > cT and cJ > cU and cJ > cV and cJ > cW and cJ > cX and cJ > cY and cJ > cZ):
        print("La imagen es  ---> J")
    elif(cK > carac0 and cK > carac2 and cK > carac3 and cK > carac4 and cK > carac5 and cK > carac6 and cK > carac7 and cK > carac8 and cK > carac9 and cK > cA and cK > carac1 and cK > cB and cK > cC and cK > cD and cK > cE and cK > cF and cK > cG and cK > cH and cK > cI and cK > cJ and cK > cL and cK > cM and cK > cN and cK > cO and cK > cP and cK > cQ and cK > cR and cK > cS and cK > cT and cK > cU and cK > cV and cK > cW and cK > cX and cK > cY and cK > cZ):
        print("La imagen es  ---> K")
    elif(cL > carac0 and cL > carac2 and cL > carac3 and cL > carac4 and cL > carac5 and cL > carac6 and cL > carac7 and cL > carac8 and cL > carac9 and cL > cA and cL > carac1 and cL > cB and cL > cC and cL > cD and cL > cE and cL > cF and cL > cG and cL > cH and cL > cI and cL > cJ and cL > cK and cL > cM and cL > cN and cL > cO and cL > cP and cL > cQ and cL > cR and cL > cS and cL > cT and cL > cU and cL > cV and cL > cW and cL > cX and cL > cY and cL > cZ):
        print("La imagen es  ---> L")
    elif(cM > carac0 and cM > carac2 and cM > carac3 and cM > carac4 and cM > carac5 and cM > carac6 and cM > carac7 and cM > carac8 and cM > carac9 and cM > cA and cM > carac1 and cM > cB and cM > cC and cM > cD and cM > cE and cM > cF and cM > cG and cM > cH and cM > cI and cM > cJ and cM > cK and cM > cL and cM > cN and cM > cO and cM > cP and cM > cQ and cM > cR and cM > cS and cM > cT and cM > cU and cM > cV and cM > cW and cM > cX and cM > cY and cM > cZ):
        print("La imagen es  ---> M")
    elif(cN > carac0 and cN > carac2 and cN > carac3 and cN > carac4 and cN > carac5 and cN > carac6 and cN > carac7 and cN > carac8 and cN > carac9 and cN > cA and cN > carac1 and cN > cB and cN > cC and cN > cD and cN > cE and cN > cF and cN > cG and cN > cH and cN > cI and cN > cJ and cN > cK and cN > cL and cN > cM and cN > cO and cN > cP and cN > cQ and cN > cR and cN > cS and cN > cT and cN > cU and cN > cV and cN > cW and cN > cX and cN > cY and cN > cZ):
        print("La imagen es  ---> N") 
    elif(cO > carac0 and cO > carac2 and cO > carac3 and cO > carac4 and cO > carac5 and cO > carac6 and cO > carac7 and cO > carac8 and cO > carac9 and cO > cA and cO > carac1 and cO > cB and cO > cC and cO > cD and cO > cE and cO > cF and cO > cG and cO > cH and cO > cI and cO > cJ and cO > cK and cO > cL and cO > cM and cO > cN and cO > cP and cO > cQ and cO > cR and cO > cS and cO > cT and cO > cU and cO > cV and cO > cW and cO > cX and cO > cY and cO > cZ):
        print("La imagen es  ---> O")
    elif(cP > carac0 and cP > carac2 and cP > carac3 and cP > carac4 and cP > carac5 and cP > carac6 and cP > carac7 and cP > carac8 and cP > carac9 and cP > cA and cP > carac1 and cP > cB and cP > cC and cP > cD and cP > cE and cP > cF and cP > cG and cP > cH and cP > cI and cP > cJ and cP > cK and cP > cL and cP > cM and cP > cN and cP > cO and cP > cQ and cP > cR and cP > cS and cP > cT and cP > cU and cP > cV and cP > cW and cP > cX and cP > cY and cP > cZ):
        print("La imagen es  ---> P")
    elif(cQ > carac0 and cQ > carac2 and cQ > carac3 and cQ > carac4 and cQ > carac5 and cQ > carac6 and cQ > carac7 and cQ > carac8 and cQ > carac9 and cQ > cA and cQ > carac1 and cQ > cB and cQ > cC and cQ > cD and cQ > cE and cQ > cF and cQ > cG and cQ > cH and cQ > cI and cQ > cJ and cQ > cK and cQ > cL and cQ > cM and cQ > cN and cQ > cO and cQ > cP and cQ > cR and cQ > cS and cQ > cT and cQ > cU and cQ > cV and cQ > cW and cQ > cX and cQ > cY and cQ > cZ):
        print("La imagen es  ---> Q")
    elif(cR > carac0 and cR > carac2 and cR > carac3 and cR > carac4 and cR > carac5 and cR > carac6 and cR > carac7 and cR > carac8 and cR > carac9 and cR > cA and cR > carac1 and cR > cB and cR > cC and cR > cD and cR > cE and cR > cF and cR > cG and cR > cH and cR > cI and cR > cJ and cR > cK and cR > cL and cR > cM and cR > cN and cR > cO and cR > cP and cR > cS and cR > cQ and cR > cT and cR > cU and cR > cV and cR > cW and cR > cX and cR > cY and cR > cZ):
        print("La imagen es  ---> R")
    elif(cS > carac0 and cS > carac2 and cS > carac3 and cS > carac4 and cS > carac5 and cS > carac6 and cS > carac7 and cS > carac8 and cS > carac9 and cS > cA and cS > carac1 and cS > cB and cS > cC and cS > cD and cS > cE and cS > cF and cS > cG and cS > cH and cS > cI and cS > cJ and cS > cK and cS > cL and cS > cM and cS > cN and cS > cO and cS > cP and cS > cR and cS > cQ and cS > cT and cS > cU and cS > cV and cS > cW and cS > cX and cS > cY and cS > cZ):
        print("La imagen es  ---> S")
    elif(cT > carac0 and cT > carac2 and cT > carac3 and cT > carac4 and cT > carac5 and cT > carac6 and cT > carac7 and cT > carac8 and cT > carac9 and cT > cA and cT > carac1 and cT > cB and cT > cC and cT > cD and cT > cE and cT > cF and cT > cG and cT > cH and cT > cI and cT > cJ and cT > cK and cT > cL and cT > cM and cT > cN and cT > cO and cT > cP and cT > cR and cT > cQ and cT > cS and cT > cU and cT > cV and cT > cW and cT > cX and cT > cY and cT > cZ):
        print("La imagen es  ---> T")
    elif(cU > carac0 and cU > carac2 and cU > carac3 and cU > carac4 and cU > carac5 and cU > carac6 and cU > carac7 and cU > carac8 and cU > carac9 and cU > cA and cU > carac1 and cU > cB and cU > cC and cU > cD and cU > cE and cU > cF and cU > cG and cU > cH and cU > cI and cU > cJ and cU > cK and cU > cL and cU > cM and cU > cN and cU > cO and cU > cP and cU > cR and cU > cQ and cU > cS and cU > cT and cU > cV and cU > cW and cU > cX and cU > cY and cU > cZ):
        print("La imagen es  ---> U")
    elif(cV > carac0 and cV > carac2 and cV > carac3 and cV > carac4 and cV > carac5 and cV > carac6 and cV > carac7 and cV > carac8 and cV > carac9 and cV > cA and cV > carac1 and cV > cB and cV > cC and cV > cD and cV > cE and cV > cF and cV > cG and cV > cH and cV > cI and cV > cJ and cV > cK and cV > cL and cV > cM and cV > cN and cV > cO and cV > cP and cV > cR and cV > cQ and cV > cS and cV > cT and cV > cU and cV > cW and cV > cX and cV > cY and cV > cZ):
        print("La imagen es  ---> V")
    elif(cW > carac0 and cW > carac2 and cW > carac3 and cW > carac4 and cW > carac5 and cW > carac6 and cW > carac7 and cW > carac8 and cW > carac9 and cW > cA and cW > carac1 and cW > cB and cW > cC and cW > cD and cW > cE and cW > cF and cW > cG and cW > cH and cW > cI and cW > cJ and cW > cK and cW > cL and cW > cM and cW > cN and cW > cO and cW > cP and cW > cR and cW > cQ and cW > cS and cW > cT and cW > cU and cW > cV and cW > cX and cW > cY and cW > cZ):
        print("La imagen es  ---> W")
    elif(cX > carac0 and cX > carac2 and cX > carac3 and cX > carac4 and cX > carac5 and cX > carac6 and cX > carac7 and cX > carac8 and cX > carac9 and cX > cA and cX > carac1 and cX > cB and cX > cC and cX > cD and cX > cE and cX > cF and cX > cG and cX > cH and cX > cI and cX > cJ and cX > cK and cX > cL and cX > cM and cX > cN and cX > cO and cX > cP and cX > cR and cX > cQ and cX > cS and cX > cT and cX > cU and cX > cV and cX > cW and cX > cY and cX > cZ):
        print("La imagen es  ---> X")
    elif(cY > carac0 and cY > carac2 and cY > carac3 and cY > carac4 and cY > carac5 and cY > carac6 and cY > carac7 and cY > carac8 and cY > carac9 and cY > cA and cY > carac1 and cY > cB and cY > cC and cY > cD and cY > cE and cY > cF and cY > cG and cY > cH and cY > cI and cY > cJ and cY > cK and cY > cL and cY > cM and cY > cN and cY > cO and cY > cP and cY > cR and cY > cQ and cY > cS and cY > cT and cY > cU and cY > cV and cY > cW and cY > cX and cY > cZ):
        print("La imagen es  ---> Y")
    elif(cZ > carac0 and cZ > carac2 and cZ > carac3 and cZ > carac4 and cZ > carac5 and cZ > carac6 and cZ > carac7 and cZ > carac8 and cZ > carac9 and cZ > cA and cZ > carac1 and cZ > cB and cZ > cC and cZ > cD and cZ > cE and cZ > cF and cZ > cG and cZ > cH and cZ > cI and cZ > cJ and cZ > cK and cZ > cL and cZ > cM and cZ > cN and cZ > cO and cZ > cP and cZ > cR and cZ > cQ and cZ > cS and cZ > cT and cZ > cU and cZ > cV and cZ > cW and cZ > cX and cZ > cY):
        print("La imagen es  ---> Z")
    
        
    
    
    
    
    
#llamada el metodo inicio, el cual inicia la ejecucion del programa
inicio()
