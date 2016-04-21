1# -*- coding: utf-8 -*-

from PIL import Image#Libreria para importar imagenes
import matplotlib.image as mpimg#libreria para leer imagenes
import csv#Libreria para abrir archivos
import os#libreria para la interaccion con el sistemaa operativo
import math#libreria para hacer operaciones matematicas
import operator#exporta conjunto de funciones

trainingSet = []#se crea la variables de un arreglo
op = open('dataset2.csv','a',newline='')#crea un archivo
escribir = csv.writer(op,delimiter=';')#lo que vaya leyende se delimita con el ;

data = []#se crea la variable del dataset
cont = 1#se cra la variable del contador

# Metodo: writeData
# Parametros: ruta del archivo, clase de la instancia recibida
# Retorno: noAplica
# Funcionamiento:
#   Abre la imagen que se le pasa, obteniene las caracteristicas de cada imagen que recibe
#   y las escribe en el dataset
def writeData(direc,clase):#funcion scribir data
    global cont #se usara la variable global cont
    data = [] #se usa la variable de el dataset
    #abrimos imagen
    img = Image.open(direc)#abrir imagen
    img2 = mpimg.imread(direc)#leemos la imagen
    col, fil = img.size #obtiene las filas y las columnsas
    data = extraccion(img2,fil,col)#guarda los datos del dataset en la variable data
    data.append(clase)#inserta la clase en el arreglo data
    data.append(cont)#contador para saber el numero de lina de la instancia
    escribir.writerow(data)#se escribe en el data
    cont += 1#se incrementa contador para numerar la siguiente linea a escribir

# Metodo: readData
# Parametros: ruta del archivo a abrir
# Retorno: clases en el dataset
# Funcionamiento:
#   Abre el archivo que se le pasa, lo lee y lo guarda en el array "data"
def readData(archivo):#funcion para leer un dataset para clasificar imagen
    global data#se usara la variable global data
    clasesDataset = []#se crea la clase para el dataset
    with open(archivo, newline='') as csvfile:#abrir el archivo .csv
        lines = csv.reader(csvfile, delimiter= ';')#lee el archivo .csv
        dataset = list(lines)#lista los elemntos del dataset en una matriz
        for x in range(len(dataset)-1):#recorrido del dataset en x
            for y in range(14):#recorrido del dataset en y
                #print(dataset[x][y])
                dataset[x][y] = float(dataset[x][y])#convierte los strings en floats
            clase = dataset[x][14]#se obtiene la clase
            if(x == 0):#por default la primera clase se guarda
                clasesDataset.append(clase)#se inserta en el array clases
            if((clase in clasesDataset) == False):#se busca que no este la clase en el arreglo clases
                clasesDataset.append(clase)#si no esta, se inserta
            data.append(dataset[x])#se inserta instancia en data
        csvfile.close()#se cierra lectura del archivo
    return clasesDataset#retorna las clases encontradas



# Parametros: imagen iterable, filas de la imagen y columnas
# Retorno: arreglo con todas las caracteristicas extraidas, data[]
# Funcionamiento:
#    Obtiene 14 caracteristicas de cada imagen que recibe
def extraccion(img2,fil,col):#extracion de una imagen, filas y columnas
    area = fil*col# Metodo: extraccion
    mcol = int(col/4)#División de columnas 
    mfil = int(fil/4)#División de filas
    data=[]#arreglo para insertar en el dataset
    
    #caracteristica 1 razon de columnas/filas
    razon = col/fil#razón de filas y columnas
    data.append(razon)#se inserta caracteristica
    
    #caracteristica 2      1's/tamaño vector col/2
    cont = 0#contador
    for x in range(fil):#for que recorre vector de forma vertical
        if(img2[x][mcol*2] == 1):#compara si el pixel tiene valor 1
            cont += 1#si la condicion se cumple se incrementa
    razon_1_en_vec_col_2 = cont/fil#se calcula la razon de 1s en el vector
    data.append(razon_1_en_vec_col_2)#se inserta caracteristica en el arreglo data
    
    #caracteristica 3    1's/tamaño de la imagen filxcol
    cont = 0#contador
    for x in range(fil):#recorrido de la imagen en x
        for z in range(col):#recoriido de la imagen y    TIPO MATRIZ
            if(img2[x][z] == 1):#compara si el pixel tiene valor 1
                cont += 1#si la condicion se cumple se incrementa
    razon_1_en_img = cont/area#se calcula la razon 1s/area de la imagen
    data.append(razon_1_en_img)#se inserta caracteristica

    #caracteristica 4      1's/tamaño vector col/4
    cont = 0#contador
    for x in range(fil):#recorrido de vector vertical
        if(img2[x][mcol] == 1):#compara si el pixel tiene valor 1
            cont += 1#si la condicion se cumple se incrementa
    razon_1_en_vec_col_4 = cont/fil#se calcula razon 1s/tam del vector
    data.append(razon_1_en_vec_col_4)#se inserta caracteristica
    
    #caracteristica 5      1's/tamaño vector 3(col/2)
    cont = 0#contador
    for x in range(fil):#recorrido de vector vertical
        if(img2[x][3*mcol] == 1):#compara si el pixel tiene valor 1
            cont += 1#si la condicion se cumple se incrementa
    razon_1_en_vec_col_3_4 = cont/fil#se calcula razon 1s/tam del vector
    data.append(razon_1_en_vec_col_3_4)#se inserta caracteristica
    
    #caracteristica 6  1's/tamanño vector fil/2
    cont = 0#contador
    for x in range(col):#recorrido de vector horizontal
        if(img2[mfil*2][x] == 1):#compara si el pixel tiene valor 1
            cont += 1#si la condicion se cumple se incrementa
    razon_1_en_vec_fil_2 = cont/col#se calcula razon 1s/tam del vector
    data.append(razon_1_en_vec_fil_2)#inserta en el arreglo data

    #caracteristica 7 1's/tamaño vector fil/4
    cont = 0#contador
    for x in range(col):#recorrido de vector horizontal
        if(img2[mfil][x] == 1):#compara si el pixel tiene valor 1
            cont += 1#si la condicion se cumple se incrementa
    razon_1_en_vec_fil_1_4 = cont/col#se calcula razon 1s/tam del vector
    data.append(razon_1_en_vec_fil_1_4)#se inserta caracteristica

    #caracteristica 8 1's/tamaño vector 3(fil/4)
    cont = 0#contador
    for x in range(col):#recorrido de vector horizontal
        if(img2[3*mfil][x] == 1):#compara si el pixel tiene valor 1
            cont += 1#si la condicion se cumple se incrementa
    razon_1_en_vec_fil_3_4 = cont/col#se calcula razon 1s/tam del vector
    data.append(razon_1_en_vec_fil_3_4)#se inserta caracteristica
    
    #se obtienen los cortes de laimagen
    cortes = 0#contador de corte 1/2
    cortes2 = 0#contador de corte 1/4
    cortes3 = 0#contador de corte 3/4
    for x in range(fil):#cortes verticales
        if (x == 0):#se valida primera pos del vector
            if(img2[x][mcol*2] == 1):#col/2#compara si el pixel tiene valor 1
                cortes += 1#si la condicion se cumple se incrementa
            if(img2[x][mcol] == 1):#col/4#compara si el pixel tiene valor 1
                cortes2 += 1#si la condicion se cumple se incrementa
            if(img2[x][mcol*3] == 1):#col 3/4#compara si el pixel tiene valor 1
                cortes3 += 1#si la condicion se cumple se incrementa
        if(img2[x][mcol*2] != img2[x-1][mcol*2]):#col/2
            cortes += 1#si la condicion se cumple se incrementa
        if(img2[x][mcol] != img2[x-1][mcol]):#col/4
            cortes2 += 1#si la condicion se cumple se incrementa
        if(img2[x][mcol*3] != img2[x-1][mcol*3]):#col 3/4
            cortes3 += 1#si la condicion se cumple se incrementa
        if(x == fil-1):#se valida ultima pos del vector
            if(img2[x][mcol*2] == 1):#col/2#compara si el pixel tiene valor 1
                cortes += 1#si la condicion se cumple se incrementa
            if(img2[x][mcol] == 1):#col/4#compara si el pixel tiene valor 1
                cortes2 += 1#si la condicion se cumple se incrementa
            if(img2[x][mcol*3] == 1):#col 3/2#compara si el pixel tiene valor 1
                cortes3 += 1#si la condicion se cumple se incrementa
    data.append(cortes)#se inserta caracteristica
    data.append(cortes2)#se inserta caracteristica
    data.append(cortes3)#se inserta caracteristica
    cortes4 = 0#contador de corte 1/2
    cortes5 = 0#contador de corte 1/4
    cortes6 = 0#contador de corte 3/4
    for x in range(col):#cortes horizontales
        if (x == 0):#se valida pos 0 del vector
            if(img2[mcol*2][x] == 1):#fil/2#compara si el pixel tiene valor 1
                cortes4 += 1#si la condicion se cumple se incrementa
            if(img2[mcol][x] == 1):#fil/4#compara si el pixel tiene valor 1
                cortes5 += 1#si la condicion se cumple se incrementa
            if(img2[mcol*3][x] == 1):#fil 3/4#compara si el pixel tiene valor 1
                cortes6 += 1#si la condicion se cumple se incrementa
        if(img2[mcol*2][x] != img2[mcol*2][x-1] and x != 0 and x != (col-1)):#fil/2
            cortes4 += 1#si la condicion se cumple se incrementa
        if(img2[mcol][x] != img2[mcol][x-1] and x != 0 and x != (col-1)):#fil/4
            cortes5 += 1#si la condicion se cumple se incrementa
        if(img2[mcol*3][x] != img2[mcol*3][x-1] and x != 0 and x != (col-1)):#fil 3/4
            cortes6 += 1#si la condicion se cumple se incrementa
        if(x == col-1):#se valida ultima pos del vector
            if(img2[mcol*2][x] == 1):#fil/2#compara si el pixel tiene valor 1
                cortes4 += 1#si la condicion se cumple se incrementa
            if(img2[mcol][x] == 1):#fil/4#compara si el pixel tiene valor 1
                cortes5 += 1#si la condicion se cumple se incrementa
            if(img2[mcol*3][x] == 1):#fil 3/4#compara si el pixel tiene valor 1
                cortes6 += 1#si la condicion se cumple se incrementa
    
    data.append(cortes4)#se inserta caracteristica
    data.append(cortes5)#se inserta caracteristica
    data.append(cortes6)#se inserta caracteristica
    return data#se retorna arreglo con todas las caracteristicas

# Metodo: mat
# Parametros: nueva instancia, dataset, tamaño
# Retorno: distancia entre dos instancias
# Funcionamiento:
#   mide la distancia euclidiana entre las dos instancias recibidas
def mat(nuevo, data, tam):#aqui se mide la distancia
	distancia = 0#distancia
	for x in range(tam):#for para definir tamaño
		distancia += pow((float(nuevo[x]) - float(data[x])), 2)#numeros flotantes con el nuevo dato 
	return math.sqrt(distancia)#regresa la operacion de la distancia
 

# Metodo: medirDistancia
# Parametros: nueva instancia y el numero K
# Retorno: array con los vecinos mas cercanos
# Funcionamiento:
#   Mide la distancia entre la nueva instancia con cada elemento del dataset, ordena estos datos
#   de menor a mayor y devuelve solo los K más cercanos a la nueva instancia
def medirDistancia(nuevo,k):#inicia el metodo para medir la distancia
	global data#se hace uso de la variable global data que tiene el dataset
	#aqui se obtienen los vecinos mas cercanos
	distancia = []#arreglo que guardara las instancias con su distancia
	tam = len(nuevo)-1#tamaño de caracteristicas que se mediran
	for x in range(len(data)):#for que recorre el dataset
		dist = mat(nuevo, data[x], tam)#se mide distancia de la nueva instancia y el dataset en pos "x"
		distancia.append((data[x], dist))#se guarda instancia con su distancia
	distancia.sort(key=operator.itemgetter(1))#ordena de menor a mayor en distancia
	#print(distancia)
	masCercanos = []#arreglo que guardara los k vecinos mas cercanos
	for x in range(k):#for que recorre hasta K
         print("Linea(Instancia): "+str(distancia[x][0][15])+ " Clase: "+str(distancia[x][0][14])+" Distancia: "+str(distancia[x][1]))
         masCercanos.append(distancia[x][0])#se guarda el k vecino mas cercano
	return masCercanos#se retornan los k vecinos mas cercanos

# Metodo: mayoria
# Parametros: array con los vecinos mas cercanos
# Retorno: caracteristicas de la imagen
# Funcionamiento:
#   Obteniene las caracteristicas de la imagen que se le pase en la ruta
def mayoria(vecinos):
	may = {} #diccionario de datos donde se guardan el numero de aceptados o denegados
	for x in range(len(vecinos)):#for que recorre el arreglo de vecinos mas cercanos
		resp = vecinos[x][-2]#se obtiene la clase de la instancia en "x"
		if resp in may:#se busca si en el diccionario may se encuentra la clase actual
			may[resp] += 1#si esta se incrementa su contador
		else:#si no
			may[resp] = 1#si no esta, se guarda con conador en 1
	print('')#imprime
	for keys,values in may.items():#recorrido para las impresiones
		print("  Instancia de tipo: "+str(keys)+"     # "+str(values))#Imprime de que tipo es la instancia
	clasesOrdenadas = sorted(may.items(), key=operator.itemgetter(1), reverse=True)#ordena de mayor a menor para regresar la clase mayor
	return clasesOrdenadas[0][0]#se retorna la clase mayor

# Metodo: obtenerCaract
# Parametros: ruta
# Retorno: caracteristicas de la imagen
# Funcionamiento:
#   Obteniene las caracteristicas de la imagen que se le pase en la ruta
def obtenerCaract(ruta):#obtiene la ruta para la carateristicas
    data = []#se declara arreglo para guardar las caaracteristicas
    img = Image.open(ruta) #Abre imagne
    img2 = mpimg.imread(ruta) #Abre imagen
    columnas, filas = img.size #Se obtienen las filas y columnas
    #Se insertan datos en el array data
    data = extraccion(img2,filas,columnas)#extraccion de caracteristicas
    return data#regresa el dato

# Metodo: main
# Parametros: ninguno
# Retorno: ninguno
# Funcionamiento:
#    controla el funcionamiento del programa, recorre el directorio
#    y los archivos a procesar, llama al metodo obtenerCaract para
#    crear el dataset
def main():#metodo main
    global data #se dice que se usara la variable global data
    print( "Menu")#se imprime menú
    opc = 0#la variable opc se inicia en 0
    opc = int(input("1.- Crear dataset\n2.- Clasificar\n  Opcion: "))#se imprime la primera opcion
    if(opc == 1):#if de opcion cuando es =1
        cont = 0#el contador se inicia en 0
        for base, dirs, files in os.walk('C:/Users/Rocio/Desktop/OCR2/ocrR2/data'):#liga de donde se localiza la carpeta
            if cont > 0:#if cuando el contador es mayor a 0
                print("Obteniendo caracteristicas de: "+str(base[len(base)-1]))#imprime un mensaje que indica que se estan obteniendo las caracteristicas
                for name in files:#nombre del archivo
                    writeData((str(base)+'/'+name),base[len(base)-1])#escribe el dato
            cont += 1#el contador se inicia en 1
        op.close()#se cierra la escritura
        print("\nDataSet creado!")#se imprime mensaje de creacion del dataset
    else:#si no
        clases = readData('C:/Users/Rocio/Desktop/OCR2/ocrR2/dataset2.csv')#dataset que abre
        print("          Información general")#se imprime información general
        print("  Caracteristicas obtenidas: 14")#se imprimen caracteristicas
        print("  Clases: ")#se imprimen clases
        for i in range(len(clases)):#inicializa for para las clases
            print("   "+str(clases[i])+", ",end='')#se imprime la clase
            if(i%5 == 0):#cada 5 calses da un salto de linea
                print('')#salto de linea
        print("  Total de clases: "+str(len(clases)))#Imprime el numero total de clases
        print("  Numero TOTAL de instancias: "+ str(len(data)))#imprime el numero total de instancias
        nuevo=[]#arreglo nuevo
        vecinos = []#arreglo vecinos
        ruta = 'C:/Users/Rocio/Desktop/OCR2/ocrR2/test/'#ruta de la carpeta con las imagenes de prueba
        ruta += input("Nombre de la imagen: ")#nombre de la imagen que desea sacar las caracteristicas
        nuevo = obtenerCaract(ruta)#pedimos las caracteristicas de la nueva instancia
        k = int(input("\n      Ingresa el número K: "))#Ingresar el numero de los k vecinos
        vecinos = medirDistancia(nuevo,k)#se mide distancia con los elementos del data set
        resultado = mayoria(vecinos) #si K>1 se hace una votacion para decidir la clasificacion
        print("\n 	Esta imagen se clasifica como: "+ str(resultado))#Se imprime el resultado

main()#metodo main
    