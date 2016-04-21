import matplotlib.image as mpimagen#Se importa la libreria image como mpimagen.
import csv#Importa la libreria para la creación de archivos csv.
import os#De la libreria os se importa la función walk

#Calcular_dimenciones()
#Mediante la función de .shape se obtienen las dimensiones de la imagen.
#A la variable dimenciones 
def Calcular_dimenciones(imagen):
    #Calcula la dimención de la imagen
    dimenciones=imagen.shape#Se le asigna a la variable "dimenciones" el tamaño de la imagen mediante la función .shape la cual devuelve las dimensiones de la imagen.
    #print('Dimenciones',dimenciones)#Se imprime la variable "dimenciones".
    return dimenciones

#Razon
#Se optiene la razon de filas entre columnas.
#Se realiza la división de las filas entre las columnas para obtener la razon de la imagen.
def Razon(dimenciones):
    razon=dimenciones[0]/dimenciones[1]#A la variable "razon" se le asigna lo obtenido de la división de dimenciones[0] (columnas) y dimenciones[1] (filas)
    #print('Razon: ',razon)#Se imprime la variable "razon".
    return razon

#pixeles_blancosNegro()
#Se contabiliza el numero de imageneles negros y el numero de imageneles pixeles_blancoss 
#encontrados en la imagen.
#Se compara la variable "imagen" en las posiciones "i" y en "j" si es diferente de cero.
#la variable pixeles_blancos aumenta, sino la variable negro aumenta haciendo asi el conteo de
#ambos dentro de toda la imagen.
#Puntos pixeles_blancoss y negros.
def Pixeles_blancos(imagen,dimenciones):        
    pixeles_blancos=0#Se inicializa la variabe "pixeles_blancos".
    for i in range(0,dimenciones[0]):#Primer ciclo for recorre las columnas de la imagen.
        for j in range(0,dimenciones[1]):#Segndo ciclo for recorre las filas de la imagen.
            if (imagen[i][j]!=0):#Comparación de la variable "imagen" en las posiciones "i" y "j" si es diferente de cero.
                pixeles_blancos=pixeles_blancos+1#Aumento de la variable si "imagen[i][j]" es diferente de cero.
    #print('Area: ',pixeles_blancos)#Se imprime la variable puntos a la cual se le asigno previamente ek valor de la división de las variables pixeles_blancos y negro.
    return pixeles_blancos

#Numero_De_Pixeles_Que_Representan_La_Imagen()
#Se recorre la imagen desde distintas posiciones para verificar 
#el numero de ceros y unos que tiene la misma en esa linea.
#Las variables dimenciones[0] y dimenciones[1] representan filas y columnas de la imagen.
#La variable "mc" esta representando una posicion especifica de las columnas en la imagen.
#La variable "mf" esta representando una posicion especifica de las filas de la imagen.
#imagen es la variable a la que se le asigno los valores de la imagne que se carga previamente.
def Numero_De_Pixeles_Que_Representan_La_Imagen(imagen,dimensiones):
    #Corte a la mitad de la imagen horizontalmente
    cont1=0
    fila_horizontal_mitad_pixeles=int(dimensiones[0]/2)#A fila_horizontal_mitad_pixeles se le asigna el valor de un entero obtenido por la divicion de dimensiones entre 2.
    for i in range(0,dimensiones[1]):#Ciclo for que recorre la columnas.
        #imagen_rayada[fila_horizontal_mitad_pixeles,i]=1
        if(imagen[fila_horizontal_mitad_pixeles][i]!=0):
            cont1=cont1+1
    cont1=cont1/dimensiones[1]
    #print(cont1)#Se imprimen los valores obtenidos en las variables "i" hasta "mcm".    
    
    #Corte a un cuarto de la imagen horizontalmente
    cont2=0
    fila_horizontal_un_cuarto_pixeles=int(fila_horizontal_mitad_pixeles/2)#A fila_horizontal_un_cuarto_pixeles se le asigna el valor de un entero obtenido por la divicion fila_horizontal_mitad_pixeles entre 2.
    for i in range(0,dimensiones[1]):#Ciclo for que recorre la columnas.
        #imagen_rayada[fila_horizontal_un_cuarto_pixeles,i]=1
        if(imagen[fila_horizontal_un_cuarto_pixeles][i]!=0):
            cont2=cont2+1
    cont2=cont2/dimensiones[1]
    #print(cont2)#Se imprimen los valores obtenidos en las variables "i" hasta "mcc".

    #Corte a tres cuartos de la imagen horizontalmente
    cont3=0
    fila_horizontal_tres_cuartos_pixeles=int(fila_horizontal_mitad_pixeles+fila_horizontal_un_cuarto_pixeles)#A mc3c (matriz columnas a tres cuartos) se le asigna el valor de un entero optenido por la suma de fila_horizontal_mitad_pixeles mas fila_horizontal_un_cuarto_pixeles.
    for i in range(0,dimensiones[1]):#Ciclo for que recorre la columnas.
        #imagen_rayada[fila_horizontal_tres_cuartos_pixeles,i]=1
        if(imagen[fila_horizontal_tres_cuartos_pixeles][i]!=0):
            cont3=cont3+1
    cont3=cont3/dimensiones[1]
    #print(cont3)#Se imprimen los valores obtenidos en las variables "i" hasta "mc3c".
        
#Inicia vertical.
    #Corte a la mitad de la imagen verticalmente
    cont4=0
    columna_vertical_mitad_pixeles=int(dimensiones[1]/2)#A columna_vertical_mitad_pixeles se le asigna el valor de un entero obtenido por la divicion de dimensiones entre 2.
    for i in range(0,dimensiones[0]):#Ciclo for que recorre la columnas.
        #imagen_rayada[i,columna_vertical_mitad_pixeles]=1
        if(imagen[i][columna_vertical_mitad_pixeles]!=0):
            cont4=cont4+1
    cont4=cont4/dimensiones[0]
    #print(cont4)#Se imprimen los valores obtenidos en las variables "i" hasta "mfm".

    #Corte a un cuarto de la imagen verticalmente
    cont5=0
    columna_vertical_un_cuarto_pixeles=int(columna_vertical_mitad_pixeles/2)#A columna_vertical_un_cuarto_pixeles se le asigna el valor de un entero obtenido por la divicion fila_vertical_mitad_pixeles entre 2.
    for i in range(0,dimensiones[0]):#Ciclo for que recorre la columnas.
        #imagen_rayada[i,columna_vertical_un_cuarto_pixeles]=1
        if(imagen[i][columna_vertical_un_cuarto_pixeles]!=0):
            cont5=cont5+1
    cont5=cont5/dimensiones[0]
    #print(cont5)#Se imprimen los valores obtenidos en las variables "i" hasta "mfc".
    
    #Corte a tres cuartos de la imagen verticalmente
    cont6=0
    columna_vertical_tres_cuartos_pixeles=int(columna_vertical_mitad_pixeles+columna_vertical_un_cuarto_pixeles)#A columna_vertical_tres_cuartos_pixeles se le asigna el valor de un entero obtenido por la suma de columna_vertical_mitad_pixeles mas columna_vertical_un_cuarto_pixeles.
    for i in range(0,dimensiones[0]):#Ciclo for que recorre la columnas.
        #imagen_rayada[i,columna_vertical_tres_cuartos_pixeles]=1
        if(imagen[i][columna_vertical_tres_cuartos_pixeles]!=0):
            cont6=cont6+1
    cont6=cont6/dimensiones[0]
    #print(cont6)#Se imprimen los valores obtenidos en las variables "i" hasta "mf3c".
    return cont1,cont2,cont3,cont4,cont5,cont6
    
#Cambios_En_La_Imagen()
#Se contabiliza el numero de cambios ue sufre la imagen al ser recorrida (ceros y unos)
#Se usa un contador el cual nos permite saber cuando se hace un corte en la imagen.
#En la variable "mc" se obtiene la posición en la imagen mediane la división.
#La variable "x" se usa para comparar.
#La variable "imagen" contiene la matriz de la imagen.

def Cambios_en_la_imagen(imagen,dimenciones):
    #Cambios a la mitad de la imagen horizontalmente
    cont7=0#Se inicializa el contador en cero.
    fila_horizontal_mitad_cortes=int(dimenciones[0]/2)#A la variable fila_horizontal_mitad_cortes se le asigna el valor de la división de dimenciones[0] entre 2.
    x=imagen[fila_horizontal_mitad_cortes,0]#A la variable x se le agrega el valor de las posiciones fila_horizontal_mitad_cortes y 0.
    for i in range(0,dimenciones[1]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[fila_horizontal_mitad_cortes,i]=1
        if (imagen[fila_horizontal_mitad_cortes,i]!=x):#Se hace la comparación de imagen en la posición fila_horizontal_mitad_cortes, i si es diferente de x.
            cont7=cont7+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[fila_horizontal_mitad_cortes,i]#a la variable x se le asigna el valor de imagen en la posición fila_horizontal_mitad_cortes,i.
    #print(cont7)#Se imprime el valor de la variable cont.       
    
    #Cambios a un cuarto de la imagen horizontalmente
    cont8=0#Se inicializa el contador en cero.
    fila_horizontal_un_cuarto_cortes=int(fila_horizontal_mitad_cortes/2)#A la variable fila_horizontal_un_cuarto_cortes se le asigna el valor de la división de fila_horizontal_mitad_cortes entre 2.
    x=imagen[fila_horizontal_un_cuarto_cortes,0]#A la variable x se le agrega el valor de las posiciones mcc y 0.
    for i in range(0,dimenciones[1]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[fila_horizontal_un_cuarto_cortes,i]=1
        if (imagen[fila_horizontal_un_cuarto_cortes,i]!=x):#Se hace la comparación de imagen en la posición fila_horizontal_mitad_cortes, i si es diferente de x.
            cont8=cont8+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[fila_horizontal_un_cuarto_cortes,i]#a la variable x se le asigna el valor de imagen en la posición fila_horizontal_mitad_cortes,i.
    #print(cont8)#Se imprime el valor de la variable cont.        

    #Cambios a tres cuartos de la imagen horizontalmente
    cont9=0#Se inicializa el contador en cero.
    fila_horizontal_tres_cuartos_cortes=int(fila_horizontal_mitad_cortes+fila_horizontal_un_cuarto_cortes)#A la variable fila_horizontal_un_cuarto_cortes se le asigna el valor de la suma de fila_horizontal_mitad_cortes mas fila_horizontal_tres_cuartos_cortes para obtener la posicion en tres cuartos.
    x=imagen[fila_horizontal_tres_cuartos_cortes,0]#A la variable x se le agrega el valor de las posiciones fila_horizontal_tres_cuartos_cortes y 0.
    for i in range(0,dimenciones[1]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[fila_horizontal_tres_cuartos_cortes,i]=1
        if (imagen[fila_horizontal_tres_cuartos_cortes,i]!=x):#Se hace la comparación de imagen en la posición fila_horizontal_tres_cuartos_cortes, i si es diferente de x.
            cont9=cont9+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[fila_horizontal_un_cuarto_cortes,i]#a la variable x se le asigna el valor de imagen en la posición fila_horizontal_tres_cuartos_cortes,i.
    #print(cont9)#Se imprime el valor de la variable cont.

#Comienzan verticales

    #Cambios a la mitad de la imagen verticalmente
    cont11=0#Se inicializa el contador en cero.
    columna_vertical_mitad_cortes=int(dimenciones[1]/2)#A la variable columna_vertical_mitad_cortes se le asigna el valor de la división de dimenciones[1] entre 2.
    x=imagen[columna_vertical_mitad_cortes,0]#A la variable x se le agrega el valor de las posiciones columna_vertical_mitad_cortes y 0.
    for i in range(0,dimenciones[0]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[i,columna_vertical_mitad_cortes]=1
        if (imagen[i,columna_vertical_mitad_cortes]!=x):#Se hace la comparación de imagen en la posición columna_vertical_mitad_cortes,i si es diferente de x.
            cont11=cont11+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[i,columna_vertical_mitad_cortes]#a la variable x se le asigna el valor de imagen en la posición i,columna_vertical_mitad_cortes.
    #print(cont11)#Se imprime el valor de la variable cont.    
    
    #Cambios a un cuarto de la imagen verticalmente
    cont10=0#Se inicializa el contador en cero.
    columna_vertical_un_cuarto_cortes=int(columna_vertical_mitad_cortes/2)#A la variable columna_vertical_un_cuarto_cortes se le asigna el valor de la división de columna_vertical_mitad_cortes entre 2.
    x=imagen[columna_vertical_un_cuarto_cortes,0]#A la variable x se le agrega el valor de las posiciones mfc y 0.
    for i in range(0,dimenciones[0]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[i,mf]=1
        if (imagen[i,columna_vertical_un_cuarto_cortes]!=x):#Se hace la comparación de imagen en la posición mfc,i si es diferente de x.
            cont10=cont10+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[i,columna_vertical_un_cuarto_cortes]#a la variable x se le asigna el valor de imagen en la posición i,mfc.
    #print(cont10)#Se imprime el valor de la variable cont.

    #Cambios a tres cuartos de la imagen verticalmente
    cont12=0#Se inicializa el contador en cero.
    columna_vertical_tres_cuartos_cortes=int(columna_vertical_mitad_cortes+columna_vertical_un_cuarto_cortes)#A la variable columna_vertical_tres_cuartos_cortes se le asigna el valor de la suma de columna_vertical_mitad_cortes mas columna_vertical_un_cuarto_cortes para obtener la posicion en tres cuartos.
    x=imagen[columna_vertical_tres_cuartos_cortes,0]#A la variable x se le agrega el valor de las posiciones columna_vertical_tres_cuartos_cortes y 0.
    for i in range(0,dimenciones[0]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[i,columna_vertical_tres_cuartos_cortes]=1
        if (imagen[i,columna_vertical_tres_cuartos_cortes]!=x):#Se hace la comparación de imagen en la posición columna_vertical_tres_cuartos_cortes,i si es diferente de x.
            cont12=cont12+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[i,columna_vertical_tres_cuartos_cortes]#a la variable x se le asigna el valor de imagen en la posición i,columna_vertical_tres_cuartos_cortes.
    #print(cont12)#Se imprime el valor de la variable cont.    

    #imagenplot = plt.imshow(imagen_rayada)#La variable imagenplot sirve para imprimir la imagen previamente cargada.

    return cont7,cont8,cont9,cont10,cont11,cont12

#Escritura_CSV
#Escribe en el archivo csv que se creo previamente con los datos obtenidos de la imagen
#como son los cortes, los cambios, etc.
#Se lee la imagen
def Escritura_CSV():
    archivo_CSV=open('DataSet.csv','w', newline='')#Se abre un archivo csv y se indica la escritura del mismo.
    salida_CSV= csv.writer(archivo_CSV)#Se transfiere un archivo a la variable "salida".
    clase=-1
    contador=0
    carpeta='imagenes'
    numero=-1
    for path, ficheros, archivos in os.walk(carpeta):
        for fname in archivos:
            nombre=path+'/'+fname
            imagen = mpimagen.imread(nombre)#Se importa la imagen a la variable.
            #imagen_rayada = mpimagen.imread(nombre)#Se importa la imagen a la variable.
            dimenciones=Calcular_dimenciones(imagen)
            razon=Razon(dimenciones)
            pixeles_blancos=Pixeles_blancos(imagen,dimenciones)
            cont1,cont2,cont3,cont4,cont5,cont6=Numero_De_Pixeles_Que_Representan_La_Imagen(imagen,dimenciones)
            cont7,cont8,cont9,cont10,cont11,cont12=Cambios_en_la_imagen(imagen,dimenciones)
            salida_CSV.writerow([razon,pixeles_blancos,cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9,cont10,cont11,cont12,clase])
            contador=contador+1
        clase=clase+1
        numero=numero+1
        if(numero<=9):
            print('Generando clase: ',numero)
    print('\n ¡ DataSet completado con exito !\n')
    archivo_CSV.close()

Escritura_CSV()


#import matplotlib.pyplot as plt#Se importa la libreria pyplot como plt.
import matplotlib.image as mpimagen#Se importa la libreria image como mpimagen.
import csv
import math
f= open('DataSet.csv')#A la variable f se le indica la apertura del archivo csv.
lns=csv.reader(f)#A la variable lns se le asignan lo leido del archivo csv de la variable f
dataset=list(lns)#A la variable dataset se le asigna en forma de matriz los valores de lns.

print('Nombre de la imagen: ',end="")#Pide el nombre del archivo imagen.
nombreimagen=input()#A la variable nombreimagen se le asigna lo ingresado por el teclado.
imagen = mpimagen.imread(nombreimagen)#Se importa la imagen a la variable.

print('Numero de vecinos a conciderar: ',end="")#Imprime la solicitud de los vecinos.
k=int(input())#A la variable k se le asigna lo ingresado por el teclado.

#Calcular_dimensiones()
#Mediante la función de .shape se obtienen las dimensiones de la imagen.
#A la variable dimensiones 
def Calcular_dimensiones(imagen):
    #Calcula la dimención de la imagen
    dimensiones=imagen.shape#Se le asigna a la variable "dimensiones" el tamaño de la imagen mediante la función .shape la cual devuelve las dimensiones de la imagen.
    return dimensiones

#Razon
#Se optiene la razon de filas entre columnas.
#Se realiza la división de las filas entre las columnas para obtener la razon de la imagen.
def Razon(dimensiones):
    razon=dimensiones[0]/dimensiones[1]#A la variable "razon" se le asigna lo obtenido de la división de dimensiones[0] (columnas) y dimensiones[1] (filas)
    return razon

#pixeles_blancosNegro()
#Se contabiliza el numero de imageneles negros y el numero de imageneles pixeles_blancos.
#encontrados en la imagen.
#Se compara la variable "imagen" en las posiciones "i" y en "j" si es diferente de cero.
#la variable pixeles_blancos aumenta, sino la variable negro aumenta haciendo asi el conteo de
#ambos dentro de toda la imagen.
#Puntos pixeles_blancoss y negros.
def Pixeles_blancos(imagen,dimensiones):        
    pixeles_blancos=0#Se inicializa la variabe "pixeles_blancos".
    for i in range(0,dimensiones[0]):#Primer ciclo for recorre las columnas de la imagen.
        for j in range(0,dimensiones[1]):#Segndo ciclo for recorre las filas de la imagen.
            if (imagen[i][j]!=0):#Comparación de la variable "imagen" en las posiciones "i" y "j" si es diferente de cero.
                pixeles_blancos=pixeles_blancos+1#Aumento de la variable si "imagen[i][j]" es diferente de cero.
    return pixeles_blancos

#Numero_De_Pixeles_Que_Representan_La_Imagen()
#Se recorre la imagen desde distintas posiciones para verificar 
#el numero de ceros y unos que tiene la misma en esa linea.
#Las variables dimensiones[0] y dimensiones[1] representan filas y columnas de la imagen.
#La variable "mc" esta representando una posicion especifica de las columnas en la imagen.
#La variable "mf" esta representando una posicion especifica de las filas de la imagen.
#imagen es la variable a la que se le asigno los valores de la imagne que se carga previamente.
def Numero_De_Pixeles_Que_Representan_La_Imagen(imagen,dimensiones):
    #Corte a la mitad de la imagen horizontalmente
    cont1=0
    fila_horizontal_mitad_pixeles=int(dimensiones[0]/2)#A fila_horizontal_mitad_pixeles se le asigna el valor de un entero obtenido por la divicion de dimensiones entre 2.
    for i in range(0,dimensiones[1]):#Ciclo for que recorre la columnas.
        #imagen_rayada[fila_horizontal_mitad_pixeles,i]=1
        if(imagen[fila_horizontal_mitad_pixeles][i]!=0):
            cont1=cont1+1
    cont1=cont1/dimensiones[1]  
    
    #Corte a un cuarto de la imagen horizontalmente
    cont2=0
    fila_horizontal_un_cuarto_pixeles=int(fila_horizontal_mitad_pixeles/2)#A fila_horizontal_un_cuarto_pixeles se le asigna el valor de un entero obtenido por la divicion fila_horizontal_mitad_pixeles entre 2.
    for i in range(0,dimensiones[1]):#Ciclo for que recorre la columnas.
        #imagen_rayada[fila_horizontal_un_cuarto_pixeles,i]=1
        if(imagen[fila_horizontal_un_cuarto_pixeles][i]!=0):
            cont2=cont2+1
    cont2=cont2/dimensiones[1]

    #Corte a tres cuartos de la imagen horizontalmente
    cont3=0
    fila_horizontal_tres_cuartos_pixeles=int(fila_horizontal_mitad_pixeles+fila_horizontal_un_cuarto_pixeles)#A mc3c (matriz columnas a tres cuartos) se le asigna el valor de un entero optenido por la suma de fila_horizontal_mitad_pixeles mas fila_horizontal_un_cuarto_pixeles.
    for i in range(0,dimensiones[1]):#Ciclo for que recorre la columnas.
        #imagen_rayada[fila_horizontal_tres_cuartos_pixeles,i]=1
        if(imagen[fila_horizontal_tres_cuartos_pixeles][i]!=0):
            cont3=cont3+1
    cont3=cont3/dimensiones[1]
        
#Inicia vertical.
    #Corte a la mitad de la imagen verticalmente
    cont4=0
    columna_vertical_mitad_pixeles=int(dimensiones[1]/2)#A columna_vertical_mitad_pixeles se le asigna el valor de un entero obtenido por la divicion de dimensiones entre 2.
    for i in range(0,dimensiones[0]):#Ciclo for que recorre la columnas.
        #imagen_rayada[i,columna_vertical_mitad_pixeles]=1
        if(imagen[i][columna_vertical_mitad_pixeles]!=0):
            cont4=cont4+1
    cont4=cont4/dimensiones[0]

    #Corte a un cuarto de la imagen verticalmente
    cont5=0
    columna_vertical_un_cuarto_pixeles=int(columna_vertical_mitad_pixeles/2)#A columna_vertical_un_cuarto_pixeles se le asigna el valor de un entero obtenido por la divicion fila_vertical_mitad_pixeles entre 2.
    for i in range(0,dimensiones[0]):#Ciclo for que recorre la columnas.
        #imagen_rayada[i,columna_vertical_un_cuarto_pixeles]=1
        if(imagen[i][columna_vertical_un_cuarto_pixeles]!=0):
            cont5=cont5+1
    cont5=cont5/dimensiones[0]
    
    #Corte a tres cuartos de la imagen verticalmente
    cont6=0
    columna_vertical_tres_cuartos_pixeles=int(columna_vertical_mitad_pixeles+columna_vertical_un_cuarto_pixeles)#A columna_vertical_tres_cuartos_pixeles se le asigna el valor de un entero obtenido por la suma de columna_vertical_mitad_pixeles mas columna_vertical_un_cuarto_pixeles.
    for i in range(0,dimensiones[0]):#Ciclo for que recorre la columnas.
        #imagen_rayada[i,columna_vertical_tres_cuartos_pixeles]=1
        if(imagen[i][columna_vertical_tres_cuartos_pixeles]!=0):
            cont6=cont6+1
    cont6=cont6/dimensiones[0]
    print('\n')#Imprime salto de linea.    
    return cont1,cont2,cont3,cont4,cont5,cont6

#Cambios_En_La_Imagen()
#Se contabiliza el numero de cambios ue sufre la imagen al ser recorrida (ceros y unos)
#Se usa un contador el cual nos permite saber cuando se hace un corte en la imagen.
#En la variable "mc" se obtiene la posición en la imagen mediane la división.
#La variable "x" se usa para comparar.
#La variable "imagen" contiene la matriz de la imagen.

def Cambios_en_la_imagen(imagen,dimensiones):
    #Cambios a la mitad de la imagen horizontalmente
    cont7=0#Se inicializa el contador en cero.
    fila_horizontal_mitad_cortes=int(dimensiones[0]/2)#A la variable fila_horizontal_mitad_cortes se le asigna el valor de la división de dimensiones[0] entre 2.
    x=imagen[fila_horizontal_mitad_cortes,0]#A la variable x se le agrega el valor de las posiciones fila_horizontal_mitad_cortes y 0.
    for i in range(0,dimensiones[1]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[fila_horizontal_mitad_cortes,i]=1
        if (imagen[fila_horizontal_mitad_cortes,i]!=x):#Se hace la comparación de imagen en la posición fila_horizontal_mitad_cortes, i si es diferente de x.
            cont7=cont7+1#Se hace el aumento de la variable si imagen es diferente de x.            x=imagen[fila_horizontal_mitad_cortes,i]#a la variable x se le asigna el valor de imagen en la posición fila_horizontal_mitad_cortes,i.
    
    #Cambios a un cuarto de la imagen horizontalmente
    cont8=0#Se inicializa el contador en cero.
    fila_horizontal_un_cuarto_cortes=int(fila_horizontal_mitad_cortes/2)#A la variable fila_horizontal_un_cuarto_cortes se le asigna el valor de la división de fila_horizontal_mitad_cortes entre 2.
    x=imagen[fila_horizontal_un_cuarto_cortes,0]#A la variable x se le agrega el valor de las posiciones mcc y 0.
    for i in range(0,dimensiones[1]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[fila_horizontal_un_cuarto_cortes,i]=1
        if (imagen[fila_horizontal_un_cuarto_cortes,i]!=x):#Se hace la comparación de imagen en la posición fila_horizontal_mitad_cortes, i si es diferente de x.
            cont8=cont8+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[fila_horizontal_un_cuarto_cortes,i]#a la variable x se le asigna el valor de imagen en la posición fila_horizontal_mitad_cortes,i.

    #Cambios a tres cuartos de la imagen horizontalmente
    cont9=0#Se inicializa el contador en cero.
    fila_horizontal_tres_cuartos_cortes=int(fila_horizontal_mitad_cortes+fila_horizontal_un_cuarto_cortes)#A la variable fila_horizontal_un_cuarto_cortes se le asigna el valor de la suma de fila_horizontal_mitad_cortes mas fila_horizontal_tres_cuartos_cortes para obtener la posicion en tres cuartos.
    x=imagen[fila_horizontal_tres_cuartos_cortes,0]#A la variable x se le agrega el valor de las posiciones fila_horizontal_tres_cuartos_cortes y 0.
    for i in range(0,dimensiones[1]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[fila_horizontal_tres_cuartos_cortes,i]=1
        if (imagen[fila_horizontal_tres_cuartos_cortes,i]!=x):#Se hace la comparación de imagen en la posición fila_horizontal_tres_cuartos_cortes, i si es diferente de x.
            cont9=cont9+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[fila_horizontal_un_cuarto_cortes,i]#a la variable x se le asigna el valor de imagen en la posición fila_horizontal_tres_cuartos_cortes,i.

#Comienzan verticales

    #Cambios a la mitad de la imagen verticalmente
    cont11=0#Se inicializa el contador en cero.
    columna_vertical_mitad_cortes=int(dimensiones[1]/2)#A la variable columna_vertical_mitad_cortes se le asigna el valor de la división de dimensiones[1] entre 2.
    x=imagen[columna_vertical_mitad_cortes,0]#A la variable x se le agrega el valor de las posiciones columna_vertical_mitad_cortes y 0.
    for i in range(0,dimensiones[0]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[i,columna_vertical_mitad_cortes]=1
        if (imagen[i,columna_vertical_mitad_cortes]!=x):#Se hace la comparación de imagen en la posición columna_vertical_mitad_cortes,i si es diferente de x.
            cont11=cont11+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[i,columna_vertical_mitad_cortes]#a la variable x se le asigna el valor de imagen en la posición i,columna_vertical_mitad_cortes.
    
    #Cambios a un cuarto de la imagen verticalmente
    cont10=0#Se inicializa el contador en cero.
    columna_vertical_un_cuarto_cortes=int(columna_vertical_mitad_cortes/2)#A la variable columna_vertical_un_cuarto_cortes se le asigna el valor de la división de columna_vertical_mitad_cortes entre 2.
    x=imagen[columna_vertical_un_cuarto_cortes,0]#A la variable x se le agrega el valor de las posiciones mfc y 0.
    for i in range(0,dimensiones[0]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[i,mf]=1
        if (imagen[i,columna_vertical_un_cuarto_cortes]!=x):#Se hace la comparación de imagen en la posición mfc,i si es diferente de x.
            cont10=cont10+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[i,columna_vertical_un_cuarto_cortes]#a la variable x se le asigna el valor de imagen en la posición i,mfc.

    #Cambios a tres cuartos de la imagen verticalmente
    cont12=0#Se inicializa el contador en cero.
    columna_vertical_tres_cuartos_cortes=int(columna_vertical_mitad_cortes+columna_vertical_un_cuarto_cortes)#A la variable columna_vertical_tres_cuartos_cortes se le asigna el valor de la suma de columna_vertical_mitad_cortes mas columna_vertical_un_cuarto_cortes para obtener la posicion en tres cuartos.
    x=imagen[columna_vertical_tres_cuartos_cortes,0]#A la variable x se le agrega el valor de las posiciones columna_vertical_tres_cuartos_cortes y 0.
    for i in range(0,dimensiones[0]):#Ciclo for recorre las columnas de la imagen.
        #imagen_rayada[i,columna_vertical_tres_cuartos_cortes]=1
        if (imagen[i,columna_vertical_tres_cuartos_cortes]!=x):#Se hace la comparación de imagen en la posición columna_vertical_tres_cuartos_cortes,i si es diferente de x.
            cont12=cont12+1#Se hace el aumento de la variable si imagen es diferente de x.
            x=imagen[i,columna_vertical_tres_cuartos_cortes]#a la variable x se le asigna el valor de imagen en la posición i,columna_vertical_tres_cuartos_cortes.

    #imagenplot = plt.imshow(imagen_rayada)#La variable imagenplot sirve para imprimir la imagen previamente cargada.
    return cont7,cont8,cont9,cont10,cont11,cont12


def Distancia_Euclidiana(razon,pixeles_blancos,cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9,cont10,cont11,cont12):

    contador=0#Se inicializa la variable en cero.

    for i in dataset:#Ciclo for que recorre el dataset.
        dataset[contador][0]=float(dataset[contador][0])#Se convierte el valor contenido en la posición contador, 0.
        dataset[contador][1]=int(dataset[contador][1])#Se convierte el valor contenido en la posición contador, 1.
        dataset[contador][2]=float(dataset[contador][2])#Se convierte el valor contenido en la posición contador, 2.
        dataset[contador][3]=float(dataset[contador][3])#Se convierte el valor contenido en la posición contador, 3.
        dataset[contador][4]=float(dataset[contador][4])#Se convierte el valor contenido en la posición contador, 4.
        dataset[contador][5]=float(dataset[contador][5])#Se convierte el valor contenido en la posición contador, 5.
        dataset[contador][6]=float(dataset[contador][6])#Se convierte el valor contenido en la posición contador, 6.
        dataset[contador][7]=float(dataset[contador][7])#Se convierte el valor contenido en la posición contador, 7.
        dataset[contador][8]=int(dataset[contador][8])#Se convierte el valor contenido en la posición contador, 8.
        dataset[contador][9]=int(dataset[contador][9])#Se convierte el valor contenido en la posición contador, 9.
        dataset[contador][10]=int(dataset[contador][10])#Se convierte el valor contenido en la posición contador, 10.
        dataset[contador][11]=int(dataset[contador][11])#Se convierte el valor contenido en la posición contador, 11.
        dataset[contador][12]=int(dataset[contador][12])#Se convierte el valor contenido en la posición contador, 12.
        dataset[contador][13]=int(dataset[contador][13])#Se convierte el valor contenido en la posición contador, 13.
        dataset[contador][14]=int(dataset[contador][14])#Se convierte el valor contenido en la posición contador, 14.

        #Se realiza la sumatoria para calcular la distancia mediante la formula de la distancia euclidiana.
        sumatoria=((dataset[contador][0]-razon)**2)+((dataset[contador][1]-pixeles_blancos)**2)+((dataset[contador][2]-cont1)**2)+((dataset[contador][3]-cont2)**2)+((dataset[contador][4]-cont3)**2)+((dataset[contador][5]-cont4)**2)+((dataset[contador][6]-cont5)**2)+((dataset[contador][7]-cont6)**2)+((dataset[contador][8]-cont7)**2)+((dataset[contador][9]-cont8)**2)+((dataset[contador][10]-cont9)**2)+((dataset[contador][11]-cont10)**2)+((dataset[contador][12]-cont11)**2)+((dataset[contador][13]-cont12)**2)
        raiz=math.sqrt(sumatoria)#Se obtiene la raiz de la sumatoria.
        dataset[contador].append(raiz)#Se asigna lo obtenido en raiz a dataset en una nueva columna.
        dataset[contador].append(contador)#Se asigna lo obtenido en contador a dataset en una nueva columna.
        contador+=1#Se realiza el aumento al contador el cual recorre las filas.

    print('En total hay',contador,'instancias')#Imprime el numero total de instancias del dataset.
    print('En total hay 14 caracteristicas')
    print('Clases: 10')
    print('Nombres de las clases: {0,1,2,3,4,5,6,7,8,9}')
    print('\n')#Imprime salto de linea.
    dataset.sort(key=lambda dataset: dataset[15])#Se realiza el ordenamiento de menor a mayor.

def Comparación():
    clase0=0#Se inicializa la variable en cero.
    clase1=0#Se inicializa la variable en cero.
    clase2=0#Se inicializa la variable en cero.
    clase3=0#Se inicializa la variable en cero.
    clase4=0#Se inicializa la variable en cero.
    clase5=0#Se inicializa la variable en cero.
    clase6=0#Se inicializa la variable en cero.
    clase7=0#Se inicializa la variable en cero.
    clase8=0#Se inicializa la variable en cero.
    clase9=0#Se inicializa la variable en cero.
    for x in range(0,k):#Ciclo for que recorre desde cero hasta k (los vecinos indicados)
        if(dataset[x][14]==0):#Se compara dataset en la posición x, 14 si es igual a cero.
            clase0=clase0+1#Si se cumple la condición se realiza un aumento en la variable que represente la clase 0.
        if(dataset[x][14]==1):#Se compara dataset en la posición x, 14 si es igual a uno.
            clase1=clase1+1#Si se cumple la condición se realiza un aumento en la variable que represente la clase 1.
        if(dataset[x][14]==2):#Se compara dataset en la posición x, 14 si es igual a dos.
            clase2=clase2+1#Si se cumple la condición se realiza un aumento en la variable que represente la clase 2.
        if(dataset[x][14]==3):#Se compara dataset en la posición x, 14 si es igual a tres.
            clase3=clase3+1#Si se cumple la condición se realiza un aumento en la variable que represente la clase 3.
        if(dataset[x][14]==4):#Se compara dataset en la posición x, 14 si es igual a cuatro.
            clase4=clase4+1#Si se cumple la condición se realiza un aumento en la variable que represente la clase 4.
        if(dataset[x][14]==5):#Se compara dataset en la posición x, 14 si es igual a cinco.
            clase5=clase5+1#Si se cumple la condición se realiza un aumento en la variable que represente la clase 5.
        if(dataset[x][14]==6):#Se compara dataset en la posición x, 14 si es igual a seis.
            clase6=clase6+1#Si se cumple la condición se realiza un aumento en la variable que represente la clase 6.
        if(dataset[x][14]==7):#Se compara dataset en la posición x, 14 si es igual a siete.
            clase7=clase7+1#Si se cumple la condición se realiza un aumento en la variable que represente la clase 7.
        if(dataset[x][14]==8):#Se compara dataset en la posición x, 14 si es igual a ocho.
            clase8=clase8+1#Si se cumple la condición se realiza un aumento en la variable que represente la clase 8.
        if(dataset[x][14]==9):#Se compara dataset en la posición x, 14 si es igual a nueve.
            clase9=clase9+1#Si se cumple la condición se realiza un aumento en la variable que represente la clase 9.
        
        print(x+1,'Instancia: ',dataset[x][16],"  Distancia: {0:.8f}".format(dataset[x][15]),"  Clase: ",[dataset[x][14]])
    print('\n')
    print(clase0,'instancias pertenecientes a la clase: 0')#Imprime el numero de instancias en la clase 0.
    print(clase1,'instancias pertenecientes a la clase: 1')#Imprime el numero de instancias en la clase 1.
    print(clase2,'instancias pertenecientes a la clase: 2')#Imprime el numero de instancias en la clase 2.
    print(clase3,'instancias pertenecientes a la clase: 3')#Imprime el numero de instancias en la clase 3.
    print(clase4,'instancias pertenecientes a la clase: 4')#Imprime el numero de instancias en la clase 4.
    print(clase5,'instancias pertenecientes a la clase: 5')#Imprime el numero de instancias en la clase 5.
    print(clase6,'instancias pertenecientes a la clase: 6')#Imprime el numero de instancias en la clase 6.
    print(clase7,'instancias pertenecientes a la clase: 7')#Imprime el numero de instancias en la clase 7.
    print(clase8,'instancias pertenecientes a la clase: 8')#Imprime el numero de instancias en la clase 8.
    print(clase9,'instancias pertenecientes a la clase: 9')#Imprime el numero de instancias en la clase 9.
        
    #Se compara si la clase 0 es mayor que todas las demas clases.
    if(clase0>clase1):
        if(clase0>clase2):
            if(clase0>clase3):
                if(clase0>clase4):
                    if(clase0>clase5):
                        if(clase0>clase6):
                            if(clase0>clase7):
                                if(clase0>clase8):
                                    if(clase0>clase9):
                                        print("\nEl numero es un 0\n")#Si las condiciones se cumplen se imprime 0.
    
    #Se compara si la clase 1 es mayor que todas las demas clases.
    if(clase1>clase0):
        if(clase1>clase2):
            if(clase1>clase3):
                if(clase1>clase4):
                    if(clase1>clase5):
                        if(clase1>clase6):
                            if(clase1>clase7):
                                if(clase1>clase8):
                                    if(clase1>clase9):
                                        print("\nEl numero es un 1\n")#Si las condiciones se cumplen se imprime 1.
    
    #Se compara si la clase 2 es mayor que todas las demas clases.
    if(clase2>clase0):
        if(clase2>clase1):
            if(clase2>clase3):
                if(clase2>clase4):
                    if(clase2>clase5):
                        if(clase2>clase6):
                            if(clase2>clase7):
                                if(clase2>clase8):
                                    if(clase2>clase9):
                                        print("\nEl numero es un 2\n")#Si las condiciones se cumplen se imprime 2.
    
    #Se compara si la clase 3 es mayor que todas las demas clases.
    if(clase3>clase0):
        if(clase3>clase1):
            if(clase3>clase2):
                if(clase3>clase4):
                    if(clase3>clase5):
                        if(clase3>clase6):
                            if(clase3>clase7):
                                if(clase3>clase8):
                                    if(clase3>clase9):
                                        print("\nEl numero es un 3\n")#Si las condiciones se cumplen se imprime 3.
    
    #Se compara si la clase 4 es mayor que todas las demas clases.
    if(clase4>clase0):
        if(clase4>clase1):
            if(clase4>clase2):
                if(clase4>clase3):
                    if(clase4>clase5):
                        if(clase4>clase6):
                            if(clase4>clase7):
                                if(clase4>clase8):
                                    if(clase4>clase9):
                                        print("\nEl numero es un 4\n")#Si las condiciones se cumplen se imprime 4.
    
    #Se compara si la clase 5 es mayor que todas las demas clases.
    if(clase5>clase0):
        if(clase5>clase1):
            if(clase5>clase2):
                if(clase5>clase3):
                    if(clase5>clase4):
                        if(clase5>clase6):
                            if(clase5>clase7):
                                if(clase5>clase8):
                                    if(clase5>clase9):
                                        print("\nEl numero es un 5\n")#Si las condiciones se cumplen se imprime 5.
    
    #Se compara si la clase 6 es mayor que todas las demas clases.
    if(clase6>clase0):
        if(clase6>clase1):
            if(clase6>clase2):
                if(clase6>clase3):
                    if(clase6>clase4):
                        if(clase6>clase5):
                            if(clase6>clase7):
                                if(clase6>clase8):
                                    if(clase6>clase9):
                                        print("\nEl numero es un 6\n")#Si las condiciones se cumplen se imprime 6.
    
    #Se compara si la clase 7 es mayor que todas las demas clases.
    if(clase7>clase0):
        if(clase7>clase1):
            if(clase7>clase2):
                if(clase7>clase3):
                    if(clase7>clase4):
                        if(clase7>clase5):
                            if(clase7>clase6):
                                if(clase7>clase8):
                                    if(clase7>clase9):
                                        print("\nEl numero es un 7\n")#Si las condiciones se cumplen se imprime 7.
    
    #Se compara si la clase 8 es mayor que todas las demas clases.
    if(clase8>clase0):
        if(clase8>clase1):
            if(clase8>clase2):
                if(clase8>clase3):
                    if(clase8>clase4):
                        if(clase8>clase5):
                            if(clase8>clase6):
                                if(clase8>clase7):
                                    if(clase8>clase9):
                                        print("\nEl numero es un 8\n")#Si las condiciones se cumplen se imprime 8.
    
    #Se compara si la clase 9 es mayor que todas las demas clases.
    if(clase9>clase0):
        if(clase9>clase1):
            if(clase9>clase2):
                if(clase9>clase3):
                    if(clase9>clase4):
                        if(clase9>clase5):
                            if(clase9>clase6):
                                if(clase9>clase7):
                                    if(clase9>clase8):
                                        print("\nEl numero es un 9\n")#Si las condiciones se cumplen se imprime 9.

def main():
    dimensiones=Calcular_dimensiones(imagen)#A la variable dimensiones se le asigna el valos obtenido en la función Calcular_dimensiones indicando los parámetros.
    razon=Razon(dimensiones)#A la variable razon se le asigna el valos obtenido en la función Razon indicando los parámetros.
    pixeles_blancos=Pixeles_blancos(imagen,dimensiones)#A la variable pixeles_blancos se le asigna el valos obtenido en la función Pixeles_blancos indicando los parámetros.
    cont1,cont2,cont3,cont4,cont5,cont6=Numero_De_Pixeles_Que_Representan_La_Imagen(imagen,dimensiones)#A las variables cont1,cont2,cont3,cont4,cont5,cont6 se le asigna el valos obtenido en la función Numero_De_Pixeles_Que_Representan_La_Imagen indicando los parámetros.
    cont7,cont8,cont9,cont10,cont11,cont12=Cambios_en_la_imagen(imagen,dimensiones)#A las variables cont7,cont8,cont9,cont10,cont11,cont12 se le asigna el valos obtenido en la función Cambios_en_la_imagen indicando los parámetros.
    Distancia_Euclidiana(razon,pixeles_blancos,cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9,cont10,cont11,cont12)#Se llama la función Distancia_Euclidiana indicando los parámetros.
    Comparación()#Se llama a la función de Comparacion.
    
main()
