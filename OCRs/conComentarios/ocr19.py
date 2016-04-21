# -*- coding: utf-8 -*-
"""
Programa: OCR
Descripcion: Obtiene caracteristicas de un conjunto de imagenes binarizadas que contienen numeros y las guarda en un archivo csv
"""
#import matplotlib.pyplot as plt
import matplotlib.image as mpimg #importo libreria para el manejo de imagenes
import csv #importo libreria para crear archivos csv
import os #importo libreria para acceder a las carpetas con las imagenes

'''
Nombre de la funcion: rutaImagen
Descripcion: Permite obtener la ruta y el nombre de la imagen a analizar
Parametros de entrada: directorio, nombreDeImagen
Resultado: Devuelve la direccion completa del archivo
'''
def rutaImagen(directorio,nombreDeImagen):
    #directorio es la direccion de la imagen nombreDeImagen es el nombre de la imagen
    nuevaRutaImagen=directorio+'/'+nombreDeImagen #variable que permite obtener la direccion y el nombre de la imagen
    return nuevaRutaImagen #devuelvo el valor obtenido

'''
Nombre de la funcion: imagen
Descripcion: Permite leer una imagen, la cual es interpretada como una matriz
Parametros de entrada: ruta (direccion del archivo)
Resultado: Genera una matriz que representa a la imagen
'''    
def imagen(ruta):
    imagen=mpimg.imread(ruta) #se obtiene la imagen y se guarda en una variable
    return imagen #devuelvo el vaolr obtenido

'''
Nombre de la funcion: dimencionesImagen
Descripcion: obtiene el largo y el ancho de una imagen (matriz)
Parametros de entrada: imagen (matriz)
Resultado: Un  arreglo con las dimenciones de la imagen
'''
def dimencionesImagen(imagen):
    dimenciones=imagen.shape #obtengo las dimenciones de la imagen
    return dimenciones #devulevo el valor obtenido

'''
Nombre de la funcion: numeroFilas
Descripcion: obtengo la cantidad de filas total de la imagen (matriz)
Parametros de entrada: dimencion (arreglo con las dimenciones de la matriz)
Resultado: obtengo la cantida de filas en la imagen
'''    
def numeroFilas(dimencion):
    numeroEnFilas=dimencion[0] #obtengo el numero total de Filas de la imagen (largo)
    return numeroEnFilas #devuelvo el valor obtenido

'''
Nombre de la funcion: numeroColumnas
Descripcion: obtengo la cantidad de columnas total de la imagen(matriz)
Parametros de entrada: dimencion (arreglo con las dimenciones de la matriz)
Resultado: obtengo la cantidad de columnas en la imagen
'''
def numeroColumnas(dimencion):
    numeroEnColumnas=dimencion[1] #obtengo el numero total de columnas de la imagen (ancho)
    return numeroEnColumnas #devuelvo el valor obtenido

'''
Nombre de la funcion: relacionTamaño
Descripcion: calculo la relacion que existe entre la divicion de largo y ancho
Parametros de entrada:largo y ancho (numero de filas y de columnas respectivamente)
Resultado: obtengo un numero que representa la relacion largo ancho
'''
def relacionTamaño(largo,ancho):
    relacion_Tamaño=largo/ancho#relacion_Tamaño es la relacion del largo entre el ancho de la imagen
    return relacion_Tamaño #devuelvo el valor obtenido

'''
Nombre de la funcion: areaNumero
Descripcion: cuento los pixeles que representan al numero en la imagen
Parametros de entrada: filas, columnas (dimenciones) y la imagen
Resultado: La cantidad de pixeles del numero
'''
def areaNumero(Filas,Columnas,imagen):
    area_Numero=0 #variable para contar los bits del area del numero en la imagen
    for i in range(0,Filas): #for para recorrer las filas de la imagen
        for j in range(0,Columnas): #for para recorrer las columnas de la imagen
            if(imagen[i][j]!=0): #condicion para clasificar el valor del bits del numero
                area_Numero=area_Numero+1 #si se cumple aumenta el contador del area del numero en la imagen
    return area_Numero #delvuelvo el valor obtenido

'''
Nombre de la funcion: filaCentral
Descripcion: obtengo el numero de la fila ubicada en la posicion central de la imagen
Parametros de entrada: filas (filas totales)
Resultado:la fila central de la imagen
'''
def filaCentral(Filas):
    fila_central=int(Filas/2) #mitad en filas de la imagen
    return fila_central #devuelvo el valor obtenido

'''
Nombre de la funcion: columnaCentral
Descripcion: obtengo el numero de la columna ubicada en la posicion central de la imagen
Parametros de entrada: columnas (columnas totales)
Resultado:la columna central de la imagen
'''
def columnaCentral(columnas):
    columna_central=int(columnas/2) #mitad en columnas de la imagen
    return columna_central #devuelvo el valor obtenido

'''
Nombre de la funcion: filaPosicionadaEnUncuarto
Descripcion: obtengo el numero de la fila ubicada en la posicion un cuarto de la imagen
Parametros de entrada: filas (filas totales)
Resultado:la fila un cuarto de la imagen
'''
def filaPosicionadaEnUnCuarto(fila_central):
    filaUnCuarto=int(fila_central/2) #fila ubicada en un cuarto de la imagen
    return filaUnCuarto #devuelvo el valor obtenido

'''
Nombre de la funcion: filaPosicionadaEnTrescuartos
Descripcion: obtengo el numero de la fila ubicada en la posicion tres cuartos de la imagen
Parametros de entrada: filas (filas totales)
Resultado:la fila tres cuartos de la imagen
'''
def filaPosicionadaEnTresCuartos(fila_central,fila_un_cuarto):
    filaTresCuartos=fila_central+fila_un_cuarto #fila ubicada en tres cuartos de la imagen
    return filaTresCuartos #devuelvo el valor obtenido

'''
Nombre de la funcion: columnaPosicionadaEnUnCuarto
Descripcion: obtengo el numero de la columna ubicada en la posicion un cuarto de la imagen
Parametros de entrada: columnas (columnas totales)
Resultado:la columna un cuarto de la imagen
'''
def columnaPosicionadaEnUnCuarto(columna_central):
    columnaUnCuarto=int(columna_central/2) #columna ubicada en un cuarto de la imagen
    return columnaUnCuarto #devuelvo el valor obtenido

'''
Nombre de la funcion: columnaPosicionadaEntresCuartos
Descripcion: obtengo el numero de la columna ubicada en la posicion tres cuartos de la imagen
Parametros de entrada: columnas (columnas totales)
Resultado:la columna tres cuartos de la imagen
'''
def columnaPosicionadaEnTresCuartos(columna_central,columna_un_cuarto):
    columnaTresCuartos=columna_central+columna_un_cuarto #columna ubicada en tres cuartos de la imagen
    return columnaTresCuartos #devuelvo el valor obtenido

'''
Nombre de la funcion: cortesEnUnaFila
Descripcion: analizo la cantidad de veces que el numero de la imagen es cortado en una fia determinada
Parametros de entrada: fila (cualquier fila), numero_columnas (columnas totales de la imagen) y la imagen
Resultado: cortes en una fila
'''
def cortesEnUnaFila(fila,numero_columnas,imagen):
    cortesEnLaFila=0 #contador de cortes en una fila de la imagen
    auxiliar=imagen[fila][0] #variable que ayudara a comparar los cortes del numero
    for i in range(0,numero_columnas): #for i para recorrer la fila obtenida de la imagen
        if(auxiliar!=imagen[fila][i]): #condicion para verificar los cortes
            auxiliar=imagen[fila][i] #cambio de valor de aux porque encontro un corte 
            cortesEnLaFila=cortesEnLaFila+1 #aumenta el contador de los cortes en la fila obtenida de la imagen
    #fin del for i
    return cortesEnLaFila #devuelvo el valor obtenido

'''
Nombre de la funcion: pixelesDelNumeroEnUnaFila
Descripcion: permite contar los pixeles de un numero en una imagen en una fila determinada
Parametros de entrada: Fila (cualquier fila), numero_columnas (columnas totales de la imagen) y la imagen
Resultado: los pixeles correspondientes al numero en la imagen de una fila
'''
def pixelesDelNumeroEnUnaFila(fila,numero_columnas,imagen):
    pixelesDelNumeroEnFila=0 #variable para contar los pixeles del numero en una fila de la imagen
    for i in range(0,numero_columnas): #for i para recorrer la fila de la imagen
        if(imagen[fila][i]!=0): #comparacion para obtener los pixeles del numero en una fila de la imagen
            pixelesDelNumeroEnFila=pixelesDelNumeroEnFila+1 #aumenta el contador de los pixeles del numero en una fila de la imagen
    return pixelesDelNumeroEnFila #devuelvo el valor obtenido

'''
Nombre de la funcion: cortesEnUnacolumna
Descripcion: analizo la cantidad de veces que el numero de la imagen es cortado en una columna determinada
Parametros de entrada: columna (cualquier columna), numero_filas (filas totales de la imagen) y la imagen
Resultado: cortes en una columna
'''
def cortesEnUnaColumna(columna,numero_filas,imagen):
    cortesEnColumna=0 #contador de cortes en una columna de la imagen
    auxiliar=imagen[0][columna] #Variable que ayudara a  comparar los cortes
    for i in range(0,numero_filas): # for i para recorre la columna deseada de la imagen
        if(auxiliar!=imagen[i][columna]): #condicion para verificar los cortes de la imagen
            auxiliar=imagen[i][columna] #cambio de valor de aux porque encontro un corte de la imagen
            cortesEnColumna= cortesEnColumna+1 #aumenta el contador de los cortes en la columna de la imagen
    return cortesEnColumna #devuelvo el valor obtenido

'''
Nombre de la funcion: pixelesDelNumeroEnUnaColumna
Descripcion: permite contar los pixeles de un numero en una imagen en una columna determinada
Parametros de entrada: columna (cualquier columna), numero_filas (filas totales de la imagen) y la imagen
Resultado: los pixeles correspondientes al numero en la imagen de una columna
'''
def pixelesDelNumeroEnUnaColumna(columna,numero_filas,imagen):
    pixelesDelNumeroEnColumna=0 #variable para contar los bits del numero en la columna central de la imagen
    for i in range(0,numero_filas): #for i para recorrer la columna de la imagen
        if(imagen[i][columna]!=0): #comparacion para reconocer los pixeles del numero en la columna de la imagen
            pixelesDelNumeroEnColumna=pixelesDelNumeroEnColumna+1 #aumenta el contador de los pixeles del numero en la columna de la imagen
    return pixelesDelNumeroEnColumna #devuelvo el valor obtenido

'''
Nombre de la funcion: creaciondataSet
Descripcion: Manda a traer al resto de funciones para obtener las caracteristicas de la imagen y guardarla en un archivo csv
Parametros de entrada: ninguno
Resultado: un archivo csv con las caracteristicas del cunjunto de imagenes
'''
def creacionDataSet():
    archivo= open('DataSet.csv', 'w', newline='') #se abre el archivo csv o se crea si no esta creado
    salida = csv.writer(archivo) #se transfiere el archivo a esta variable para poder escribir en el
    clase=-1 #se crea la variable clase que servira para indicar a que numero pertenecen las caracteristicas obtenidas
    carpetaDeImagenes='arialSegmented' #nombre de la carpeta que contiene las imagenes
    #inicia for
    #existen 3 variables: dirName que indica el nombre del directorio principal y subcarpetas
    #subdirList que indica las subcarpetas de cada carpeta
    #fileList que proporciona una lista con los nombres de los archivos de cada carpeta
    for dirName, subdirList, fileList in os.walk(carpetaDeImagenes): #for para recorer los archivos de la carpeta principal
        #for para recorer las subcarpetas. fname es para obtener el nombre de cada imagen
        for fname in fileList: #for para obtener los nombre de las imagenes
            rutaDeLaImagen=rutaImagen(dirName,fname) #obtengo la ruta de la imagen y su nombre
            imagenNueva=imagen(rutaDeLaImagen) #genero una matriz que representa a la imagen a analizar
            dimencionesDeLaImagen=dimencionesImagen(imagenNueva) #obtengo el largo  y ancho de la imagen (matriz) y las guardo en un arreglo
            numeroDeFilas=numeroFilas(dimencionesDeLaImagen) #obtengo el numero de filas total (largo de la imagen)
            numeroDeColumnas=numeroColumnas(dimencionesDeLaImagen) #obtengo el numero de columnas total (ancho de la imagen)
            #comienzo a obtener las caracteristicas de la imagen
            #Primer caracteristica: relacion de las dimenciones de la imagen
            relacionLargoEntreAncho=relacionTamaño(numeroDeFilas,numeroDeColumnas) #mando a traer esta funcion y la guardo en la variable relacionLargoEntreAncho
            #Segunda caracteristica: cantidad de pixeles del numero en la imagen
            areaDelNumero=areaNumero(numeroDeFilas,numeroDeColumnas,imagenNueva)#mando a traer esta funcion y la guardo en la variable areaDelNumero
            #ubico la fila central de la imagen
            FilaCentral=filaCentral(numeroDeFilas) #mando a traer esta funcion y la guardo en la variable filaCentral
            #ubico la columna central de la imagen
            ColumnaCentral=columnaCentral(numeroDeColumnas) #mando a traer esta funcion y la guardo en la variable ColumnaCentral
            #Tercera caracteristica: cortes del numero en la fila central de la imagen
            CortesEnLaFilaCentral=cortesEnUnaFila(FilaCentral,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable CortesEnLaFilaCentral
            #Cuarta caracteristica: pixeles  del numero en la fila central de la imagen
            pixelesDelNumeroEnLaFilaCentral=pixelesDelNumeroEnUnaFila(FilaCentral,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroenLaFilaCentral
            #Quinta caracteristica: cortes del numero en la columna central de la imagen
            cortesEnLaColumnaCentral=cortesEnUnaColumna(ColumnaCentral,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaColumnaCentral
            #Sexta caracteristica: pixeles del numero en la columna central de la imagen
            pixelesDelNumeroEnLaColumnaCentral=pixelesDelNumeroEnUnaColumna(ColumnaCentral,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaColumnaCentral
            #ubico la fila posicionada en un cuarto de la imagen (la relacion es base a las filas)
            filaEnUnCuarto=filaPosicionadaEnUnCuarto(FilaCentral) #mando a traer esta funcion y la guardo en la variable filaEnUnCuarto
            #ubico la fila posiciona en tres Cuartos de la imagen (la relacion es base a las filas)
            filaEnTresCuartos=filaPosicionadaEnTresCuartos(FilaCentral,filaEnUnCuarto) #mando a traer esta funcion y la guardo en la variable filaEnTresCuartos
            #ubico la columna posicionada en un cuarto de la imagen (la relacion es base a las columnas)
            columnaEnUnCuarto=columnaPosicionadaEnUnCuarto(ColumnaCentral) #mando a traer esta funcion y la guardo en la variable columnaEnUnCuarto
            #ubico la columna posicionada en tres cuartos de la imagen (la relacion es base a las columnas)
            columnaEnTresCuartos=columnaPosicionadaEnTresCuartos(ColumnaCentral,columnaEnUnCuarto) #mando a traer esta funcion y la guardo en la variable columnaEnTresCuartos
            #Septima caracteristica: cortes del numero en la fila un cuarto de la imagen
            cortesEnLaFilaUnCuarto=cortesEnUnaFila(filaEnUnCuarto,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaFilaUnCuarto
            #Octava caracteristica: pixeles del numero en la fila ubicada en un cuarto de la imagen
            pixelesDelNumeroEnLaFilaUnCuarto=pixelesDelNumeroEnUnaFila(filaEnUnCuarto,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaFilaUnCuarto
            #Novena caracteristica: cortes del numero en la fila tres cuartos de la imagen
            cortesEnLaFilaTresCuartos=cortesEnUnaFila(filaEnTresCuartos,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaFilaTresCuartos
            #Decima caracteristica: pixeles del numero en la fila ubicada en tres cuartos de la imagen
            pixelesDelNumeroEnLaFilaTresCuartos=pixelesDelNumeroEnUnaFila(filaEnTresCuartos,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaFilaTresCuartos
            #Onceava caracteristica: cortes del numero en la columna ubicada en un cuarto de la imagen
            cortesEnLaColumnaUnCuarto=cortesEnUnaColumna(columnaEnUnCuarto,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaColumnaUnCuarto
            #Doceava caracteristica: pixeles del numero en la columna ubicada en un cuarto de la imagen
            pixelesDelNumeroEnLaColumnaUnCuarto=pixelesDelNumeroEnUnaColumna(columnaEnUnCuarto,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaColumnaUnCuarto
            #Treceava caracteristica: cortes del numero en la columna ubicada en tres cuartos de la imagen
            cortesEnLaColumnaTresCuartos=cortesEnUnaColumna(columnaEnTresCuartos,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaColumnaTresCuartos
            #Catorceava caracteristica: pixeles del numero en la columna ubicada en tres cuartos de la imagen
            pixelesDelNumeroEnLaColumnaTresCuartos=pixelesDelNumeroEnUnaColumna(columnaEnTresCuartos,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaColumnaTresCuartos
            salida.writerow([relacionLargoEntreAncho,areaDelNumero,CortesEnLaFilaCentral,pixelesDelNumeroEnLaFilaCentral,cortesEnLaColumnaCentral,pixelesDelNumeroEnLaColumnaCentral,cortesEnLaFilaUnCuarto,pixelesDelNumeroEnLaFilaUnCuarto,cortesEnLaFilaTresCuartos,pixelesDelNumeroEnLaFilaTresCuartos,cortesEnLaColumnaUnCuarto,pixelesDelNumeroEnLaColumnaUnCuarto,cortesEnLaColumnaTresCuartos,pixelesDelNumeroEnLaColumnaTresCuartos,clase]) #escribo las caracteristicas en el archivo csv
        #fin del for fname
        clase=clase+1 #aumento la clase en uno cuando termine de leer una subcarpeta
    #fin del for dirName
    archivo.close() #Se cierra el archivo
#funcion principal que realiza en su interior realiza todos los procesos para crear el dataset
creacionDataSet() #mando a traer a la funcion creaciondataset


# -*- coding: utf-8 -*-
"""
Programa: Clasificacion
Descripcion: Permite clasificar un numero  contenido en una imagen binarizada
"""
#impprto las libreria adecuadas para trabajar
import matplotlib.image as mpimg #importo libreria para el manejo de imagenes
import csv #importo la libreria para el manejo de archivos csv
import math #importo la libreria para poder usar raiz cuadrada
import OCR as Funciones #importo el proyecto OCR y un objeto para acceder a sus funciones y no reescribir codigo

'''
Nombre de la funcion: lecturaDelDataset
Descripcion: Permite acceder a un archivo csv y guardar los datos en una matriz
Parametros de entrada: Ninguno
Resultado: Obtengo una matriz
'''
def lecturaDelDataSet():
    f= open('DataSet.csv') #abro un archivo csv
    lns=csv.reader(f) #obtengo la informacion del archivo
    dataset=list(lns) #guardo la informacion obtenida en una matriz
    f.close() #cierro el archivo
    return dataset #devuelvo la matriz con los datos

'''
Nombre de la funcion: convertirDataset
Descripcion: Cambio el tipo de los datos del dataset de string a flotantes para realizar operaciones
Parametros de entrada: dataset (matriz con los datos)
Resultado: Un dataset con datos tipo flotante
'''
def convertirDataSet(dataset):
    fila=0 #inicio un contador que marcara el inicio de las filas en el dataset
    for i in dataset: #inicia el for para recorrer el dataset
        dataset[fila][0]=float(dataset[fila][0]) #convierto este dato a tipo flotante
        dataset[fila][1]=float(dataset[fila][1]) #convierto este dato a tipo flotante
        dataset[fila][2]=float(dataset[fila][2]) #convierto este dato a tipo flotante
        dataset[fila][3]=float(dataset[fila][3]) #convierto este dato a tipo flotante
        dataset[fila][4]=float(dataset[fila][4]) #convierto este dato a tipo flotante
        dataset[fila][5]=float(dataset[fila][5]) #convierto este dato a tipo flotante
        dataset[fila][6]=float(dataset[fila][6]) #convierto este dato a tipo flotante
        dataset[fila][7]=float(dataset[fila][7]) #convierto este dato a tipo flotante
        dataset[fila][8]=float(dataset[fila][8]) #convierto este dato a tipo flotante
        dataset[fila][9]=float(dataset[fila][9]) #convierto este dato a tipo flotante
        dataset[fila][10]=float(dataset[fila][10]) #convierto este dato a tipo flotante
        dataset[fila][11]=float(dataset[fila][11]) #convierto este dato a tipo flotante
        dataset[fila][12]=float(dataset[fila][12]) #convierto este dato a tipo flotante
        dataset[fila][13]=float(dataset[fila][13]) #convierto este dato a tipo flotante
        dataset[fila][14]=float(dataset[fila][14]) #convierto este dato a tipo flotante
        fila+=1 #aumento la variable fila para permitirme acceder a todas las filas del dataset
    return dataset #devuelvo el dataset convertido

'''
Nombre de la funcion: distancias
Descripcion: obtengo las distancias entre la nueva instancia y los datos del dataset
Parametros de entrada: dataset, y las caracteristicas de la nueva imagen
Resultado: un nuevo dataset con las distancias
'''
def distancias(dataset,caracteristica1,caracteristica2,caracteristica3,caracteristica4,caracteristica5,caracteristica6,caracteristica7,caracteristica8,caracteristica9,caracteristica10,caracteristica11,caracteristica12,caracteristica13,caracteristica14):
    fila=0 #inicio un contador que marcara el inicio de las filas en el dataset
    for i in dataset: #inicio el for para recorrer el dataset
        #Realizo la primer parte de la formula, que es una sumatoria de las diferencias entre caractristicas del dataset y la nueva instancia elevadas al cuadrado
        sumatoria=((dataset[fila][0]-caracteristica1)**2)+((dataset[fila][1]-caracteristica2)**2+((dataset[fila][2]-caracteristica3)**2)+((dataset[fila][3]-caracteristica4)**2)+((dataset[fila][4]-caracteristica5)**2)+((dataset[fila][5]-caracteristica6)**2)+((dataset[fila][6]-caracteristica7)**2)+((dataset[fila][7]-caracteristica8)**2)+((dataset[fila][8]-caracteristica9)**2)+((dataset[fila][9]-caracteristica10)**2)+((dataset[fila][10]-caracteristica11)**2)+((dataset[fila][11]-caracteristica12)**2)+((dataset[fila][12]-caracteristica13)**2)+((dataset[fila][13]-caracteristica14)**2))
        distancia=math.sqrt(sumatoria) #calculo la raiz cuadrada, la ultima parte de la formula
        dataset[fila].append(distancia) #agrego el valor obtenido al dataset
        dataset[fila].append(fila+1) #agrego la pocicion al elemento
        fila+=1 #aumento la variable fila para acceder a todas las filas del dataset
    return dataset #devuelvo el dataset con las distancias de todos  los datos o instancias

'''
Nombre de la funcion: datasetOrden
Descripcion: ordeno el dataset en referencia a la distacia, la mas corta va al inicio
Parametros de entrada: dataset, con las distancias
Resultado: dataset ordenado
'''
def datasetOrden(dataset):
    dataset.sort(key=lambda dataset: dataset[15]) #ordeno el dataset en base las distancias
    return dataset #devuelvo el dataset ordenado

'''
Nombre de la funcion: imagen
Descripcion: obtengo la ruta de la instancia a clasificar
Parametros de entrada: Ninguno
Resultado: una imagen para analizar
'''
def imagen():
    print('indica el nombre de la imagen deseada: ')
    nombre=input() #pido el nombre de la imagen
    ruta='imagenes' #carpeta con las imagenes a analizar
    nombreCompleto=ruta+'/'+nombre #ruta Y nombre de la imagen
    img=mpimg.imread(nombreCompleto) #ruta de la imagen
    return img #devuelvo a la imagen obtenida

'''
Nombre de la funcion: vecinos
Descripcion: considero el numero de vecinos para clasificar
Parametros de entrada: Ninguno
Resultado: El numero de vecinos a evaluar
'''
def vecinos():
    print("Numero de vecinos a considerar: ") #indico que se necesitan vecinos para evaluar
    k_vecinos=int(input()) #guardo el numero de vecinos en una variable
    return k_vecinos #devuelvo el numero de vecinos deseados

'''
Nombre de la funcion: clasificar
Descripcion: permite clasificar una nueva instancia o imagen
Parametros de entrada: dataset, kvecinos (numero de vecinos)
Resultado: decidir a que numero pertenece
'''
def clasificar(dataset,kVecinos):
    clase_0=0 #contador que indica la clase 0 (numero 0)
    clase_1=0 #contador que indica la clase 1 (numero 1)
    clase_2=0 #contador que indica la clase 2 (numero 2)
    clase_3=0 #contador que indica la clase 3 (numero 3)
    clase_4=0 #contador que indica la clase 4 (numero 4)
    clase_5=0 #contador que indica la clase 5 (numero 5)
    clase_6=0 #contador que indica la clase 6 (numero 6)
    clase_7=0 #contador que indica la clase 7 (numero 7)
    clase_8=0 #contador que indica la clase 8 (numero 8)
    clase_9=0 #contador que indica la clase 9 (numero 9)
    for i in range(0,kVecinos): #inicia for para recorrer a los vecinos mas cercanos
        if(dataset[i][14]==0): #condicion para conocer si un vecino pertenece a la clase 0
            clase_0+=1 #aumento de la clase 0
        if(dataset[i][14]==1): #condicion para conocer si un vecino pertenece a la clase 1
            clase_1+=1 #aumento de la clase 1
        if(dataset[i][14]==2): #condicion para conocer si un vecino pertenece a la clase 2
            clase_2+=1 #aumento de la clase 2
        if(dataset[i][14]==3): #condicion para conocer si un vecino pertenece a la clase 3
            clase_3+=1 #aumento de la clase 3
        if(dataset[i][14]==4): #condicion para conocer si un vecino pertenece a la clase 4
            clase_4+=1 #aumento de la clase 4
        if(dataset[i][14]==5): #condicion para conocer si un vecino pertenece a la clase 5
            clase_5+=1 #aumento de la clase 5
        if(dataset[i][14]==6): #condicion para conocer si un vecino pertenece a la clase 6
            clase_6+=1 #aumento de la clase 6
        if(dataset[i][14]==7): #condicion para conocer si un vecino pertenece a la clase 7
            clase_7+=1 #aumento de la clase 7
        if(dataset[i][14]==8): #condicion para conocer si un vecino pertenece a la clase 8
            clase_8+=1 #aumento de la clase 8
        if(dataset[i][14]==9): #condicion para conocer si un vecino pertenece a la clase 9
            clase_9+=1 #aumento de la clase 9
            
    #ubico al numero de la clase y el total de vecinos pertenecientes a ella en una matriz
    clases=[[0,clase_0],[1,clase_1],[2,clase_2],[3,clase_3],[4,clase_4],[5,clase_5],[6,clase_6],[7,clase_7],[8,clase_8],[9,clase_9]]
    clases.sort(key=lambda clases: clases[1]) #ordeno la matriz conforme al mayor numero de vecinos ordenados
    return clases

'''
Nombre de la funcion: imprencion
Descripcion: Muestra los resultados obtenidos
Parametros: clasificacion (numero de instancias por clase), dataset (datos) y K_vecinos
Resultado: los resultados de la clasificacion
'''
def imprecion(clasificacion,dataset,k_vecinos):
    instancias=len(dataset) #obtengo las instancias totales
    #Comienzo a imprimir la informacion mas general
    clasesEnDataset=[0,1,2,3,4,5,6,7,8,9]
    print('--------------------- Informacion general ---------------------------')
    print('Numero de intancias: ',instancias) #imprimo el numero de instancias
    print('Propiedades por instancia: 14') #imprimo el numero de caracteristicas
    print('Clases totales: 10') #imprimo el numero de clases
    print('Nombre de las clases: ') #indico el nombre de clases
    print(clasesEnDataset) #imprimo las claes
    print('---------------------------------------------------------------------\n')
    print('--------------------- vecinos mas cercanos --------------------------')
    for i in range (0,k_vecinos): #for para recorrer los vecinos mas cercanos
        #imprimo a l os vecinos mas cercanos
        print('Vecino: ',(i+1),' Instancia: ',dataset[i][16],' Distancia: ',dataset[i][15],' Clase: ',dataset[i][14])
    print('---------------------------------------------------------------------\n')
    print('--------------------- Instancias por clase --------------------------')
    for i in range (9,-1,-1):
        if(clasificacion[i][1]>0):
            print(clasificacion[i][1],' instancias pertenecen a la clase: ',clasificacion[i][0])
    print('---------------------------------------------------------------------\n')    
    if(clasificacion[9][1]==clasificacion[8][1]): #comparo si hubo un empate
        print('La imagen pertenece a la clase: ',dataset[0][14]) #en caso de empate la clase sera la del vecino mas cecarno
    else:
        print('La imagen pertenece a la clase: ', clasificacion[9][0]) #En caso contrario sera la clase con el mayor numero de vecinos
    print()




imagenNueva=imagen()#leo una imagen para sacar sus caracteristicas y clasificarla
dimencionesDeLaImagen=Funciones.dimencionesImagen(imagenNueva) #obtengo el largo  y ancho de la imagen (matriz) y las guardo en un arreglo
numeroDeFilas=Funciones.numeroFilas(dimencionesDeLaImagen) #obtengo el numero de filas total (largo de la imagen)
numeroDeColumnas=Funciones.numeroColumnas(dimencionesDeLaImagen) #obtengo el numero de columnas total (ancho de la imagen)
#comienzo a obtener las caracteristicas de la imagen
#Primer caracteristica: relacion de las dimenciones de la imagen
relacionLargoEntreAncho=Funciones.relacionTamaño(numeroDeFilas,numeroDeColumnas) #mando a traer esta funcion y la guardo en la variable relacionLargoEntreAncho
#Segunda caracteristica: cantidad de pixeles del numero en la imagen
areaDelNumero=Funciones.areaNumero(numeroDeFilas,numeroDeColumnas,imagenNueva)#mando a traer esta funcion y la guardo en la variable areaDelNumero
#ubico la fila central de la imagen
FilaCentral=Funciones.filaCentral(numeroDeFilas) #mando a traer esta funcion y la guardo en la variable filaCentral
#ubico la columna central de la imagen
ColumnaCentral=Funciones.columnaCentral(numeroDeColumnas) #mando a traer esta funcion y la guardo en la variable ColumnaCentral
#Tercera caracteristica: cortes del numero en la fila central de la imagen
CortesEnLaFilaCentral=Funciones.cortesEnUnaFila(FilaCentral,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable CortesEnLaFilaCentral
#Cuarta caracteristica: pixeles  del numero en la fila central de la imagen
pixelesDelNumeroEnLaFilaCentral=Funciones.pixelesDelNumeroEnUnaFila(FilaCentral,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroenLaFilaCentral
#Quinta caracteristica: cortes del numero en la columna central de la imagen
cortesEnLaColumnaCentral=Funciones.cortesEnUnaColumna(ColumnaCentral,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaColumnaCentral
#Sexta caracteristica: pixeles del numero en la columna central de la imagen
pixelesDelNumeroEnLaColumnaCentral=Funciones.pixelesDelNumeroEnUnaColumna(ColumnaCentral,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaColumnaCentral
#ubico la fila posicionada en un cuarto de la imagen (la relacion es base a las filas)
filaEnUnCuarto=Funciones.filaPosicionadaEnUnCuarto(FilaCentral) #mando a traer esta funcion y la guardo en la variable filaEnUnCuarto
#ubico la fila posiciona en tres Cuartos de la imagen (la relacion es base a las filas)
filaEnTresCuartos=Funciones.filaPosicionadaEnTresCuartos(FilaCentral,filaEnUnCuarto) #mando a traer esta funcion y la guardo en la variable filaEnTresCuartos
#ubico la columna posicionada en un cuarto de la imagen (la relacion es base a las columnas)
columnaEnUnCuarto=Funciones.columnaPosicionadaEnUnCuarto(ColumnaCentral) #mando a traer esta funcion y la guardo en la variable columnaEnUnCuarto
#ubico la columna posicionada en tres cuartos de la imagen (la relacion es base a las columnas)
columnaEnTresCuartos=Funciones.columnaPosicionadaEnTresCuartos(ColumnaCentral,columnaEnUnCuarto) #mando a traer esta funcion y la guardo en la variable columnaEnTresCuartos
#Septima caracteristica: cortes del numero en la fila un cuarto de la imagen
cortesEnLaFilaUnCuarto=Funciones.cortesEnUnaFila(filaEnUnCuarto,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaFilaUnCuarto
#Octava caracteristica: pixeles del numero en la fila ubicada en un cuarto de la imagen
pixelesDelNumeroEnLaFilaUnCuarto=Funciones.pixelesDelNumeroEnUnaFila(filaEnUnCuarto,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaFilaUnCuarto
#Novena caracteristica: cortes del numero en la fila tres cuartos de la imagen
cortesEnLaFilaTresCuartos=Funciones.cortesEnUnaFila(filaEnTresCuartos,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaFilaTresCuartos
#Decima caracteristica: pixeles del numero en la fila ubicada en tres cuartos de la imagen
pixelesDelNumeroEnLaFilaTresCuartos=Funciones.pixelesDelNumeroEnUnaFila(filaEnTresCuartos,numeroDeColumnas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaFilaTresCuartos
#Onceava caracteristica: cortes del numero en la columna ubicada en un cuarto de la imagen
cortesEnLaColumnaUnCuarto=Funciones.cortesEnUnaColumna(columnaEnUnCuarto,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaColumnaUnCuarto
#Doceava caracteristica: pixeles del numero en la columna ubicada en un cuarto de la imagen
pixelesDelNumeroEnLaColumnaUnCuarto=Funciones.pixelesDelNumeroEnUnaColumna(columnaEnUnCuarto,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaColumnaUnCuarto
#Treceava caracteristica: cortes del numero en la columna ubicada en tres cuartos de la imagen
cortesEnLaColumnaTresCuartos=Funciones.cortesEnUnaColumna(columnaEnTresCuartos,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable cortesEnLaColumnaTresCuartos
#Catorceava caracteristica: pixeles del numero en la columna ubicada en tres cuartos de la imagen
pixelesDelNumeroEnLaColumnaTresCuartos=Funciones.pixelesDelNumeroEnUnaColumna(columnaEnTresCuartos,numeroDeFilas,imagenNueva) #mando a traer esta funcion y la guardo en la variable pixelesDelNumeroEnLaColumnaTresCuartos

DataSetOriginal=lecturaDelDataSet() #leo el dataset
DataSetConvertido=convertirDataSet(DataSetOriginal) #convierto el dataset a flotantes
#Calculo las distancias en el dataset
DataSetConDistancias=distancias(DataSetConvertido,relacionLargoEntreAncho,areaDelNumero,CortesEnLaFilaCentral,pixelesDelNumeroEnLaFilaCentral,cortesEnLaColumnaCentral,pixelesDelNumeroEnLaColumnaCentral,cortesEnLaFilaUnCuarto,pixelesDelNumeroEnLaFilaUnCuarto,cortesEnLaFilaTresCuartos,pixelesDelNumeroEnLaFilaTresCuartos,cortesEnLaColumnaUnCuarto,pixelesDelNumeroEnLaColumnaUnCuarto,cortesEnLaColumnaTresCuartos,pixelesDelNumeroEnLaColumnaTresCuartos)
DataSetOrdenado=datasetOrden(DataSetConDistancias) #ordeno el dataset
numeroDeVecinos=vecinos() #pido el numero de vecinos a considerar
clasificacionDeInstancia=clasificar(DataSetOrdenado,numeroDeVecinos) #clasifico el numero de vecinos
imprecion(clasificacionDeInstancia,DataSetOrdenado,numeroDeVecinos)
