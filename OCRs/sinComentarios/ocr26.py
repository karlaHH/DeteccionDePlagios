import KNN 
import generarDataSet 
import os 
print ("Inserte un número:")
opcion=int(input ("1.-Generar Dataset\n2.-Clasificar Imagen\n3.-Salir\n"))
os.system("cls")
if(opcion<1 or opcion>3):
    print("Error")
if (opcion==1):
    generarDataSet.DataSet()
if (opcion==2):
    KNN.instancias()
if(opcion==3):
    os.system("cls")

    
import matplotlib.pyplot as plt
import matplotlib.image as mpimg 
import os 

def datos():
    print("Inserte el nombre de la imagen: ")
    nombre_imagen=(input())
    os.system("cls")
    img=mpimg.imread(nombre_imagen)
    imgplot=plt.imshow(img)
    mat=img
    tam=img.shape
    return img,tam,mat,imgplot 

def RazonFilascolumnas(tam):
    razonFilasEntreColumnas=tam[0]/tam[1]
    return razonFilasEntreColumnas
      
def RazonPixelesBlancos(tam,mat):
    contarPixelesBlancos=0
    for i in range(0,tam[0]):
       for j in range(0,tam[1]):
           if(mat[i][j]!=0):
              contarPixelesBlancos=contarPixelesBlancos+1
    return contarPixelesBlancos
    
def CambiosPrimeraLineaHorizontal(tam,img):
    posicionPrimeraLineaHorizontal=int(tam[0]/4)
    contarCambiosPrimeraLineaHorizontal=0
    aux=img[posicionPrimeraLineaHorizontal][0]
    for i in range(0,tam[1]):
        if(aux!=img[posicionPrimeraLineaHorizontal][i]):
            aux=img[posicionPrimeraLineaHorizontal][i]
            contarCambiosPrimeraLineaHorizontal=contarCambiosPrimeraLineaHorizontal+1
        
    return contarCambiosPrimeraLineaHorizontal
    
def CambiosSegundaLineaHorizontal(tam,img):
    posicionSegundaLineaHorizontal=int(tam[0]/2)
    contarCambiosSegundaLineaHorizontal=0
    aux=img[posicionSegundaLineaHorizontal][0]
    for i in range(0,tam[1]):
        if(aux!=img[posicionSegundaLineaHorizontal][i]):
            aux=img[posicionSegundaLineaHorizontal][i]
            contarCambiosSegundaLineaHorizontal=contarCambiosSegundaLineaHorizontal+1
        
    return contarCambiosSegundaLineaHorizontal
    
def CambiosTerceraLineaHorizontal(tam,img):
    posicionTerceraLineaHorizontal=int((tam[0]/4)*3)
    contarCambiosTerceraLineaHorizontal=0
    aux=img[posicionTerceraLineaHorizontal][0]
    for i in range(0,tam[1]):
        if(aux!=img[posicionTerceraLineaHorizontal][i]):
            aux=img[posicionTerceraLineaHorizontal][i]
            contarCambiosTerceraLineaHorizontal=contarCambiosTerceraLineaHorizontal+1
        
    return contarCambiosTerceraLineaHorizontal
    
def CambioPrimeraLineaVertical(tam,img):
    posicionPrimeraLineaVerticalal=int(tam[1]/4)
    contarCambiosPrimeraLineaVertical=0
    aux=img[0][posicionPrimeraLineaVerticalal]
    for i in range(0,tam[0]):
        if(aux!=img[i][posicionPrimeraLineaVerticalal]):
            aux=img[i][posicionPrimeraLineaVerticalal]
            contarCambiosPrimeraLineaVertical=contarCambiosPrimeraLineaVertical+1
        
    return contarCambiosPrimeraLineaVertical
    
def CambioSegundaLineaVertical(tam,img):
    posicionSegundaLineaVertical=int(tam[1]/2)
    contarCambiosSegundaLineaVertical=0
    aux=img[0][posicionSegundaLineaVertical]
    for i in range(0,tam[0]):
        if(aux!=img[i][posicionSegundaLineaVertical]):
            aux=img[i][posicionSegundaLineaVertical]
            contarCambiosSegundaLineaVertical=contarCambiosSegundaLineaVertical+1
        
    return contarCambiosSegundaLineaVertical
      
def CambioTerceraLineaVertical(tam,img):
    posicionTerceraLineaVertical=int((tam[1]/4)*3)
    contarCambiosTerceraLineaVertical=0
    aux=img[0][posicionTerceraLineaVertical]
    for i in range(0,tam[0]):
        if(aux!=img[i][posicionTerceraLineaVertical]):
            aux=img[i][posicionTerceraLineaVertical]
            contarCambiosTerceraLineaVertical=contarCambiosTerceraLineaVertical+1
        
    return contarCambiosTerceraLineaVertical
    
def ContarPixelesPrimeraLineaHorizontal(tam,img):
    posicionprimeraLineaHorizontal = int(tam[0]/4)
    contarPixelesPrimeraLineaHorizontal=0
    for i in range(0,tam[1]):
        if(img[posicionprimeraLineaHorizontal][i]!=0):
            contarPixelesPrimeraLineaHorizontal=contarPixelesPrimeraLineaHorizontal+1
        
    return contarPixelesPrimeraLineaHorizontal
    
def ContarPixelesSegundaLineaHorizontal(tam,img):
    posicionsegundaLineaHorizontal=int(tam[0]/2)
    contarPixelesSegundaLineaHorizontal=0
    for i in range(0,tam[1]):
        if(img[posicionsegundaLineaHorizontal][i]!=0):
            contarPixelesSegundaLineaHorizontal=contarPixelesSegundaLineaHorizontal+1
        
    return contarPixelesSegundaLineaHorizontal
    
def ContarPixelesTerceraLineaHorizontal(tam,img):
    posicionterceraLineaHorizontal=int((tam[0]/4)*3)
    contarPixelesTerceraLineaHorizontal=0
    for i in range(0,tam[1]):
        if(img[posicionterceraLineaHorizontal][i]!=0):
            contarPixelesTerceraLineaHorizontal=contarPixelesTerceraLineaHorizontal+1
        
    return contarPixelesTerceraLineaHorizontal
    
def ContarPixelesPrimeraLineaVertical(tam,img):
    posicionprimeraLineaVertical=int(tam[1]/4)
    contarPixelesPrimeraLineaVertical=0
    for i in range(0,tam[0]):
        if(img[i][posicionprimeraLineaVertical]!=0):
            contarPixelesPrimeraLineaVertical=contarPixelesPrimeraLineaVertical+1
        
    return contarPixelesPrimeraLineaVertical
    
def ContarPixelesSegundaLineaVertical(tam,img):
    posicionsegundaLineaVertical=int(tam[1]/2)
    contarPixelesSegundaLineaVertical=0
    for i in range(0,tam[0]):
        if(img[i][posicionsegundaLineaVertical]!=0):
            contarPixelesSegundaLineaVertical=contarPixelesSegundaLineaVertical+1
        
    return contarPixelesSegundaLineaVertical
    
def ContarPixelesTerceraLineaVertical(tam,img):
    posicionterceraLineaVertical=int((tam[1]/4)*3)
    contarPixelesTerceraLineaVertical=0
    for i in range(0,tam[0]):
        if(img[i][posicionterceraLineaVertical]!=0):
            contarPixelesTerceraLineaVertical=contarPixelesTerceraLineaVertical+1
        
    return contarPixelesTerceraLineaVertical


import matplotlib.image as mpimg 
import os 
import csv 
import Caracteristicas 
def DataSet():
    root="arialSegmented"
    archivo= open ("DataSet.csv", "w",newline='')
    salida=csv.writer(archivo)
    clase=-1
    posiciones_dataset=0
    for dirName, subdirlist, filelist in os.walk(root):
        for fname in filelist:
            posiciones_dataset=posiciones_dataset+1
            nameima=dirName+'/'+fname 
            print("Generando DataSet....")
            img=mpimg.imread(nameima)
            mat=img
            tam=mat.shape
            
            razonFilasEntreColumnas=Caracteristicas.RazonFilascolumnas(tam)
            contarPixelesBlancos=Caracteristicas.RazonPixelesBlancos(tam,mat)
            contarCambiosPrimeraLineaHorizontal=Caracteristicas.CambiosPrimeraLineaHorizontal(tam,img)
            contarCambiosSegundaLineaHorizontal=Caracteristicas.CambiosSegundaLineaHorizontal(tam,img)
            contarCambiosTerceraLineaHorizontal=Caracteristicas.CambiosTerceraLineaHorizontal(tam,img)
            contarCambiosPrimeraLineaVertical=Caracteristicas.CambioPrimeraLineaVertical(tam,img)
            contarCambiosSegundaLineaVertical=Caracteristicas.CambioSegundaLineaVertical(tam,img)
            contarCambiosTerceraLineaVertical=Caracteristicas.CambioTerceraLineaVertical(tam,img)
            contarPixelesPrimeraLineaHorizontal=Caracteristicas.ContarPixelesPrimeraLineaHorizontal(tam,img)
            contarPixelesSegundaLineaHorizontal=Caracteristicas.ContarPixelesSegundaLineaHorizontal(tam,img)
            contarPixelesTerceraLineaHorizontal=Caracteristicas.ContarPixelesTerceraLineaHorizontal(tam,img)
            contarPixelesPrimeraLineaVertical=Caracteristicas.ContarPixelesPrimeraLineaVertical(tam,img)
            contarPixelesSegundaLineaVertical=Caracteristicas.ContarPixelesSegundaLineaVertical(tam,img)
            contarPixelesTerceraLineaVertical=Caracteristicas.ContarPixelesTerceraLineaVertical(tam,img)
            
            salida.writerow([razonFilasEntreColumnas,contarPixelesBlancos,contarCambiosPrimeraLineaHorizontal,contarCambiosSegundaLineaHorizontal,contarCambiosTerceraLineaHorizontal,contarCambiosPrimeraLineaVertical,contarCambiosSegundaLineaVertical,contarCambiosTerceraLineaVertical,contarPixelesPrimeraLineaHorizontal,contarPixelesSegundaLineaHorizontal,contarPixelesTerceraLineaHorizontal,contarPixelesPrimeraLineaVertical,contarPixelesSegundaLineaVertical,contarPixelesTerceraLineaVertical,posiciones_dataset,clase])
        clase=clase+1
        os.system("cls")
    print ("El DataSet esta listo....!!!!")
    archivo.close()

    
import csv
import math
import os
import Caracteristicas
def Clasificacion():
    img,tam,mat,imgplot=Caracteristicas.datos()
    razonFilasEntreColumnas=Caracteristicas.RazonFilascolumnas(tam)
    contarPixelesBlancos=Caracteristicas.RazonPixelesBlancos(tam,mat)
    contarCambiosPrimeraLineaHorizontal=Caracteristicas.CambiosPrimeraLineaHorizontal(tam,img)
    contarCambiosSegundaLineaHorizontal=Caracteristicas.CambiosSegundaLineaHorizontal(tam,img)
    contarCambiosTerceraLineaHorizontal=Caracteristicas.CambiosTerceraLineaHorizontal(tam,img)
    contarCambiosPrimeraLineaVertical=Caracteristicas.CambioPrimeraLineaVertical(tam,img)
    contarCambiosSegundaLineaVertical=Caracteristicas.CambioSegundaLineaVertical(tam,img)
    contarCambiosTerceraLineaVertical=Caracteristicas.CambioTerceraLineaVertical(tam,img)
    contarPixelesPrimeraLineaHorizontal=Caracteristicas.ContarPixelesPrimeraLineaHorizontal(tam,img)
    contarPixelesSegundaLineaHorizontal=Caracteristicas.ContarPixelesSegundaLineaHorizontal(tam,img)
    contarPixelesTerceraLineaHorizontal=Caracteristicas.ContarPixelesTerceraLineaHorizontal(tam,img)
    contarPixelesPrimeraLineaVertical=Caracteristicas.ContarPixelesPrimeraLineaVertical(tam,img)
    contarPixelesSegundaLineaVertical=Caracteristicas.ContarPixelesSegundaLineaVertical(tam,img)
    contarPixelesTerceraLineaVertical=Caracteristicas.ContarPixelesTerceraLineaVertical(tam,img)
    
    abrir= open('DataSet.csv')
    leer_dataset=csv.reader(abrir)
    dataset=list(leer_dataset)
    print("\n\nIngrese lo que se pide a continuación")
    print("\n\nNumero de vecinos a considerar: ",end="")
    numeroKVecinos=int(input())
    os.system("cls")
    contador=0
    for i in dataset:
        dataset[contador][0]=float(dataset[contador][0])
        dataset[contador][1]=int(dataset[contador][1])
        dataset[contador][2]=int(dataset[contador][2])
        dataset[contador][3]=int(dataset[contador][3])
        dataset[contador][4]=int(dataset[contador][4])
        dataset[contador][5]=int(dataset[contador][5])
        dataset[contador][6]=int(dataset[contador][6])
        dataset[contador][7]=int(dataset[contador][7])
        dataset[contador][8]=int(dataset[contador][8])
        dataset[contador][9]=int(dataset[contador][9])
        dataset[contador][10]=int(dataset[contador][10])
        dataset[contador][11]=int(dataset[contador][11])
        dataset[contador][12]=int(dataset[contador][12])
        dataset[contador][13]=int(dataset[contador][13])
        dataset[contador][14]=int(dataset[contador][14])
        dataset[contador][15]=int(dataset[contador][15])
        
        
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
        raiz=math.sqrt(distancia)
        dataset[contador].append(raiz)
        contador+=1
    dataset.sort(key=lambda dataset: dataset[14],reverse=True)
    print ("\tInformacón del DataSet")
    print ("No. Total de instancias: ", dataset [0][14])
    dataset.sort(key=lambda dataset: dataset[16])
    print("Instancia del K vecino mas cercano: ", dataset[0][14])
    print ("\nK vecinos mas cercanos:")
    for k_Vecinos_Cercanos in range (0,numeroKVecinos):
        print ("Instancia:", dataset[k_Vecinos_Cercanos][14], "\tDistancia:","%.4f" %dataset[k_Vecinos_Cercanos][16], "    Clase", dataset[k_Vecinos_Cercanos][15])
    return dataset, numeroKVecinos
    
def instancias():
    dataset,numeroKVecinos = Clasificacion()
    clase0=0
    clase1=0
    clase2=0
    clase3=0
    clase4=0
    clase5=0
    clase6=0
    clase7=0
    clase8=0
    clase9=0
    
    numero_filas=10
    numero_columnas=2
    clase_final = []
    for filas in range(numero_filas):
        clase_final.append([])
        for columnas in range(numero_columnas):
            clase_final[filas].append(None)
    
    for caracteristica in range(0,numeroKVecinos):
        if(dataset[caracteristica][15]==0):
            clase0=clase0+1
        if(dataset[caracteristica][15]==1):
            clase1=clase1+1
        if(dataset[caracteristica][15]==2):
            clase2=clase2+1
        if(dataset[caracteristica][15]==3):
            clase3=clase3+1
        if(dataset[caracteristica][15]==4):
            clase4=clase4+1
        if(dataset[caracteristica][15]==5):
            clase5=clase5+1
        if(dataset[caracteristica][15]==6):
            clase6=clase6+1
        if(dataset[caracteristica][15]==7):
            clase7=clase7+1
        if(dataset[caracteristica][15]==8):
            clase8=clase8+1
        if(dataset[caracteristica][15]==9):
            clase9=clase9+1
            
    clase_final[0]=clase0,0
    clase_final[1]=clase1,1
    clase_final[2]=clase2,2
    clase_final[3]=clase3,3
    clase_final[4]=clase4,4
    clase_final[5]=clase5,5
    clase_final[6]=clase6,6
    clase_final[7]=clase7,7
    clase_final[8]=clase8,8
    clase_final[9]=clase9,9
    
    clase_final.sort(key=None, reverse=True)
    print ("\nNúmero de Instancias por clase: ")
    for conteo_instancias in range(0,10):
            print ("",clase_final[conteo_instancias][0],
            "   Instancias de la clase:",clase_final[conteo_instancias][1]) 
    print ("\n\nLa imagen es un :", clase_final[0][1]) 
    
    
    
