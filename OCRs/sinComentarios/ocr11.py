
 

import matplotlib.image as mpimg 
import csv 
import os 


def rutaImagen(directorio,nombreDeImagen):
    
    nuevaRutaImagen=directorio+'/'+nombreDeImagen 
    return nuevaRutaImagen 

    
def imagen(ruta):
    imagen=mpimg.imread(ruta) 
    return imagen 


def dimencionesImagen(imagen):
    dimenciones=imagen.shape 
    return dimenciones 

    
def numeroFilas(dimencion):
    numeroEnFilas=dimencion[0] 
    return numeroEnFilas 


def numeroColumnas(dimencion):
    numeroEnColumnas=dimencion[1] 
    return numeroEnColumnas 


def relacionTamaño(largo,ancho):
    relacion_Tamaño=largo/ancho
    return relacion_Tamaño 


def areaNumero(Filas,Columnas,imagen):
    area_Numero=0 
    for i in range(0,Filas): 
        for j in range(0,Columnas): 
            if(imagen[i][j]!=0): 
                area_Numero=area_Numero+1 
    return area_Numero 


def filaCentral(Filas):
    fila_central=int(Filas/2) 
    return fila_central 


def columnaCentral(columnas):
    columna_central=int(columnas/2) 
    return columna_central 


def filaPosicionadaEnUnCuarto(fila_central):
    filaUnCuarto=int(fila_central/2) 
    return filaUnCuarto 


def filaPosicionadaEnTresCuartos(fila_central,fila_un_cuarto):
    filaTresCuartos=fila_central+fila_un_cuarto 
    return filaTresCuartos 


def columnaPosicionadaEnUnCuarto(columna_central):
    columnaUnCuarto=int(columna_central/2) 
    return columnaUnCuarto 


def columnaPosicionadaEnTresCuartos(columna_central,columna_un_cuarto):
    columnaTresCuartos=columna_central+columna_un_cuarto 
    return columnaTresCuartos 


def cortesEnUnaFila(fila,numero_columnas,imagen):
    cortesEnLaFila=0 
    auxiliar=imagen[fila][0] 
    for i in range(0,numero_columnas): 
        if(auxiliar!=imagen[fila][i]): 
            auxiliar=imagen[fila][i] 
            cortesEnLaFila=cortesEnLaFila+1 
    
    return cortesEnLaFila 


def pixelesDelNumeroEnUnaFila(fila,numero_columnas,imagen):
    pixelesDelNumeroEnFila=0 
    for i in range(0,numero_columnas): 
        if(imagen[fila][i]!=0): 
            pixelesDelNumeroEnFila=pixelesDelNumeroEnFila+1 
    return pixelesDelNumeroEnFila 


def cortesEnUnaColumna(columna,numero_filas,imagen):
    cortesEnColumna=0 
    auxiliar=imagen[0][columna] 
    for i in range(0,numero_filas): 
        if(auxiliar!=imagen[i][columna]): 
            auxiliar=imagen[i][columna] 
            cortesEnColumna= cortesEnColumna+1 
    return cortesEnColumna 


def pixelesDelNumeroEnUnaColumna(columna,numero_filas,imagen):
    pixelesDelNumeroEnColumna=0 
    for i in range(0,numero_filas): 
        if(imagen[i][columna]!=0): 
            pixelesDelNumeroEnColumna=pixelesDelNumeroEnColumna+1 
    return pixelesDelNumeroEnColumna 


def creacionDataSet():
    archivo= open('DataSet.csv', 'w', newline='') 
    salida = csv.writer(archivo) 
    clase=-1 
    carpetaDeImagenes='arialSegmented' 
    
    
    
    
    for dirName, subdirList, fileList in os.walk(carpetaDeImagenes): 
        
        for fname in fileList: 
            rutaDeLaImagen=rutaImagen(dirName,fname) 
            imagenNueva=imagen(rutaDeLaImagen) 
            dimencionesDeLaImagen=dimencionesImagen(imagenNueva) 
            numeroDeFilas=numeroFilas(dimencionesDeLaImagen) 
            numeroDeColumnas=numeroColumnas(dimencionesDeLaImagen) 
            
            
            relacionLargoEntreAncho=relacionTamaño(numeroDeFilas,numeroDeColumnas) 
            
            areaDelNumero=areaNumero(numeroDeFilas,numeroDeColumnas,imagenNueva)
            
            FilaCentral=filaCentral(numeroDeFilas) 
            
            ColumnaCentral=columnaCentral(numeroDeColumnas) 
            
            CortesEnLaFilaCentral=cortesEnUnaFila(FilaCentral,numeroDeColumnas,imagenNueva) 
            
            pixelesDelNumeroEnLaFilaCentral=pixelesDelNumeroEnUnaFila(FilaCentral,numeroDeColumnas,imagenNueva) 
            
            cortesEnLaColumnaCentral=cortesEnUnaColumna(ColumnaCentral,numeroDeFilas,imagenNueva) 
            
            pixelesDelNumeroEnLaColumnaCentral=pixelesDelNumeroEnUnaColumna(ColumnaCentral,numeroDeFilas,imagenNueva) 
            
            filaEnUnCuarto=filaPosicionadaEnUnCuarto(FilaCentral) 
            
            filaEnTresCuartos=filaPosicionadaEnTresCuartos(FilaCentral,filaEnUnCuarto) 
            
            columnaEnUnCuarto=columnaPosicionadaEnUnCuarto(ColumnaCentral) 
            
            columnaEnTresCuartos=columnaPosicionadaEnTresCuartos(ColumnaCentral,columnaEnUnCuarto) 
            
            cortesEnLaFilaUnCuarto=cortesEnUnaFila(filaEnUnCuarto,numeroDeColumnas,imagenNueva) 
            
            pixelesDelNumeroEnLaFilaUnCuarto=pixelesDelNumeroEnUnaFila(filaEnUnCuarto,numeroDeColumnas,imagenNueva) 
            
            cortesEnLaFilaTresCuartos=cortesEnUnaFila(filaEnTresCuartos,numeroDeColumnas,imagenNueva) 
            
            pixelesDelNumeroEnLaFilaTresCuartos=pixelesDelNumeroEnUnaFila(filaEnTresCuartos,numeroDeColumnas,imagenNueva) 
            
            cortesEnLaColumnaUnCuarto=cortesEnUnaColumna(columnaEnUnCuarto,numeroDeFilas,imagenNueva) 
            
            pixelesDelNumeroEnLaColumnaUnCuarto=pixelesDelNumeroEnUnaColumna(columnaEnUnCuarto,numeroDeFilas,imagenNueva) 
            
            cortesEnLaColumnaTresCuartos=cortesEnUnaColumna(columnaEnTresCuartos,numeroDeFilas,imagenNueva) 
            
            pixelesDelNumeroEnLaColumnaTresCuartos=pixelesDelNumeroEnUnaColumna(columnaEnTresCuartos,numeroDeFilas,imagenNueva) 
            salida.writerow([relacionLargoEntreAncho,areaDelNumero,CortesEnLaFilaCentral,pixelesDelNumeroEnLaFilaCentral,cortesEnLaColumnaCentral,pixelesDelNumeroEnLaColumnaCentral,cortesEnLaFilaUnCuarto,pixelesDelNumeroEnLaFilaUnCuarto,cortesEnLaFilaTresCuartos,pixelesDelNumeroEnLaFilaTresCuartos,cortesEnLaColumnaUnCuarto,pixelesDelNumeroEnLaColumnaUnCuarto,cortesEnLaColumnaTresCuartos,pixelesDelNumeroEnLaColumnaTresCuartos,clase]) 
        
        clase=clase+1 
    
    archivo.close() 

creacionDataSet() 



 

import matplotlib.image as mpimg 
import csv 
import math 
import OCR as Funciones 


def lecturaDelDataSet():
    f= open('DataSet.csv') 
    lns=csv.reader(f) 
    dataset=list(lns) 
    f.close() 
    return dataset 


def convertirDataSet(dataset):
    fila=0 
    for i in dataset: 
        dataset[fila][0]=float(dataset[fila][0]) 
        dataset[fila][1]=float(dataset[fila][1]) 
        dataset[fila][2]=float(dataset[fila][2]) 
        dataset[fila][3]=float(dataset[fila][3]) 
        dataset[fila][4]=float(dataset[fila][4]) 
        dataset[fila][5]=float(dataset[fila][5]) 
        dataset[fila][6]=float(dataset[fila][6]) 
        dataset[fila][7]=float(dataset[fila][7]) 
        dataset[fila][8]=float(dataset[fila][8]) 
        dataset[fila][9]=float(dataset[fila][9]) 
        dataset[fila][10]=float(dataset[fila][10]) 
        dataset[fila][11]=float(dataset[fila][11]) 
        dataset[fila][12]=float(dataset[fila][12]) 
        dataset[fila][13]=float(dataset[fila][13]) 
        dataset[fila][14]=float(dataset[fila][14]) 
        fila+=1 
    return dataset 


def distancias(dataset,caracteristica1,caracteristica2,caracteristica3,caracteristica4,caracteristica5,caracteristica6,caracteristica7,caracteristica8,caracteristica9,caracteristica10,caracteristica11,caracteristica12,caracteristica13,caracteristica14):
    fila=0 
    for i in dataset: 
        
        sumatoria=((dataset[fila][0]-caracteristica1)**2)+((dataset[fila][1]-caracteristica2)**2+((dataset[fila][2]-caracteristica3)**2)+((dataset[fila][3]-caracteristica4)**2)+((dataset[fila][4]-caracteristica5)**2)+((dataset[fila][5]-caracteristica6)**2)+((dataset[fila][6]-caracteristica7)**2)+((dataset[fila][7]-caracteristica8)**2)+((dataset[fila][8]-caracteristica9)**2)+((dataset[fila][9]-caracteristica10)**2)+((dataset[fila][10]-caracteristica11)**2)+((dataset[fila][11]-caracteristica12)**2)+((dataset[fila][12]-caracteristica13)**2)+((dataset[fila][13]-caracteristica14)**2))
        distancia=math.sqrt(sumatoria) 
        dataset[fila].append(distancia) 
        dataset[fila].append(fila+1) 
        fila+=1 
    return dataset 


def datasetOrden(dataset):
    dataset.sort(key=lambda dataset: dataset[15]) 
    return dataset 


def imagen():
    print('indica el nombre de la imagen deseada: ')
    nombre=input() 
    ruta='imagenes' 
    nombreCompleto=ruta+'/'+nombre 
    img=mpimg.imread(nombreCompleto) 
    return img 


def vecinos():
    print("Numero de vecinos a considerar: ") 
    k_vecinos=int(input()) 
    return k_vecinos 


def clasificar(dataset,kVecinos):
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
    for i in range(0,kVecinos): 
        if(dataset[i][14]==0): 
            clase_0+=1 
        if(dataset[i][14]==1): 
            clase_1+=1 
        if(dataset[i][14]==2): 
            clase_2+=1 
        if(dataset[i][14]==3): 
            clase_3+=1 
        if(dataset[i][14]==4): 
            clase_4+=1 
        if(dataset[i][14]==5): 
            clase_5+=1 
        if(dataset[i][14]==6): 
            clase_6+=1 
        if(dataset[i][14]==7): 
            clase_7+=1 
        if(dataset[i][14]==8): 
            clase_8+=1 
        if(dataset[i][14]==9): 
            clase_9+=1 
            
    
    clases=[[0,clase_0],[1,clase_1],[2,clase_2],[3,clase_3],[4,clase_4],[5,clase_5],[6,clase_6],[7,clase_7],[8,clase_8],[9,clase_9]]
    clases.sort(key=lambda clases: clases[1]) 
    return clases


def imprecion(clasificacion,dataset,k_vecinos):
    instancias=len(dataset) 
    
    clasesEnDataset=[0,1,2,3,4,5,6,7,8,9]
    print('--------------------- Informacion general ---------------------------')
    print('Numero de intancias: ',instancias) 
    print('Propiedades por instancia: 14') 
    print('Clases totales: 10') 
    print('Nombre de las clases: ') 
    print(clasesEnDataset) 
    print('---------------------------------------------------------------------\n')
    print('--------------------- vecinos mas cercanos --------------------------')
    for i in range (0,k_vecinos): 
        
        print('Vecino: ',(i+1),' Instancia: ',dataset[i][16],' Distancia: ',dataset[i][15],' Clase: ',dataset[i][14])
    print('---------------------------------------------------------------------\n')
    print('--------------------- Instancias por clase --------------------------')
    for i in range (9,-1,-1):
        if(clasificacion[i][1]>0):
            print(clasificacion[i][1],' instancias pertenecen a la clase: ',clasificacion[i][0])
    print('---------------------------------------------------------------------\n')    
    if(clasificacion[9][1]==clasificacion[8][1]): 
        print('La imagen pertenece a la clase: ',dataset[0][14]) 
    else:
        print('La imagen pertenece a la clase: ', clasificacion[9][0]) 
    print()




imagenNueva=imagen()
dimencionesDeLaImagen=Funciones.dimencionesImagen(imagenNueva) 
numeroDeFilas=Funciones.numeroFilas(dimencionesDeLaImagen) 
numeroDeColumnas=Funciones.numeroColumnas(dimencionesDeLaImagen) 


relacionLargoEntreAncho=Funciones.relacionTamaño(numeroDeFilas,numeroDeColumnas) 

areaDelNumero=Funciones.areaNumero(numeroDeFilas,numeroDeColumnas,imagenNueva)

FilaCentral=Funciones.filaCentral(numeroDeFilas) 

ColumnaCentral=Funciones.columnaCentral(numeroDeColumnas) 

CortesEnLaFilaCentral=Funciones.cortesEnUnaFila(FilaCentral,numeroDeColumnas,imagenNueva) 

pixelesDelNumeroEnLaFilaCentral=Funciones.pixelesDelNumeroEnUnaFila(FilaCentral,numeroDeColumnas,imagenNueva) 

cortesEnLaColumnaCentral=Funciones.cortesEnUnaColumna(ColumnaCentral,numeroDeFilas,imagenNueva) 

pixelesDelNumeroEnLaColumnaCentral=Funciones.pixelesDelNumeroEnUnaColumna(ColumnaCentral,numeroDeFilas,imagenNueva) 

filaEnUnCuarto=Funciones.filaPosicionadaEnUnCuarto(FilaCentral) 

filaEnTresCuartos=Funciones.filaPosicionadaEnTresCuartos(FilaCentral,filaEnUnCuarto) 

columnaEnUnCuarto=Funciones.columnaPosicionadaEnUnCuarto(ColumnaCentral) 

columnaEnTresCuartos=Funciones.columnaPosicionadaEnTresCuartos(ColumnaCentral,columnaEnUnCuarto) 

cortesEnLaFilaUnCuarto=Funciones.cortesEnUnaFila(filaEnUnCuarto,numeroDeColumnas,imagenNueva) 

pixelesDelNumeroEnLaFilaUnCuarto=Funciones.pixelesDelNumeroEnUnaFila(filaEnUnCuarto,numeroDeColumnas,imagenNueva) 

cortesEnLaFilaTresCuartos=Funciones.cortesEnUnaFila(filaEnTresCuartos,numeroDeColumnas,imagenNueva) 

pixelesDelNumeroEnLaFilaTresCuartos=Funciones.pixelesDelNumeroEnUnaFila(filaEnTresCuartos,numeroDeColumnas,imagenNueva) 

cortesEnLaColumnaUnCuarto=Funciones.cortesEnUnaColumna(columnaEnUnCuarto,numeroDeFilas,imagenNueva) 

pixelesDelNumeroEnLaColumnaUnCuarto=Funciones.pixelesDelNumeroEnUnaColumna(columnaEnUnCuarto,numeroDeFilas,imagenNueva) 

cortesEnLaColumnaTresCuartos=Funciones.cortesEnUnaColumna(columnaEnTresCuartos,numeroDeFilas,imagenNueva) 

pixelesDelNumeroEnLaColumnaTresCuartos=Funciones.pixelesDelNumeroEnUnaColumna(columnaEnTresCuartos,numeroDeFilas,imagenNueva) 

DataSetOriginal=lecturaDelDataSet() 
DataSetConvertido=convertirDataSet(DataSetOriginal) 

DataSetConDistancias=distancias(DataSetConvertido,relacionLargoEntreAncho,areaDelNumero,CortesEnLaFilaCentral,pixelesDelNumeroEnLaFilaCentral,cortesEnLaColumnaCentral,pixelesDelNumeroEnLaColumnaCentral,cortesEnLaFilaUnCuarto,pixelesDelNumeroEnLaFilaUnCuarto,cortesEnLaFilaTresCuartos,pixelesDelNumeroEnLaFilaTresCuartos,cortesEnLaColumnaUnCuarto,pixelesDelNumeroEnLaColumnaUnCuarto,cortesEnLaColumnaTresCuartos,pixelesDelNumeroEnLaColumnaTresCuartos)
DataSetOrdenado=datasetOrden(DataSetConDistancias) 
numeroDeVecinos=vecinos() 
clasificacionDeInstancia=clasificar(DataSetOrdenado,numeroDeVecinos) 
imprecion(clasificacionDeInstancia,DataSetOrdenado,numeroDeVecinos)

