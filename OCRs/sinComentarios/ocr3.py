
 

import os    
import matplotlib.image as mpimg
import csv
import math
import operator











def abrirImagen():
    arreglo=[] 
    print (">> CREANDO EL DATASET...")
    for x in range(0,10): 
        clase=x 
        print (" Extrayendo datos de la Clase=",clase)
        
        direc="trainingSet/arialSegmented/"+str(clase)+"/" 
        
        
        imagenes=directory("trainingSet/arialSegmented/"+str(clase))
        j=0
        for i in range(0,imagenes): 
            j1 = "%03d" % j  
            temp = os.path.exists(direc+str(clase)+"_"+str(j1)+".png")
            
            
            
            
            
            while not(temp):
                j+=1 
                j1 = "%03d" % j 
                temp = os.path.exists(direc+str(clase)+"_"+str(j1)+".png")
            
            
            if (os.path.exists(direc+str(clase)+"_"+str(j1)+".png")):
            
            
                
                
                
                img=mpimg.imread(direc+str(clase)+"_"+str(j1)+".png")
                vp1=p1(img)  
                vp2=p2(img) 
                vp3=p3(img) 
                vp4=p4(img) 
                vp5=p5(img) 
                vp6=p6(img) 
                vp7=p7(img) 
                vp8=p8(img) 
                vp9=p9(img) 
                vp10=p10(img) 
                vp11=p11(img) 
                vp12=p12(img) 
                vp13=p13(img) 
                vp14=p14(img) 
                      
                
                linea=str(vp1)+","+str(vp2)+","+str(vp3)+","+str(vp4)+","+str(vp5)+","+str(vp6)+","+str(vp7)+","+str(vp8)+","+str(vp9)+","+str(vp10)+","+str(vp11)+","+str(vp12)+","+str(vp13)+","+str(vp14)+","+str(clase)
                
                
                arreglo.append(linea)

                j+=1
    
    archivoCSV(arreglo)
    print ("\n>> DATASET CREADO CON EXITO <<")

        





def p1(imagen):
    filas=len(imagen[:,0]) 
    col=len(imagen[0,:])   
    pro1=filas/col 
    return pro1 






def p2(imagen):
    con1=0 
    filas=len(imagen[:,0])  
    col=len(imagen[0,:])    
    for i in range(0,filas): 
        for j in range(0,col): 
            if(imagen[i,j]==1): 
                con1=con1+1 
    con1=con1/(filas*col)
    return con1






def p3(imagen):
    con1=0 
    filas=len(imagen[:,0])  
    col=len(imagen[0,:])    
    mitad=int(filas/2) 
    for i in imagen[int(mitad),:]: 
        if(i==1): 
            con1=con1+1 
    
    con1=con1/col 
    return con1






def p4(imagen):
    con1=0 
    filas=len(imagen[:,0])  
    col=len(imagen[0,:])    
    cuarto=int(filas/4)    
    for i in imagen[int(cuarto),:]: 
        if(i==1): 
            con1=con1+1
    
    con1=con1/col
    return con1






def p5(imagen):
    con1=0 
    filas=len(imagen[:,0])  
    col=len(imagen[0,:])    
    cuarto=int(3*(filas/4))      
    for i in imagen[cuarto,:]:
        if(i==1):
            con1=con1+1
    
    con1=con1/col
    return con1






def p6(imagen):
    con1=0 
    filas=len(imagen[:,0])  
    col=len(imagen[0,:])    
    mitad=int(col/2) 
    for i in imagen[:,mitad]:
        if(i==1):
            con1=con1+1
    
    con1=con1/filas
    return con1






def p7(imagen):
    con1=0 
    filas=len(imagen[:,0])  
    col=len(imagen[0,:])    
    cuarto=int(col/4)
    for i in imagen[:,cuarto]:
        if(i==1):
            con1=con1+1
    
    con1=con1/filas
    return con1






def p8(imagen):
    con1=0
    col=len(imagen[0,:])  
    filas=len(imagen[:,0])
    cuarto3=int(3*col/4)
    for i in imagen[:,cuarto3]:
        if(i==1):
            con1=con1+1
    
    con1=con1/filas
    return con1






def p9(imagen):
    con1=0 
    filas=len(imagen[:,0])  
    col=len(imagen[0,:])   
    mitad=int(filas/2)    
    h=0
    for i in range(len(imagen[mitad,:])-1): 
        x=imagen[mitad,h]
        j=h+1
        y=imagen[mitad,j]
        
        if(y!=x): 
            con1+=1
        
        h+=1
    if imagen[mitad,0]==1:
            con1+=1 
    if  imagen[mitad,(col-1)]==1:
            con1+=1
    return con1 






def p10(imagen):
    con1=0 
    filas=len(imagen[:,0])  
    col=len(imagen[0,:])    
    cuarto=int(filas/4)
    h=0
    for i in range(len(imagen[cuarto,:])-1):
        x=imagen[cuarto,h]
        j=h+1
        y=imagen[cuarto,j]
        
        if(x!=y): 
            con1+=1
        h+=1
    if imagen[cuarto,0]==1:
            con1+=1
    if  imagen[cuarto,(col-1)]==1:
            con1+=1
    return con1






def p11(imagen):
    con1=0 
    filas=len(imagen[:,0])  
    col=len(imagen[0,:])    
    cuarto=int(3*(filas/4))
    h=0
    for i in range(len(imagen[cuarto,:])-1):
        x=imagen[cuarto,h]
        j=h+1
        y=imagen[cuarto,j]
        if(x!=y):
            con1+=1
        h+=1
    if imagen[cuarto,0]==1:
            con1+=1
    if  imagen[cuarto,(col-1)]==1:
            con1+=1
    return con1






def p12(imagen):
    con1=0 
    col=len(imagen[0,:])    
    filas=len(imagen[:,0])  
    mitad=int(col/2)
    h=0
    for i in range(len(imagen[:,mitad])-1):
        x=imagen[h,mitad]
        j=h+1
        y=imagen[j,mitad]
        if(x!=y):
            con1+=1
        h+=1
    if imagen[0,mitad]==1:
            con1+=1
    if  imagen[(filas-1),mitad]==1:
            con1+=1
    
    return con1






def p13(imagen):
    con1=0 
    col=len(imagen[0,:])    
    filas=len(imagen[:,0])  
    cuarto=int(col/4)
    h=0
    for i in range(len(imagen[:,cuarto])-1):
        x=imagen[h,cuarto]
        j=h+1
        y=imagen[j,cuarto]
        
        if(x!=y):
            con1+=1
        h+=1
    if imagen[0,cuarto]==1:
            con1+=1
    if  imagen[(filas-1),cuarto]==1:
            con1+=1
    return con1






def p14(imagen):
    con1=0 
    col=len(imagen[0,:])    
    filas=len(imagen[:,0])  
    cuarto=int(3*(col/4))
    h=0
    for i in range(len(imagen[:,cuarto])-1):
        x=imagen[h,cuarto]
        j=h+1
        y=imagen[j,cuarto]
        
        if(x!=y):
            con1+=1
        h+=1
    if imagen[0,cuarto]==1:
            con1+=1
    if  imagen[(filas-1),cuarto]==1:
            con1+=1
    return con1






def directory(direc):
  lista = [] 
  lista = os.listdir(direc) 
  conta = 0 
  for i in lista:
      conta += 1 
  return conta 






def archivoCSV(arreglo): 
    f = open('dataset.csv', 'w')
    for i in range(len(arreglo)):
        f.write(arreglo[i]+"\n")
    f.close()






def leerCSV(nombre): 
    reader = csv.reader(open('dataset.csv'))
    distancias=[]
    nuevaA=[]
    nueva=instanciaN(nombre).split(",")
    
    for k in nueva:
        nuevaA.append(k) 
    num=0
    for i in reader:
        d=0
        num+=1
        for h in range(len(i)-1):
            xi=float(i[h])
            xj=float(nuevaA[h])
            d+=(xi-xj)**2
        dis=math.sqrt(d)
        distancias.append((num,str(i[14]),dis))
        
    return distancias






def menorMayor(arreglo,k):
    listaord=[]
    listaord = sorted(arreglo, key=operator.itemgetter(2), reverse=False)
    
    
    vecinos=[]
    
    for x in range(0,k):
        vecinos.append(listaord[x])
    
    return vecinos






def kvecinos(arreglo):
    uno=0
    dos=0
    tres=0
    cuatro=0
    cinco=0
    seis=0
    siete=0
    ocho=0
    nueve=0
    zero=0
    lista=[]
    
    for x in arreglo:
        n=int(x[1])
        if n==0:
            zero+=1
        if n==1:
            uno+=1
        if n==2:
            dos+=1
        if n==3:
            tres+=1
        if n==4:
            cuatro+=1
        if n==5:
            cinco+=1
        if n==6:
            seis+=1
        if n==7:
            siete+=1
        if n==8:
            ocho+=1
        if n==9:
            nueve+=1
    lista.append((0,zero))
    lista.append((1,uno))
    lista.append((2,dos))
    lista.append((3,tres))
    lista.append((4,cuatro))
    lista.append((5,cinco))
    lista.append((6,seis))
    lista.append((7,siete))
    lista.append((8,ocho))
    lista.append((9,nueve))
    
    
    
    return lista






def listaOrd(lista):
    listaord = sorted(lista, key=operator.itemgetter(1), reverse=True)
    
    
    f=listaord[0]
    print("--------------------------------------------------------------")
    print(">> RESULTADO <<")
    print ("La imagen pertenece a la clase--->",f[0])
    





def instanciaN(nombre):
    img=mpimg.imread(nombre)
    
    vp1=p1(img)
    vp2=p2(img) 
    vp3=p3(img) 
    vp4=p4(img) 
    vp5=p5(img) 
    vp6=p6(img) 
    vp7=p7(img) 
    vp8=p8(img) 
    vp9=p9(img) 
    vp10=p10(img) 
    vp11=p11(img) 
    vp12=p12(img) 
    vp13=p13(img) 
    vp14=p14(img) 
    
    linea=str(vp1)+","+str(vp2)+","+str(vp3)+","+str(vp4)+","+str(vp5)+","+str(vp6)+","+str(vp7)+","+str(vp8)+","+str(vp9)+","+str(vp10)+","+str(vp11)+","+str(vp12)+","+str(vp13)+","+str(vp14)

    return linea




def menu():
    abrirImagen()
    
    print("\n\nInserta la direccion de la imagen: ")
    
    nombre=input()
    dis=leerCSV(nombre)
    print("Inserta el valor de K")
    
    k=int(input())
    print("---------------------------------------------------------------")
    print(">> INFORMACIÓN GENERAL <<")
    print("# Instancias del dataset: 2376")
    print("# Características por instancia: 14")
    print("# Clases: 10")
    for i in range(0,10):
        print("Clase:",i)
    print("---------------------------------------------------------------")
    vecinos=menorMayor(dis,k)
    print("Valor K=",k)
    j=0
    for i in vecinos:
        j+=1
        
        print("No.",j,"#Instancia",i[0],"Clase:",i[1],"Distancia:",i[2])
    kv=kvecinos(vecinos)
    print("----------------------------------------------------------------")
    print(">> RESUMEN <<")
    for h in kv:
        print ("Clase",h[0],"=",h[1])
    listaOrd(kv)
    
    
    

menu()

