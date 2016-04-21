1

from PIL import Image
import matplotlib.image as mpimg
import csv
import os
import math
import operator

trainingSet = []
op = open('dataset2.csv','a',newline='')
escribir = csv.writer(op,delimiter=';')

data = []
cont = 1







def writeData(direc,clase):
    global cont 
    data = [] 
    
    img = Image.open(direc)
    img2 = mpimg.imread(direc)
    col, fil = img.size 
    data = extraccion(img2,fil,col)
    data.append(clase)
    data.append(cont)
    escribir.writerow(data)
    cont += 1






def readData(archivo):
    global data
    clasesDataset = []
    with open(archivo, newline='') as csvfile:
        lines = csv.reader(csvfile, delimiter= ';')
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(14):
                
                dataset[x][y] = float(dataset[x][y])
            clase = dataset[x][14]
            if(x == 0):
                clasesDataset.append(clase)
            if((clase in clasesDataset) == False):
                clasesDataset.append(clase)
            data.append(dataset[x])
        csvfile.close()
    return clasesDataset







def extraccion(img2,fil,col):
    area = fil*col
    mcol = int(col/4)
    mfil = int(fil/4)
    data=[]
    
    
    razon = col/fil
    data.append(razon)
    
    
    cont = 0
    for x in range(fil):
        if(img2[x][mcol*2] == 1):
            cont += 1
    razon_1_en_vec_col_2 = cont/fil
    data.append(razon_1_en_vec_col_2)
    
    
    cont = 0
    for x in range(fil):
        for z in range(col):
            if(img2[x][z] == 1):
                cont += 1
    razon_1_en_img = cont/area
    data.append(razon_1_en_img)

    
    cont = 0
    for x in range(fil):
        if(img2[x][mcol] == 1):
            cont += 1
    razon_1_en_vec_col_4 = cont/fil
    data.append(razon_1_en_vec_col_4)
    
    
    cont = 0
    for x in range(fil):
        if(img2[x][3*mcol] == 1):
            cont += 1
    razon_1_en_vec_col_3_4 = cont/fil
    data.append(razon_1_en_vec_col_3_4)
    
    
    cont = 0
    for x in range(col):
        if(img2[mfil*2][x] == 1):
            cont += 1
    razon_1_en_vec_fil_2 = cont/col
    data.append(razon_1_en_vec_fil_2)

    
    cont = 0
    for x in range(col):
        if(img2[mfil][x] == 1):
            cont += 1
    razon_1_en_vec_fil_1_4 = cont/col
    data.append(razon_1_en_vec_fil_1_4)

    
    cont = 0
    for x in range(col):
        if(img2[3*mfil][x] == 1):
            cont += 1
    razon_1_en_vec_fil_3_4 = cont/col
    data.append(razon_1_en_vec_fil_3_4)
    
    
    cortes = 0
    cortes2 = 0
    cortes3 = 0
    for x in range(fil):
        if (x == 0):
            if(img2[x][mcol*2] == 1):
                cortes += 1
            if(img2[x][mcol] == 1):
                cortes2 += 1
            if(img2[x][mcol*3] == 1):
                cortes3 += 1
        if(img2[x][mcol*2] != img2[x-1][mcol*2]):
            cortes += 1
        if(img2[x][mcol] != img2[x-1][mcol]):
            cortes2 += 1
        if(img2[x][mcol*3] != img2[x-1][mcol*3]):
            cortes3 += 1
        if(x == fil-1):
            if(img2[x][mcol*2] == 1):
                cortes += 1
            if(img2[x][mcol] == 1):
                cortes2 += 1
            if(img2[x][mcol*3] == 1):
                cortes3 += 1
    data.append(cortes)
    data.append(cortes2)
    data.append(cortes3)
    cortes4 = 0
    cortes5 = 0
    cortes6 = 0
    for x in range(col):
        if (x == 0):
            if(img2[mcol*2][x] == 1):
                cortes4 += 1
            if(img2[mcol][x] == 1):
                cortes5 += 1
            if(img2[mcol*3][x] == 1):
                cortes6 += 1
        if(img2[mcol*2][x] != img2[mcol*2][x-1] and x != 0 and x != (col-1)):
            cortes4 += 1
        if(img2[mcol][x] != img2[mcol][x-1] and x != 0 and x != (col-1)):
            cortes5 += 1
        if(img2[mcol*3][x] != img2[mcol*3][x-1] and x != 0 and x != (col-1)):
            cortes6 += 1
        if(x == col-1):
            if(img2[mcol*2][x] == 1):
                cortes4 += 1
            if(img2[mcol][x] == 1):
                cortes5 += 1
            if(img2[mcol*3][x] == 1):
                cortes6 += 1
    
    data.append(cortes4)
    data.append(cortes5)
    data.append(cortes6)
    return data






def mat(nuevo, data, tam):
	distancia = 0
	for x in range(tam):
		distancia += pow((float(nuevo[x]) - float(data[x])), 2)
	return math.sqrt(distancia)
 







def medirDistancia(nuevo,k):
	global data
	
	distancia = []
	tam = len(nuevo)-1
	for x in range(len(data)):
		dist = mat(nuevo, data[x], tam)
		distancia.append((data[x], dist))
	distancia.sort(key=operator.itemgetter(1))
	
	masCercanos = []
	for x in range(k):
         print("Linea(Instancia): "+str(distancia[x][0][15])+ " Clase: "+str(distancia[x][0][14])+" Distancia: "+str(distancia[x][1]))
         masCercanos.append(distancia[x][0])
	return masCercanos






def mayoria(vecinos):
	may = {} 
	for x in range(len(vecinos)):
		resp = vecinos[x][-2]
		if resp in may:
			may[resp] += 1
		else:
			may[resp] = 1
	print('')
	for keys,values in may.items():
		print("  Instancia de tipo: "+str(keys)+"     # "+str(values))
	clasesOrdenadas = sorted(may.items(), key=operator.itemgetter(1), reverse=True)
	return clasesOrdenadas[0][0]






def obtenerCaract(ruta):
    data = []
    img = Image.open(ruta) 
    img2 = mpimg.imread(ruta) 
    columnas, filas = img.size 
    
    data = extraccion(img2,filas,columnas)
    return data








def main():
    global data 
    print( "Menu")
    opc = 0
    opc = int(input("1.- Crear dataset\n2.- Clasificar\n  Opcion: "))
    if(opc == 1):
        cont = 0
        for base, dirs, files in os.walk('C:/Users/Rocio/Desktop/OCR2/ocrR2/data'):
            if cont > 0:
                print("Obteniendo caracteristicas de: "+str(base[len(base)-1]))
                for name in files:
                    writeData((str(base)+'/'+name),base[len(base)-1])
            cont += 1
        op.close()
        print("\nDataSet creado!")
    else:
        clases = readData('C:/Users/Rocio/Desktop/OCR2/ocrR2/dataset2.csv')
        print("          Información general")
        print("  Caracteristicas obtenidas: 14")
        print("  Clases: ")
        for i in range(len(clases)):
            print("   "+str(clases[i])+", ",end='')
            if(i%5 == 0):
                print('')
        print("  Total de clases: "+str(len(clases)))
        print("  Numero TOTAL de instancias: "+ str(len(data)))
        nuevo=[]
        vecinos = []
        ruta = 'C:/Users/Rocio/Desktop/OCR2/ocrR2/test/'
        ruta += input("Nombre de la imagen: ")
        nuevo = obtenerCaract(ruta)
        k = int(input("\n      Ingresa el número K: "))
        vecinos = medirDistancia(nuevo,k)
        resultado = mayoria(vecinos) 
        print("\n 	Esta imagen se clasifica como: "+ str(resultado))

main()
    
