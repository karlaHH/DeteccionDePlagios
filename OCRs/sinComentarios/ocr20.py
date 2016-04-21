
 


import matplotlib.image as mpimg 
import csv
import os


archivo= open('DataSetNew.csv', 'w', newline='') 
salida = csv.writer(archivo) 
 
def FilasEntreColumnas(tam):
    FilasColumnas=tam[0]/tam[1] 
    print("Procesando imagen: ",FilasColumnas)
    return FilasColumnas
    
    
def Area(tam, mat):
    areaB=0 
    areaN=0 
    for i in range(0,tam[0]): 
        for j in range(0,tam[1]): 
            if(mat[i][j]!=0): 
                areaN=areaN+1 
            else:
                areaB=areaB+1 
    print("Número de Blancos: " ,areaB)     
            
        
    return areaB
        

def FilasDeCorteUnCuarto(tam,mat):
    cortes1=0
    CFuncuarto=int(tam[1]/4)
    Aux1=mat[CFuncuarto][0]
    for i in range(0,tam[1]):
        if(Aux1!=mat[CFuncuarto][i]):
            Aux1=mat[CFuncuarto][i]
            cortes1=cortes1+1
        
    
    print("Número de cortes en la fila a 1/4: ",cortes1)
    return cortes1

def FilasCorteEnMedio(tam,mat):
    cortes2=0
    CFenmedio=int(tam[0]/2)
    Aux=mat[CFenmedio][0]
    for i in range(0,tam[1]):
        if(Aux!=mat[CFenmedio][i]):
            Aux=mat[CFenmedio][i]
            cortes2=cortes2+1
        
    
    print("Número de cortes en la fila de en medio: ",cortes2)
    return cortes2

def FilasDeCorteTresCuartos(tam,mat):
    cortes3=0
    CFtrescuatro=int((tam[0]/4)*3)
    Aux2=mat[CFtrescuatro][0]
    for i in range(0,tam[1]):
        if(Aux2!=mat[CFtrescuatro][i]):
            Aux2=mat[CFtrescuatro][i]
            cortes3=cortes3+1
        
    
    print("Número de cortes en la fila a 3/4: ",cortes3)
    return cortes3
        

def ColumnasCortesAUnCuarto(tam,mat):
    cortes4=0
    CCuncuarto=int(tam[1]/4)
    Aux4=mat[0][CCuncuarto]
    for i in range(0,tam[0]):
        if(Aux4!=mat[i][CCuncuarto]):
            Aux4=mat[i][CCuncuarto]
            cortes4=cortes4+1
        
    
    print("Número de cortes en la columna a 1/4: ",cortes4)
    return cortes4

def ColumnasCorteEnMedio(tam,mat):
    cortes5=0
    CCenmedio=int(tam[1]/2)
    Aux3=mat[0][CCenmedio]
    for i in range(0,tam[0]):
        if(Aux3!=mat[i][CCenmedio]):
            Aux3=mat[i][CCenmedio]
            cortes5=cortes5+1
        
    
    print("Número de cortes en la columna de en medio: ",cortes5)
    return cortes5

def ColumnasCortesATresCuartos(tam,mat):
    cortes6=0
    CCtrescuartos=int((tam[1]/4)*3)
    Aux5=mat[0][CCtrescuartos]
    for i in range(0,tam[0]):
        if(Aux5!=mat[i][CCtrescuartos]):
            Aux5=mat[i][CCtrescuartos]
            cortes6=cortes6+1
        
    
    print("Número de cortes en la columna a 3/4: ",cortes6)
    return cortes6
        

def AreaDeFilasAUnCuarto(tam,mat):
    cont1=0
    uncuarto=int(tam[0]/4)
    mat[uncuarto][0]
    for i in range(0,tam[1]):
        if (mat[uncuarto][i]!=0):
            
            cont1=cont1+1
        
    
    cont1/tam[1]
    print("Número de píxeles en la fila a 1/4: ",cont1)
    return cont1

def AreaDeFilasEnMedio(tam,mat):
    cont2=0
    enmedio=int(tam[0]/2)
    mat[enmedio][0]
    for i in range(0,tam[1]):
        if (mat[enmedio][i]!=0):
            
            cont2=cont2+1
        
    
    cont2/tam[1]
    print("Número de píxeles en la fila de en medio: ",cont2)
    return cont2 

def AreaDeFilasTresCuartos(tam,mat):
    cont3=0
    trescuatro=int((tam[0]/4)*3)
    mat[trescuatro][0]
    for i in range(0,tam[1]):
        if (mat[trescuatro][i]!=0):
            
            cont3=cont3+1
        
    
    cont3/tam[1]
    print("Número de píxeles en la fila a 3/4: ",cont3)
    return cont3
        

def AreadeColumnasAUnCuarto(tam,mat):
    cont4=0
    Cuncuarto=int(tam[1]/4)
    mat[Cuncuarto][0]
    for i in range(0,tam[0]):
        if (mat[i][Cuncuarto]!=0):
            
            cont4=cont4+1
        
    
    cont4/tam[0]
    print("Número de píxeles en la columna a 1/4: ",cont4)
    return cont4

def AreaDeColumnasEnMedio(tam,mat):
    cont5=0
    Cenmedio=int(tam[1]/2)
    mat[Cenmedio][0]
    for i in range(0,tam[0]):
        if (mat[i][Cenmedio]!=0):
            
            cont5=cont5+1
        
    
    cont5/tam[0]
    print("Número de píxeles en la columna de en medio: ",cont5)
    return cont5

def AreaDeColumnasTresCuartos(tam,mat):
    cont6=0
    Ctrescuatro=int((tam[1]/4)*3)
    mat[Ctrescuatro][0]
    for i in range(0,tam[0]):
        if (mat[i][Ctrescuatro]!=0):
            
            cont6=cont6+1
        
    
    cont6/tam[0]
    print("Número de píxeles en la columna a 3/4: ",cont6)
    return cont6

clase=-1 
root='arialSegmented' 




for dirName, subdirList, fileList in os.walk(root): 
    
    for fname in fileList: 
        nameima=dirName+'/'+fname 
        img=mpimg.imread(nameima) 
        
        mat=img 
        tam=mat.shape 
        Razon=FilasEntreColumnas(tam)
        area=Area(tam,mat)
        FCorteC=FilasDeCorteUnCuarto(tam,mat)
        FCorteM=FilasCorteEnMedio(tam,mat)
        FCorteTC=FilasDeCorteTresCuartos(tam,mat)
        CCortesC=ColumnasCortesAUnCuarto(tam,mat)
        CCortesM=ColumnasCorteEnMedio(tam,mat)
        CCortesTC=ColumnasCortesATresCuartos(tam,mat)
        AFilasC=AreaDeFilasAUnCuarto(tam,mat)
        AFilasM=AreaDeFilasEnMedio(tam,mat)
        AFilasTC=AreaDeFilasTresCuartos(tam,mat)
        AColumnasC=AreadeColumnasAUnCuarto(tam,mat)
        AColumnasM=AreaDeColumnasEnMedio(tam,mat)
        AColumnasTC=AreaDeColumnasTresCuartos(tam,mat)
        
        salida.writerow([Razon,area,FCorteC,FCorteM,FCorteTC,CCortesC,CCortesM,CCortesTC,AFilasC,AFilasM,AFilasTC,AColumnasC,AColumnasM,AColumnasTC,clase])
        
    clase=clase+1 
    
archivo.close() 




 

import matplotlib.image as mpimg 
import csv
import math
Archivo= open('DataSetNew.csv')
lns=csv.reader(Archivo) 
dataset=list(lns)
print("Nombre de la imagen: ")
NImagen=(input())
img=mpimg.imread(NImagen)
mat=img 
tam=mat.shape





print('][][][][][][][][]][][][][][][][][][][][][][][][][][][][][][][][][][][')


def FilasEntreColumnas(tam):
    FilasColumnas=tam[0]/tam[1] 
    print("Procesando imagen: ",FilasColumnas)
    return FilasColumnas
    
    
def Area(tam, mat):
    areaB=0 
    areaN=0 
    for i in range(0,tam[0]): 
        for j in range(0,tam[1]): 
            if(mat[i][j]!=0): 
                areaN=areaN+1 
            else:
                areaB=areaB+1 
    print("Número de Blancos: " ,areaB)     
            
        
    return areaB
        

def FilasDeCorteUnCuarto(tam,mat):
    cortes1=0
    CFuncuarto=int(tam[1]/4)
    Aux1=mat[CFuncuarto][0]
    for i in range(0,tam[1]):
        if(Aux1!=mat[CFuncuarto][i]):
            Aux1=mat[CFuncuarto][i]
            cortes1=cortes1+1
        
    
    print("Número de cortes en la fila a 1/4: ",cortes1)
    return cortes1

def FilasCorteEnMedio(tam,mat):
    cortes2=0
    CFenmedio=int(tam[0]/2)
    Aux=mat[CFenmedio][0]
    for i in range(0,tam[1]):
        if(Aux!=mat[CFenmedio][i]):
            Aux=mat[CFenmedio][i]
            cortes2=cortes2+1
        
    
    print("Número de cortes en la fila de en medio: ",cortes2)
    return cortes2

def FilasDeCorteTresCuartos(tam,mat):
    cortes3=0
    CFtrescuatro=int((tam[0]/4)*3)
    Aux2=mat[CFtrescuatro][0]
    for i in range(0,tam[1]):
        if(Aux2!=mat[CFtrescuatro][i]):
            Aux2=mat[CFtrescuatro][i]
            cortes3=cortes3+1
        
    
    print("Número de cortes en la fila a 3/4: ",cortes3)
    return cortes3
        

def ColumnasCortesAUnCuarto(tam,mat):
    cortes4=0
    CCuncuarto=int(tam[1]/4)
    Aux4=mat[0][CCuncuarto]
    for i in range(0,tam[0]):
        if(Aux4!=mat[i][CCuncuarto]):
            Aux4=mat[i][CCuncuarto]
            cortes4=cortes4+1
        
    
    print("Número de cortes en la columna a 1/4: ",cortes4)
    return cortes4

def ColumnasCorteEnMedio(tam,mat):
    cortes5=0
    CCenmedio=int(tam[1]/2)
    Aux3=mat[0][CCenmedio]
    for i in range(0,tam[0]):
        if(Aux3!=mat[i][CCenmedio]):
            Aux3=mat[i][CCenmedio]
            cortes5=cortes5+1
        
    
    print("Número de cortes en la columna de en medio: ",cortes5)
    return cortes5

def ColumnasCortesATresCuartos(tam,mat):
    cortes6=0
    CCtrescuartos=int((tam[1]/4)*3)
    Aux5=mat[0][CCtrescuartos]
    for i in range(0,tam[0]):
        if(Aux5!=mat[i][CCtrescuartos]):
            Aux5=mat[i][CCtrescuartos]
            cortes6=cortes6+1
        
    
    print("Número de cortes en la columna a 3/4: ",cortes6)
    return cortes6
        

def AreaDeFilasAUnCuarto(tam,mat):
    cont1=0
    uncuarto=int(tam[0]/4)
    mat[uncuarto][0]
    for i in range(0,tam[1]):
        if (mat[uncuarto][i]!=0):
            
            cont1=cont1+1
        
    
    cont1/tam[1]
    print("Número de píxeles en la fila a 1/4: ",cont1)
    return cont1

def AreaDeFilasEnMedio(tam,mat):
    cont2=0
    enmedio=int(tam[0]/2)
    mat[enmedio][0]
    for i in range(0,tam[1]):
        if (mat[enmedio][i]!=0):
            
            cont2=cont2+1
        
    
    cont2/tam[1]
    print("Número de píxeles en la fila de en medio: ",cont2)
    return cont2 

def AreaDeFilasTresCuartos(tam,mat):
    cont3=0
    trescuatro=int((tam[0]/4)*3)
    mat[trescuatro][0]
    for i in range(0,tam[1]):
        if (mat[trescuatro][i]!=0):
            
            cont3=cont3+1
        
    
    cont3/tam[1]
    print("Número de píxeles en la fila a 3/4: ",cont3)
    return cont3
        

def AreadeColumnasAUnCuarto(tam,mat):
    cont4=0
    Cuncuarto=int(tam[1]/4)
    mat[Cuncuarto][0]
    for i in range(0,tam[0]):
        if (mat[i][Cuncuarto]!=0):
            
            cont4=cont4+1
        
    
    cont4/tam[0]
    print("Número de píxeles en la columna a 1/4: ",cont4)
    return cont4

def AreaDeColumnasEnMedio(tam,mat):
    cont5=0
    Cenmedio=int(tam[1]/2)
    mat[Cenmedio][0]
    for i in range(0,tam[0]):
        if (mat[i][Cenmedio]!=0):
            cont5/tam[0]
            cont5=cont5+1
        
    
    cont5/tam[0]
    print("Número de píxeles en la columna de en medio: ",cont5)
    return cont5

def AreaDeColumnasTresCuartos(tam,mat):
    cont6=0
    Ctrescuatro=int((tam[1]/4)*3)
    mat[Ctrescuatro][0]
    for i in range(0,tam[0]):
        if (mat[i][Ctrescuatro]!=0):
            
            cont6=cont6+1
        
    
    cont6/tam[0]
    print("Número de píxeles en la columna a 3/4: ",cont6)
    return cont6

def knn(Razon,area,FCorteC,FCorteM,FCorteTC,CCortesC,CCortesM,CCortesTC,AFilasC,AFilasM,AFilasTC,AColumnasC,AColumnasM,AColumnasTC):
    print('><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><')    
    print("Numero de vecinos a considerar: ",end="")
    NumerokVecinos=int(input())
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


        interna=((dataset[contador][0]-Razon)**2)+((dataset[contador][1]-area)**2)+((dataset[contador][2]-FCorteC)**2)+((dataset[contador][3]-FCorteM)**2)+((dataset[contador][4]-FCorteTC)**2)+((dataset[contador][5]-CCortesC)**2)+((dataset[contador][6]-CCortesM)**2)+((dataset[contador][7]-CCortesTC)**2)+((dataset[contador][8]-AFilasC)**2)+((dataset[contador][9]-AFilasM)**2)+((dataset[contador][10]-AFilasTC)**2)+((dataset[contador][11]-AColumnasC)**2)+((dataset[contador][12]-AColumnasM)**2)+((dataset[contador][13]-AColumnasTC)**2)
        raiz=math.sqrt(interna)
        dataset[contador].append(raiz)
        dataset[contador].append(contador)
        contador=contador+1
              
    dataset.sort(key=lambda dataset: dataset[15])
    
    print('********************************************************************')
    print('\t Información general: ')
    print('    Formato de la Imagen: .png ')
    print('    Número de instancias: ',contador)
    print('    Número de Caracteristicas: 14')
    print('    Número de Clases: 10 ')
    print('    Nombre de las clases:{0,1,2,3,4,5,6,7,8,9}')
    print('|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| \n')   

    ContadorClase0=0
    ContadorClase1=0
    ContadorClase2=0
    ContadorClase3=0
    ContadorClase4=0
    ContadorClase5=0
    ContadorClase6=0
    ContadorClase7=0
    ContadorClase8=0
    ContadorClase9=0
    
    for i in range(0,NumerokVecinos):
          if(dataset[i][14]==0):
              ContadorClase0=ContadorClase0+1
              
          if (dataset[i][14]==1):
              ContadorClase1=ContadorClase1+1 
          
          if (dataset[i][14]==2):
              ContadorClase2=ContadorClase2+1
        
          if (dataset[i][14]==3):
              ContadorClase3=ContadorClase3+1
          
          if (dataset[i][14]==4):
              ContadorClase4=ContadorClase4+1
        
          if (dataset[i][14]==5):
              ContadorClase5=ContadorClase5+1
          
          if (dataset[i][14]==6):
              ContadorClase6=ContadorClase6+1
        
          if (dataset[i][14]==7):
              ContadorClase7=ContadorClase7+1
         
          if (dataset[i][14]==8):
              ContadorClase8=ContadorClase8+1
          
          if (dataset[i][14]==9):
              ContadorClase9=ContadorClase9+1      
          
          print('# Instancia',dataset[i][16],' | Distancia obtenida  ',dataset[i][15],' | Clase ',dataset[i][14])
    print('*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+')
    print('Resumen de instancias')
    print('Se encontraron: ',ContadorClase0,'instancias de la clase : 0') 
    print('Se encontraron: ',ContadorClase1,'instancias de la clase : 1')
    print('Se encontraron: ',ContadorClase2,'instancias de la clase : 2')
    print('Se encontraron: ',ContadorClase3,'instancias de la clase : 3')
    print('Se encontraron: ',ContadorClase4,'instancias de la clase : 4')
    print('Se encontraron: ',ContadorClase5,'instancias de la clase : 5')
    print('Se encontraron: ',ContadorClase6,'instancias de la clase : 6')
    print('Se encontraron: ',ContadorClase7,'instancias de la clase : 7')
    print('Se encontraron: ',ContadorClase8,'instancias de la clase : 8')
    print('Se encontraron: ',ContadorClase9,'instancias de la clase : 9\n\t')
    
    if(ContadorClase0>ContadorClase1):
        if(ContadorClase0>ContadorClase2):
            if(ContadorClase0>ContadorClase3):
                if(ContadorClase0>ContadorClase4):
                    if(ContadorClase0>ContadorClase5):
                        if(ContadorClase0>ContadorClase6):
                            if(ContadorClase0>ContadorClase7):
                                if(ContadorClase0>ContadorClase8):
                                    if(ContadorClase0>ContadorClase9):
                                        print('La Imagen es un 0');
    
    if(ContadorClase1>ContadorClase0):
        if(ContadorClase1>ContadorClase2):
            if(ContadorClase1>ContadorClase3): 
                if(ContadorClase1>ContadorClase4):
                    if(ContadorClase1>ContadorClase5):
                        if(ContadorClase1>ContadorClase6):
                            if(ContadorClase1>ContadorClase7):
                                if(ContadorClase1>ContadorClase8):
                                    if(ContadorClase1>ContadorClase9):
                                        print('La Imagen es un 1');
    
    if(ContadorClase2>ContadorClase0):
        if(ContadorClase2>ContadorClase1):
            if(ContadorClase2>ContadorClase3): 
                if(ContadorClase2>ContadorClase4):
                    if(ContadorClase2>ContadorClase5):
                        if(ContadorClase2>ContadorClase6):
                            if(ContadorClase2>ContadorClase7):
                                if(ContadorClase2>ContadorClase8):
                                    if(ContadorClase2>ContadorClase9):
                                        print('La Imagen es un 2');
      
    if(ContadorClase3>ContadorClase0):
        if(ContadorClase3>ContadorClase1):
            if(ContadorClase3>ContadorClase2):
                if(ContadorClase3>ContadorClase4):
                    if (ContadorClase3>ContadorClase5):
                        if(ContadorClase3>ContadorClase6):
                            if(ContadorClase3>ContadorClase7):
                                if(ContadorClase3>ContadorClase8):
                                    if(ContadorClase3>ContadorClase9):
                                        print('La Imagen es un 3');
    
    if(ContadorClase4>ContadorClase1):
        if(ContadorClase4>ContadorClase2):
            if(ContadorClase4>ContadorClase3):
                if(ContadorClase4>ContadorClase0):
                    if(ContadorClase4>ContadorClase5):
                        if(ContadorClase4>ContadorClase6):
                            if(ContadorClase4>ContadorClase7):
                                if(ContadorClase4>ContadorClase8):
                                    if(ContadorClase4>ContadorClase9):
                                        print('La Imagen es un 4');
    
    if(ContadorClase5>ContadorClase1):
        if(ContadorClase5>ContadorClase2):
            if(ContadorClase5>ContadorClase3):
                if(ContadorClase5>ContadorClase4):
                    if (ContadorClase5>ContadorClase0):
                        if (ContadorClase5>ContadorClase6):
                            if (ContadorClase5>ContadorClase7):
                                if (ContadorClase5>ContadorClase8):
                                    if (ContadorClase5>ContadorClase9):
                                        print('La Imagen es un 5');
    
    if(ContadorClase6>ContadorClase1):
        if(ContadorClase6>ContadorClase2):
            if(ContadorClase6>ContadorClase3):
                if(ContadorClase6>ContadorClase4):
                    if(ContadorClase6>ContadorClase5):
                        if(ContadorClase6>ContadorClase0):
                            if(ContadorClase6>ContadorClase7):
                                if(ContadorClase6>ContadorClase8):
                                    if(ContadorClase6>ContadorClase9):
                                        print('La Imagen es un 6');
    
    if(ContadorClase7>ContadorClase1):
        if(ContadorClase7>ContadorClase2):
            if(ContadorClase7>ContadorClase3):
                if(ContadorClase7>ContadorClase4):
                    if(ContadorClase7>ContadorClase5):
                        if(ContadorClase7>ContadorClase6):
                            if(ContadorClase7>ContadorClase0):
                                if(ContadorClase7>ContadorClase8):
                                    if(ContadorClase7>ContadorClase9):
                                        print('La Imagen es un 7');
    
    if(ContadorClase8>ContadorClase1):
        if(ContadorClase8>ContadorClase2):
            if(ContadorClase8>ContadorClase3):
                if(ContadorClase8>ContadorClase4):
                    if(ContadorClase8>ContadorClase5):
                        if(ContadorClase8>ContadorClase6):
                            if(ContadorClase8>ContadorClase7):
                                if(ContadorClase8>ContadorClase0):
                                    if(ContadorClase8>ContadorClase9):
                                        print('La Imagen es un 8');
    
    if(ContadorClase9>ContadorClase0):
        if(ContadorClase9>ContadorClase1):
                if(ContadorClase9>ContadorClase2):
                    if(ContadorClase9>ContadorClase3):
                        if(ContadorClase9>ContadorClase4):
                            if(ContadorClase9>ContadorClase5):
                                if(ContadorClase9>ContadorClase6):
                                    if(ContadorClase9>ContadorClase7):
                                        if(ContadorClase9>ContadorClase8):
                                            print('La Imagen es un 9');
                                            

Razon=FilasEntreColumnas(tam)
area=Area(tam,mat)
FCorteC=FilasDeCorteUnCuarto(tam,mat)
FCorteM=FilasCorteEnMedio(tam,mat)
FCorteTC=FilasDeCorteTresCuartos(tam,mat)
CCortesC=ColumnasCortesAUnCuarto(tam,mat)
CCortesM=ColumnasCorteEnMedio(tam,mat)
CCortesTC=ColumnasCortesATresCuartos(tam,mat)
AFilasC=AreaDeFilasAUnCuarto(tam,mat)
AFilasM=AreaDeFilasEnMedio(tam,mat)
AFilasTC=AreaDeFilasTresCuartos(tam,mat)
AColumnasC=AreadeColumnasAUnCuarto(tam,mat)
AColumnasM=AreaDeColumnasEnMedio(tam,mat)
AColumnasTC=AreaDeColumnasTresCuartos(tam,mat)

knn(Razon,area,FCorteC,FCorteM,FCorteTC,CCortesC,CCortesM,CCortesTC,AFilasC,AFilasM,AFilasTC,AColumnasC,AColumnasM,AColumnasTC)

