import matplotlib.image as mpimagen
import csv
import os




def Calcular_dimenciones(imagen):
    
    dimenciones=imagen.shape
    
    return dimenciones




def Razon(dimenciones):
    razon=dimenciones[0]/dimenciones[1]
    
    return razon








def Pixeles_blancos(imagen,dimenciones):        
    pixeles_blancos=0
    for i in range(0,dimenciones[0]):
        for j in range(0,dimenciones[1]):
            if (imagen[i][j]!=0):
                pixeles_blancos=pixeles_blancos+1
    
    return pixeles_blancos








def Numero_De_Pixeles_Que_Representan_La_Imagen(imagen,dimensiones):
    
    cont1=0
    fila_horizontal_mitad_pixeles=int(dimensiones[0]/2)
    for i in range(0,dimensiones[1]):
        
        if(imagen[fila_horizontal_mitad_pixeles][i]!=0):
            cont1=cont1+1
    cont1=cont1/dimensiones[1]
    
    
    
    cont2=0
    fila_horizontal_un_cuarto_pixeles=int(fila_horizontal_mitad_pixeles/2)
    for i in range(0,dimensiones[1]):
        
        if(imagen[fila_horizontal_un_cuarto_pixeles][i]!=0):
            cont2=cont2+1
    cont2=cont2/dimensiones[1]
    

    
    cont3=0
    fila_horizontal_tres_cuartos_pixeles=int(fila_horizontal_mitad_pixeles+fila_horizontal_un_cuarto_pixeles)
    for i in range(0,dimensiones[1]):
        
        if(imagen[fila_horizontal_tres_cuartos_pixeles][i]!=0):
            cont3=cont3+1
    cont3=cont3/dimensiones[1]
    
        

    
    cont4=0
    columna_vertical_mitad_pixeles=int(dimensiones[1]/2)
    for i in range(0,dimensiones[0]):
        
        if(imagen[i][columna_vertical_mitad_pixeles]!=0):
            cont4=cont4+1
    cont4=cont4/dimensiones[0]
    

    
    cont5=0
    columna_vertical_un_cuarto_pixeles=int(columna_vertical_mitad_pixeles/2)
    for i in range(0,dimensiones[0]):
        
        if(imagen[i][columna_vertical_un_cuarto_pixeles]!=0):
            cont5=cont5+1
    cont5=cont5/dimensiones[0]
    
    
    
    cont6=0
    columna_vertical_tres_cuartos_pixeles=int(columna_vertical_mitad_pixeles+columna_vertical_un_cuarto_pixeles)
    for i in range(0,dimensiones[0]):
        
        if(imagen[i][columna_vertical_tres_cuartos_pixeles]!=0):
            cont6=cont6+1
    cont6=cont6/dimensiones[0]
    
    return cont1,cont2,cont3,cont4,cont5,cont6
    







def Cambios_en_la_imagen(imagen,dimenciones):
    
    cont7=0
    fila_horizontal_mitad_cortes=int(dimenciones[0]/2)
    x=imagen[fila_horizontal_mitad_cortes,0]
    for i in range(0,dimenciones[1]):
        
        if (imagen[fila_horizontal_mitad_cortes,i]!=x):
            cont7=cont7+1
            x=imagen[fila_horizontal_mitad_cortes,i]
    
    
    
    cont8=0
    fila_horizontal_un_cuarto_cortes=int(fila_horizontal_mitad_cortes/2)
    x=imagen[fila_horizontal_un_cuarto_cortes,0]
    for i in range(0,dimenciones[1]):
        
        if (imagen[fila_horizontal_un_cuarto_cortes,i]!=x):
            cont8=cont8+1
            x=imagen[fila_horizontal_un_cuarto_cortes,i]
    

    
    cont9=0
    fila_horizontal_tres_cuartos_cortes=int(fila_horizontal_mitad_cortes+fila_horizontal_un_cuarto_cortes)
    x=imagen[fila_horizontal_tres_cuartos_cortes,0]
    for i in range(0,dimenciones[1]):
        
        if (imagen[fila_horizontal_tres_cuartos_cortes,i]!=x):
            cont9=cont9+1
            x=imagen[fila_horizontal_un_cuarto_cortes,i]
    



    
    cont11=0
    columna_vertical_mitad_cortes=int(dimenciones[1]/2)
    x=imagen[columna_vertical_mitad_cortes,0]
    for i in range(0,dimenciones[0]):
        
        if (imagen[i,columna_vertical_mitad_cortes]!=x):
            cont11=cont11+1
            x=imagen[i,columna_vertical_mitad_cortes]
    
    
    
    cont10=0
    columna_vertical_un_cuarto_cortes=int(columna_vertical_mitad_cortes/2)
    x=imagen[columna_vertical_un_cuarto_cortes,0]
    for i in range(0,dimenciones[0]):
        
        if (imagen[i,columna_vertical_un_cuarto_cortes]!=x):
            cont10=cont10+1
            x=imagen[i,columna_vertical_un_cuarto_cortes]
    

    
    cont12=0
    columna_vertical_tres_cuartos_cortes=int(columna_vertical_mitad_cortes+columna_vertical_un_cuarto_cortes)
    x=imagen[columna_vertical_tres_cuartos_cortes,0]
    for i in range(0,dimenciones[0]):
        
        if (imagen[i,columna_vertical_tres_cuartos_cortes]!=x):
            cont12=cont12+1
            x=imagen[i,columna_vertical_tres_cuartos_cortes]
    

    

    return cont7,cont8,cont9,cont10,cont11,cont12





def Escritura_CSV():
    archivo_CSV=open('DataSet.csv','w', newline='')
    salida_CSV= csv.writer(archivo_CSV)
    clase=-1
    contador=0
    carpeta='imagenes'
    numero=-1
    for path, ficheros, archivos in os.walk(carpeta):
        for fname in archivos:
            nombre=path+'/'+fname
            imagen = mpimagen.imread(nombre)
            
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



import matplotlib.image as mpimagen
import csv
import math
f= open('DataSet.csv')
lns=csv.reader(f)
dataset=list(lns)

print('Nombre de la imagen: ',end="")
nombreimagen=input()
imagen = mpimagen.imread(nombreimagen)

print('Numero de vecinos a conciderar: ',end="")
k=int(input())




def Calcular_dimensiones(imagen):
    
    dimensiones=imagen.shape
    return dimensiones




def Razon(dimensiones):
    razon=dimensiones[0]/dimensiones[1]
    return razon








def Pixeles_blancos(imagen,dimensiones):        
    pixeles_blancos=0
    for i in range(0,dimensiones[0]):
        for j in range(0,dimensiones[1]):
            if (imagen[i][j]!=0):
                pixeles_blancos=pixeles_blancos+1
    return pixeles_blancos








def Numero_De_Pixeles_Que_Representan_La_Imagen(imagen,dimensiones):
    
    cont1=0
    fila_horizontal_mitad_pixeles=int(dimensiones[0]/2)
    for i in range(0,dimensiones[1]):
        
        if(imagen[fila_horizontal_mitad_pixeles][i]!=0):
            cont1=cont1+1
    cont1=cont1/dimensiones[1]  
    
    
    cont2=0
    fila_horizontal_un_cuarto_pixeles=int(fila_horizontal_mitad_pixeles/2)
    for i in range(0,dimensiones[1]):
        
        if(imagen[fila_horizontal_un_cuarto_pixeles][i]!=0):
            cont2=cont2+1
    cont2=cont2/dimensiones[1]

    
    cont3=0
    fila_horizontal_tres_cuartos_pixeles=int(fila_horizontal_mitad_pixeles+fila_horizontal_un_cuarto_pixeles)
    for i in range(0,dimensiones[1]):
        
        if(imagen[fila_horizontal_tres_cuartos_pixeles][i]!=0):
            cont3=cont3+1
    cont3=cont3/dimensiones[1]
        

    
    cont4=0
    columna_vertical_mitad_pixeles=int(dimensiones[1]/2)
    for i in range(0,dimensiones[0]):
        
        if(imagen[i][columna_vertical_mitad_pixeles]!=0):
            cont4=cont4+1
    cont4=cont4/dimensiones[0]

    
    cont5=0
    columna_vertical_un_cuarto_pixeles=int(columna_vertical_mitad_pixeles/2)
    for i in range(0,dimensiones[0]):
        
        if(imagen[i][columna_vertical_un_cuarto_pixeles]!=0):
            cont5=cont5+1
    cont5=cont5/dimensiones[0]
    
    
    cont6=0
    columna_vertical_tres_cuartos_pixeles=int(columna_vertical_mitad_pixeles+columna_vertical_un_cuarto_pixeles)
    for i in range(0,dimensiones[0]):
        
        if(imagen[i][columna_vertical_tres_cuartos_pixeles]!=0):
            cont6=cont6+1
    cont6=cont6/dimensiones[0]
    print('\n')
    return cont1,cont2,cont3,cont4,cont5,cont6








def Cambios_en_la_imagen(imagen,dimensiones):
    
    cont7=0
    fila_horizontal_mitad_cortes=int(dimensiones[0]/2)
    x=imagen[fila_horizontal_mitad_cortes,0]
    for i in range(0,dimensiones[1]):
        
        if (imagen[fila_horizontal_mitad_cortes,i]!=x):
            cont7=cont7+1
    
    
    cont8=0
    fila_horizontal_un_cuarto_cortes=int(fila_horizontal_mitad_cortes/2)
    x=imagen[fila_horizontal_un_cuarto_cortes,0]
    for i in range(0,dimensiones[1]):
        
        if (imagen[fila_horizontal_un_cuarto_cortes,i]!=x):
            cont8=cont8+1
            x=imagen[fila_horizontal_un_cuarto_cortes,i]

    
    cont9=0
    fila_horizontal_tres_cuartos_cortes=int(fila_horizontal_mitad_cortes+fila_horizontal_un_cuarto_cortes)
    x=imagen[fila_horizontal_tres_cuartos_cortes,0]
    for i in range(0,dimensiones[1]):
        
        if (imagen[fila_horizontal_tres_cuartos_cortes,i]!=x):
            cont9=cont9+1
            x=imagen[fila_horizontal_un_cuarto_cortes,i]



    
    cont11=0
    columna_vertical_mitad_cortes=int(dimensiones[1]/2)
    x=imagen[columna_vertical_mitad_cortes,0]
    for i in range(0,dimensiones[0]):
        
        if (imagen[i,columna_vertical_mitad_cortes]!=x):
            cont11=cont11+1
            x=imagen[i,columna_vertical_mitad_cortes]
    
    
    cont10=0
    columna_vertical_un_cuarto_cortes=int(columna_vertical_mitad_cortes/2)
    x=imagen[columna_vertical_un_cuarto_cortes,0]
    for i in range(0,dimensiones[0]):
        
        if (imagen[i,columna_vertical_un_cuarto_cortes]!=x):
            cont10=cont10+1
            x=imagen[i,columna_vertical_un_cuarto_cortes]

    
    cont12=0
    columna_vertical_tres_cuartos_cortes=int(columna_vertical_mitad_cortes+columna_vertical_un_cuarto_cortes)
    x=imagen[columna_vertical_tres_cuartos_cortes,0]
    for i in range(0,dimensiones[0]):
        
        if (imagen[i,columna_vertical_tres_cuartos_cortes]!=x):
            cont12=cont12+1
            x=imagen[i,columna_vertical_tres_cuartos_cortes]

    
    return cont7,cont8,cont9,cont10,cont11,cont12


def Distancia_Euclidiana(razon,pixeles_blancos,cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9,cont10,cont11,cont12):

    contador=0

    for i in dataset:
        dataset[contador][0]=float(dataset[contador][0])
        dataset[contador][1]=int(dataset[contador][1])
        dataset[contador][2]=float(dataset[contador][2])
        dataset[contador][3]=float(dataset[contador][3])
        dataset[contador][4]=float(dataset[contador][4])
        dataset[contador][5]=float(dataset[contador][5])
        dataset[contador][6]=float(dataset[contador][6])
        dataset[contador][7]=float(dataset[contador][7])
        dataset[contador][8]=int(dataset[contador][8])
        dataset[contador][9]=int(dataset[contador][9])
        dataset[contador][10]=int(dataset[contador][10])
        dataset[contador][11]=int(dataset[contador][11])
        dataset[contador][12]=int(dataset[contador][12])
        dataset[contador][13]=int(dataset[contador][13])
        dataset[contador][14]=int(dataset[contador][14])

        
        sumatoria=((dataset[contador][0]-razon)**2)+((dataset[contador][1]-pixeles_blancos)**2)+((dataset[contador][2]-cont1)**2)+((dataset[contador][3]-cont2)**2)+((dataset[contador][4]-cont3)**2)+((dataset[contador][5]-cont4)**2)+((dataset[contador][6]-cont5)**2)+((dataset[contador][7]-cont6)**2)+((dataset[contador][8]-cont7)**2)+((dataset[contador][9]-cont8)**2)+((dataset[contador][10]-cont9)**2)+((dataset[contador][11]-cont10)**2)+((dataset[contador][12]-cont11)**2)+((dataset[contador][13]-cont12)**2)
        raiz=math.sqrt(sumatoria)
        dataset[contador].append(raiz)
        dataset[contador].append(contador)
        contador+=1

    print('En total hay',contador,'instancias')
    print('En total hay 14 caracteristicas')
    print('Clases: 10')
    print('Nombres de las clases: {0,1,2,3,4,5,6,7,8,9}')
    print('\n')
    dataset.sort(key=lambda dataset: dataset[15])

def Comparación():
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
    for x in range(0,k):
        if(dataset[x][14]==0):
            clase0=clase0+1
        if(dataset[x][14]==1):
            clase1=clase1+1
        if(dataset[x][14]==2):
            clase2=clase2+1
        if(dataset[x][14]==3):
            clase3=clase3+1
        if(dataset[x][14]==4):
            clase4=clase4+1
        if(dataset[x][14]==5):
            clase5=clase5+1
        if(dataset[x][14]==6):
            clase6=clase6+1
        if(dataset[x][14]==7):
            clase7=clase7+1
        if(dataset[x][14]==8):
            clase8=clase8+1
        if(dataset[x][14]==9):
            clase9=clase9+1
        
        print(x+1,'Instancia: ',dataset[x][16],"  Distancia: {0:.8f}".format(dataset[x][15]),"  Clase: ",[dataset[x][14]])
    print('\n')
    print(clase0,'instancias pertenecientes a la clase: 0')
    print(clase1,'instancias pertenecientes a la clase: 1')
    print(clase2,'instancias pertenecientes a la clase: 2')
    print(clase3,'instancias pertenecientes a la clase: 3')
    print(clase4,'instancias pertenecientes a la clase: 4')
    print(clase5,'instancias pertenecientes a la clase: 5')
    print(clase6,'instancias pertenecientes a la clase: 6')
    print(clase7,'instancias pertenecientes a la clase: 7')
    print(clase8,'instancias pertenecientes a la clase: 8')
    print(clase9,'instancias pertenecientes a la clase: 9')
        
    
    if(clase0>clase1):
        if(clase0>clase2):
            if(clase0>clase3):
                if(clase0>clase4):
                    if(clase0>clase5):
                        if(clase0>clase6):
                            if(clase0>clase7):
                                if(clase0>clase8):
                                    if(clase0>clase9):
                                        print("\nEl numero es un 0\n")
    
    
    if(clase1>clase0):
        if(clase1>clase2):
            if(clase1>clase3):
                if(clase1>clase4):
                    if(clase1>clase5):
                        if(clase1>clase6):
                            if(clase1>clase7):
                                if(clase1>clase8):
                                    if(clase1>clase9):
                                        print("\nEl numero es un 1\n")
    
    
    if(clase2>clase0):
        if(clase2>clase1):
            if(clase2>clase3):
                if(clase2>clase4):
                    if(clase2>clase5):
                        if(clase2>clase6):
                            if(clase2>clase7):
                                if(clase2>clase8):
                                    if(clase2>clase9):
                                        print("\nEl numero es un 2\n")
    
    
    if(clase3>clase0):
        if(clase3>clase1):
            if(clase3>clase2):
                if(clase3>clase4):
                    if(clase3>clase5):
                        if(clase3>clase6):
                            if(clase3>clase7):
                                if(clase3>clase8):
                                    if(clase3>clase9):
                                        print("\nEl numero es un 3\n")
    
    
    if(clase4>clase0):
        if(clase4>clase1):
            if(clase4>clase2):
                if(clase4>clase3):
                    if(clase4>clase5):
                        if(clase4>clase6):
                            if(clase4>clase7):
                                if(clase4>clase8):
                                    if(clase4>clase9):
                                        print("\nEl numero es un 4\n")
    
    
    if(clase5>clase0):
        if(clase5>clase1):
            if(clase5>clase2):
                if(clase5>clase3):
                    if(clase5>clase4):
                        if(clase5>clase6):
                            if(clase5>clase7):
                                if(clase5>clase8):
                                    if(clase5>clase9):
                                        print("\nEl numero es un 5\n")
    
    
    if(clase6>clase0):
        if(clase6>clase1):
            if(clase6>clase2):
                if(clase6>clase3):
                    if(clase6>clase4):
                        if(clase6>clase5):
                            if(clase6>clase7):
                                if(clase6>clase8):
                                    if(clase6>clase9):
                                        print("\nEl numero es un 6\n")
    
    
    if(clase7>clase0):
        if(clase7>clase1):
            if(clase7>clase2):
                if(clase7>clase3):
                    if(clase7>clase4):
                        if(clase7>clase5):
                            if(clase7>clase6):
                                if(clase7>clase8):
                                    if(clase7>clase9):
                                        print("\nEl numero es un 7\n")
    
    
    if(clase8>clase0):
        if(clase8>clase1):
            if(clase8>clase2):
                if(clase8>clase3):
                    if(clase8>clase4):
                        if(clase8>clase5):
                            if(clase8>clase6):
                                if(clase8>clase7):
                                    if(clase8>clase9):
                                        print("\nEl numero es un 8\n")
    
    
    if(clase9>clase0):
        if(clase9>clase1):
            if(clase9>clase2):
                if(clase9>clase3):
                    if(clase9>clase4):
                        if(clase9>clase5):
                            if(clase9>clase6):
                                if(clase9>clase7):
                                    if(clase9>clase8):
                                        print("\nEl numero es un 9\n")

def main():
    dimensiones=Calcular_dimensiones(imagen)
    razon=Razon(dimensiones)
    pixeles_blancos=Pixeles_blancos(imagen,dimensiones)
    cont1,cont2,cont3,cont4,cont5,cont6=Numero_De_Pixeles_Que_Representan_La_Imagen(imagen,dimensiones)
    cont7,cont8,cont9,cont10,cont11,cont12=Cambios_en_la_imagen(imagen,dimensiones)
    Distancia_Euclidiana(razon,pixeles_blancos,cont1,cont2,cont3,cont4,cont5,cont6,cont7,cont8,cont9,cont10,cont11,cont12)
    Comparación()
    
main()

