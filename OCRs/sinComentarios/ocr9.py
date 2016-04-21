






























import os
import matplotlib.image as im
from PIL import Image as IM
import csv,math
from time import time








def menu():
    mensaje =  
    print(mensaje)
    repetir = 1
    while(repetir == 1):
        print("\nMenu de opciones\n1 --> Generar el archivo .csv\n2 --> Aplicar el OCR mediante KNN")
        opcion = int(input('------>  '))
        if(opcion == 1):
            path = input('Ingresa la ruta de la carpeta padre\n')
            load(path)
        elif(opcion == 2):
            knn()
        else:
            print("Ha ingresado una opcion incorrecta")
            menu()
        print("Desea ejecutar de nuevo el programa??\n1 --> Si\n2 --> No")
        repetir = int(input('---->  '))
    print("Programa finalizado, elaborado por: Roberto, Marcos\n\t\t8 B")








def load(padre):
    
    rutas = []
    
    for (path, carpetas, archivos) in os.walk(padre):
        
        for name in archivos:
            
            ruta = path+"/"+name
            rutas.append(ruta)
    leer(sorted(rutas))








def leer(rutas):
    
    inicio = time()
    archivo = input('Escribe el nombre del archivo para guardar los datos\n')
    n_archivo = archivo + ".csv"
    abrir = open(n_archivo,'w')
    csvsalida = open(n_archivo, 'w', newline='')
    escribir = csv.writer(csvsalida)
    print("Escribiendo las caracteristicas en el archivo csv")
    print("Sea paciente, este proceso puede llevar unos minutos")
    t = 0
    carpeta = -1
    for i in range(len(rutas)): 
        instancias = []
        img=im.imread(rutas[i])
        img1 = IM.open(rutas[i])
        col, filas = img1.size
        instancias.extend([(i+1),float(filas)/float(col),atr2(img,filas,col)])
        r_col = atributos(img, filas, col,True)
        r_filas = atributos(img, filas, col,False) 
        
        instancias.extend([r_col[0],r_col[1],r_col[2],r_filas[0],r_filas[1],r_filas[2],r_col[3],r_col[4],r_col[5],r_filas[3],r_filas[4],r_filas[5]])
        
        instancias.append(int(rutas[i][6]))
        
        data = [(instancias[0],instancias[1],instancias[2],instancias[3],instancias[4],instancias[5],instancias[6],instancias[7],instancias[8],instancias[9],instancias[10],instancias[11],instancias[12],instancias[13],instancias[14],instancias[15])]
        escribir.writerows(data)
        t = i+1
        if(carpeta != int(rutas[i][6])):
            carpeta +=1
            print("\nProgreso actual = escribiendo datos de la carpeta ---> "+str(rutas[i][6]))
            print("Progreso total global ---> "+str(carpeta)+str("0%"))
        
    csvsalida.close()
    fin = time()
    print("Progreso total global ---> 100%")
    tt =  ((fin - inicio)/60)
    print("\n\n#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print("------> Informacion general del dataset creado")
    print("------> Instancias escritas en el archivo "+str(t))
    print("------> Cantidad de caracteristicas de cada instancia : 16")
    print("------> Descripcion de cada caracteristica")
    descripcion =  
    
    print(descripcion)
    print("Clases : 0 --> 1 --> 2 --> 3 --> 4 --> 5 --> 6 --> 7 --> 8 --> 9")
    print("-----> Nombre del archivo csv generado "+n_archivo)
    print("\n\nTiempo de procesamiento de las imagenes =  %.2f minutos." % tt)








def atr2(img, filas, col):
    unos = 0
    for i in range(filas):
        for j in range(col):
            if(img[i][j] == 1):
                unos+=1
    return unos/(filas*col)








def atributos(img, filas, col,isCol):
    
    tam = filas*col
    
    atri1 = atri2 = atri3 = 0
    
    if(isCol == True):
        condicion_atri1 = int(col/2)
        condicion_atri2 = int(col/4)
        condicion_atri3 = int((col/4)*3)
    elif(isCol == False):
        condicion_atri1 = int(filas/2)
        condicion_atri2 = int(filas/4)
        condicion_atri3 = int((filas/4)*3)
    
    lista1 = []
    lista2 = []
    lista3 = []
    
    for i in range(filas):
        for j in range(col):
            if(isCol == True):
                if(j == condicion_atri1):
                    lista1.append(img[i][j])
                    if(img[i][j] == 1):
                        atri1+=1
                if(j == condicion_atri2):
                    lista2.append(img[i][j])
                    if(img[i][j] == 1):
                        atri2+=1
                if(j == condicion_atri3):
                    lista3.append(img[i][j])
                    if(img[i][j] == 1):
                        atri3+=1
            elif(isCol == False):
                if(i == condicion_atri1):
                    lista1.append(img[i][j])
                    if(img[i][j] == 1):
                        atri1+=1
                if(i == condicion_atri2):
                    lista2.append(img[i][j])
                    if(img[i][j] == 1):
                        atri2+=1
                if(i == condicion_atri3):
                    lista3.append(img[i][j])
                    if(img[i][j] == 1):
                        atri3+=1
    
    inicio1 = lista1[0]
    inicio2 = lista2[0]
    inicio3 = lista3[0]
    
    corte1 = corte2 = corte3 = 0
    
    if(lista1[0] == 1):
        corte1+=1
    if(lista2[0] == 1):
        corte2+=1
    if(lista3[0] == 1):
        corte3+=1
    
    if(lista1[len(lista1)-1] == 1):
        corte1+=1
    if(lista2[len(lista1)-1] == 1):
        corte2+=1
    if(lista3[len(lista1)-1] == 1):
        corte3+=1
    
    for l in range(len(lista1)):
        if(inicio1 != lista1[l]):
            inicio1 = lista1[l]
            corte1+=1
        if(inicio2 != lista2[l]):
            inicio2 = lista2[l]
            corte2+=1
        if(inicio3 != lista3[l]):
            inicio3 = lista3[l]
            corte3+=1
    atributos = [(atri1/tam), (atri2/tam), (atri3/tam), corte1, corte2, corte3]
    return atributos








def knn():
    print("Aplicando el metodo KNN para el reconocimiento de imagenes OCR")
    print("Ingrese la ruta del archivo csv")
    ruta = input('----->  ')+".csv"
    
    print("Ingrese la ruta de la imagen que desea reconocer")
    r_imagen = input('----->  ')+".png"
    r = "test/"+r_imagen
    nueva = carac_imagen(r)
    leer_data(ruta,nueva)








def carac_imagen(r_imagen):
    datos = []
    img=im.imread(r_imagen)
    img1 = IM.open(r_imagen)
    col, filas = img1.size
    datos.extend([float(filas)/float(col),atr2(img,filas,col)])
    r_col = atributos(img, filas, col,True)
    r_filas = atributos(img, filas, col,False) 
    col,filas = img1.size
    r_col = atributos(img, filas, col,True)
    r_filas = atributos(img, filas, col,False) 
    
    datos.extend([r_col[0],r_col[1],r_col[2],r_filas[0],r_filas[1],r_filas[2],r_col[3],r_col[4],r_col[5],r_filas[3],r_filas[4],r_filas[5]])
    return datos








def leer_data(ruta,x):
    read = csv.reader(open(ruta,'r'))
    datos_distancia = []
    dis = 0
    for index,row in enumerate(read):
        
        y = [float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7]),float(row[8]),float(row[9]),float(row[10]),float(row[11]),float(row[12]),float(row[13]),float(row[14])]
        dis = distancia(x,y)
        atri = []
        atri.extend([int(index+1),dis,int(row[15])])
        datos_distancia.append(atri)
    vecinos(datos_distancia,ruta)








def distancia(x,y):
    total = 0.0
    for i in range(len(x)):
        total+=((float(x[i])-float(y[i]))**2)
    return math.sqrt(total)








def vecinos(datos_distancia,ruta):
    print("Ingrese el valor de K")
    k = int(input('----->  '))
    solo_distancias = []
    for x in range(len(datos_distancia)):
        solo_distancias.append(datos_distancia[x][1])
    veci = []
    distan = sorted(solo_distancias)
    for i in range(len(distan)):
        if(i == int(k)):
            break
        else:
            veci.append(distan[i])
    contador_distancias = 1
    print("\n\n")
    lista_a_ordenar = []
    for z in range(len(datos_distancia)):
        for y in range(len(veci)):
            if(veci[y] == datos_distancia[z][1]):
                
                lista = []
                lista.extend([datos_distancia[z][0],datos_distancia[z][1],datos_distancia[z][2]])
                lista_a_ordenar.append(lista)
                contador_distancias+=1
    ordenar_distancias(lista_a_ordenar)

    
    c0 = c1 = c2 = c3 = c4 = c5 = c6 = c7 = c8 = c9 = c = 0
    read = csv.reader(open(ruta,'r'))
    for index,row in enumerate(read):
        for j in range(k):
            if(solo_distancias[c] == veci[j]):
                if(int(row[15]) == 0):
                    c0+=1
                elif(int(row[15]) == 1):
                    c1+=1
                elif(int(row[15]) == 2):
                    c2+=1
                elif(int(row[15]) == 3):
                    c3+=1
                elif(int(row[15]) == 4):
                    c4+=1
                elif(int(row[15]) == 5):
                    c5+=1
                elif(int(row[15]) == 6):
                    c6+=1
                elif(int(row[15]) == 7):
                    c7+=1
                elif(int(row[15]) == 8):
                    c8+=1
                elif(int(row[15]) == 9):
                    c9+=1
        c+=1
    
    print("\n------------------------------------------")
    print("\nInstancias de la clase 0 --> "+str(c0))
    print("Instancias de la clase 1 --> "+str(c1))
    print("Instancias de la clase 2 --> "+str(c2))
    print("Instancias de la clase 3 --> "+str(c3))
    print("Instancias de la clase 4 --> "+str(c4))
    print("Instancias de la clase 5 --> "+str(c5))
    print("Instancias de la clase 6 --> "+str(c6))
    print("Instancias de la clase 7 --> "+str(c7))
    print("Instancias de la clase 8 --> "+str(c8))
    print("Instancias de la clase 9 --> "+str(c9))
    print("\n\n")
    
    if(c0 > c1 and c0 > c2 and c0 > c3 and c0 > c4 and c0 > c5 and c0 > c6 and c0 > c7 and c0 > c8 and c0 > c9):
        print("---------------------------------------\n")
        print("La imagen ingresada es de clase  ---> 0")
    elif(c1 > c0 and c1 > c2 and c1 > c3 and c1 > c4 and c1 > c5 and c1 > c6 and c1 > c7 and c1 > c8 and c1 > c9):
        print("---------------------------------------\n")
        print("La imagen ingresada es de clase  ---> 1")
    elif(c2 > c0 and c2 > c1 and c2 > c3 and c2 > c4 and c2 > c5 and c2 > c6 and c2 > c7 and c2 > c8 and c2 > c9):
        print("---------------------------------------\n")
        print("La imagen ingresada es de clase  ---> 2")
    elif(c3 > c0 and c3 > c1 and c3 > c2 and c3 > c4 and c3 > c5 and c3 > c6 and c3 > c7 and c3 > c8 and c3 > c9):
        print("---------------------------------------\n")
        print("La imagen ingresada es de clase  ---> 3")
    elif(c4 > c0 and c4 > c1 and c4 > c2 and c4 > c3 and c4 > c5 and c4 > c6 and c4 > c7 and c4 > c8 and c4 > c9):
        print("---------------------------------------\n")
        print("La imagen ingresada es de clase  ---> 4")
    elif(c5 > c0 and c5 > c1 and c5 > c2 and c5 > c3 and c5 > c4 and c5 > c6 and c5 > c7 and c5 > c8 and c5 > c9):
        print("---------------------------------------\n")
        print("La imagen ingresada es de clase  ---> 5")
    elif(c6 > c0 and c6 > c1 and c6 > c2 and c6 > c3 and c6 > c4 and c6 > c5 and c6 > c7 and c6 > c8 and c6 > c9):
        print("---------------------------------------\n")
        print("La imagen ingresada es de clase  ---> 6")
    elif(c7 > c0 and c7 > c1 and c7 > c2 and c7 > c3 and c7 > c4 and c7 > c5 and c7 > c6 and c7 > c8 and c7 > c9):
        print("---------------------------------------\n")
        print("La imagen ingresada es de clase  ---> 7")
    elif(c8 > c0 and c8 > c1 and c8 > c2 and c8 > c3 and c8 > c4 and c8 > c5 and c8 > c6 and c8 > c7 and c8 > c9):
        print("---------------------------------------\n")
        print("La imagen ingresada es de clase  ---> 8")
    elif(c9 > c0 and c9 > c1 and c9 > c2 and c9 > c3 and c9 > c4 and c9 > c5 and c9 > c6 and c9 > c7 and c9 > c8):
        print("-----------------------------------------\n")
        print("La imagen ingresada es de clase  ---> 9")
    print("\n\n")  








def ordenar_distancias(lista):
    for z in range(len(lista)):
        for i in range(len(lista)-1):
            if(lista[i][1] > lista[i+1][1]):
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
    conta = 1
    for j in range(len(lista)):
        print("No. --> "+str(conta)+"\tinstancia --> "+str(lista[j][0])+"\tclase --> "+str(lista[j][2])+"\tdistancia --> "+str(lista[j][1]))
        conta+=1

menu()

