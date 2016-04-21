
 

import matplotlib.image as imgs

import os

import csv




alto=0

ancho=0




def primerCaracteristica(img):
    
    tam=img.size
    
    alto=len(img)
    
    ancho=int(tam/alto)
    
    contadorDeUnos = 0
    
    for a in range(alto):
        for b in range(ancho):
            
            dato = (int(img[a][b]))
            
            if dato!=1:
                
                contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)
    





def segundaCaracteristica(img):
    
    tam=img.size
    
    alto=len(img)
    
    ancho=int(tam/alto)
    
    
    prom = ancho/alto
    
    return prom





def tercerCaracteristica(img):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    filaIntermedia = int(ancho/2)
    
    contadorDeUnos = 0
    
    for al in range(alto):
        
        dato = (int(img[al][filaIntermedia]))
        
        if dato == 1:
            
            contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)
    




def cuartaCaracteristica(img):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    filaUnCuarto= int(ancho/4)
    
    contadorDeUnos = 0
    
    for al in range(alto):
        
        dato = (int(img[al][filaUnCuarto]))
        
        if dato == 1:
            
           contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)





def quintaCaracteristica(img):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    filaTresCuartos = int((int(ancho/4))*3)
    
    contadorDeUnos = 0
    
    for al in range(alto):
        
        dato = (int(img[al][filaTresCuartos]))
        
        if dato == 1:
            
            contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)
       




def sextaCaracteristica(img):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    colItermedia = int(alto/2)
    
    contadorDeUnos = 0
    
    for fil in range(alto):
        
        for col in range(ancho):
            
            if fil == colItermedia:
                
                dato = (int(img[colItermedia][col]))
                
                if dato == 1:
                    
                    contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)





def septimaCaracteristica(img):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    columnaUnCuarto = int(alto/4)
    
    contadorDeUnos = 0
    
    for fil in range(alto):
        
        for col in range(ancho):
            
            if fil == columnaUnCuarto:
                
                dato = (int(img[columnaUnCuarto][col]))
                
                if dato == 1:
                    
                    contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)






def octavaCaracteristica(img):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    colTresCuartos = int((int(alto/4))*3)
    
    contadorDeUnos = 0
    
    for fil in range(alto):
        
        for col in range(ancho):
            
            if fil == colTresCuartos:
                
                dato = (int(img[fil][col]))
                
                if dato == 1:
                    
                    contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)






def novenaCaracteristica(img):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    columnaIntermedia = int(ancho/2)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for fil in range(alto):
        
        dato = (int(img[fil][columnaIntermedia]))
        
        if dato!=corte:
            
            contadorDeCortes = contadorDeCortes+1
            
    
    return contadorDeCortes/(alto*ancho)






def decimaCaracteristica(img):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    filaUnCuarto = int(ancho/4)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for fil in range(alto):
        
        dato = (int(img[fil][filaUnCuarto]))
        
        if dato!=corte:
            
            contadorDeCortes = contadorDeCortes+1
            
    
    return contadorDeCortes/(alto*ancho)





def onceavaCaracteristica(img):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    col = int((int(ancho/4))*3)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for al in range(alto):
        
        dato = (int(img[al][col]))
        
        if dato!=corte:
            
            contadorDeCortes = contadorDeCortes+1
            
    
    return contadorDeCortes/(alto*ancho)





def doceavaCaracteristica(img):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    columaIntermedia = int(alto/2)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for an in range(alto):
        
        for an2 in range(ancho):
            
            if an==columaIntermedia:
                
                dato = (int(img[columaIntermedia][an2]))
                
                if dato!=corte:
                    
                    contadorDeCortes = contadorDeCortes+1
                    
    
    return contadorDeCortes/(alto*ancho)





def treceavaCaracteristica(img):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    columnaUnCuarto = int(alto/4)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for fil in range(alto):
        
        for col in range(ancho):
            
            if fil == columnaUnCuarto:
                
                dato = (int(img[columnaUnCuarto][col]))
                
                if dato!=corte:
                    
                    contadorDeCortes = contadorDeCortes+1
                    
    
    return contadorDeCortes/(alto*ancho)





def catorceavaCaracteristica(img):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    columnaTresCuartos = int((int(alto/4))*3)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for fil in range(alto):
        
        for col in range(ancho):
            
            if fil == columnaTresCuartos:
                
                dato = (int(img[columnaTresCuartos][col]))
                
                if dato!=corte:
                    
                    contadorDeCortes = contadorDeCortes+1
                    
    
    return contadorDeCortes/(alto*ancho)



print("obteniendo carracteristicas, por favor espere un momento")
matriz = [] 

for i in range(2369):
    matriz.append([0]*15)

rootDir = 'DatosPrueba'

name=''

x=0

y=0

for dirName, subdirList, fileList in os.walk(rootDir):
    
    
    for fname in fileList:
        
        name=dirName+"/"+fname
        
        img = imgs.imread(name)
        
        
        matriz[x][y]=primerCaracteristica(img)
        
        y=y+1
        matriz[x][y]=segundaCaracteristica(img)
        
        y=y+1
        matriz[x][y]=tercerCaracteristica(img)
        
        y=y+1
        matriz[x][y]=cuartaCaracteristica(img)
        
        y=y+1
        matriz[x][y]=quintaCaracteristica(img)
        
        y=y+1
        matriz[x][y]=sextaCaracteristica(img)
        
        y=y+1
        matriz[x][y]=septimaCaracteristica(img)
        
        y=y+1
        matriz[x][y]=octavaCaracteristica(img)
        
        y=y+1
        matriz[x][y]=novenaCaracteristica(img)
        
        y=y+1
        matriz[x][y]=decimaCaracteristica(img)
        
        y=y+1
        matriz[x][y]=onceavaCaracteristica(img)
        y=y+1
        matriz[x][y]=doceavaCaracteristica(img)
        y=y+1
        matriz[x][y]=treceavaCaracteristica(img)
        y=y+1
        matriz[x][y]=catorceavaCaracteristica(img)
        y=y+1
        matriz[x][y]=name[12]
        
        x = x+1
        
        y = 0   
        





archivo = open('dataSet.csv','w',newline='')

escritura = csv.writer(archivo)

escritura.writerow(["C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","Clase"])

print("Creando dataset, por favor espere un momento")
escritura.writerows(matriz)

del escritura

print("Dataset ha sido creado con exito")
archivo.close()



 

import matplotlib.image as mpimg
from PIL import Image
import math
import csv


matriz = []

contadorCero = 0
contadorUno = 0
contadorDos = 0
contadorTres = 0
contadorCuatro = 0
contadorCinco = 0
contadorSeis = 0
contadorSiete = 0
contadorOcho = 0
contadorNueve = 0
x = 0
y = 0
contadorClase = 0

for i in range(2369):
    
    matriz.append([0.0]*15)


def primerCaracteristica(img,alto,ancho):
    
    tam=img.size
    
    alto=len(img)
    
    ancho=int(tam/alto)
    
    contadorDeUnos = 0
    
    for a in range(alto):
        for b in range(ancho):
            
            dato = (int(img[a][b]))
            
            if dato!=1:
                
                contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)
    





def segundaCaracteristica(img,alto,ancho):
    
    tam=img.size
    
    alto=len(img)
    
    ancho=int(tam/alto)
    
    
    prom = ancho/alto
    
    return prom





def tercerCaracteristica(img,alto,ancho):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    filaIntermedia = int(ancho/2)
    
    contadorDeUnos = 0
    
    for al in range(alto):
        
        dato = (int(img[al][filaIntermedia]))
        
        if dato == 1:
            
            contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)
    




def cuartaCaracteristica(img,alto,ancho):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    filaUnCuarto= int(ancho/4)
    
    contadorDeUnos = 0
    
    for al in range(alto):
        
        dato = (int(img[al][filaUnCuarto]))
        
        if dato == 1:
            
           contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)





def quintaCaracteristica(img,alto,ancho):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    filaTresCuartos = int((int(ancho/4))*3)
    
    contadorDeUnos = 0
    
    for al in range(alto):
        
        dato = (int(img[al][filaTresCuartos]))
        
        if dato == 1:
            
            contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)
       




def sextaCaracteristica(img,alto,ancho):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    colItermedia = int(alto/2)
    
    contadorDeUnos = 0
    
    for fil in range(alto):
        
        for col in range(ancho):
            
            if fil == colItermedia:
                
                dato = (int(img[colItermedia][col]))
                
                if dato == 1:
                    
                    contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)





def septimaCaracteristica(img,alto,ancho):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    columnaUnCuarto = int(alto/4)
    
    contadorDeUnos = 0
    
    for fil in range(alto):
        
        for col in range(ancho):
            
            if fil == columnaUnCuarto:
                
                dato = (int(img[columnaUnCuarto][col]))
                
                if dato == 1:
                    
                    contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)






def octavaCaracteristica(img,alto,ancho):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    colTresCuartos = int((int(alto/4))*3)
    
    contadorDeUnos = 0
    
    for fil in range(alto):
        
        for col in range(ancho):
            
            if fil == colTresCuartos:
                
                dato = (int(img[fil][col]))
                
                if dato == 1:
                    
                    contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)






def novenaCaracteristica(img,alto,ancho):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    columnaIntermedia = int(ancho/2)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for fil in range(alto):
        
        dato = (int(img[fil][columnaIntermedia]))
        
        if dato!=corte:
            
            contadorDeCortes = contadorDeCortes+1
            
    
    return contadorDeCortes/(alto*ancho)






def decimaCaracteristica(img,alto,ancho):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    filaUnCuarto = int(ancho/4)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for fil in range(alto):
        
        dato = (int(img[fil][filaUnCuarto]))
        
        if dato!=corte:
            
            contadorDeCortes = contadorDeCortes+1
            
    
    return contadorDeCortes/(alto*ancho)





def onceavaCaracteristica(img,alto,ancho):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    col = int((int(ancho/4))*3)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for al in range(alto):
        
        dato = (int(img[al][col]))
        
        if dato!=corte:
            
            contadorDeCortes = contadorDeCortes+1
            
    
    return contadorDeCortes/(alto*ancho)





def doceavaCaracteristica(img,alto,ancho):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    columaIntermedia = int(alto/2)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for an in range(alto):
        
        for an2 in range(ancho):
            
            if an==columaIntermedia:
                
                dato = (int(img[columaIntermedia][an2]))
                
                if dato!=corte:
                    
                    contadorDeCortes = contadorDeCortes+1
                    
    
    return contadorDeCortes/(alto*ancho)





def treceavaCaracteristica(img,alto,ancho):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    columnaUnCuarto = int(alto/4)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for fil in range(alto):
        
        for col in range(ancho):
            
            if fil == columnaUnCuarto:
                
                dato = (int(img[columnaUnCuarto][col]))
                
                if dato!=corte:
                    
                    contadorDeCortes = contadorDeCortes+1
                    
    
    return contadorDeCortes/(alto*ancho)





def catorceavaCaracteristica(img,alto,ancho):
    
    tam=img.size
    alto=len(img)
    ancho=int(tam/alto)
    
    columnaTresCuartos = int((int(alto/4))*3)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for fil in range(alto):
        
        for col in range(ancho):
            
            if fil == columnaTresCuartos:
                
                dato = (int(img[columnaTresCuartos][col]))
                
                if dato!=corte:
                    
                    contadorDeCortes = contadorDeCortes+1
                    
    
    return contadorDeCortes/(alto*ancho)



def kNN(img, numVeci):
   
    imgc = mpimg.imread(img)
    
    mat = []
    
    knn = []
    
    cont = 0

    
    imgCoFi = Image.open(img)
    
    (fil,col) = imgCoFi.size
    
    for x in range(2369+1):
        
        mat.append(['']*15)
    
    for x in range(2369):
        
        knn.append(['']*3)
    
    reader = csv.reader(open('dataSet.csv'))
    
    for index,row in enumerate(reader):
        
        for cont in range(15):
            
            mat[index][cont] = row[cont]
    
    imagen2P1 = primerCaracteristica(imgc,col,fil)
    imagen2P2=segundaCaracteristica(imgc, col,fil)               
    imagen2P3=tercerCaracteristica(imgc, col,fil)               
    imagen2P4=cuartaCaracteristica(imgc, col,fil)               
    imagen2P5=quintaCaracteristica(imgc, col,fil)               
    imagen2P6=sextaCaracteristica(imgc, col,fil)               
    imagen2P7=septimaCaracteristica(imgc, col,fil)               
    imagen2P8=octavaCaracteristica(imgc, col,fil)              
    imagen2P9=novenaCaracteristica(imgc, col,fil)               
    imagen2P10=decimaCaracteristica(imgc, col,fil)             
    imagen2P11=onceavaCaracteristica(imgc, col,fil)             
    imagen2P12=doceavaCaracteristica(imgc, col,fil)             
    imagen2P13=treceavaCaracteristica(imgc, col,fil)            
    imagen2P14=catorceavaCaracteristica(imgc, col,fil)             
    for val in range(2369):
        
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
        
        dist = math.sqrt(((p1-imagen2P1)**2)+((p2-imagen2P2)**2)+((p3-imagen2P3)**2)+((p4-imagen2P4)**2)+((p5-imagen2P5)**2)+((p6-imagen2P6)**2)+((p7-imagen2P7)**2)+((p8-imagen2P8)**2)+((p9-imagen2P9)**2)+((p10-imagen2P10)**2)+((p11-imagen2P11)**2)+((p12-imagen2P12)**2)+((p13-imagen2P13)**2)+((p14-imagen2P14)**2))
        
        knn[val][0] = val+1
        knn[val][1] = dist
        
        knn[val][2] = mat[val+1][14]
    
    res=[]
    
    for x in range(numVeci):
        
        res.append([0.0]*3)
    
    
    elementos = knn
    
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
    
    return res




nomImg = input('¿Qué imagen deseas buscar? ')
numVeci = int(input('Ingresa el número de vecinos: '))
nomImg = nomImg+".png"
mat = kNN(nomImg, numVeci)



print("________________________________________________________________________")
print("              Información general del Dataset cargado")
print("________________________________________________________________________")
print("Numero de instancias en el dataSet: 2369")
print("Numero de Caracteristicas: 14")
print("Numero de clases: 10")
print("Clases: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9")
print("________________________________________________________________________")
print("                               KNN")



print("Vecino: \t"+"Posición dataSet: \t"+"Clase: \t"+"Distancia:\t")
print("________________________________________________________________________")
for va in range(numVeci):
    print("   "+str(va+1)+"\t"+"        "+str(mat[va][0])+" \t  "+str(mat[va][2])+"\t"+"%.10f"%mat[va][1])
    
    if(mat[va][2]=='0'):
        contadorCero = contadorCero+1
    elif(mat[va][2]=='1'):
        contadorUno = contadorUno+1
    elif(mat[va][2]=='2'):
        contadorDos = contadorDos+1
    elif(mat[va][2]=='3'):
        contadorTres = contadorTres+1
    elif(mat[va][2]=='4'):
        contadorCuatro = contadorCuatro+1
    elif(mat[va][2]=='5'):
        contadorCinco = contadorCinco+1
    elif(mat[va][2]=='6'):
        contadorSeis = contadorSeis+1
    elif(mat[va][2]=='7'):
        contadorSiete = contadorSiete+1
    elif(mat[va][2]=='8'):
        contadorOcho = contadorOcho+1 
    elif(mat[va][2]=='9'):
        contadorNueve = contadorNueve+1        
print("________________________________________________________________________")
print("               Informe final sobre vecinos de KNN ")



print("Instancias "+"Clase "+"Vecinos encontrados")
print("________________________________________________________________________")
print("   237"+"   "+"    0"+"          "+str(contadorCero))
print("   237"+"   "+"    0"+"          "+str(contadorUno))
print("   237"+"   "+"    0"+"          "+str(contadorDos))
print("   237"+"   "+"    0"+"          "+str(contadorTres))
print("   237"+"   "+"    0"+"          "+str(contadorCuatro))
print("   237"+"   "+"    0"+"          "+str(contadorCinco))
print("   237"+"   "+"    0"+"          "+str(contadorSeis))
print("   237"+"   "+"    0"+"          "+str(contadorSiete))
print("   237"+"   "+"    0"+"          "+str(contadorOcho))
print("   237"+"   "+"    0"+"          "+str(contadorNueve))
print("")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print('              La Imagen pertenece a la clase ',mat[0][2])
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

