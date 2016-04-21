
import matplotlib.image as mpimg
import os
import csv





def Area (img):
    [filas,columnas]=img.shape 
    area=filas*columnas
    return area




def Relacion(img):
    [numero_filas,numero_columnas]=img.shape
    razon=numero_filas/numero_columnas
    return razon




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
    
    




def lineaHorizontal(filas,columnas,img):
    mitad=filas/2
    mitad=int(mitad)
    cortado=0
    puntos1=0
    for i in range(0,columnas):
    
        if img[mitad,i]==1:
            puntos1+=1
        if img[mitad,i]!=img[mitad,i-1]:
            cortado+=1
    
   
   
    return cortado,puntos1
    




def lineaVertical(filas,columnas,img):
    
    mitad=0
    cortado=0
    mitad=columnas/2
    mitad=int(mitad)
    puntos1=0
    for i in range(0,filas):
    
        if img[i,mitad]==1:
            puntos1+=1
        if img[i,mitad]!=img[i-1,mitad]:
            cortado+=1
    
    
    return cortado,puntos1
    




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





def BuscarArchivos(ruta): 
    path =ruta
    
    lstFiles = []
 
     
    lstDir = os.walk(path)   

    for root, dirs, files in lstDir:
        for fichero in files:
            (nombreFichero, extension) = os.path.splitext(fichero)
            if(extension == ".png"):
                lstFiles.append(nombreFichero+extension)
                        
    
    
    
                        
    return lstFiles





def lineasVerticalesyHorizontales2(img):
    
    [filas,columnas]=img.shape   
    mitadfila=filas/2 
    mitadcolumna=columnas/2
    mitadfila=int(mitadfila) 
    mitadcolumna=int(mitadcolumna) 

    aux1=mitadfila+(filas/10)
    aux2=mitadfila-(filas/10)
    aux3=mitadcolumna+(columnas/10)
    aux4=mitadcolumna-(columnas/10)
    blancos1=0 
    blancos2=0 
    cortado1=0 
    cortado2=0 
    
     
    for i in range(0,columnas):
        
        if img[aux1,i]==1:
            blancos1+=1
        if img[aux2,i]==1:
            blancos1+=1
        
        if img[aux1,i]!=img[aux1,i-1]:
            cortado1+=1
        if img[aux2,i]!=img[aux2,i-1]:
            cortado1+=1
    
    for i in range (0,filas):
         
        if img[i,aux3]!=img[i-1,aux3]:
            cortado2+=1
        if img[i,aux4]!=img[i-1,aux4]:
            cortado2+=1
        
        if img[i,aux3]==1:
            blancos2+=1
        if img[i,aux4]==1:
            blancos2+=1
    return blancos1,blancos2,cortado1,cortado2
        



def main(opc):
    
    if opc=="si":
        ruta='numeros/'
        archivo= open('dataset.csv', 'w', newline='')
        salida = csv.writer(archivo)
        contador=1
        for i in range(0,10):
            print("Obteniendo caracteristicas de... "+str(i))
            ruta=ruta+str(i) 
            ls=BuscarArchivos(ruta) 
            
            for j in range(0,len(ls)):
                rutaimagen=ruta+'/'+ls[j] 
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
                dato9=x1+x2 
                dato10=x3+x4
                dato11=negro1
                dato12=negro2
                dato13=(dato3+dato4)/fila 
                [dato14,dato15]=pixelesNegrosYBlancos(fila,columna,img)
                salida.writerow([dato1,dato2,dato3,dato4,dato5,dato6,dato7,dato8,dato9,dato10,dato11,dato12,dato13,dato14,dato15,i,contador])
                
                contador+=1
            ruta='numeros/'
        print("termino de crear las caracteristicas")   
        archivo.close()

print("¿Desea crear un nuevo dataset?")
opcion=input()

main(opcion)

    
import csv
import math
import OCR
import matplotlib.image as mpimg
f= open('dataset.csv')
lns=csv.reader(f)
print("Por favor ingrse el nombre del archivo que se va a leer: ",end="")
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
dato9=x1+x2 
dato10=x3+x4
dato11=negro1
dato12=negro2
dato13=(dato3+dato4)/fila 
[dato14,dato15]=OCR.pixelesNegrosYBlancos(fila,columna,img)


prediccion=[dato1,dato2,dato3,dato4,dato5,dato6,dato7,dato8,dato9,dato10,dato11,dato12,dato13,dato14,dato15] 
contador=0



for i in Matrix:
    aux=0
    aux=(pow((Matrix[contador][0]-dato1),2))+ (pow((Matrix[contador][1]-dato2),2))+ (pow((Matrix[contador][2]-dato3),2))+ (pow((Matrix[contador][3]-dato4),2))+(pow((Matrix[contador][4]-dato5),2)) +(pow((Matrix[contador][5]-dato6),2))
    aux=aux+(pow((Matrix[contador][6]-dato7),2))+ (pow((Matrix[contador][7]-dato8),2))+ (pow((Matrix[contador][8]-dato9),2))+ (pow((Matrix[contador][9]-dato10),2))+(pow((Matrix[contador][10]-dato11),2)) +(pow((Matrix[contador][11]-dato12),2))
    aux=aux+(pow((Matrix[contador][12]-dato13),2))+ (pow((Matrix[contador][13]-dato14),2))+ (pow((Matrix[contador][14]-dato15),2))     
    aux=math.sqrt(aux)
    Matrix[contador].append(aux)
    contador+=1
print(Matrix[0])
Matrix.sort(key=lambda Matrix: Matrix[17])


print("Por favor ingrese el numero de K vecinos a tomar en cuenta: ",end="")
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

print("\t\tInformación sobre el dataset ************************\n\n")
print("Numero de instancias: "+str(len(Matrix)))
print("Numero de clases: 10")
print("Nombre de las clases: 0,1,2,3,4,5,6,7,8,9 ")
print("Número de propiedades por instancia: "+str(len(dataset[0])-2))
print(len(Matrix))
print("\t\t Resultados de la clasificacion*************\n")
for i in range(0,k):
    print("\n")
    print("Vecino #"+str(i+1))
    print ("Numero de instancia: "+str(Matrix[i][16])+"\tDistancia euclidiana: "+str(Matrix[i][17])+"\tClase a la que pertenece: "+str(Matrix[i][15]))
print("\n")    


for i in range  (k):
    
    
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

totales=[[contador0,"El numero es un 0"],[contador1,"El numero es un 1"],[contador2,"El numero es un 2"],[contador3,"El numero es un 3"],[contador4,"El numero es un 4"],[contador5,"El numero es un 5"],[contador6,"El numero es un 6"],[contador7,"El numero es un 7"],[contador8,"El numero es un 8"],[contador9,"El numero es un 9"],]

print("****************************************************************\n")
for i in range(0,len(totales)):
    print("Se encontraron "+str(totales[i][0])+" resigistros de la clase "+str(i))
totales.sort(key=lambda totales: totales[0])
print("\n\n\t*****Resultado*****\n\n")
print (totales[9][1])

