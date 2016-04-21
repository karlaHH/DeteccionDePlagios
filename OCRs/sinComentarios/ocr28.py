





import os

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








def obtenerPropiedad1(img,alto,ancho):
    
    contadorDeUnos = 0
    
    for a in range(alto):
        for b in range(ancho):
            
            dato = (int(img[a][b]))
            
            if dato!=1:
                
                contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)








def obtenerPropiedad2(img,alto,ancho):
    
    
    prom = ancho/alto
    
    return prom









def obtenerPropiedad3(img,alto,ancho):
    
    filaIntermedia = int(ancho/2)
    
    contadorDeUnos = 0
    
    for al in range(alto):
        
        dato = (int(img[al][filaIntermedia]))
        
        if dato == 1:
            
            contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)
    







def obtenerPropiedad4(img,alto,ancho):
    
    filaUnCuarto= int(ancho/4)
    
    contadorDeUnos = 0
    
    for al in range(alto):
        
        dato = (int(img[al][filaUnCuarto]))
        
        if dato == 1:
            
           contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)








def obtenerPropiedad5(img,alto,ancho):
    
    filaTresCuartos = int((int(ancho/4))*3)
    
    contadorDeUnos = 0
    
    for al in range(alto):
        
        dato = (int(img[al][filaTresCuartos]))
        
        if dato == 1:
            
            contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)








def obtenerPropiedad6(img,alto,ancho):
    
    colItermedia = int(alto/2)
    
    contadorDeUnos = 0
    
    for fil in range(alto):
        
        for col in range(ancho):
            
            if fil == colItermedia:
                
                dato = (int(img[colItermedia][col]))
                
                if dato == 1:
                    
                    contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)








def obtenerPropiedad7(img,alto,ancho):
    
    columnaUnCuarto = int(alto/4)
    
    contadorDeUnos = 0
    
    for fil in range(alto):
        
        for col in range(ancho):
            
            if fil == columnaUnCuarto:
                
                dato = (int(img[columnaUnCuarto][col]))
                
                if dato == 1:
                    
                    contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)








def obtenerPropiedad8(img,alto,ancho):
    
    colTresCuartos = int((int(alto/4))*3)
    
    contadorDeUnos = 0
    
    for fil in range(alto):
        
        for col in range(ancho):
            
            if fil == colTresCuartos:
                
                dato = (int(img[fil][col]))
                
                if dato == 1:
                    
                    contadorDeUnos = contadorDeUnos+1
    
    return contadorDeUnos/(alto*ancho)








def obtenerPropiedad9(img,alto,ancho):
    
    columnaIntermedia = int(ancho/2)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for fil in range(alto):
        
        dato = (int(img[fil][columnaIntermedia]))
        
        if dato!=corte:
            
            contadorDeCortes = contadorDeCortes+1
            
    
    return contadorDeCortes/(alto*ancho)








def obtenerPropiedad10(img,alto,ancho):
    
    filaUnCuarto = int(ancho/4)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for fil in range(alto):
        
        dato = (int(img[fil][filaUnCuarto]))
        
        if dato!=corte:
            
            contadorDeCortes = contadorDeCortes+1
            
    
    return contadorDeCortes/(alto*ancho)








def obtenerPropiedad11(img,alto,ancho):
    
    col = int((int(ancho/4))*3)
    
    contadorDeCortes = 0
    
    corte = 0
    
    for al in range(alto):
        
        dato = (int(img[al][col]))
        
        if dato!=corte:
            
            contadorDeCortes = contadorDeCortes+1
            
    
    return contadorDeCortes/(alto*ancho)








def obtenerPropiedad12(img,alto,ancho):
    
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








def obtenerPropiedad13(img,alto,ancho):
    
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








def obtenerPropiedad14(img,alto,ancho):
    
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
    
    
    i2P1 = obtenerPropiedad1(imgc,col,fil)
    
    
    i2P2=obtenerPropiedad2(imgc, col,fil)               
    
    
    i2P3=obtenerPropiedad3(imgc, col,fil)               
    
    
    i2P4=obtenerPropiedad4(imgc, col,fil)               
    
    
    i2P5=obtenerPropiedad5(imgc, col,fil)               
    
    
    i2P6=obtenerPropiedad6(imgc, col,fil)               
    
    
    i2P7=obtenerPropiedad7(imgc, col,fil)               
    
    
    i2P8=obtenerPropiedad8(imgc, col,fil)              
    
    
    i2P9=obtenerPropiedad9(imgc, col,fil)               
    
    
    i2P10=obtenerPropiedad10(imgc, col,fil)             
    
    
    i2P11=obtenerPropiedad11(imgc, col,fil)             
    
    
    i2P12=obtenerPropiedad12(imgc, col,fil)             
    
    
    i2P13=obtenerPropiedad13(imgc, col,fil)            
    
    
    i2P14=obtenerPropiedad14(imgc, col,fil)             
    
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
        
        dist = math.sqrt(((p1-i2P1)**2)+((p2-i2P2)**2)+((p3-i2P3)**2)+((p4-i2P4)**2)+((p5-i2P5)**2)+((p6-i2P6)**2)+((p7-i2P7)**2)+((p8-i2P8)**2)+((p9-i2P9)**2)+((p10-i2P10)**2)+((p11-i2P11)**2)+((p12-i2P12)**2)+((p13-i2P13)**2)+((p14-i2P14)**2))
        
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




rootDir = 'dataSet'

name=''


for directorio, subDir, listaArchivos in os.walk(rootDir):
    
    
    
    for archivo in listaArchivos:
        
        rutaArchivo = directorio+"/"+archivo
        
        imgCF = Image.open(rutaArchivo)
        
        img = mpimg.imread(rutaArchivo)
        
        
        (ancho,alto) = imgCF.size
        
        
        matriz[x][y] = obtenerPropiedad1(img,alto,ancho)
        
        y = y+1
        
        
        matriz[x][y] = obtenerPropiedad2(img,alto,ancho)
        
        y = y+1
        
        
        matriz[x][y] = obtenerPropiedad3(img,alto,ancho)
        
        y = y+1
        
        
        matriz[x][y] = obtenerPropiedad4(img,alto,ancho)
        
        y = y+1
        
        
        matriz[x][y] = obtenerPropiedad5(img,alto,ancho)
        
        y = y+1
        
        
        matriz[x][y] = obtenerPropiedad6(img,alto,ancho)
        
        y = y+1
        
        
        matriz[x][y] = obtenerPropiedad7(img,alto,ancho)
        
        y = y+1
        
        
        matriz[x][y] = obtenerPropiedad8(img,alto,ancho)
        
        y = y+1
        
        
        matriz[x][y] = obtenerPropiedad9(img,alto,ancho)
        
        y = y+1
        
        
        matriz[x][y] = obtenerPropiedad10(img,alto,ancho)
       
        y = y+1
        
        
        matriz[x][y] = obtenerPropiedad11(img,alto,ancho)
        
        y = y+1
        
        
        matriz[x][y] = obtenerPropiedad12(img,alto,ancho)
        
        y = y+1
        
        
        matriz[x][y] = obtenerPropiedad13(img,alto,ancho)
        
        y = y+1
        
        
        matriz[x][y] = obtenerPropiedad14(img,alto,ancho)
        
        y = y+1
        matriz[x][y] = contadorClase-1
        
        x = x+1
        
        y = 0
    contadorClase = contadorClase+1
    




datosMatriz = matriz

csvOut = open('dataSet.csv','w',newline='')

out = csv.writer(csvOut)

out.writerow(["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P11","P12",
              "P13","P14","Clase"])

out.writerows(datosMatriz)

del out

csvOut.close()




nomImg = input('Nombre de la imagen a buscar: ')

numVeci = int(input('Número de vecinos: '))

nomImg = nomImg+".png"

mat = kNN(nomImg, numVeci)




print("******************************************************************")

print("Numero de instancias en el dataSet: "+str(2369))

print("Numero de propiedades (Caracteristicas): "+str(14))

print("Numero de clases: "+str(10))

print("Clases; 0, 1, 2, 3, 4, 5, 6, 7, 8, 9")
print("******************************************************************")
print("")
print("******************************************************************")


print("Vecino: \t"+"Posición dataSet: \t"+"Clase: \t"+"Distancia:\t")

for va in range(numVeci):


    print(str(va+1)+"\t"+str(mat[va][0])+" \t\t"+str(mat[va][2])+
           "\t"+"%.10f"%mat[va][1])
    
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
print("******************************************************************")
print("")
print("******************************************************************")


print("Instancias:\t "+"Clase:\t"+"Vecinos encontrados: ")

print(str(237)+"\t "+"0"+"\t"+str(contadorCero))

print(str(237)+"\t "+"1"+"\t"+str(contadorUno))

print(str(236)+"\t "+"2"+"\t"+str(contadorDos))

print(str(237)+"\t "+"3"+"\t"+str(contadorTres))

print(str(237)+"\t "+"4"+"\t"+str(contadorCuatro))

print(str(237)+"\t "+"5"+"\t"+str(contadorCinco))

print(str(237)+"\t "+"6"+"\t"+str(contadorSeis))

print(str(237)+"\t "+"7"+"\t"+str(contadorSiete))

print(str(237)+"\t "+"8"+"\t"+str(contadorOcho))

print(str(237)+"\t "+"9"+"\t"+str(contadorNueve))
print("******************************************************************")
print("")
print("******************************************************************")

print('La Imagen es de clase: ',mat[0][2])
print("******************************************************************")

