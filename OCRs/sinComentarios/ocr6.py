
import matplotlib.image as mpimg
from PIL import Image
import os
import csv

 
a = 0
b = 0
conClase = 0
opcion = 0
matrizDataSet = []
for i in range(2370):
    matrizDataSet.append([0.0]*15)
    
    

def OP1(imagen, columnas, filas):
    promedioColFil = columnas/filas
    return promedioColFil


def OP2(imagen, columnas, filas):
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            uno = (int(imagen[i][j]))
            if(uno != 0):
                contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos


def OP3(imagen, columnas, filas):
    colInter = int(columnas/2)
    contUnos = 0
    promedioUnos = 0    
    for i in range(filas):
        for j in range(columnas):
            if(j == colInter):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos


def OP4(imagen, columnas, filas):
    colCuarto = int(columnas/4)
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            if(j == colCuarto):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos


def OP5(imagen, columnas, filas):
    colTresCuartos = int((columnas/4)*3)
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            if(j == colTresCuartos):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos


def OP6(imagen, columnas, filas):
    filInter = int(filas/2)
    contUnos = 0
    promedioUnos = 0    
    for i in range(filas):
        for j in range(columnas):
            if(i == filInter):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos


def OP7(imagen, columnas, filas):
    filCuarto = int(filas/4)
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            if(i == filCuarto):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos


def OP8(imagen, columnas, filas):
    filTresCuartos = int((filas/4)*3)
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            if(i == filTresCuartos):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos


def OP9(imagen, columnas, filas):
    colInter = int(columnas/2)
    contCortes = 0
    corte = 0
    for j in range(columnas):
        dato = (int(imagen[j][colInter]))
        if dato!=corte:
            contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes


def OP10(imagen, columnas, filas):
    colCuarto = int(columnas/4)
    contCortes = 0
    corte = 0
    for j in range(columnas):
        dato = (int(imagen[j][colCuarto]))
        if dato!=corte:
            contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes


def OP11(imagen, columnas, filas):
    colTresCuartos = int((columnas/4)*3)
    contCortes = 0
    corte = 0
    for j in range(columnas):
        dato = (int(imagen[j][colTresCuartos]))
        if dato!=corte:
            contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes


def OP12(imagen, columnas, filas):
    filInter = int(filas/2)
    contCortes = 0
    corte = 0
    for i in range(filas):
        for j in range(columnas):
            if i==filInter:
                dato = (int(imagen[filInter][j]))
                if dato!=corte:
                    contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes


def OP13(imagen, columnas, filas):
    filCuarto = int(filas/4)
    contCortes = 0
    corte = 0
    for i in range(filas):
        for j in range(columnas):
            if i==filCuarto:
                dato = (int(imagen[filCuarto][j]))
                if dato!=corte:
                    contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes


def OP14(imagen, columnas, filas):
    filTresCuartos = int((filas/4)*3)
    contCortes = 0
    corte = 0
    for i in range(filas):
        for j in range(columnas):
            if i==filTresCuartos:
                dato = (int(imagen[filTresCuartos][j]))
                if dato!=corte:
                    contCortes = contCortes+1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes
    

    

print("####Genera dataSet####")

carpeta = str(input("Ingrese Nombre de la Carpeta: "))

for directorio, subDirectorio, listArchivos in os.walk(carpeta):
    for file in listArchivos:
        png = directorio+"/"+file            
        imagen1 = mpimg.imread(png)
        imagen2 = Image.open(png)
        (columnas, filas) = imagen2.size
        matrizDataSet[a][b] = OP1(imagen1, columnas, filas)
        b = b+1
        matrizDataSet[a][b]= OP2(imagen1, columnas, filas)
        b +=1            
        matrizDataSet[a][b] = OP3(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP4(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP5(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP6(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP7(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP8(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP9(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP10(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP11(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP12(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP13(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = OP14(imagen1, columnas, filas)
        b +=1
        matrizDataSet[a][b] = conClase-1
        a +=1
        b = 0
    conClase = conClase+1
datosMatriz = matrizDataSet
csvSalida = open('DataSet.csv','w',newline='')
Salida = csv.writer(csvSalida)
Salida.writerow(["Propiedad1","Propiedad2","Propiedad3","Propiedad4",
                 "Propiedad5","Propiedad6","Propiedad7","Propiedad8",
                 "Propiedad9","Propiedad10","Propiedad11","Propiedad12",
                 "Propiedad13","Propiedad14","Clase"])
Salida.writerows(datosMatriz)
del Salida
csvSalida.close()
print("DataSet Generado: XD")


import matplotlib.image as mpimg
from PIL import Image
import csv
import math
 
CC = 0
CU = 0
CD = 0
CT = 0
CCT = 0
CCC = 0
CS = 0
CSi = 0
CO = 0
CN = 0



def OP1(imagen, columnas, filas):  
    promedioColFil = columnas/filas
    return promedioColFil


def OP2(imagen, columnas, filas):  
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            uno = (int(imagen[i][j]))
            if(uno != 0):
                contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos


def OP3(imagen, columnas, filas): 
    colInter = int(columnas/2)
    contUnos = 0
    promedioUnos = 0    
    for i in range(filas):
        for j in range(columnas):
            if(j == colInter):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos


def OP4(imagen, columnas, filas): 
    colCuarto = int(columnas/4)
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            if(j == colCuarto):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos


def OP5(imagen, columnas, filas): 
    colTresCuartos = int((columnas/4)*3)
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            if(j == colTresCuartos):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos


def OP6(imagen, columnas, filas): 
    filInter = int(filas/2)
    contUnos = 0
    promedioUnos = 0    
    for i in range(filas):
        for j in range(columnas):
            if(i == filInter):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos


def OP7(imagen, columnas, filas): 
    filCuarto = int(filas/4)
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            if(i == filCuarto):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos


def OP8(imagen, columnas, filas):  
    filTresCuartos = int((filas/4)*3)
    contUnos = 0
    promedioUnos = 0
    for i in range(filas):
        for j in range(columnas):
            if(i == filTresCuartos):
                if(imagen[i][j] != 0):
                    contUnos += 1
    promedioUnos = contUnos/(columnas*filas)
    return promedioUnos


def OP9(imagen, columnas, filas): 
    colInter = int(columnas/2)
    contCortes = 0
    corte = 0
    for j in range(columnas):
        dato = (int(imagen[j][colInter]))
        if dato!=corte:
            contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes


def OP10(imagen, columnas, filas): 
    colCuarto = int(columnas/4)
    contCortes = 0
    corte = 0
    for j in range(columnas):
        dato = (int(imagen[j][colCuarto]))
        if dato!=corte:
            contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes


def OP11(imagen, columnas, filas): 
    colTresCuartos = int((columnas/4)*3)
    contCortes = 0
    corte = 0
    for j in range(columnas):
        dato = (int(imagen[j][colTresCuartos]))
        if dato!=corte:
            contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes


def OP12(imagen, columnas, filas): 
    filInter = int(filas/2)
    contCortes = 0
    corte = 0
    for i in range(filas):
        for j in range(columnas):
            if i==filInter:
                dato = (int(imagen[filInter][j]))
                if dato!=corte:
                    contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes


def OP13(imagen, columnas, filas): 
    filCuarto = int(filas/4)
    contCortes = 0
    corte = 0
    for i in range(filas):
        for j in range(columnas):
            if i==filCuarto:
                dato = (int(imagen[filCuarto][j]))
                if dato!=corte:
                    contCortes += 1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes


def OP14(imagen, columnas, filas): 
    filTresCuartos = int((filas/4)*3)
    contCortes = 0
    corte = 0
    for i in range(filas):
        for j in range(columnas):
            if i==filTresCuartos:
                dato = (int(imagen[filTresCuartos][j]))
                if dato!=corte:
                    contCortes = contCortes+1
    promedioCortes = contCortes/(columnas*filas)
    return promedioCortes

    




def caracteristicas(imgen, nV): 
    imgenEntrada = mpimg.imread(imgen)  
    mat = []                            
    knn = []                            
    cont = 0
    imgCoFi = Image.open(imgen)
    (fil,col) = imgCoFi.size
   
   
    for x in range(2370+1): 
        mat.append(['']*15)    
    
    for x in range(2370):
        knn.append(['']*3)   
    reader = csv.reader(open('dataSet.csv')) 
    
    for index,row in enumerate(reader):  
        for cont in range(15): 
            mat[index][cont] = row[cont] 
            
    KOP1 = OP1(imgenEntrada,fil, col) 
    KOP2 = OP2(imgenEntrada,fil, col) 
    KOP3 = OP3(imgenEntrada,fil, col) 
    KOP4 = OP4(imgenEntrada,fil, col) 
    KOP5 = OP5(imgenEntrada,fil, col) 
    KOP6 = OP6(imgenEntrada,fil, col) 
    KOP7 = OP7(imgenEntrada,fil, col) 
    KOP8 = OP8(imgenEntrada,fil, col) 
    KOP9 = OP9(imgenEntrada,fil, col) 
    KOP10 = OP10(imgenEntrada,fil, col) 
    KOP11 = OP11(imgenEntrada,fil, col) 
    KOP12 = OP12(imgenEntrada,fil, col) 
    KOP13 = OP13(imgenEntrada,fil, col) 
    KOP14 = OP14(imgenEntrada,fil, col)
    
    for val in range(2370):  
        p1 = float(mat[val+1][0])   
        p2 = float(mat[val+1][1])   
        p3 = float(mat[val+1][2])   
        p4 = float(mat[val+1][3])   
        p5 = float(mat[val+1][4])   
        p6 = float(mat[val+1][5])   
        p7 = float(mat[val+1][6])   
        p8 = float(mat[val+1][7])   
        p9 = float(mat[val+1][8])   
        p10 = float(mat[val+1][9])  
        p11 = float(mat[val+1][10]) 
        p12 = float(mat[val+1][11]) 
        p13 = float(mat[val+1][12]) 
        p14 = float(mat[val+1][13])
        
        dist = math.sqrt(((p1-KOP1)**2)+((p2-KOP2)**2)+((p3-KOP3)**2)+
                        ((p4-KOP4)**2)+((p5-KOP5)**2)+((p6-KOP6)**2)+
                        ((p7-KOP7)**2)+((p8-KOP8)**2)+((p9-KOP9)**2)+
                        ((p10-KOP10)**2)+((p11-KOP11)**2)+((p12-KOP12)**2)+
                        ((p13-KOP13)**2)+((p14-KOP14)**2))       
        knn[val][0] = val+1  
        knn[val][1] = dist   
        knn[val][2] = mat[val+1][14]  
        
    res=[]  
    for x in range(nV):  
        res.append([0.0]*3)  
    elementos = knn 
    apun = 0
    for i in range(nV):  
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
    return res

    

dataSet = str(input("Ingrese Nombre del Archivo: "))
imagen = str(input("Ingrese el Ruta de la Imagen: "))
nV = int(input('Número de vecinos: '))
matData = caracteristicas(imagen, nV)
print("Numero de instancias en el dataSet: "+str(2370))
print("Numero de Propiedades: "+str(15))
print("Numero de clases: "+str(10))
print("Clases; 0, 1, 2, 3, 4, 5, 6, 7, 8, 9")
for i in range(nV):
    print(" Vecino: "+str(i+1)+"\n Posicion DataSet: "+str(matData[i][0])+
        "\n Clase: "+str(matData[i][2])+"\n Distancia: ",matData[i][1])
    if(matData[i][2]=='0'):
        CC += 1
    elif(matData[i][2]=='1'):
        CU += 1
    elif(matData[i][2]=='2'):
        CD += 1
    elif(matData[i][2]=='3'):
        CT += 1
    elif(matData[i][2]=='4'):
        CCT += 1
    elif(matData[i][2]=='5'):
        CCC +=1
    elif(matData[i][2]=='6'):
        CS += 1
    elif(matData[i][2]=='7'):
        CSi += 1
    elif(matData[i][2]=='8'):
        CO += 1
    elif(matData[i][2]=='9'):
        CN += 1
 
print("Instancias:"+str(237)+" Clase: "+"0"+" Vecinos encontrados:"+str(CC))
print("Instancias:"+str(237)+" Clase: "+"1"+" Vecinos encontrados:"+str(CU))
print("Instancias:"+str(237)+" Clase: "+"2"+" Vecinos encontrados:"+str(CD))
print("Instancias:"+str(237)+" Clase: "+"3"+" Vecinos encontrados:"+str(CT))
print("Instancias:"+str(237)+" Clase: "+"4"+" Vecinos encontrados:"+str(CCT))
print("Instancias:"+str(237)+" Clase: "+"5"+" Vecinos encontrados:"+str(CCC))
print("Instancias:"+str(237)+" Clase: "+"6"+" Vecinos encontrados:"+str(CS))
print("Instancias:"+str(237)+" Clase: "+"7"+" Vecinos encontrados:"+str(CSi))
print("Instancias:"+str(237)+" Clase: "+"8"+" Vecinos encontrados:"+str(CO))
print("Instancias:"+str(237)+" Clase: "+"9"+" Vecinos encontrados:"+str(CN))
print('La Imagen pertenece a la Clase: ',matData[0][2])

