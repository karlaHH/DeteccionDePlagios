
 
import KNN_funciones 
import Dataset 
import os 
print ("Qué deseas realizar:")
opcion=int(input ("\t1.-Generar Dataset\n\t2.-Clasificar Imagen\n\t3.-Salir\n"))
os.system("cls")
opcion_dos=0
while(opcion!=3):
    if(opcion<1 or opcion>3):
        print("Error")
    if (opcion==1):
        Dataset.dataset()
    if (opcion==2):
        KNN_funciones.instancias()
    input("\n\nPulsa una tecla para continuar...")
    os.system("cls")
    opcion_dos=int(input("Deseas Realizar algo mas?\n\t1.-SI\n\t2.-Salir\n"))
    os.system("cls")
    if (opcion_dos==1):
        print ("Qué deseas realizar:")
        opcion=int(input ("\t1.-Generar Dataset\n\t2.-Clasificar Imagen\n\t3.-Salir\n"))
        os.system("cls")
    else:
        opcion=3
if(opcion==3):
    os.system("cls")
    print("Adios")



 
import matplotlib.image as mpimg
import os
 
def datos_imagen():
    print("Nombre de la imagen: ")
    nombre_imagen=(input())
    os.system("cls")
    img=mpimg.imread(nombre_imagen)
    
    
    return img
     
def lectura():
    img=datos_imagen()
    imgplot=img
    imagen=imgplot.shape
    limx= imagen[1]
    limy= imagen[0]
    div_x=int(limx/2)
    div_y=int(limy/2)
    return limx,limy, imgplot, div_x,div_y
     
def primera_segunda_carac(limx, limy,imgplot):
    relacion_1=limy/limx
    fila=0
    columna=0
    relacion_2=0
    aux=0
    for fila in range (0, limy):
        for columna in range (0,limx):
            if (imgplot[fila,columna]==1):
                aux=aux+1
    relacion_2=(limx*limy)/aux
    return relacion_1, relacion_2
     
def tecera_cuarta_carac(limx,limy,imgplot,div_x,div_y):
    fila=0
    vertical_cambios=0
    vertical_numero=0
    aux=imgplot[fila,div_x]
    for fila in range (0, limy):
        if (imgplot[fila, div_x]!=aux):
            vertical_cambios=vertical_cambios+1
            aux=imgplot[fila,div_x]
        if (imgplot[fila, div_x]==1):
            vertical_numero=vertical_numero+1
    return vertical_cambios,vertical_numero

     
def quinta_sexta_carac(limx,limy,imgplot,div_x,div_y):
    columna=0
    horizontal_cambios=0
    horizontal_numero=0
    aux=imgplot[div_y,columna]
    for columna in range (0, limx):
        if (imgplot[div_y, columna]!=aux):
            horizontal_cambios=horizontal_cambios+1
            aux=imgplot[div_y,columna] 
        if (imgplot[div_y, columna]==1):
            horizontal_numero=horizontal_numero+1
    return horizontal_cambios, horizontal_numero
         
def septima_octava_carac(limx,limy,imgplot,div_x,div_y):
    fila=0
    vertical_cambios_izquierda=0
    vertical_cambios_numeros_izquierda=0
    division=int(limx/4)
    aux=imgplot[fila,division]
    for fila in range (0, limy):
        if (imgplot[fila, division]!=aux):
            vertical_cambios_izquierda=vertical_cambios_izquierda+1
            aux=imgplot[fila,division]
        if (imgplot[fila, division]==1):
            vertical_cambios_numeros_izquierda=vertical_cambios_numeros_izquierda+1
    return vertical_cambios_izquierda,vertical_cambios_numeros_izquierda
        
def novena_decima_carac(limx,limy,imgplot,div_x,div_y):
    fila=0
    vertical_cambios_derecha=0
    vertical_cambios_numeros_derecha=0
    division=int (limx/4)
    division=limx-division
    aux=imgplot[fila,division]
    for fila in range (0, limy):
        if (imgplot[fila, division]!=aux):
            vertical_cambios_derecha=vertical_cambios_derecha+1
            aux=imgplot[fila,division]
        if (imgplot[fila, division]==1):
            vertical_cambios_numeros_derecha=vertical_cambios_numeros_derecha+1  
    return vertical_cambios_derecha,vertical_cambios_numeros_derecha
      
def once_doce_carac(limx,limy,imgplot,div_x,div_y):
    columna=0
    horizontal_cambios_arriba=0
    horizontal_numero_arriba=0
    division=int (limy/4)
    aux=imgplot[division,columna]
    for columna in range (0, limx):
        if (imgplot[division, columna]!=aux):
            horizontal_cambios_arriba=horizontal_cambios_arriba+1
            aux=imgplot[division,columna]
        if (imgplot[division, columna]==1):
            horizontal_numero_arriba=horizontal_numero_arriba+1
    return horizontal_cambios_arriba, horizontal_numero_arriba
     
def trece_catorce_caract(limx,limy,imgplot,div_x,div_y):
    columna=0
    horizontal_cambios_abajo=0
    horizontal_numero_abajo=0
    division=int (limy/4)
    division=limy-division
    aux=imgplot[division,columna]
    for columna in range (0, limx):
        if (imgplot[division, columna]!=aux):
            horizontal_cambios_abajo=horizontal_cambios_abajo+1
            aux=imgplot[division,columna]
        if (imgplot[division, columna]==1):
            horizontal_numero_abajo=horizontal_numero_abajo+1
    return horizontal_cambios_abajo,horizontal_numero_abajo



 
import matplotlib.image as mpimg
import csv
import os
import Caracteristicas
 
def dataset():
    root='Numeros'
    archivo= open('DataSet_Final.csv', 'w', newline='')
    salida = csv.writer(archivo)
    porcentaje=''
    clase=0
    posiciones_dataset=0
    for dirName, subdirList, fileList in os.walk(root):
        print("Estamos trabajando en el dataset\n",porcentaje)
        porcentaje=porcentaje+'.#'
        for fname in fileList:
            posiciones_dataset=posiciones_dataset+1
            nameima=dirName+'/'+fname
            imgplot=mpimg.imread(nameima)
            imagen=imgplot.shape
            limx= imagen[1]
            limy= imagen[0]
            div_x=int(limx/2)
            div_y=int(limy/2)
            relacion_1,relacion_2=Caracteristicas.primera_segunda_carac(limx, limy,imgplot)
            recta_cambios,recta_numero=Caracteristicas.tecera_cuarta_carac(limx,limy,imgplot,div_x,div_y)
            perpendicular_cambios,perpendicular_numero=Caracteristicas.quinta_sexta_carac(limx,limy,imgplot,div_x,div_y)
            recta_cambios_izquierda,recta_cambios_numeros=Caracteristicas.septima_octava_carac(limx,limy,imgplot,div_x,div_y)
            recta_cambios_derecha,recta_cambios_derecha_numeros=Caracteristicas.novena_decima_carac(limx,limy,imgplot,div_x,div_y)
            perpendicular_cambios_arriba, perpendicular_numero_arriba=Caracteristicas.once_doce_carac(limx,limy,imgplot,div_x,div_y)
            perpendicular_cambios_abajo, perpendicular_numero_abajo=Caracteristicas.trece_catorce_caract(limx,limy,imgplot,div_x,div_y)
            salida.writerow([relacion_1,relacion_2, recta_cambios,recta_numero,perpendicular_cambios, 
                             perpendicular_numero, recta_cambios_izquierda,recta_cambios_numeros, recta_cambios_derecha,
                             recta_cambios_derecha_numeros, perpendicular_cambios_arriba, perpendicular_numero_arriba,
                             perpendicular_cambios_abajo, perpendicular_numero_abajo,posiciones_dataset,clase-1])
        clase=clase+1
        os.system("cls")
    print ("Dataset Terminado")
    archivo.close()
    
    

 

import csv
import math
import Caracteristicas
import os
 
def Clasificacion():
    limx,limy, imgplot, div_x,div_y=Caracteristicas.lectura()
     
    relacion_1,relacion_2=Caracteristicas.primera_segunda_carac(limx, limy,imgplot)
     
    vertical_cambios,vertical_numero=Caracteristicas.tecera_cuarta_carac(limx,limy,imgplot,div_x,div_y)
     
    horizontal_cambios,horizontal_numero=Caracteristicas.quinta_sexta_carac(limx,limy,imgplot,div_x,div_y)
     
    vertical_cambios_izquierda,vertical_cambios_numeros=Caracteristicas.septima_octava_carac(limx,limy,imgplot,div_x,div_y)
     
    vertical_cambios_derecha,vertical_cambios_derecha_numeros=Caracteristicas.novena_decima_carac(limx,limy,imgplot,div_x,div_y)
         
    horizontal_cambios_arriba, horizontal_numero_arriba=Caracteristicas.once_doce_carac(limx,limy,imgplot,div_x,div_y)
         
    horizontal_cambios_abajo, horizontal_numero_abajo=Caracteristicas.trece_catorce_caract(limx,limy,imgplot,div_x,div_y)    
            
    abrir= open('DataSet_Final.csv')
    leer_dataset=csv.reader(abrir)
    dataset=list(leer_dataset)
    print ("Por favor ingrese los datos solicitados")
    print("Numero de vecinos a considerar: ",end="")
    numero_vecinos=int(input())
    os.system("cls")
    contador=0
    for i in dataset:
        dataset[contador][0]=float(dataset[contador][0])
        dataset[contador][1]=float(dataset[contador][1])
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
        distancia_previa=(((dataset[contador][0]-relacion_1)**2)+((dataset[contador][1]-relacion_2)**2)
        +((dataset[contador][2]-vertical_cambios)**2)+((dataset[contador][3]-vertical_numero)**2)+
        ((dataset[contador][4]-horizontal_cambios)**2)+((dataset[contador][5]-horizontal_numero)**2)+
        ((dataset[contador][6]-vertical_cambios_izquierda)**2)+((dataset[contador][7]-vertical_cambios_numeros)**2)+
        ((dataset[contador][8]-vertical_cambios_derecha)**2)+((dataset[contador][9]-vertical_cambios_derecha_numeros)**2)+
        ((dataset[contador][10]-horizontal_cambios_arriba)**2)+((dataset[contador][11]-horizontal_numero_arriba)**2)+
        ((dataset[contador][12]-horizontal_cambios_abajo)**2)+((dataset[contador][13]-horizontal_numero_abajo)**2))
         
        raiz=math.sqrt(distancia_previa)
        dataset[contador].append(raiz)
        contador+=1
    dataset.sort(key=lambda dataset: dataset[14],reverse=True)
    print ("\t\tDataset info:\nNúmero total de instancias:", dataset [0][14],"\nTotal de caracteristicas por instancia: 14 \nTotal de clases: 10\nNombre de las clases:{0,1,2,3,4,5,6,7,8,9}")
    dataset.sort(key=lambda dataset: dataset[16])
    print("Instancia del K vecino mas cercano:", dataset[0][14])
    print ("\nk vecinos mas cercanos:")
    for K_vecinos in range (0,numero_vecinos):
        print ("\tInstancia:", dataset[K_vecinos][14], "\tDistancia:",
               "%.5f" %dataset[K_vecinos][16], "\tClase", dataset[K_vecinos][15])
    return dataset, numero_vecinos

 
def instancias():
    dataset,numero_vecinos=Clasificacion()
    clase_0=0
    clase_1=0
    clase_2=0
    clase_3=0
    clase_4=0
    clase_5=0
    clase_6=0
    clase_7=0
    clase_8=0
    clase_9=0
    
    numero_filas=10
    numero_columnas=2
    clase_final = []
    for filas in range(numero_filas):
        clase_final.append([])
        for columnas in range(numero_columnas):
            clase_final[filas].append(None)
    
    for caracteristica in range(0,numero_vecinos):
        if(dataset[caracteristica][15]==0):
            clase_0=clase_0+1
        if(dataset[caracteristica][15]==1):
            clase_1=clase_1+1
        if(dataset[caracteristica][15]==2):
            clase_2=clase_2+1
        if(dataset[caracteristica][15]==3):
            clase_3=clase_3+1
        if(dataset[caracteristica][15]==4):
            clase_4=clase_4+1
        if(dataset[caracteristica][15]==5):
            clase_5=clase_5+1
        if(dataset[caracteristica][15]==6):
            clase_6=clase_6+1
        if(dataset[caracteristica][15]==7):
            clase_7=clase_7+1
        if(dataset[caracteristica][15]==8):
            clase_8=clase_8+1
        if(dataset[caracteristica][15]==9):
            clase_9=clase_9+1
            
    clase_final[0]=clase_0,0
    clase_final[1]=clase_1,1
    clase_final[2]=clase_2,2
    clase_final[3]=clase_3,3
    clase_final[4]=clase_4,4
    clase_final[5]=clase_5,5
    clase_final[6]=clase_6,6
    clase_final[7]=clase_7,7
    clase_final[8]=clase_8,8
    clase_final[9]=clase_9,9
    
    clase_final.sort(key=None, reverse=True)
    print ("\nNúmero de Instancias por clase:")
    for conteo_instancias in range(0,10):
            print ("\t",clase_final[conteo_instancias][0],
            "\tInstancias de la clase:",clase_final[conteo_instancias][1]) 
    print ("\nLa imagen es el numero:", clase_final[0][1]) 

