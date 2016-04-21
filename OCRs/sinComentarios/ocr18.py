
 
import temp
import knn

opcion=0

while(opcion!=3):
    print("Selecciona una opcion ")
    opcion=int(input ("\t1.-Generar Dataset\n\t2.-Clasificar Imagen\n\t3.-Salir\n"))

    if(opcion<1 or opcion>3):
        print("Error")
    if (opcion==1):
        temp.creardataset()
    if (opcion==2):
        knn.instancias_de_la_clase()
        
print("Adios")


import matplotlib.image as mpimg
import os
import csv






def Area(img):
    [columnas,filas]=img.shape
    area=filas*columnas
    return area
    




def Tamaño(img):
    [columnas,filas]=img.shape
    tamaño=filas/columnas
    return tamaño





def Linea1Horizontal(img):
    [columnas,filas]=img.shape
    columnas=columnas/2
    columnas=columnas/2
    columnas=int(columnas)
    cortador=0
    contadorblanco=0
    for i in range (filas):
        
        
        if img[columnas,i]!= img[columnas,i-1]:
            cortador+=1
        if img[columnas,i] == 1:
            contadorblanco+=1
    
    contadorblanco=(columnas/filas)/contadorblanco
    return cortador, contadorblanco






def Linea2Horizontal(img):
    [columnas,filas]=img.shape
    columnas=columnas/2
    columnas=int(columnas)
    cortador=0
    contadorblanco=0
    for i in range (filas):
        
        
        if img[columnas,i]!= img[columnas,i-1]:
            cortador+=1
        if img[columnas,i] == 1:
            contadorblanco+=1
   
    contadorblanco=(columnas/filas)/contadorblanco
    return cortador, contadorblanco






def Linea3Horizontal(img):
    [columnas,filas]=img.shape
    columnas=columnas/2
    columnas=columnas/2
    columnas=columnas*3
    columnas=int(columnas)
    cortador=0
    contadorblanco=0
    for i in range (filas):
        
        
        if img[columnas,i]!= img[columnas,i-1]:
            cortador+=1
        if img[columnas,i] == 1:
            contadorblanco+=1
    
    contadorblanco=(columnas/filas)/contadorblanco
    return cortador,contadorblanco





def Linea1Vertical(img):
    [columnas,filas]=img.shape
    filas=filas/2
    filas=filas/2
    filas=int(filas)
    cortador=0
    contadorblanco=0
    for i in range (columnas):
        
        
        if img[i,filas]!= img[i-1,filas]:
            cortador+=1
        if img[i,filas] == 1:
            contadorblanco+=1
    
    contadorblanco=(columnas/filas)/contadorblanco
    return cortador, contadorblanco
    





def Linea2Vertical(img):
    [columnas,filas]=img.shape
    filas=filas/2
    filas=int(filas)
    cortador=0
    contadorblanco=0
    for i in range (columnas):
        
        
        if img[i,filas]!= img[i-1,filas]:
            cortador+=1
        if img[i,filas] == 1:
            contadorblanco+=1
    
    contadorblanco=(columnas/filas)/contadorblanco
    return cortador, contadorblanco





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

    




def Linea3Vertical(img):
    [columnas,filas]=img.shape
    filas=filas/2
    filas=filas/2
    filas=filas*3
    filas=int(filas)
    cortador=0
    contadorblanco=0
    for i in range (columnas):
        
        
        if img[i,filas]!= img[i-1,filas]:
            cortador+=1 
        if img[i,filas] == 1:
            contadorblanco+=1
   
    contadorblanco=(columnas/filas)/contadorblanco
    return cortador,contadorblanco






def creardataset():
    ruta='prueba/'
    archivo= open('resultado.csv', 'w', newline='')
    salida = csv.writer(archivo)
    numero=0
    for i in range(10):
        print("trabajando data set caracteristica del: "+str(i))
        ruta=ruta+str(i)
        ls=BuscarArchivos(ruta)
        
        
        for j in range(0,len(ls)):
            numero+=1
            rutaimagen=ruta+'/'+ls[j]
            img=mpimg.imread(rutaimagen)
            caracteristica1=Linea1Horizontal(img)
            caracteristica2=Linea2Horizontal(img)
            caracteristica3=Linea3Horizontal(img)
            caracteristica4=Linea1Vertical(img)
            caracteristica5=Linea2Vertical(img)
            caracteristica6=Linea3Vertical(img)
            caracteristica7=Area(img)
            caracteristica8=Tamaño(img)
            
            salida.writerow([caracteristica1[0],caracteristica1[1],caracteristica2[0],caracteristica2[1],caracteristica3[0],caracteristica3[1],caracteristica4[0],caracteristica4[1],caracteristica5[0],caracteristica5[1],caracteristica6[0],caracteristica6[1],caracteristica7,caracteristica8,numero,i])
        ruta='prueba/'
    
    archivo.close()
    return salida 


 
  
   
    
    
    
import csv
import math
import temp
import matplotlib.image as mpimg
    




def clasificacion():
    contador=0
    print("Nombre de la imagen: ")
    nombre_imagen=(input())
    img=mpimg.imread(nombre_imagen)
    dato1=temp.Linea1Horizontal(img)
    dato2=temp.Linea2Horizontal(img)
    dato3=temp.Linea3Horizontal(img)
    dato4=temp.Linea1Vertical(img)
    dato5=temp.Linea2Vertical(img)
    dato6=temp.Linea3Vertical(img)
    dato7=temp.Area(img)
    dato8=temp.Tamaño(img)

    abrir= open('resultado.csv')
    lectura_de_dataset=csv.reader(abrir)
    dataset=list(lectura_de_dataset)
    print("Numero de vecinos a considerar: ",end="")
    numero_vecinos=int(input())
    
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
        dataset[contador][14]=int(dataset[contador][14])
        dataset[contador][15]=int(dataset[contador][15])
        
        contador+=1
        
        Matrix=dataset
        
        prediccion=[dato1[0],dato1[1],dato2[0],dato2[1],dato3[0],dato3[1],dato4[0],dato4[1],dato5[0],dato5[1],dato6[0],dato6[1],dato7,dato8]
    contador=0
    
    
    
    for i in Matrix:
            aux=0
            aux=(pow((Matrix[contador][0]-dato1[0]),2))+ (pow((Matrix[contador][1]-dato1[1]),2))+ (pow((Matrix[contador][2]-dato2[0]),2))+ (pow((Matrix[contador][3]-dato2[1]),2))+(pow((Matrix[contador][4]-dato3[0]),2)) +(pow((Matrix[contador][5]-dato3[1]),2))
            aux=aux+(pow((Matrix[contador][6]-dato4[0]),2))+ (pow((Matrix[contador][7]-dato4[1]),2))+ (pow((Matrix[contador][8]-dato5[0]),2))+ (pow((Matrix[contador][9]-dato5[1]),2))+(pow((Matrix[contador][10]-dato6[0]),2)) +(pow((Matrix[contador][11]-dato6[1]),2))
            aux=aux+(pow((Matrix[contador][12]-dato7),2))+ (pow((Matrix[contador][13]-dato8),2))
            aux=math.sqrt(aux)
            dataset[contador].append(aux)
            contador+=1
            
            
    Matrix.sort(key=lambda Matrix: Matrix[14],reverse=True)
    print ("\t\tDataset info:\nNúmero total de instancias:", Matrix[0][14])
    Matrix.sort(key=lambda Matrix: Matrix[16])
    print("Instancia del K vecino mas cercano:", Matrix[0][14])
    print ("\nk vecinos mas cercanos:")
    for K_vecinos in range (0,numero_vecinos):
        print ("\tInstancia:", Matrix[K_vecinos][14], "\tDistancia:",
               "%.5f" %Matrix[K_vecinos][16], "\tClase", Matrix[K_vecinos][15])
           
    return prediccion, Matrix, numero_vecinos
def instancias_de_la_clase():
    prediccion,Matrix,numero_vecinos=clasificacion()
    k=numero_vecinos
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
    
    numero_filas=10
    numero_columnas=2
    clase_final = []
    for filas in range(numero_filas):
        clase_final.append([])
        for columnas in range(numero_columnas):
            clase_final[filas].append(None)
            
    for caracateristica in range(k):
    
            
            if Matrix[caracateristica][15]==1:
                contador1+=1
            if Matrix[caracateristica][15]==2:
                contador2+=1
            if Matrix[caracateristica][15]==3:
                contador3+=1
            if Matrix[caracateristica][15]==4:
                contador4+=1
            if Matrix[caracateristica][15]==5:
                contador5+=1
            if Matrix[caracateristica][15]==6:
                contador6+=1
            if Matrix[caracateristica][15]==7:
                contador7+=1
            if Matrix[caracateristica][15]==8:
                contador8+=1
            if Matrix[caracateristica][15]==9:
                contador9+=1
            if Matrix[caracateristica][15]==0:
                contador0+=1
                
    clase_final[0]=contador0,0
    clase_final[1]=contador1,1
    clase_final[2]=contador2,2
    clase_final[3]=contador3,3
    clase_final[4]=contador4,4
    clase_final[5]=contador5,5
    clase_final[6]=contador6,6
    clase_final[7]=contador7,7
    clase_final[8]=contador8,8
    clase_final[9]=contador9,9
    
    clase_final.sort(key=None, reverse=True)
    print ("\nNúmero de Instancias por clase:")
    for conteo_instancias in range(0,10):
            print ("\t",clase_final[conteo_instancias][0],
            "\tInstancias de la clase:",clase_final[conteo_instancias][1]) 
    print ("\nLa imagen es el numero:", clase_final[0][1]) 

    
