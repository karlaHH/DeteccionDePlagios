







import math
from PIL import Image
import matplotlib.image as mpimg
import csv
import os


 









def caracteristica1(img):
  ima=Image.open(img)
  columnas,filas=ima.size
  razon=filas/columnas
  
  return razon
  
  







def caracteristica2(img):
  ima=Image.open(img)
  imag = mpimg.imread(img)
  columnas,filas=ima.size
  contador1 = 0
  tamano=filas*columnas
  for fils in range(filas):
      for cols in range(columnas):
          if(imag[fils][cols]==1):
              contador1+=1
  
  caracteristica = contador1/tamano
  return caracteristica







def caracteristica3(img):
  ima=Image.open(img)
  imag = mpimg.imread(img)
  columnas,filas=ima.size
  contador1 = 0
  tamano=filas*columnas
  for fils in range(filas):
      if(imag[fils][int(columnas/2)]==1):
          contador1+=1
  
  caracteristica = contador1/tamano
  return caracteristica








def caracteristica4(img):
  ima=Image.open(img)
  imag = mpimg.imread(img)
  columnas,filas=ima.size
  contador1 = 0
  tamano=filas*columnas
  for fils in range(filas):
      if(imag[fils][int(columnas/4)]==1):
          contador1+=1
  
  caracteristica = contador1/tamano
  return caracteristica








def caracteristica5(img):
  ima=Image.open(img)
  imag = mpimg.imread(img)
  columnas,filas=ima.size
  contador1 = 0
  tamano=filas*columnas
  for fils in range(filas):
      if(imag[fils][3*int(columnas/4)]==1):
          contador1+=1
  
  caracteristica = contador1/tamano
  return caracteristica








def caracteristica6(img):
  ima=Image.open(img)
  imag = mpimg.imread(img)
  columnas,filas=ima.size
  contador1 = 0
  tamano=filas*columnas
  for cols in range(columnas):
    if(imag[int(filas/2)][cols]==1):
      contador1+=1
  
  caracteristica = contador1/tamano
  return caracteristica







def caracteristica7(img):
  ima=Image.open(img)
  imag = mpimg.imread(img)
  columnas,filas=ima.size
  contador1 = 0
  tamano=filas*columnas
  for cols in range(columnas):
      if(imag[int(columnas/4)][cols]==1):
          contador1+=1
  
  caracteristica = contador1/tamano
  return caracteristica








def caracteristica8(img):
  ima=Image.open(img)
  imag = mpimg.imread(img)
  columnas,filas=ima.size
  contador1 = 0
  tamano=filas*columnas
  for cols in range(columnas):
      if(imag[3*int(columnas/4)][cols] == 1):
          contador1+=1
          
  
  caracteristica = contador1/tamano
  return caracteristica








def caracteristica9(img):
  ima=Image.open(img)
  imag = mpimg.imread(img)
  columnas,filas=ima.size
  cortes = 0
  
  for indice in range(filas):
      if(imag[indice][int(columnas/2)]==1 and indice==0):
          cortes+=1
      if(imag[indice][int(columnas/2)]!=imag[indice-1][int(columnas/2)] and indice!=0):
          cortes+=1
      if(imag[indice][int(columnas/2)]==1 and indice==(filas-1)):
          cortes+=1
  
  return cortes







def caracteristica10(img):
  ima=Image.open(img)
  imag = mpimg.imread(img)
  columnas,filas=ima.size
  cortes = 0
  
  for indice in range(filas):
      if(imag[indice][int(columnas/4)]==1 and indice==0):
          cortes+=1
      if(imag[indice][int(columnas/4)]!=imag[indice-1][int(columnas/4)] and indice!=0):
          cortes+=1
      if(imag[indice][int(columnas/4)]==1 and indice==(filas-1)):
          cortes+=1          
          
  return cortes








def caracteristica11(img):
  ima=Image.open(img)
  imag = mpimg.imread(img)
  columnas,filas=ima.size
  cortes = 0
  
  
  for indice in range(columnas):
      if(imag[int(3*filas/4)][indice]==1 and indice==0):
          cortes+=1
      if(imag[int(3*filas/4)][indice]!=imag[int(3*filas/4)][indice-1] and indice!=0):
          cortes+=1
      if(imag[int(3*filas/4)][indice]==1 and indice==(columnas-1)):
          cortes+=1  
          
  return cortes







def caracteristica12(img):
  ima=Image.open(img)
  imag = mpimg.imread(img)
  columnas,filas=ima.size
  cortes = 0
  
  for indice in range(columnas):
      if(imag[int(filas/2)][indice]==1 and indice==0):
          cortes+=1
      if(imag[int(filas/2)][indice]!=imag[int(filas/2)][indice-1] and indice!=0):
          cortes+=1
      if(imag[int(filas/2)][indice]==1 and indice==(columnas-1)):
          cortes+=1
          
  return cortes







def caracteristica13(img):
  ima=Image.open(img)
  imag = mpimg.imread(img)
  columnas,filas=ima.size
  cortes = 0
  
  for indice in range(columnas):
      if(imag[int(filas/4)][indice]==1 and indice==0):
          cortes+=1
      if(imag[int(filas/4)][indice]!=imag[int(filas/4)][indice-1] and indice!=0):
          cortes+=1
      if(imag[int(filas/4)][indice]==1 and indice==(columnas-1)):
          cortes+=1
          
  return cortes







def caracteristica14(img):
  ima=Image.open(img)
  imag = mpimg.imread(img)
  columnas,filas=ima.size
  cortes = 0
  
  for indice in range(columnas):
      if(imag[int(3*filas/4)][indice]==1 and indice==0):
          cortes+=1
      if(imag[int(3*filas/4)][indice]!=imag[int(3*filas/4)][indice-1] and indice!=0):
          cortes+=1
      if(imag[int(3*filas/4)][indice]==1 and indice==(columnas-1)):
          cortes+=1
          
  return cortes


def calcular_distancia(d1,d2):
  total = 0.0
  for i in range(len(d1)):
    total+=((float(d1[i])-float(d2[i]))**2)
  return math.sqrt(total)        
    






def dataset():
    archivo=open('Dataset.csv','w',newline='')
    escribir = csv.writer(archivo)
    i=0
    for (path,carpetas,files) in os.walk("img"):
        print(path)
        for im in files:
            
            atributos=[]
            imagen=path+"/"+im
            ruta = (path+"/"+im)
            clase = int(ruta[4])
            c1=caracteristica1(imagen)
            c2=caracteristica2(imagen)
            c3=caracteristica3(imagen)
            c4=caracteristica4(imagen)
            c5=caracteristica5(imagen)
            c6=caracteristica6(imagen)
            c7=caracteristica7(imagen)
            c8=caracteristica8(imagen)
            c9=caracteristica9(imagen)
            c10=caracteristica10(imagen)
            c11=caracteristica11(imagen)
            c12=caracteristica12(imagen)
            c13=caracteristica13(imagen)
            c14=caracteristica14(imagen)
            atributos.append(i+1)
            atributos.append(c1)
            atributos.append(c2)
            atributos.append(c3)
            atributos.append(c4)
            atributos.append(c5)
            atributos.append(c6)
            atributos.append(c7)
            atributos.append(c8)
            atributos.append(c9)
            atributos.append(c10)
            atributos.append(c11)
            atributos.append(c12)
            atributos.append(c13)
            atributos.append(c14)
            dataset = [(atributos[0],atributos[1],atributos[2],atributos[3],atributos[4],atributos[5],atributos[6],atributos[7],atributos[8],atributos[9],atributos[10],atributos[11],atributos[12],atributos[13],atributos[14],clase)]
            escribir.writerows(dataset)
            i+=1
    archivo.close()
    print("\n")
    print ("Dataset creado correctamente")
    print("\n")
    print("El numero total de clases es 10\nClases: 0,1,2,3,4,5,6,7,8,9  \nEl numero total de caracteristicas son 14")
    print("\n")
    print("El numero de instacias es: "+str(i))
    print("\n")



def knn():
  
  print("Ingresa el nombre de la imagen")
  o=input('')+".png"
  atributos=[]
  c1=caracteristica1(o)
  c2=caracteristica2(o)
  c3=caracteristica3(o)
  c4=caracteristica4(o)
  c5=caracteristica5(o)
  c6=caracteristica6(o)
  c7=caracteristica7(o)
  c8=caracteristica8(o)
  c9=caracteristica9(o)
  c10=caracteristica10(o)
  c11=caracteristica11(o)
  c12=caracteristica12(o)
  c13=caracteristica13(o)
  c14=caracteristica14(o)
  atributos.append(c1)
  atributos.append(c2)
  atributos.append(c3)
  atributos.append(c4)
  atributos.append(c5)
  atributos.append(c6)
  atributos.append(c7)
  atributos.append(c8)
  atributos.append(c9)
  atributos.append(c10)
  atributos.append(c11)
  atributos.append(c12)
  atributos.append(c13)
  atributos.append(c14)
  data_temp = [atributos[0],atributos[1],atributos[2],atributos[3],atributos[4],atributos[5],atributos[6],atributos[7],atributos[8],atributos[9],atributos[10],atributos[11],atributos[12],atributos[13]]
  read = csv.reader(open('Dataset.csv','r'))
  datos_distancia = []
  dis = 0
  for index,row in enumerate(read):
    
    y = [float(row[1]),float(row[2]),float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7]),float(row[8]),float(row[9]),float(row[10]),float(row[11]),float(row[12]),float(row[13]),float(row[14])]
    
    dis = calcular_distancia(data_temp,y)
    
    atri = []
    
    atri.append(int(index+1))
    
    atri.append(dis)
    
    atri.append(int(row[15]))
    
    datos_distancia.append(atri)
  
  result_knn(datos_distancia)  
    
    
    
def result_knn(datos_instacia):
  lectura = csv.reader(open("Dataset.csv",'r'))
  print("Ingrese el valor de K")
  k = int(input())
  solo_distancias = []
  for x in range(len(datos_instacia)):
      
      solo_distancias.append(datos_instacia[x][1])
   
  veci = []
  distan = sorted(solo_distancias)
  for i in range(len(distan)):
      if(i == int(k)):
          break
      else:
          veci.append(distan[i])
  print("Numero de Intancias 1733\nNumero de CLases 10 \nNumero de Caracteristicas 14\n")
  print("=========================================================")
  print("\nEl valor de K es ="+str(k)+"\nNo Instancia     Distancia          Clase")
  for z in range(len(datos_instacia)):
    for y in range(len(veci)):
        if(veci[y] == datos_instacia[z][1]):
            print(" "+str(datos_instacia[z][0])+"        "+str(datos_instacia[z][1])+"   "+str(datos_instacia[z][2]))

  
  
  conta=0
  
  uno=0
  dos=0
  tres=0
  cuatro=0
  cinco=0
  seis=0
  siete=0
  ocho=0
  nueve=0
  cero=0
  print("\n")
  print("=========================================================")
  
  for index,row in enumerate(lectura):
    for x in range(k):
        
            if(solo_distancias[conta] == veci[x]):
                if(int(row[15]) == 1):
                    uno+=1
                elif(int(row[15]) == 2):
                    dos+=1
                elif(int(row[15]) == 3):
                    tres+=1
                elif(int(row[15]) == 4):
                    cuatro+=1
                elif(int(row[15]) == 5):
                    cinco+=1
                elif(int(row[15]) == 6):
                    seis+=1
                elif(int(row[15]) == 7):
                    siete+=1
                elif(int(row[15]) == 8):
                    ocho+=1
                elif(int(row[15]) == 9):
                    nueve+=1
                elif(int(row[15]) == 0):
                    cero+=1
    conta+=1
    
     
    
  if(cero>uno and cero>dos and cero>tres and cero>cuatro and cero>cinco and cero>seis and cero>siete and cero> ocho and cero>nueve):
      print("Esta imagen pertenece a la clase cero")
  elif(uno>cero and uno>dos and uno>tres and uno>cuatro and uno>cinco and uno>seis and uno>siete and uno>ocho and uno>nueve):
      print("Esta imagen pertenece a la clase uno")
  elif(dos>cero and dos>uno and dos>tres and dos>cuatro and dos>cinco and dos>seis and dos>siete and dos>ocho and dos>nueve):
      print("Esta imagen pertenece a la clase dos")
  elif(tres>cero and tres>dos and tres>uno and tres>cuatro and tres>cinco and tres>seis and tres>siete and tres>ocho and tres>nueve):
      print("Esta imagen pertenece a la clase tres")
  elif(cuatro>cero and cuatro>dos and cuatro>tres and cuatro>uno and cuatro>cinco and cuatro>seis and cuatro>siete and cuatro>ocho and cuatro>nueve):
      print("Esta imagen pertenece a la clase cuatro")
  elif(cinco>cero and cinco>dos and cinco>tres and cinco>cuatro and cinco>uno and cinco>seis and cinco>siete and cinco>ocho and cinco>nueve):
      print("Esta imagen pertenece a la clase cinco")
  elif(seis>cero and seis>dos and seis>tres and seis>cuatro and seis>cinco and seis>uno and seis>siete and seis>ocho and seis>nueve):
      print("Esta imagen pertenece a la clase seis")
  elif(siete>cero and siete>dos and siete>tres and siete>cuatro and siete>cinco and siete>seis and siete>uno and siete>ocho and siete>nueve):
      print("Esta imagen pertenece a la clase siete")
  elif(ocho>cero and ocho>dos and ocho>tres and ocho>cuatro and ocho>cinco and ocho>seis and ocho>siete and ocho>uno and ocho>nueve):
      print("Esta imagen pertenece a la clase ocho")
  elif(nueve>cero and nueve>dos and nueve>tres and nueve>cuatro and nueve>cinco and nueve>seis and nueve>siete and nueve>ocho and nueve>uno):
      print("Esta imagen pertenece a la clase nueve")
  


def menu():
  os.system('clear')
  menu=1
  while menu==1:
      
      print ("\n")
      print("1.-Crear dataset")
      print("2.-Aplicar metodo de clasificacion Knn")
      opcion=int(input())
      
      if(opcion==1):
          dataset()
      
      elif(opcion==2):
         knn()
         print("=========================================================")
         print("\n")
      else:
          
         print("Ha ingresado una opcion incorrecta")
         menu()
         
      print("Seguir con el programa")
      print("1.-Si")
      print("2.-No")
      menu = int(input())
menu()

