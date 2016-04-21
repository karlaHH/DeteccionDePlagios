import matplotlib.image as mpimagen 
import os
         
         
import csv

 

def RazonFilasnColumnas(Dimensiones):
    
    
    RelacionEntreFilasyColumnas=Dimensiones[0]/Dimensiones[1]
    
    print(RelacionEntreFilasyColumnas)
    
    return RelacionEntreFilasyColumnas



def PixelesQueConformanElAreaDeLaFigura(imagen,Dimensiones):
    
    ContadorDePixelesQueConformanElAreaDeLaFigura=0
    
    for i in range(0,Dimensiones[0]):
        
       for j in range(0,Dimensiones[1]):
           
           
           if(imagen[i][j]!=0):

              ContadorDePixelesQueConformanElAreaDeLaFigura=ContadorDePixelesQueConformanElAreaDeLaFigura+1
    
    print(ContadorDePixelesQueConformanElAreaDeLaFigura)
    
    return ContadorDePixelesQueConformanElAreaDeLaFigura


def NumeroDeCambiosEfectuadosEnLaFilaPosicionadaAUnCuarto(imagen,Dimensiones):
    
    PosicionDeLaFilaAunCuarto = int(Dimensiones[0]/4)
    
    ContadorDeCambiosEnLaFilaAunCuarto=0
    
    aux=imagen[PosicionDeLaFilaAunCuarto][0]
    
    for i in range(0,Dimensiones[1]):
        
        
        if(aux!=imagen[PosicionDeLaFilaAunCuarto][i]):
            
            aux=imagen[PosicionDeLaFilaAunCuarto][i]
            
            ContadorDeCambiosEnLaFilaAunCuarto=ContadorDeCambiosEnLaFilaAunCuarto+1
        
    
    print(ContadorDeCambiosEnLaFilaAunCuarto)
    
    return ContadorDeCambiosEnLaFilaAunCuarto

def NumeroDeCambiosEfectuadosEnLaFilaCentral(imagen,Dimensiones):
    
    PosicionDeLaFilaCentral=int(Dimensiones[0]/2)
    
    ContadorDeCambiosEnLaFilaCentral=0
    
    aux=imagen[PosicionDeLaFilaCentral][0]
    
    for i in range(0,Dimensiones[1]):
        
        if(aux!=imagen[PosicionDeLaFilaCentral][i]):
          
          aux=imagen[PosicionDeLaFilaCentral][i]
          
          ContadorDeCambiosEnLaFilaCentral=ContadorDeCambiosEnLaFilaCentral+1
        
    
    print(ContadorDeCambiosEnLaFilaCentral)
    return ContadorDeCambiosEnLaFilaCentral

def NumeroDeCambiosEfectuadosEnLaFilaPosicionadaATresCuartos(imagen,Dimensiones):
    
    PosicionDeLaFilaATresCuartos=int((Dimensiones[0]/4)*3)
    
    ContadorDeCambiosEnLaFilaATresCuartos=0
    
    aux=imagen[PosicionDeLaFilaATresCuartos][0]
    
    for i in range(0,Dimensiones[1]):
        if(aux!=imagen[PosicionDeLaFilaATresCuartos][i]):
            aux=imagen[PosicionDeLaFilaATresCuartos][i]
            ContadorDeCambiosEnLaFilaATresCuartos=ContadorDeCambiosEnLaFilaATresCuartos+1
        
    print(ContadorDeCambiosEnLaFilaATresCuartos)
    
    return ContadorDeCambiosEnLaFilaATresCuartos    


def NumeroDeCambioEfectuadosEnLaColumnaAUnCuarto(imagen,Dimensiones):
    
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/4)
    
    ContadorDeCambiosEnLaColumnaAUnCuarto=0
    
    aux=imagen[0][PosicionDeLaColumnaAUnCuarto]
    for i in range(0,Dimensiones[0]):
        if(aux!=imagen[i][PosicionDeLaColumnaAUnCuarto]):
            aux=imagen[i][PosicionDeLaColumnaAUnCuarto]
            ContadorDeCambiosEnLaColumnaAUnCuarto=ContadorDeCambiosEnLaColumnaAUnCuarto+1
        
    print(ContadorDeCambiosEnLaColumnaAUnCuarto)
    return ContadorDeCambiosEnLaColumnaAUnCuarto



def NumeroDeCambioEfectuadosEnLaColumnaCentral(imagen,Dimensiones):
    PosicionDeLaColumnaCentral=int(Dimensiones[1]/2)
    ContadorDeCambiosEnLaColumnaCentral=0
    aux=imagen[0][PosicionDeLaColumnaCentral]
    for i in range(0,Dimensiones[0]):
        
        if(aux!=imagen[i][PosicionDeLaColumnaCentral]):
            aux=imagen[i][PosicionDeLaColumnaCentral]
            ContadorDeCambiosEnLaColumnaCentral=ContadorDeCambiosEnLaColumnaCentral+1
        
    print(ContadorDeCambiosEnLaColumnaCentral)
    
    return ContadorDeCambiosEnLaColumnaCentral



def NumeroDeCambioEfectuadosEnLaColumnaATresCuartos(imagen,Dimensiones):
    PosicionDeLaColumnaATresCuartos=int((Dimensiones[1]/4)*3)
    ContadorDeCambiosEnLaColumnaATresCuartos=0
    aux=imagen[0][PosicionDeLaColumnaATresCuartos]
    for i in range(0,Dimensiones[0]):
        if(aux!=imagen[i][PosicionDeLaColumnaATresCuartos]):
            aux=imagen[i][PosicionDeLaColumnaATresCuartos]
            ContadorDeCambiosEnLaColumnaATresCuartos=ContadorDeCambiosEnLaColumnaATresCuartos+1
        
    print(ContadorDeCambiosEnLaColumnaATresCuartos)
    
    return ContadorDeCambiosEnLaColumnaATresCuartos

def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto(imagen,Dimensiones):
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/4)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto=0
    
    for i in range(0,Dimensiones[0]):
        
        if(imagen[i][PosicionDeLaColumnaAUnCuarto]!=0):
            
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto+1
        
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto)   
    
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto


def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral(imagen,Dimensiones):
    
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/2)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral=0
    
    for i in range(0,Dimensiones[0]):
        

        if(imagen[i][PosicionDeLaColumnaAUnCuarto]!=0):
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral+1
        
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral)
    
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral



def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos(imagen,Dimensiones):
    PosicionDeLaColumnaATresCuartos=int((Dimensiones[1]/4)*3)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos=0
    
    for i in range(0,Dimensiones[0]):
        
        
        if(imagen[i][PosicionDeLaColumnaATresCuartos]!=0):
            
            
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos+1
        
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos) 
    
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos


def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaAUnCuarto(imagen,Dimensiones):
    PosicionDeLaFilaAUnCuarto=int(Dimensiones[0]/4)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos=0
    
    for i in range(0,Dimensiones[1]):
        
        
        if(imagen[PosicionDeLaFilaAUnCuarto][i]!=0):
            
            
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos+1
        
    
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos)
    
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos


def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaCentral(imagen,Dimensiones):
    PLH=int(Dimensiones[0]/2)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral=0
    
    for i in range(0,Dimensiones[1]):
        
        
        if(imagen[PLH][i]!=0):
            
            
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral+1
        
    
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral) 
    
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral


def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaATresCuartos(imagen,Dimensiones):
    PLH=int((Dimensiones[0]/4)*3)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos=0
    
    for i in range(0,Dimensiones[1]):
        
        
        if(imagen[PLH][i]!=0):
            
            
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos+1
       
       
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos)
    
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos



def GenerarDataSet(RazonFilasnColumnas,PixelesQueConformanElAreaDeLaFigura,NumeroDeCambiosEfectuadosEnLaFilaPosicionadaAUnCuarto,NumeroDeCambiosEfectuadosEnLaFilaCentral,NumeroDeCambiosEfectuadosEnLaFilaPosicionadaATresCuartos,NumeroDeCambioEfectuadosEnLaColumnaAUnCuarto,NumeroDeCambioEfectuadosEnLaColumnaCentral,NumeroDeCambioEfectuadosEnLaColumnaATresCuartos,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaAUnCuarto,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaCentral,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaATresCuartos):

    Carpeta='arialSegmented'

    Archivo=open('DataSet.csv','w',newline='')

    salida=csv.writer(Archivo)

    clase=-1

    for dir, subdirlist, filelist in os.walk(Carpeta):
    
      for fname in filelist:
        
        
        Direccionimagen=dir+'/'+fname
        
        imagen=mpimagen.imread(Direccionimagen)
        
        
        
        


        Dimensiones=imagen.shape
        print('Dimensiones de la imagen ',Dimensiones)
     
     
        FilaEntreColumna = RazonFilasnColumnas(Dimensiones)
        AreaDeLaFigura = PixelesQueConformanElAreaDeLaFigura(imagen,Dimensiones)
        NumeroDeCambiosFilaUcCuarto = NumeroDeCambiosEfectuadosEnLaFilaPosicionadaAUnCuarto(imagen,Dimensiones)     
        NumeroDeCambiosFilaCentral = NumeroDeCambiosEfectuadosEnLaFilaCentral(imagen,Dimensiones)
        NumeroDeCambiosFilaTresCuartos = NumeroDeCambiosEfectuadosEnLaFilaPosicionadaATresCuartos(imagen,Dimensiones)
        NumeroDeCambiosColumnasaUCuarto = NumeroDeCambioEfectuadosEnLaColumnaAUnCuarto(imagen,Dimensiones)
        NumeroDeCambiosColumnCentral = NumeroDeCambioEfectuadosEnLaColumnaCentral(imagen,Dimensiones)
        NumeroDeCambiosColumnaTresCuartos = NumeroDeCambioEfectuadosEnLaColumnaATresCuartos(imagen,Dimensiones)
        NumeroPixelesColumnaUnCuarto = NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto(imagen,Dimensiones)
        NumeroPixelesColumnaCentral = NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral(imagen,Dimensiones)
        NumeroPixelesColumnaTresCuartos = NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos(imagen,Dimensiones)
        NumeroPixelesFilaUnCuarto = NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaAUnCuarto(imagen,Dimensiones)
        NumeroPixelesFilaCentral = NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaCentral(imagen,Dimensiones)
        NumeroPixelesFilaTresCuartos = NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaATresCuartos(imagen,Dimensiones)
      
      
      
        salida.writerow([FilaEntreColumna,AreaDeLaFigura,NumeroDeCambiosFilaUcCuarto,
                         NumeroDeCambiosFilaCentral, NumeroDeCambiosFilaTresCuartos, 
                         NumeroDeCambiosColumnasaUCuarto, NumeroDeCambiosColumnCentral, 
                         NumeroDeCambiosColumnaTresCuartos, NumeroPixelesColumnaUnCuarto,
                         NumeroPixelesColumnaCentral,NumeroPixelesColumnaTresCuartos,
                         NumeroPixelesFilaUnCuarto,NumeroPixelesFilaCentral,NumeroPixelesFilaTresCuartos,clase])
    
    
      clase=clase+1
    print(clase)

    Archivo.close()
    
    return(imagen,Dimensiones)                               


GenerarDataSet(RazonFilasnColumnas,PixelesQueConformanElAreaDeLaFigura,NumeroDeCambiosEfectuadosEnLaFilaPosicionadaAUnCuarto,NumeroDeCambiosEfectuadosEnLaFilaCentral,NumeroDeCambiosEfectuadosEnLaFilaPosicionadaATresCuartos,NumeroDeCambioEfectuadosEnLaColumnaAUnCuarto,NumeroDeCambioEfectuadosEnLaColumnaCentral,NumeroDeCambioEfectuadosEnLaColumnaATresCuartos,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaAUnCuarto,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaCentral,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaATresCuartos)


import matplotlib.image as mpimg 
import csv 
import math

def LeerDataset():
    
    SeleccionarDataset= open('DataSet.csv')
    
    lns=csv.reader(SeleccionarDataset) 

    dataset=list(lns)
    return dataset

def SeleccionarImagen():
    print("Ingresa el nombre de la imagen ",end="")
    Nombre=(input())
    
    imagen=mpimg.imread('imagenes de prueba'+'/'+Nombre)
    
    
    
    
    return imagen

def CalcularDimensiones(imagen):
    Dimensiones=imagen.shape
    return Dimensiones


 

def RazonFilasnColumnasNuevaInstancia(Dimensiones):
    
    
    RelacionEntreFilasyColumnas=Dimensiones[0]/Dimensiones[1]
    
    
    
    return RelacionEntreFilasyColumnas



def PixelesQueConformanElAreaDeLaFiguraNuevaInstancia(imagen,Dimensiones):
    
    ContadorDePixelesQueConformanElAreaDeLaFigura=0
    
    for i in range(0,Dimensiones[0]):
        
       for j in range(0,Dimensiones[1]):
           
           
           if(imagen[i][j]!=0):

              ContadorDePixelesQueConformanElAreaDeLaFigura=ContadorDePixelesQueConformanElAreaDeLaFigura+1
    
    
    
    return ContadorDePixelesQueConformanElAreaDeLaFigura


def NumeroDeCambiosEfectuadosEnLaFilaPosicionadaAUnCuartoNuevaInstancia(imagen,Dimensiones):
    
    PosicionDeLaFilaAunCuarto = int(Dimensiones[0]/4)
    
    ContadorDeCambiosEnLaFilaAunCuarto=0
    
    aux=imagen[PosicionDeLaFilaAunCuarto][0]
    
    for i in range(0,Dimensiones[1]):
        
        
        if(aux!=imagen[PosicionDeLaFilaAunCuarto][i]):
            
            aux=imagen[PosicionDeLaFilaAunCuarto][i]
            
            ContadorDeCambiosEnLaFilaAunCuarto=ContadorDeCambiosEnLaFilaAunCuarto+1
        
    
    
    
    return ContadorDeCambiosEnLaFilaAunCuarto

def NumeroDeCambiosEfectuadosEnLaFilaCentralNuevaInstancia(imagen,Dimensiones):
    
    PosicionDeLaFilaCentral=int(Dimensiones[0]/2)
    
    ContadorDeCambiosEnLaFilaCentral=0
    
    aux=imagen[PosicionDeLaFilaCentral][0]
    
    for i in range(0,Dimensiones[1]):
        
        if(aux!=imagen[PosicionDeLaFilaCentral][i]):
          
          aux=imagen[PosicionDeLaFilaCentral][i]
          
          ContadorDeCambiosEnLaFilaCentral=ContadorDeCambiosEnLaFilaCentral+1
        
    
    
    return ContadorDeCambiosEnLaFilaCentral

def NumeroDeCambiosEfectuadosEnLaFilaPosicionadaATresCuartosNuevaInstancia(imagen,Dimensiones):
    
    PosicionDeLaFilaATresCuartos=int((Dimensiones[0]/4)*3)
    
    ContadorDeCambiosEnLaFilaATresCuartos=0
    
    aux=imagen[PosicionDeLaFilaATresCuartos][0]
    
    for i in range(0,Dimensiones[1]):
        if(aux!=imagen[PosicionDeLaFilaATresCuartos][i]):
            aux=imagen[PosicionDeLaFilaATresCuartos][i]
            ContadorDeCambiosEnLaFilaATresCuartos=ContadorDeCambiosEnLaFilaATresCuartos+1
        
    
    
    return ContadorDeCambiosEnLaFilaATresCuartos    


def NumeroDeCambioEfectuadosEnLaColumnaAUnCuartoNuevaInstancia(imagen,Dimensiones):
    
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/4)
    
    ContadorDeCambiosEnLaColumnaAUnCuarto=0
    
    aux=imagen[0][PosicionDeLaColumnaAUnCuarto]
    for i in range(0,Dimensiones[0]):
        if(aux!=imagen[i][PosicionDeLaColumnaAUnCuarto]):
            aux=imagen[i][PosicionDeLaColumnaAUnCuarto]
            ContadorDeCambiosEnLaColumnaAUnCuarto=ContadorDeCambiosEnLaColumnaAUnCuarto+1
        
    
    return ContadorDeCambiosEnLaColumnaAUnCuarto



def NumeroDeCambioEfectuadosEnLaColumnaCentralNuevaInstancia(imagen,Dimensiones):
    PosicionDeLaColumnaCentral=int(Dimensiones[1]/2)
    ContadorDeCambiosEnLaColumnaCentral=0
    aux=imagen[0][PosicionDeLaColumnaCentral]
    for i in range(0,Dimensiones[0]):
        
        if(aux!=imagen[i][PosicionDeLaColumnaCentral]):
            aux=imagen[i][PosicionDeLaColumnaCentral]
            ContadorDeCambiosEnLaColumnaCentral=ContadorDeCambiosEnLaColumnaCentral+1
        
    
    
    return ContadorDeCambiosEnLaColumnaCentral



def NumeroDeCambioEfectuadosEnLaColumnaATresCuartosNuevaInstancia(imagen,Dimensiones):
    PosicionDeLaColumnaATresCuartos=int((Dimensiones[1]/4)*3)
    ContadorDeCambiosEnLaColumnaATresCuartos=0
    aux=imagen[0][PosicionDeLaColumnaATresCuartos]
    for i in range(0,Dimensiones[0]):
        if(aux!=imagen[i][PosicionDeLaColumnaATresCuartos]):
            aux=imagen[i][PosicionDeLaColumnaATresCuartos]
            ContadorDeCambiosEnLaColumnaATresCuartos=ContadorDeCambiosEnLaColumnaATresCuartos+1
        
    
    
    return ContadorDeCambiosEnLaColumnaATresCuartos

def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuartoNuevaInstancia(imagen,Dimensiones):
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/4)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto=0
    
    for i in range(0,Dimensiones[0]):
        
        if(imagen[i][PosicionDeLaColumnaAUnCuarto]!=0):
            
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto+1
        
    
    
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto


def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentralNuevaInstancia(imagen,Dimensiones):
    
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/2)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral=0
    
    for i in range(0,Dimensiones[0]):
        

        if(imagen[i][PosicionDeLaColumnaAUnCuarto]!=0):
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral+1
        
    
    
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral



def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartosNuevaInstancia(imagen,Dimensiones):
    PosicionDeLaColumnaATresCuartos=int((Dimensiones[1]/4)*3)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos=0
    
    for i in range(0,Dimensiones[0]):
        
        
        if(imagen[i][PosicionDeLaColumnaATresCuartos]!=0):
            
            
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos+1
        
    
    
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos


def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaAUnCuartoNuevaInstancia(imagen,Dimensiones):
    PosicionDeLaFilaAUnCuarto=int(Dimensiones[0]/4)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos=0
    
    for i in range(0,Dimensiones[1]):
        
        
        if(imagen[PosicionDeLaFilaAUnCuarto][i]!=0):
            
            
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos+1
        
    
    
    
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos


def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaCentralNuevaInstancia(imagen,Dimensiones):
    PLH=int(Dimensiones[0]/2)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral=0
    
    for i in range(0,Dimensiones[1]):
        
        
        if(imagen[PLH][i]!=0):
            
            
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral+1
        
    
    
    
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral


def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaATresCuartosNuevaInstancia(imagen,Dimensiones):
    PLH=int((Dimensiones[0]/4)*3)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos=0
    
    for i in range(0,Dimensiones[1]):
        
        
        if(imagen[PLH][i]!=0):
            
            
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos+1
       
       
    
    
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos
def Vecinos():
    
    print("Numero de vecinos a considerar: ",end="")
    
    NumerokVecinos=int(input())
    
    print('\n')
    return NumerokVecinos


def KNN(dataset,NumerokVecinos,Dimensiones,RelacionEntreFilasyColumnas,ContadorDePixelesQueConformanElAreaDeLaFigura,ContadorDeCambiosEnLaFilaAunCuarto,ContadorDeCambiosEnLaFilaCentral,ContadorDeCambiosEnLaFilaATresCuartos,ContadorDeCambiosEnLaColumnaAUnCuarto,ContadorDeCambiosEnLaColumnaCentral,ContadorDeCambiosEnLaColumnaATresCuartos,ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto,ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral,ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos,ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos,ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral,ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos):
   contadordeInstancias=0



   
   for i in dataset:
          dataset[contadordeInstancias][0]=float(dataset[contadordeInstancias][0])
          dataset[contadordeInstancias][1]=int(dataset[contadordeInstancias][1])  
          dataset[contadordeInstancias][2]=int(dataset[contadordeInstancias][2])  
          dataset[contadordeInstancias][3]=int(dataset[contadordeInstancias][3])  
          dataset[contadordeInstancias][4]=int(dataset[contadordeInstancias][4])  
          dataset[contadordeInstancias][5]=int(dataset[contadordeInstancias][5])
          dataset[contadordeInstancias][6]=int(dataset[contadordeInstancias][6])
          dataset[contadordeInstancias][7]=int(dataset[contadordeInstancias][7])
          dataset[contadordeInstancias][8]=int(dataset[contadordeInstancias][8])
          dataset[contadordeInstancias][9]=int(dataset[contadordeInstancias][9])
          dataset[contadordeInstancias][10]=int(dataset[contadordeInstancias][10])
          dataset[contadordeInstancias][11]=int(dataset[contadordeInstancias][11])
          dataset[contadordeInstancias][12]=int(dataset[contadordeInstancias][12])
          dataset[contadordeInstancias][13]=int(dataset[contadordeInstancias][13])
          dataset[contadordeInstancias][14]=int(dataset[contadordeInstancias][14])
          
          
          
          
          
          OperacionesCaracteristicasNuevasInstancias=((dataset[contadordeInstancias][0]-FilaEntreColumna)**2)+((dataset[contadordeInstancias][1]-AreaDeLaFigura)**2)+((dataset[contadordeInstancias][2]-NumeroDeCambiosFilaUcCuarto)**2)+((dataset[contadordeInstancias][3]-NumeroDeCambiosFilaCentral)**2)+((dataset[contadordeInstancias][4]-NumeroDeCambiosFilaTresCuartos)**2)+((dataset[contadordeInstancias][5]-NumeroDeCambiosColumnasaUCuarto)**2)+((dataset[contadordeInstancias][6]-NumeroDeCambiosColumnCentral)**2)+((dataset[contadordeInstancias][7]-NumeroDeCambiosColumnaTresCuartos)**2)+((dataset[contadordeInstancias][8]-NumeroPixelesColumnaUnCuarto)**2)+((dataset[contadordeInstancias][9]-NumeroPixelesColumnaCentral)**2)+((dataset[contadordeInstancias][10]-NumeroPixelesColumnaTresCuartos)**2)+((dataset[contadordeInstancias][11]-NumeroPixelesFilaUnCuarto)**2)+((dataset[contadordeInstancias][12]-NumeroPixelesFilaCentral)**2)+((dataset[contadordeInstancias][13]-NumeroPixelesFilaTresCuartos)**2)
          
          Funcionraiz=math.sqrt(OperacionesCaracteristicasNuevasInstancias)
          
          dataset[contadordeInstancias].append(Funcionraiz)
          
          dataset[contadordeInstancias].append(contadordeInstancias+1)
          
          contadordeInstancias+=1

   print('Total de Instancias: ',contadordeInstancias)

   print('Numero de Caracteristicas: 14')

   print('Numero de Clases: 10')

   print('Clases: [0,1,2,3,4,5,6,7,8,9]\n')          

   dataset.sort(key=lambda dataset: dataset[15])


   ContadorClase0=0
   ContadorClase1=1
   ContadorClase2=2
   ContadorClase3=3
   ContadorClase4=4
   ContadorClase5=5
   ContadorClase6=6
   ContadorClase7=7
   ContadorClase8=8
   ContadorClase9=9



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
      


   if((ContadorClase0>ContadorClase1) and (ContadorClase0>ContadorClase2) and (ContadorClase0>ContadorClase3) and (ContadorClase0>ContadorClase4) and (ContadorClase0>ContadorClase5) and (ContadorClase0>ContadorClase6) and (ContadorClase0>ContadorClase7)and (ContadorClase0>ContadorClase8) and (ContadorClase0>ContadorClase9) ):
        print('La Imagen es un 0');     
  

   if((ContadorClase1>ContadorClase0) and (ContadorClase1>ContadorClase2) and (ContadorClase1>ContadorClase3) and (ContadorClase1>ContadorClase4) and (ContadorClase1>ContadorClase5) and (ContadorClase1>ContadorClase6) and (ContadorClase1>ContadorClase7)and (ContadorClase1>ContadorClase8) and (ContadorClase1>ContadorClase9) ):
        print('La Imagen es un 1');      

   if((ContadorClase2>ContadorClase0) and (ContadorClase2>ContadorClase1) and (ContadorClase2>ContadorClase3) and (ContadorClase2>ContadorClase4) and (ContadorClase2>ContadorClase5) and (ContadorClase2>ContadorClase6) and (ContadorClase2>ContadorClase7)and (ContadorClase2>ContadorClase8) and (ContadorClase2>ContadorClase9) ):
        print('La Imagen es un 2');     

   if((ContadorClase3>ContadorClase1) and (ContadorClase3>ContadorClase2) and (ContadorClase3>ContadorClase0) and (ContadorClase3>ContadorClase4) and (ContadorClase3>ContadorClase5) and (ContadorClase3>ContadorClase6) and (ContadorClase3>ContadorClase7)and (ContadorClase3>ContadorClase8) and (ContadorClase3>ContadorClase9) ):
        print('La Imagen es un 3');

   if((ContadorClase4>ContadorClase1) and (ContadorClase4>ContadorClase2) and (ContadorClase4>ContadorClase3) and (ContadorClase4>ContadorClase0) and (ContadorClase4>ContadorClase5) and (ContadorClase4>ContadorClase6) and (ContadorClase4>ContadorClase7)and (ContadorClase4>ContadorClase8) and (ContadorClase4>ContadorClase9) ):
        print('La Imagen es un 4');

   if((ContadorClase5>ContadorClase1) and (ContadorClase5>ContadorClase2) and (ContadorClase5>ContadorClase3) and (ContadorClase5>ContadorClase4) and (ContadorClase5>ContadorClase0) and (ContadorClase5>ContadorClase6) and (ContadorClase5>ContadorClase7)and (ContadorClase5>ContadorClase8) and (ContadorClase5>ContadorClase9) ):
        print('La Imagen es un 5');

   if((ContadorClase6>ContadorClase1) and (ContadorClase6>ContadorClase2) and (ContadorClase6>ContadorClase3) and (ContadorClase6>ContadorClase4) and (ContadorClase6>ContadorClase5) and (ContadorClase6>ContadorClase0) and (ContadorClase6>ContadorClase7)and (ContadorClase6>ContadorClase8) and (ContadorClase6>ContadorClase9) ):
        print('La Imagen es un 6');      

   if((ContadorClase7>ContadorClase1) and (ContadorClase7>ContadorClase2) and (ContadorClase7>ContadorClase3) and (ContadorClase7>ContadorClase4) and (ContadorClase7>ContadorClase5) and (ContadorClase7>ContadorClase6) and (ContadorClase7>ContadorClase0)and (ContadorClase7>ContadorClase8) and (ContadorClase7>ContadorClase9) ):
        print('La Imagen es un 7');      

   if((ContadorClase8>ContadorClase1) and (ContadorClase8>ContadorClase2) and (ContadorClase8>ContadorClase3) and (ContadorClase8>ContadorClase4) and (ContadorClase8>ContadorClase5) and (ContadorClase8>ContadorClase6) and (ContadorClase8>ContadorClase7)and (ContadorClase8>ContadorClase0) and (ContadorClase8>ContadorClase9) ):
        print('La Imagen es un 8');      

   if((ContadorClase9>ContadorClase1) and (ContadorClase9>ContadorClase2) and (ContadorClase9>ContadorClase3) and (ContadorClase9>ContadorClase4) and (ContadorClase9>ContadorClase5) and (ContadorClase9>ContadorClase6) and (ContadorClase9>ContadorClase7)and (ContadorClase9>ContadorClase8) and (ContadorClase9>ContadorClase0) ):
        print('La Imagen es un 9');
  
  


def Descripcion(dataset,NumerokVecinos): 
  for i in range (0,NumerokVecinos):
    
    print('Vecino:',(i+1),' ','Ubicacion:',dataset[i][16],' ','Clase:',dataset[i][14],'Distancia:',dataset[i][15])




def Numerosdevecinosdeunaclase(dataset,NumerokVecinos):
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
    
    for i in range(0,NumerokVecinos):
        
        if(dataset[i][14]==0):
            
            clase0=clase0+1
        
        if(dataset[i][14]==1):
            
            clase1=clase1+1
       
        if(dataset[i][14]==2):
            
            clase2=clase2+1
        
        if(dataset[i][14]==3):
            
            clase3=clase3+1
        
        if(dataset[i][14]==4):
            
            clase4=clase4+1
       
        if(dataset[i][14]==5):
            
            clase5=clase5+1
        
        if(dataset[i][14]==6):
            
            clase6=clase6+1
       
        if(dataset[i][14]==7):
            
            clase7=clase7+1
       
        if(dataset[i][14]==8):
            
            clase0=clase8+1
        
        if(dataset[i][14]==9):
            
            clase9=clase9+1            
    print('\n')    
    print('Total de instancias que pertenecen a la clase 0: ',clase0)
    print('Total de instancias que pertenecen a la clase 1: ',clase1)
    print('Total de instancias que pertenecen a la clase 2: ',clase2)
    print('Total de instancias que pertenecen a la clase 3: ',clase3)
    print('Total de instancias que pertenecen a la clase 4: ',clase4)
    print('Total de instancias que pertenecen a la clase 5: ',clase5)
    print('Total de instancias que pertenecen a la clase 6: ',clase6)
    print('Total de instancias que pertenecen a la clase 7: ',clase7)
    print('Total de instancias que pertenecen a la clase 8: ',clase8)
    print('Total de instancias que pertenecen a la clase 9: ',clase9)
dataset=LeerDataset()
imagen=SeleccionarImagen()
Dimensiones=CalcularDimensiones(imagen)
NumerokVecinos= int(Vecinos())

FilaEntreColumna = float (RazonFilasnColumnasNuevaInstancia(Dimensiones))
AreaDeLaFigura = int (PixelesQueConformanElAreaDeLaFiguraNuevaInstancia(imagen,Dimensiones))
NumeroDeCambiosFilaUcCuarto = int (NumeroDeCambiosEfectuadosEnLaFilaPosicionadaAUnCuartoNuevaInstancia(imagen,Dimensiones))     
NumeroDeCambiosFilaCentral =int( NumeroDeCambiosEfectuadosEnLaFilaCentralNuevaInstancia(imagen,Dimensiones))
NumeroDeCambiosFilaTresCuartos =int( NumeroDeCambiosEfectuadosEnLaFilaPosicionadaATresCuartosNuevaInstancia(imagen,Dimensiones))
NumeroDeCambiosColumnasaUCuarto =int( NumeroDeCambioEfectuadosEnLaColumnaAUnCuartoNuevaInstancia(imagen,Dimensiones))
NumeroDeCambiosColumnCentral = int(NumeroDeCambioEfectuadosEnLaColumnaCentralNuevaInstancia(imagen,Dimensiones))
NumeroDeCambiosColumnaTresCuartos =int( NumeroDeCambioEfectuadosEnLaColumnaATresCuartosNuevaInstancia(imagen,Dimensiones))
NumeroPixelesColumnaUnCuarto = int(NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuartoNuevaInstancia(imagen,Dimensiones))
NumeroPixelesColumnaCentral = int(NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentralNuevaInstancia(imagen,Dimensiones))
NumeroPixelesColumnaTresCuartos =int( NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartosNuevaInstancia(imagen,Dimensiones))
NumeroPixelesFilaUnCuarto = int(NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaAUnCuartoNuevaInstancia(imagen,Dimensiones))
NumeroPixelesFilaCentral = int(NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaCentralNuevaInstancia(imagen,Dimensiones))
NumeroPixelesFilaTresCuartos =int( NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaATresCuartosNuevaInstancia(imagen,Dimensiones))


KNN(dataset,NumerokVecinos,Dimensiones,FilaEntreColumna,AreaDeLaFigura,NumeroDeCambiosFilaUcCuarto,NumeroDeCambiosFilaCentral,NumeroDeCambiosFilaTresCuartos,NumeroDeCambiosColumnasaUCuarto,NumeroDeCambiosColumnCentral,NumeroDeCambiosColumnaTresCuartos,NumeroPixelesColumnaUnCuarto,NumeroPixelesColumnaCentral,NumeroPixelesColumnaTresCuartos,NumeroPixelesFilaUnCuarto,NumeroPixelesFilaCentral,NumeroPixelesFilaTresCuartos)
Descripcion(dataset,NumerokVecinos)    
Numerosdevecinosdeunaclase(dataset,NumerokVecinos)

