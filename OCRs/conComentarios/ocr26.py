import matplotlib.image as mpimagen ##sirve para trabajar con imagenes como matlab
import os#El módulo os nos permite acceder a funcionalidades dependientes del Sistema Operativo. 
         #Sobre todo, aquellas que nos refieren información sobre el entorno del mismo y 
         #nos permiten manipular la estructura de directorios (para leer y escribir archivos
import csv#Libreria para el manejo de archivos csv

 
#Razón de nFilas/nColumnas  recibimos como parametro las dimensiones de la matriz que conforma la imagen
def RazonFilasnColumnas(Dimensiones):
    
    #Definimos una variable en la cual se almacenara el resultado  de dividir las filas entre las columnas
    RelacionEntreFilasyColumnas=Dimensiones[0]/Dimensiones[1]
    #Imprimimos la variable que almacena el resultado de nFilas/nColumnas de la imagen
    print(RelacionEntreFilasyColumnas)
    #Retornamos nuestra variable
    return RelacionEntreFilasyColumnas

#Funcion para calcular cuntos pixeles conforman la figura en la imagen
#Recibimos como parametros imagen y Dimensiones         
def PixelesQueConformanElAreaDeLaFigura(imagen,Dimensiones):
    #Declaramos un contador el cual inicializamos en 0
    ContadorDePixelesQueConformanElAreaDeLaFigura=0
    #Utilizamos un ciclo for para recorrer las Filas de la matriz asignando un rango que va desde 0 hasta el numero de columnas que conforman la matriz
    for i in range(0,Dimensiones[0]):
        #Utilizamos un segund ciclo for para recorrer las columnas que conforman la matriz
       for j in range(0,Dimensiones[1]):
           #Utilizamos una condicion en la cual decimos que el valor almacenado en la matriz en la posicion [i][j] es diferente de 0  nos aumente el contador
           #de pixeles  que conforman la figura en la imagen
           if(imagen[i][j]!=0):

              ContadorDePixelesQueConformanElAreaDeLaFigura=ContadorDePixelesQueConformanElAreaDeLaFigura+1
    #Imprimimos el contador y este nos arrojara el numero de veces en la que la condicion se cumplio lo que significa el numero de pixeles que conforman la figura en la  imagen          
    print(ContadorDePixelesQueConformanElAreaDeLaFigura)
    #Retornamos nuestra variable           
    return ContadorDePixelesQueConformanElAreaDeLaFigura
#Esta funcion es para encontrar a traves de una posicion situada a un cuarto en relacion a las filas de la matriz las veces en las que hubo un cambio 
#Recibimos como parametros imagen y Dimensiones
def NumeroDeCambiosEfectuadosEnLaFilaPosicionadaAUnCuarto(imagen,Dimensiones):
    #Declaramos una variable la cual almacenara un valor entero dado por la obtencion del Dimensiones del numero de filas entre un valor de 4 para obtener la posicion a un cuarto de la matriz
    PosicionDeLaFilaAunCuarto = int(Dimensiones[0]/4)
    #Declaramos un contador que inicializamos en 0
    ContadorDeCambiosEnLaFilaAunCuarto=0
    #Declaramos una variable auxiliar a la cual asignaremos el valor que contenga la posicion en que inicializamos el recorrido de la matriz para encontrar los cambios efectuados ahi
    aux=imagen[PosicionDeLaFilaAunCuarto][0]
    #inicializamos nuestro ciclo para recorrer las columnas de la matriz
    for i in range(0,Dimensiones[1]):
        #Declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz realice algo
        
        if(aux!=imagen[PosicionDeLaFilaAunCuarto][i]):
            #Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            aux=imagen[PosicionDeLaFilaAunCuarto][i]
            #Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
            ContadorDeCambiosEnLaFilaAunCuarto=ContadorDeCambiosEnLaFilaAunCuarto+1
        #imagen[FilaPosicionadaAunCuarto][i]=1
    #Imprimimos el contador de cambios         
    print(ContadorDeCambiosEnLaFilaAunCuarto)
    #Retornamos nuestra el resultado de nuestra variable
    return ContadorDeCambiosEnLaFilaAunCuarto
#Esta funcion es para encontrar a traves de una posicion situada a la mitad en relacion a las filas de la matriz las veces en las que hubo un cambio
def NumeroDeCambiosEfectuadosEnLaFilaCentral(imagen,Dimensiones):
    #Declaramos una variable la cual almacenara un valor entero dado por la obtencion del Dimensiones del numero de filas entre 2
    PosicionDeLaFilaCentral=int(Dimensiones[0]/2)
    #Declaramos un contador para determinar el numero de cambios que hubo en el recorrido de la matriz y  que inicializamos en 0
    ContadorDeCambiosEnLaFilaCentral=0
    #Declaramos una variable auxiliar a la cual asignaremos el valor que contenga la posicion en que inicializamos el recorrido de la matriz para encontrar los cambios efectuados ahi
    aux=imagen[PosicionDeLaFilaCentral][0]
    #inicializamos nuestro ciclo para recorrer las columnas de la matriz
    for i in range(0,Dimensiones[1]):
        #Declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz realice algo       
        if(aux!=imagen[PosicionDeLaFilaCentral][i]):
          #Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz  
          aux=imagen[PosicionDeLaFilaCentral][i]
          #Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
          ContadorDeCambiosEnLaFilaCentral=ContadorDeCambiosEnLaFilaCentral+1
        #imagen[mitadHo][i]=1   
    #Imprimimos el contador de cambios       
    print(ContadorDeCambiosEnLaFilaCentral)
    return ContadorDeCambiosEnLaFilaCentral
#Esta funcion es para encontrar a traves de una posicion situada a la mitad en relacion a las filas de la matriz las veces en las que hubo un cambio 
def NumeroDeCambiosEfectuadosEnLaFilaPosicionadaATresCuartos(imagen,Dimensiones):
    #Declaramos una variable la cual almacenara un valor entero dado por la obtencion del Dimensiones del numero de filas entre 4 y multiplicado por tres para obtener la posicion a Tres Cuartos
    PosicionDeLaFilaATresCuartos=int((Dimensiones[0]/4)*3)
    #Declaramos un contador para determinar el numero de cambios que hubo en el recorrido de la matriz y  que inicializamos en 0
    ContadorDeCambiosEnLaFilaATresCuartos=0
    #Declaramos una variable auxiliar a la cual asignaremos el valor que contenga la posicion en que inicializamos el recorrido de la matriz 
    aux=imagen[PosicionDeLaFilaATresCuartos][0]
    #inicializamos nuestro ciclo para recorrer las Columnas de la matriz
    for i in range(0,Dimensiones[1]):
        if(aux!=imagen[PosicionDeLaFilaATresCuartos][i]):
            aux=imagen[PosicionDeLaFilaATresCuartos][i]
            ContadorDeCambiosEnLaFilaATresCuartos=ContadorDeCambiosEnLaFilaATresCuartos+1
        #imagen[TLinea][i]=1    
    print(ContadorDeCambiosEnLaFilaATresCuartos)
    
    return ContadorDeCambiosEnLaFilaATresCuartos    
#En esta funcion calculamos en que posisicion se encuentra un cuarto de la matriz con respecto a lñas columnas
#Recibimos como parametros imagen y Dimensiones    
def NumeroDeCambioEfectuadosEnLaColumnaAUnCuarto(imagen,Dimensiones):
    #Declaramos una variable la cual almacenara un valor entero dado por la obtencion de Dimensiones del numero de columnas entre 4  para obtener la posicion a un  Cuarto
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/4)
    #Declaramos un contador para determinar el numero de cambios que hubo en el recorrido de la matriz y  que inicializamos en 0
    ContadorDeCambiosEnLaColumnaAUnCuarto=0
    #Declaramos una variable auxiliar a la cual asignaremos el valor que contenga la posicion en que inicializamos el recorrido de la matriz 
    aux=imagen[0][PosicionDeLaColumnaAUnCuarto]
    for i in range(0,Dimensiones[0]):
        if(aux!=imagen[i][PosicionDeLaColumnaAUnCuarto]):
            aux=imagen[i][PosicionDeLaColumnaAUnCuarto]
            ContadorDeCambiosEnLaColumnaAUnCuarto=ContadorDeCambiosEnLaColumnaAUnCuarto+1
        #imagen[i][pv]=1    
    print(ContadorDeCambiosEnLaColumnaAUnCuarto)
    return ContadorDeCambiosEnLaColumnaAUnCuarto
#En esta funcion calculamos la posiscion que ocupa la columna central de la matriz 
#Dividiendo entre 2 el total de las columnas 
#con ello pretendemos saber cuantas veces hubo un cambio en esa columna    
def NumeroDeCambioEfectuadosEnLaColumnaCentral(imagen,Dimensiones):
    PosicionDeLaColumnaCentral=int(Dimensiones[1]/2)
    ContadorDeCambiosEnLaColumnaCentral=0
    aux=imagen[0][PosicionDeLaColumnaCentral]
    for i in range(0,Dimensiones[0]):
        
        if(aux!=imagen[i][PosicionDeLaColumnaCentral]):
            aux=imagen[i][PosicionDeLaColumnaCentral]
            ContadorDeCambiosEnLaColumnaCentral=ContadorDeCambiosEnLaColumnaCentral+1
        #imagen[i][V]=1
    print(ContadorDeCambiosEnLaColumnaCentral)
    #Retornamos la variable que contiene el resultado de los cambios efectuados 
    return ContadorDeCambiosEnLaColumnaCentral
#En esta funcion calculamos la posiscion que ocupa la columna a tres cuartos  de la matriz
#Dividiendo el total de las columnas entre 4 y multiplicandola por 3
#utilizaremos nuevamente una variable auxiliar la cual no ayudara encontrar los cambios que se generan en esa parte de la matriz
def NumeroDeCambioEfectuadosEnLaColumnaATresCuartos(imagen,Dimensiones):
    PosicionDeLaColumnaATresCuartos=int((Dimensiones[1]/4)*3)
    ContadorDeCambiosEnLaColumnaATresCuartos=0
    aux=imagen[0][PosicionDeLaColumnaATresCuartos]
    for i in range(0,Dimensiones[0]):
        if(aux!=imagen[i][PosicionDeLaColumnaATresCuartos]):
            aux=imagen[i][PosicionDeLaColumnaATresCuartos]
            ContadorDeCambiosEnLaColumnaATresCuartos=ContadorDeCambiosEnLaColumnaATresCuartos+1
        #imagen[i][TV]=1
    print(ContadorDeCambiosEnLaColumnaATresCuartos)
    #Retornamos la variable que contiene el resultado de los cambios efectuados 
    return ContadorDeCambiosEnLaColumnaATresCuartos
#En esta funcion calculamos la posicion a un cuarto de la matriz y los pixeles que forman parte de la figura en esta columna  
def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto(imagen,Dimensiones):
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/4)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto=0
    
    for i in range(0,Dimensiones[0]):
        #La condicion espara que cada que encuetre un valor distinto a 0 lo tome en cuenta
        if(imagen[i][PosicionDeLaColumnaAUnCuarto]!=0):
            #el contador aumentara cada que la ondicion detecte un valor diferente a 0
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto+1
        #imagen[i][PLV]=1    
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto)   
    #Retornamos la variable que alverga el resultado calculado en la funcion
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto
#En esta funcion calculamos la posicion de la columna central de la matriz 
#Contamos los pixeles que conforman la figura en esta columna     
def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral(imagen,Dimensiones):
    #Declaramos una variable que alberga un valor entero calculado a partir de la divicion entre el total de columnas entre 2    
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/2)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral=0
    #El ciclo recorre las filas
    for i in range(0,Dimensiones[0]):
        #La condicion espara que cada que encuetre un valor distinto a 0 lo tome en cuenta

        if(imagen[i][PosicionDeLaColumnaAUnCuarto]!=0):
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral+1
        #imagen[i][ML]=1    
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral)
    #Retornamos la variable que contiene el resultado calculado de los pixeles en la columna
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral
#En esta funcion calculamos la posicion de la columna situada a tres cuartos de la matriz
#Dividiendo el total de las columnas entre 4 y multiplicandola por 3 almacenando el resultado en 
#una variable de tipo entero     
def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos(imagen,Dimensiones):
    PosicionDeLaColumnaATresCuartos=int((Dimensiones[1]/4)*3)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos=0
    #El ciclo recorre las filas
    for i in range(0,Dimensiones[0]):
        #La condicion es para detectar dentro del la columna que hemos especificado 
        #Los pixeles que conforman la imagen 
        if(imagen[i][PosicionDeLaColumnaATresCuartos]!=0):
            #Cada que la condicion se cumpla un contador ira en aumento 
            #obtendremos el numero de pixeles en esa columna que forman parte de la figura
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos+1
        #imagen[i][TLV]=1    
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos) 
    #Retornamos la variable que contiene el reusultado de pixeles 
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos
#En esta funcion calculamos la posicion de la fila situada a un cuartos de la matriz
#Dividiendo el total de filas entre 4 el resultado lo guardamos en una variable de tipo entero    
def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaAUnCuarto(imagen,Dimensiones):
    PosicionDeLaFilaAUnCuarto=int(Dimensiones[0]/4)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos=0
    #Recorremos las columnas 
    for i in range(0,Dimensiones[1]):
        #La condicion es para detectar dentro del la fila que hemos especificado 
        #Los pixeles que conforman la imagen 
        if(imagen[PosicionDeLaFilaAUnCuarto][i]!=0):
            #Cada que la condicion se cumpla un contador ira en aumento 
            #obtendremos el numero de pixeles en esa fila que forman parte de la figura
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos+1
        #imagen[PLH][i]=1    
    #Imprimimos el resultado del contador        
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos)
    #Retornamos la variable que contiene el resultado de los pixeles 
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos
#En esta funcion calculamos la posicion que ocupa la fila central de la matriz 
#Guardamos en resultado en una variable de tipo entero al dividir el total de filas entre 2
def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaCentral(imagen,Dimensiones):
    PLH=int(Dimensiones[0]/2)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral=0
    #Recorremos las columas
    for i in range(0,Dimensiones[1]):
        #La condicion es para detectar dentro del la fila que hemos especificado 
        #Los pixeles que conforman la imagen 
        if(imagen[PLH][i]!=0):
            #Cada que la condicion se cumpla un contador ira en aumento 
            #obtendremos el numero de pixeles en esa fila que forman parte de la figura
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral+1
        #imagen[PLH][i]=1
    #Imprimimos el resultado del contador        
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral) 
    #Retornamos la variable que contiene el resultado de los pixeles
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral
#En esta funcion calculamos la posicion que ocupa la fila a tres cuartos de la matriz 
#Guardamos en resultado en una variable de tipo entero al dividir el total de filas entre 4 y multiplicamos por 3    
def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaATresCuartos(imagen,Dimensiones):
    PLH=int((Dimensiones[0]/4)*3)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos=0
    #Recorremos las columas
    for i in range(0,Dimensiones[1]):
        #Cada que la condicion se cumpla un contador ira en aumento 
        #obtendremos el numero de pixeles en esa fila que forman parte de la figura
        if(imagen[PLH][i]!=0):
            #Cada que la condicion se cumpla un contador ira en aumento 
            #obtendremos el numero de pixeles en esa fila que forman parte de la figura
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos+1
       # imagen[PLH][i]=1  
       #Imprimimos el contador     
    print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos)
    #Retornamos la variable que contiene el resultado de los pixeles
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos

#En esta funcion recibimos como parametros las variables que contienen los resultados de las funciones anteriores
#para comenzar a generar en un documento todas las caracteristicas de las imagenes que se usaran como instancias
def GenerarDataSet(RazonFilasnColumnas,PixelesQueConformanElAreaDeLaFigura,NumeroDeCambiosEfectuadosEnLaFilaPosicionadaAUnCuarto,NumeroDeCambiosEfectuadosEnLaFilaCentral,NumeroDeCambiosEfectuadosEnLaFilaPosicionadaATresCuartos,NumeroDeCambioEfectuadosEnLaColumnaAUnCuarto,NumeroDeCambioEfectuadosEnLaColumnaCentral,NumeroDeCambioEfectuadosEnLaColumnaATresCuartos,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaAUnCuarto,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaCentral,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaATresCuartos):
#Designamos la carpeta en la cual se comenzara el recorrido de subcarpetas que contienen lasimagnes 
    Carpeta='arialSegmented'
#Creamos el archivo con la extencion csv 
    Archivo=open('DataSet.csv','w',newline='')
#Como salida obtenemos el archivo que fue escrito con las caracteristicas obtenidas del conjunto de imagenes
    salida=csv.writer(Archivo)
#Esta variable es un contador que aumentara conforme entra a otra subcarpeta para extraer las caracteristicas del conjunto de imagenes que alberga
    clase=-1
#Declaramos un ciclo for para recorrer la carpeta,subcarpetas y archivos que se encuentran en la carpeta raiz
    for dir, subdirlist, filelist in os.walk(Carpeta):
    #Un segundo ciclo  for para recorrer imagen por imagen dentro de una lista de imagenes     
      for fname in filelist:
        
        #Asignamos a una variable la direccion y el nombre de la imagen que se le  extraeran sus caracteristicas 
        Direccionimagen=dir+'/'+fname
        
        imagen=mpimagen.imread(Direccionimagen)
        #Mostramos la imagen
        #imagenplot=plt.imshow(imagen)
        
        
#Utilizamos el atributo shape para retornar las dimensiones de la matriz que conforma la imagen
#Asignamos el Dimensiones de la matriz a una variable llamada Dimensiones 
        Dimensiones=imagen.shape
        print('Dimensiones de la imagen ',Dimensiones)
     #Mandamos a llamar nuestras funciones para mostrar los procesos de calculo que se efectuaron    
     #Declaramos variables y  asignamos  el valor que se generaron en cada funcion    
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
      #Esta linea nos sirve para ir escribiendo los valores dentro del archivo que creamos anteriormente
      #entre parentesis y corchetes se colocan las variables que almacenan los recultados 
      #Estos se dejara de efectuar hasta que no encuentre mas resultados que almacenar en el documento   
        salida.writerow([FilaEntreColumna,AreaDeLaFigura,NumeroDeCambiosFilaUcCuarto,
                         NumeroDeCambiosFilaCentral, NumeroDeCambiosFilaTresCuartos, 
                         NumeroDeCambiosColumnasaUCuarto, NumeroDeCambiosColumnCentral, 
                         NumeroDeCambiosColumnaTresCuartos, NumeroPixelesColumnaUnCuarto,
                         NumeroPixelesColumnaCentral,NumeroPixelesColumnaTresCuartos,
                         NumeroPixelesFilaUnCuarto,NumeroPixelesFilaCentral,NumeroPixelesFilaTresCuartos,clase])
    #La variable clase hace referencia a las subcarpetas que va analizando el codigo para ir obteniendo las caracteristicas del conjunto de imagenes
    #Esta ira aunmentado de uno en uno cada que analice una nueva subcarpeta                     
      clase=clase+1
    print(clase)
#Cerramos el archivo una vez que se termina de generar el socumento     
    Archivo.close()
    #Retornamos la imagen y las dimensiones de cada una
    return(imagen,Dimensiones)                               

#Mandamos a llamar nuestra funcion principal que es la de generar dataset para que esta ejecute todas las demas funciones.    
GenerarDataSet(RazonFilasnColumnas,PixelesQueConformanElAreaDeLaFigura,NumeroDeCambiosEfectuadosEnLaFilaPosicionadaAUnCuarto,NumeroDeCambiosEfectuadosEnLaFilaCentral,NumeroDeCambiosEfectuadosEnLaFilaPosicionadaATresCuartos,NumeroDeCambioEfectuadosEnLaColumnaAUnCuarto,NumeroDeCambioEfectuadosEnLaColumnaCentral,NumeroDeCambioEfectuadosEnLaColumnaATresCuartos,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral,NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaAUnCuarto,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaCentral,NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaATresCuartos)


import matplotlib.image as mpimg #sirve para trabajar con imagenes como matlab
import csv #Libreria para el manejo de archivos csv
import math#Poporsiona acceso a las funciones matematicas 
#Funcion para leer acceder a los datos en el dataset 
def LeerDataset():
    #Con esta linea seleccionamos el archiv que vamos a utilizar para lectura de datos
    SeleccionarDataset= open('DataSet.csv')
    #Utilizamos el atributo reader para leer linea por linea el contenido del archivo que seleccionamos
    lns=csv.reader(SeleccionarDataset) 

    dataset=list(lns)
    return dataset
#Funcion para seleccionar la imagen    
def SeleccionarImagen():
    print("Ingresa el nombre de la imagen ",end="")
    Nombre=(input())
    #Cargamos la imagen que vamos a utilizar como nueva instancia 
    imagen=mpimg.imread('imagenes de prueba'+'/'+Nombre)
    #Mostramos la imagen
    #imgplot=plt.imshow(img)
    #Utilizamos el atributo shape para retornar las dimensiones de la matriz que conforma la imagen
    #Asignamos el tamaño de la matriz a una variable llamada Dimensiones 
    return imagen
#Funcion para obtener las dimensiones de la imagen    
def CalcularDimensiones(imagen):
    Dimensiones=imagen.shape
    return Dimensiones
#Imprimimos las dimensiones de la imagen como referencia del numero de filas y columnas que la conforman 
#print('Dimenciones de la imagen ',Dimensiones)
 
#Razón de nFilas/nColumnas  recibimos como parametro las dimensiones de la matriz que conforma la imagen
def RazonFilasnColumnasNuevaInstancia(Dimensiones):
    
    #Definimos una variable en la cual se almacenara el resultado  de dividir las filas entre las columnas
    RelacionEntreFilasyColumnas=Dimensiones[0]/Dimensiones[1]
    #Imprimimos la variable que almacena el resultado de nFilas/nColumnas de la imagen
    #print(RelacionEntreFilasyColumnas)
    #Retornamos nuestra variable
    return RelacionEntreFilasyColumnas

#Funcion para calcular cuntos pixeles conforman la figura en la imagen
#Recibimos como parametros imagen y Dimensiones         
def PixelesQueConformanElAreaDeLaFiguraNuevaInstancia(imagen,Dimensiones):
    #Declaramos un contador el cual inicializamos en 0
    ContadorDePixelesQueConformanElAreaDeLaFigura=0
    #Utilizamos un ciclo for para recorrer las Filas de la matriz asignando un rango que va desde 0 hasta el numero de columnas que conforman la matriz
    for i in range(0,Dimensiones[0]):
        #Utilizamos un segund ciclo for para recorrer las columnas que conforman la matriz
       for j in range(0,Dimensiones[1]):
           #Utilizamos una condicion en la cual decimos que el valor almacenado en la matriz en la posicion [i][j] es diferente de 0  nos aumente el contador
           #de pixeles  que conforman la figura en la imagen
           if(imagen[i][j]!=0):

              ContadorDePixelesQueConformanElAreaDeLaFigura=ContadorDePixelesQueConformanElAreaDeLaFigura+1
    #Imprimimos el contador y este nos arrojara el numero de veces en la que la condicion se cumplio lo que significa el numero de pixeles que conforman la figura en la  imagen          
    #print(ContadorDePixelesQueConformanElAreaDeLaFigura)
    #Retornamos nuestra variable           
    return ContadorDePixelesQueConformanElAreaDeLaFigura
#Esta funcion es para encontrar a traves de una posicion situada a un cuarto en relacion a las filas de la matriz las veces en las que hubo un cambio 
#Recibimos como parametros imagen y Dimensiones
def NumeroDeCambiosEfectuadosEnLaFilaPosicionadaAUnCuartoNuevaInstancia(imagen,Dimensiones):
    #Declaramos una variable la cual almacenara un valor entero dado por la obtencion del Dimensiones del numero de filas entre un valor de 4 para obtener la posicion a un cuarto de la matriz
    PosicionDeLaFilaAunCuarto = int(Dimensiones[0]/4)
    #Declaramos un contador que inicializamos en 0
    ContadorDeCambiosEnLaFilaAunCuarto=0
    #Declaramos una variable auxiliar a la cual asignaremos el valor que contenga la posicion en que inicializamos el recorrido de la matriz para encontrar los cambios efectuados ahi
    aux=imagen[PosicionDeLaFilaAunCuarto][0]
    #inicializamos nuestro ciclo para recorrer las columnas de la matriz
    for i in range(0,Dimensiones[1]):
        #Declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz realice algo
        
        if(aux!=imagen[PosicionDeLaFilaAunCuarto][i]):
            #Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz
            aux=imagen[PosicionDeLaFilaAunCuarto][i]
            #Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
            ContadorDeCambiosEnLaFilaAunCuarto=ContadorDeCambiosEnLaFilaAunCuarto+1
        #imagen[FilaPosicionadaAunCuarto][i]=1
    #Imprimimos el contador de cambios         
    #print(ContadorDeCambiosEnLaFilaAunCuarto)
    #Retornamos nuestra el resultado de nuestra variable
    return ContadorDeCambiosEnLaFilaAunCuarto
#Esta funcion es para encontrar a traves de una posicion situada a la mitad en relacion a las filas de la matriz las veces en las que hubo un cambio
def NumeroDeCambiosEfectuadosEnLaFilaCentralNuevaInstancia(imagen,Dimensiones):
    #Declaramos una variable la cual almacenara un valor entero dado por la obtencion del Dimensiones del numero de filas entre 2
    PosicionDeLaFilaCentral=int(Dimensiones[0]/2)
    #Declaramos un contador para determinar el numero de cambios que hubo en el recorrido de la matriz y  que inicializamos en 0
    ContadorDeCambiosEnLaFilaCentral=0
    #Declaramos una variable auxiliar a la cual asignaremos el valor que contenga la posicion en que inicializamos el recorrido de la matriz para encontrar los cambios efectuados ahi
    aux=imagen[PosicionDeLaFilaCentral][0]
    #inicializamos nuestro ciclo para recorrer las columnas de la matriz
    for i in range(0,Dimensiones[1]):
        #Declaramos una condicion en la cual especificamos que si nuestra variable auxiliar es diferente del valor que se encuentre en la posicion que inicializamos en el recorrido de la mtriz realice algo       
        if(aux!=imagen[PosicionDeLaFilaCentral][i]):
          #Cuando la condicion se cumpla le reasignamos el valor a nuestra variable auxiliar para que esta tenga el valor en la que se encuentra la matriz  
          aux=imagen[PosicionDeLaFilaCentral][i]
          #Nuestro contador de cambios aumenta en uno cada vez que la condicion se cumpla
          ContadorDeCambiosEnLaFilaCentral=ContadorDeCambiosEnLaFilaCentral+1
        #imagen[mitadHo][i]=1   
    #Imprimimos el contador de cambios       
    #print(ContadorDeCambiosEnLaFilaCentral)
    return ContadorDeCambiosEnLaFilaCentral
#Esta funcion es para encontrar a traves de una posicion situada a la mitad en relacion a las filas de la matriz las veces en las que hubo un cambio 
def NumeroDeCambiosEfectuadosEnLaFilaPosicionadaATresCuartosNuevaInstancia(imagen,Dimensiones):
    #Declaramos una variable la cual almacenara un valor entero dado por la obtencion del Dimensiones del numero de filas entre 4 y multiplicado por tres para obtener la posicion a Tres Cuartos
    PosicionDeLaFilaATresCuartos=int((Dimensiones[0]/4)*3)
    #Declaramos un contador para determinar el numero de cambios que hubo en el recorrido de la matriz y  que inicializamos en 0
    ContadorDeCambiosEnLaFilaATresCuartos=0
    #Declaramos una variable auxiliar a la cual asignaremos el valor que contenga la posicion en que inicializamos el recorrido de la matriz 
    aux=imagen[PosicionDeLaFilaATresCuartos][0]
    #inicializamos nuestro ciclo para recorrer las Columnas de la matriz
    for i in range(0,Dimensiones[1]):
        if(aux!=imagen[PosicionDeLaFilaATresCuartos][i]):
            aux=imagen[PosicionDeLaFilaATresCuartos][i]
            ContadorDeCambiosEnLaFilaATresCuartos=ContadorDeCambiosEnLaFilaATresCuartos+1
        #imagen[TLinea][i]=1    
    #print(ContadorDeCambiosEnLaFilaATresCuartos)
    
    return ContadorDeCambiosEnLaFilaATresCuartos    
#En esta funcion calculamos en que posisicion se encuentra un cuarto de la matriz con respecto a lñas columnas
#Recibimos como parametros imagen y Dimensiones    
def NumeroDeCambioEfectuadosEnLaColumnaAUnCuartoNuevaInstancia(imagen,Dimensiones):
    #Declaramos una variable la cual almacenara un valor entero dado por la obtencion de Dimensiones del numero de columnas entre 4  para obtener la posicion a un  Cuarto
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/4)
    #Declaramos un contador para determinar el numero de cambios que hubo en el recorrido de la matriz y  que inicializamos en 0
    ContadorDeCambiosEnLaColumnaAUnCuarto=0
    #Declaramos una variable auxiliar a la cual asignaremos el valor que contenga la posicion en que inicializamos el recorrido de la matriz 
    aux=imagen[0][PosicionDeLaColumnaAUnCuarto]
    for i in range(0,Dimensiones[0]):
        if(aux!=imagen[i][PosicionDeLaColumnaAUnCuarto]):
            aux=imagen[i][PosicionDeLaColumnaAUnCuarto]
            ContadorDeCambiosEnLaColumnaAUnCuarto=ContadorDeCambiosEnLaColumnaAUnCuarto+1
        #imagen[i][pv]=1    
    #print(ContadorDeCambiosEnLaColumnaAUnCuarto)
    return ContadorDeCambiosEnLaColumnaAUnCuarto
#En esta funcion calculamos la posiscion que ocupa la columna central de la matriz 
#Dividiendo entre 2 el total de las columnas 
#con ello pretendemos saber cuantas veces hubo un cambio en esa columna    
def NumeroDeCambioEfectuadosEnLaColumnaCentralNuevaInstancia(imagen,Dimensiones):
    PosicionDeLaColumnaCentral=int(Dimensiones[1]/2)
    ContadorDeCambiosEnLaColumnaCentral=0
    aux=imagen[0][PosicionDeLaColumnaCentral]
    for i in range(0,Dimensiones[0]):
        
        if(aux!=imagen[i][PosicionDeLaColumnaCentral]):
            aux=imagen[i][PosicionDeLaColumnaCentral]
            ContadorDeCambiosEnLaColumnaCentral=ContadorDeCambiosEnLaColumnaCentral+1
        #imagen[i][V]=1
    #print(ContadorDeCambiosEnLaColumnaCentral)
    #Retornamos la variable que contiene el resultado de los cambios efectuados 
    return ContadorDeCambiosEnLaColumnaCentral
#En esta funcion calculamos la posiscion que ocupa la columna a tres cuartos  de la matriz
#Dividiendo el total de las columnas entre 4 y multiplicandola por 3
#utilizaremos nuevamente una variable auxiliar la cual no ayudara encontrar los cambios que se generan en esa parte de la matriz
def NumeroDeCambioEfectuadosEnLaColumnaATresCuartosNuevaInstancia(imagen,Dimensiones):
    PosicionDeLaColumnaATresCuartos=int((Dimensiones[1]/4)*3)
    ContadorDeCambiosEnLaColumnaATresCuartos=0
    aux=imagen[0][PosicionDeLaColumnaATresCuartos]
    for i in range(0,Dimensiones[0]):
        if(aux!=imagen[i][PosicionDeLaColumnaATresCuartos]):
            aux=imagen[i][PosicionDeLaColumnaATresCuartos]
            ContadorDeCambiosEnLaColumnaATresCuartos=ContadorDeCambiosEnLaColumnaATresCuartos+1
        #imagen[i][TV]=1
    #print(ContadorDeCambiosEnLaColumnaATresCuartos)
    #Retornamos la variable que contiene el resultado de los cambios efectuados 
    return ContadorDeCambiosEnLaColumnaATresCuartos
#En esta funcion calculamos la posicion a un cuarto de la matriz y los pixeles que forman parte de la figura en esta columna  
def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuartoNuevaInstancia(imagen,Dimensiones):
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/4)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto=0
    
    for i in range(0,Dimensiones[0]):
        #La condicion espara que cada que encuetre un valor distinto a 0 lo tome en cuenta
        if(imagen[i][PosicionDeLaColumnaAUnCuarto]!=0):
            #el contador aumentara cada que la ondicion detecte un valor diferente a 0
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto+1
        #imagen[i][PLV]=1    
    #print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto)   
    #Retornamos la variable que alverga el resultado calculado en la funcion
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto
#En esta funcion calculamos la posicion de la columna central de la matriz 
#Contamos los pixeles que conforman la figura en esta columna     
def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentralNuevaInstancia(imagen,Dimensiones):
    #Declaramos una variable que alberga un valor entero calculado a partir de la divicion entre el total de columnas entre 2    
    PosicionDeLaColumnaAUnCuarto=int(Dimensiones[1]/2)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral=0
    #El ciclo recorre las filas
    for i in range(0,Dimensiones[0]):
        #La condicion espara que cada que encuetre un valor distinto a 0 lo tome en cuenta

        if(imagen[i][PosicionDeLaColumnaAUnCuarto]!=0):
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral+1
        #imagen[i][ML]=1    
    #print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral)
    #Retornamos la variable que contiene el resultado calculado de los pixeles en la columna
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral
#En esta funcion calculamos la posicion de la columna situada a tres cuartos de la matriz
#Dividiendo el total de las columnas entre 4 y multiplicandola por 3 almacenando el resultado en 
#una variable de tipo entero     
def NumeroDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartosNuevaInstancia(imagen,Dimensiones):
    PosicionDeLaColumnaATresCuartos=int((Dimensiones[1]/4)*3)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos=0
    #El ciclo recorre las filas
    for i in range(0,Dimensiones[0]):
        #La condicion es para detectar dentro del la columna que hemos especificado 
        #Los pixeles que conforman la imagen 
        if(imagen[i][PosicionDeLaColumnaATresCuartos]!=0):
            #Cada que la condicion se cumpla un contador ira en aumento 
            #obtendremos el numero de pixeles en esa columna que forman parte de la figura
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos+1
        #imagen[i][TLV]=1    
    #print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos) 
    #Retornamos la variable que contiene el reusultado de pixeles 
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos
#En esta funcion calculamos la posicion de la fila situada a un cuartos de la matriz
#Dividiendo el total de filas entre 4 el resultado lo guardamos en una variable de tipo entero    
def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaAUnCuartoNuevaInstancia(imagen,Dimensiones):
    PosicionDeLaFilaAUnCuarto=int(Dimensiones[0]/4)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos=0
    #Recorremos las columnas 
    for i in range(0,Dimensiones[1]):
        #La condicion es para detectar dentro del la fila que hemos especificado 
        #Los pixeles que conforman la imagen 
        if(imagen[PosicionDeLaFilaAUnCuarto][i]!=0):
            #Cada que la condicion se cumpla un contador ira en aumento 
            #obtendremos el numero de pixeles en esa fila que forman parte de la figura
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos+1
        #imagen[PLH][i]=1    
    #Imprimimos el resultado del contador        
    #print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos)
    #Retornamos la variable que contiene el resultado de los pixeles 
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos
#En esta funcion calculamos la posicion que ocupa la fila central de la matriz 
#Guardamos en resultado en una variable de tipo entero al dividir el total de filas entre 2
def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaCentralNuevaInstancia(imagen,Dimensiones):
    PLH=int(Dimensiones[0]/2)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral=0
    #Recorremos las columas
    for i in range(0,Dimensiones[1]):
        #La condicion es para detectar dentro del la fila que hemos especificado 
        #Los pixeles que conforman la imagen 
        if(imagen[PLH][i]!=0):
            #Cada que la condicion se cumpla un contador ira en aumento 
            #obtendremos el numero de pixeles en esa fila que forman parte de la figura
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral+1
        #imagen[PLH][i]=1
    #Imprimimos el resultado del contador        
    #print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral) 
    #Retornamos la variable que contiene el resultado de los pixeles
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral
#En esta funcion calculamos la posicion que ocupa la fila a tres cuartos de la matriz 
#Guardamos en resultado en una variable de tipo entero al dividir el total de filas entre 4 y multiplicamos por 3    
def NumeroDePixelesQueConformanParteDeLaFiguraEnLaFilaATresCuartosNuevaInstancia(imagen,Dimensiones):
    PLH=int((Dimensiones[0]/4)*3)
    ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos=0
    #Recorremos las columas
    for i in range(0,Dimensiones[1]):
        #Cada que la condicion se cumpla un contador ira en aumento 
        #obtendremos el numero de pixeles en esa fila que forman parte de la figura
        if(imagen[PLH][i]!=0):
            #Cada que la condicion se cumpla un contador ira en aumento 
            #obtendremos el numero de pixeles en esa fila que forman parte de la figura
            ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos=ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos+1
       # imagen[PLH][i]=1  
       #Imprimimos el contador     
    #print(ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos)
    #Retornamos la variable que contiene el resultado de los pixeles
    return ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos
def Vecinos():
    #Mensaje que nos pide agreguemos el numero de kvecinos a considerar    
    print("Numero de vecinos a considerar: ",end="")
    #Con esta linea asignamos a una variable el valor de entrada que asignemos desde teclado
    NumerokVecinos=int(input())
    #Imprimimos un salto de linea para dar un poco de formato en la impresion
    print('\n')
    return NumerokVecinos
#Declaramos un contador que va desde 0 

def KNN(dataset,NumerokVecinos,Dimensiones,RelacionEntreFilasyColumnas,ContadorDePixelesQueConformanElAreaDeLaFigura,ContadorDeCambiosEnLaFilaAunCuarto,ContadorDeCambiosEnLaFilaCentral,ContadorDeCambiosEnLaFilaATresCuartos,ContadorDeCambiosEnLaColumnaAUnCuarto,ContadorDeCambiosEnLaColumnaCentral,ContadorDeCambiosEnLaColumnaATresCuartos,ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaAUnCuarto,ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaCentral,ContadorDePixelesQueFormanParteDeLaFiguraEnLaColumnaATresCuartos,ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaAUnCuartos,ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaCentral,ContadorDePixelesQueFormanParteDeLaFiguraEnLaFilaATresCuartos):
   contadordeInstancias=0

#Mandamos a llamar nuestras funciones para mostrar los procesos de calculo que se efectuaron    
#Declaramos variables y  asignamos  el valor que se generaron en cada funcion    
   #Recorremos las filas y columnas del dataset para acceder a los datos que tiene nuestro archivo
   for i in dataset:
          dataset[contadordeInstancias][0]=float(dataset[contadordeInstancias][0])#Asignamos los valores que tiene cada columna a cada posicion de la matriz y convertimos los valores a valores numericos
          dataset[contadordeInstancias][1]=int(dataset[contadordeInstancias][1])  #entero y en el caso de la primera posicion flotante puesto que los valores que estamos obteniendo al ser una funcion de lectura
          dataset[contadordeInstancias][2]=int(dataset[contadordeInstancias][2])  #Recibimos puros caracteres y no valores numericos
          dataset[contadordeInstancias][3]=int(dataset[contadordeInstancias][3])  # por ello convertimos el tipo de variable para 
          dataset[contadordeInstancias][4]=int(dataset[contadordeInstancias][4])  # poder realizar operaciones con el archivo
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
          
          
          #En esta linea Declaramos una variable en la cual le asignaremos el valor que resulte
          #de calcular entre las caracteristicas obtenidas del dataset con las caracteristicas de la
          #imagen que recibimos como nueva instancia
          OperacionesCaracteristicasNuevasInstancias=((dataset[contadordeInstancias][0]-FilaEntreColumna)**2)+((dataset[contadordeInstancias][1]-AreaDeLaFigura)**2)+((dataset[contadordeInstancias][2]-NumeroDeCambiosFilaUcCuarto)**2)+((dataset[contadordeInstancias][3]-NumeroDeCambiosFilaCentral)**2)+((dataset[contadordeInstancias][4]-NumeroDeCambiosFilaTresCuartos)**2)+((dataset[contadordeInstancias][5]-NumeroDeCambiosColumnasaUCuarto)**2)+((dataset[contadordeInstancias][6]-NumeroDeCambiosColumnCentral)**2)+((dataset[contadordeInstancias][7]-NumeroDeCambiosColumnaTresCuartos)**2)+((dataset[contadordeInstancias][8]-NumeroPixelesColumnaUnCuarto)**2)+((dataset[contadordeInstancias][9]-NumeroPixelesColumnaCentral)**2)+((dataset[contadordeInstancias][10]-NumeroPixelesColumnaTresCuartos)**2)+((dataset[contadordeInstancias][11]-NumeroPixelesFilaUnCuarto)**2)+((dataset[contadordeInstancias][12]-NumeroPixelesFilaCentral)**2)+((dataset[contadordeInstancias][13]-NumeroPixelesFilaTresCuartos)**2)
          #El atributo .sqrt nos permite obtener la raiz cuadrada de el resultado obtenido anteriormente
          Funcionraiz=math.sqrt(OperacionesCaracteristicasNuevasInstancias)
          #Generamos un nuvo apartado que contiene las distancias optenidas 
          dataset[contadordeInstancias].append(Funcionraiz)
          #Generamos un nuevo apartado para que contiene el numero de fila en que se encuentra el vecino que comparo
          dataset[contadordeInstancias].append(contadordeInstancias+1)
          #Incrementamos el contador para obtener el total de instancias que se analizaron del dataset           
          contadordeInstancias+=1
#Imprimimos el contador de instancas y este nos devolvera el resultado de cuantos istancias se tomaron en el dataset                
   print('Total de Instancias: ',contadordeInstancias)
#Imprimimos el numero de caracteristicas que se tomaron 
   print('Numero de Caracteristicas: 14')
#Imprimimos el numero de clases a las que pertenencen las instancias 
   print('Numero de Clases: 10')
#Imprimimos el nombre de las clases y un salto de linea para dar un poco de formato a la impresion
   print('Clases: [0,1,2,3,4,5,6,7,8,9]\n')          
#Funcion para ordenar el dataset y lo almacena nuevamente en el dataset          
   dataset.sort(key=lambda dataset: dataset[15])
#Declaramos contadores que nos serviran para verificar a que clase pertenece la imagen que 
#queremos comparar
   ContadorClase0=0#contador de la clase 0
   ContadorClase1=1#contador de la clase 1
   ContadorClase2=2#contador de la clase 2
   ContadorClase3=3#contador de la clase 3
   ContadorClase4=4#contador de la clase 4
   ContadorClase5=5#contador de la clase 5
   ContadorClase6=6#contador de la clase 6
   ContadorClase7=7#contador de la clase 7
   ContadorClase8=8#contador de la clase 8
   ContadorClase9=9#contador de la clase 9

#Declaramos un ciclo el cual va desde 0 a el numero de kvecinos que hemos asignado para que compare

   for i in range(0,NumerokVecinos):
    #Con estas condiciones comparamos las clases con los kvecinos para determinar cuantas veces los kvecinos pertenecieron a una clase 
      #En esta condicion especificamos que se el dataset en la posicion y la columna 14 son igual a 0 aumente de uno en uno el contador que hemos designado
      if(dataset[i][14]==0):
         ContadorClase0=ContadorClase0+1
      
      #En esta condicion especificamos que se el dataset en la posicion y la columna 14 son igual a 1 aumente de uno en uno el contador que hemos designado
      if (dataset[i][14]==1):
         ContadorClase1=ContadorClase1+1 
      #En esta condicion especificamos que se el dataset en la posicion y la columna 14 son igual a 2 aumente de uno en uno el contador que hemos designado
      if (dataset[i][14]==2):
         ContadorClase2=ContadorClase2+1
      #En esta condicion especificamos que se el dataset en la posicion y la columna 14 son igual a 3 aumente de uno en uno el contador que hemos designado
      if (dataset[i][14]==3):
         ContadorClase3=ContadorClase3+1
      #En esta condicion especificamos que se el dataset en la posicion y la columna 14 son igual a 4 aumente de uno en uno el contador que hemos designado
      if (dataset[i][14]==4):
         ContadorClase4=ContadorClase4+1
    #En esta condicion especificamos que se el dataset en la posicion y la columna 14 son igual a 5 aumente de uno en uno el contador que hemos designado
      if (dataset[i][14]==5):
         ContadorClase5=ContadorClase5+1
      #En esta condicion especificamos que se el dataset en la posicion y la columna 14 son igual a 6 aumente de uno en uno el contador que hemos designado
      if (dataset[i][14]==6):
         ContadorClase6=ContadorClase6+1
    #En esta condicion especificamos que se el dataset en la posicion y la columna 14 son igual a 7 aumente de uno en uno el contador que hemos designado
      if (dataset[i][14]==7):
         ContadorClase7=ContadorClase7+1
     #En esta condicion especificamos que se el dataset en la posicion y la columna 14 son igual a 8 aumente de uno en uno el contador que hemos designado
      if (dataset[i][14]==8):
         ContadorClase8=ContadorClase8+1
      #En esta condicion especificamos que se el dataset en la posicion y la columna 14 son igual a 9 aumente de uno en uno el contador que hemos designado
      if (dataset[i][14]==9):
         ContadorClase9=ContadorClase9+1
      

#En esta condicion especificamos que si el contador es mayo a los demas entonces nos imprima que la clase pertenece a el contador con el numero mas alto de repeticiones      
   if((ContadorClase0>ContadorClase1) and (ContadorClase0>ContadorClase2) and (ContadorClase0>ContadorClase3) and (ContadorClase0>ContadorClase4) and (ContadorClase0>ContadorClase5) and (ContadorClase0>ContadorClase6) and (ContadorClase0>ContadorClase7)and (ContadorClase0>ContadorClase8) and (ContadorClase0>ContadorClase9) ):
        print('La Imagen es un 0');     
  
#En esta condicion especificamos que si el contador es mayo a los demas entonces nos imprima que la clase pertenece a el contador con el numero mas alto de repeticiones
   if((ContadorClase1>ContadorClase0) and (ContadorClase1>ContadorClase2) and (ContadorClase1>ContadorClase3) and (ContadorClase1>ContadorClase4) and (ContadorClase1>ContadorClase5) and (ContadorClase1>ContadorClase6) and (ContadorClase1>ContadorClase7)and (ContadorClase1>ContadorClase8) and (ContadorClase1>ContadorClase9) ):
        print('La Imagen es un 1');      
#En esta condicion especificamos que si el contador es mayo a los demas entonces nos imprima que la clase pertenece a el contador con el numero mas alto de repeticiones
   if((ContadorClase2>ContadorClase0) and (ContadorClase2>ContadorClase1) and (ContadorClase2>ContadorClase3) and (ContadorClase2>ContadorClase4) and (ContadorClase2>ContadorClase5) and (ContadorClase2>ContadorClase6) and (ContadorClase2>ContadorClase7)and (ContadorClase2>ContadorClase8) and (ContadorClase2>ContadorClase9) ):
        print('La Imagen es un 2');     
#En esta condicion especificamos que si el contador es mayo a los demas entonces nos imprima que la clase pertenece a el contador con el numero mas alto de repeticiones  
   if((ContadorClase3>ContadorClase1) and (ContadorClase3>ContadorClase2) and (ContadorClase3>ContadorClase0) and (ContadorClase3>ContadorClase4) and (ContadorClase3>ContadorClase5) and (ContadorClase3>ContadorClase6) and (ContadorClase3>ContadorClase7)and (ContadorClase3>ContadorClase8) and (ContadorClase3>ContadorClase9) ):
        print('La Imagen es un 3');
#En esta condicion especificamos que si el contador es mayo a los demas entonces nos imprima que la clase pertenece a el contador con el numero mas alto de repeticiones
   if((ContadorClase4>ContadorClase1) and (ContadorClase4>ContadorClase2) and (ContadorClase4>ContadorClase3) and (ContadorClase4>ContadorClase0) and (ContadorClase4>ContadorClase5) and (ContadorClase4>ContadorClase6) and (ContadorClase4>ContadorClase7)and (ContadorClase4>ContadorClase8) and (ContadorClase4>ContadorClase9) ):
        print('La Imagen es un 4');
#En esta condicion especificamos que si el contador es mayo a los demas entonces nos imprima que la clase pertenece a el contador con el numero mas alto de repeticiones
   if((ContadorClase5>ContadorClase1) and (ContadorClase5>ContadorClase2) and (ContadorClase5>ContadorClase3) and (ContadorClase5>ContadorClase4) and (ContadorClase5>ContadorClase0) and (ContadorClase5>ContadorClase6) and (ContadorClase5>ContadorClase7)and (ContadorClase5>ContadorClase8) and (ContadorClase5>ContadorClase9) ):
        print('La Imagen es un 5');
#En esta condicion especificamos que si el contador es mayo a los demas entonces nos imprima que la clase pertenece a el contador con el numero mas alto de repeticiones
   if((ContadorClase6>ContadorClase1) and (ContadorClase6>ContadorClase2) and (ContadorClase6>ContadorClase3) and (ContadorClase6>ContadorClase4) and (ContadorClase6>ContadorClase5) and (ContadorClase6>ContadorClase0) and (ContadorClase6>ContadorClase7)and (ContadorClase6>ContadorClase8) and (ContadorClase6>ContadorClase9) ):
        print('La Imagen es un 6');      
#En esta condicion especificamos que si el contador es mayo a los demas entonces nos imprima que la clase pertenece a el contador con el numero mas alto de repeticiones
   if((ContadorClase7>ContadorClase1) and (ContadorClase7>ContadorClase2) and (ContadorClase7>ContadorClase3) and (ContadorClase7>ContadorClase4) and (ContadorClase7>ContadorClase5) and (ContadorClase7>ContadorClase6) and (ContadorClase7>ContadorClase0)and (ContadorClase7>ContadorClase8) and (ContadorClase7>ContadorClase9) ):
        print('La Imagen es un 7');      
#En esta condicion especificamos que si el contador es mayo a los demas entonces nos imprima que la clase pertenece a el contador con el numero mas alto de repeticiones
   if((ContadorClase8>ContadorClase1) and (ContadorClase8>ContadorClase2) and (ContadorClase8>ContadorClase3) and (ContadorClase8>ContadorClase4) and (ContadorClase8>ContadorClase5) and (ContadorClase8>ContadorClase6) and (ContadorClase8>ContadorClase7)and (ContadorClase8>ContadorClase0) and (ContadorClase8>ContadorClase9) ):
        print('La Imagen es un 8');      
#En esta condicion especificamos que si el contador es mayo a los demas entonces nos imprima que la clase pertenece a el contador con el numero mas alto de repeticiones
   if((ContadorClase9>ContadorClase1) and (ContadorClase9>ContadorClase2) and (ContadorClase9>ContadorClase3) and (ContadorClase9>ContadorClase4) and (ContadorClase9>ContadorClase5) and (ContadorClase9>ContadorClase6) and (ContadorClase9>ContadorClase7)and (ContadorClase9>ContadorClase8) and (ContadorClase9>ContadorClase0) ):
        print('La Imagen es un 9');
  
  
#En este ciclo que va desde 0 a los kvecinos imprimimos la clase de los kvecinos mas cercanos 
#a nuestra nueva instancia, las distancias y la ubicacion en la que se encuentran dentro de nuestro dataset
def Descripcion(dataset,NumerokVecinos): 
  for i in range (0,NumerokVecinos):
    #Imprimimos el numero de vecino que se encuentra mas cerca de nuestra instancia, la ubicacion en la que se encuentra dentro de nuestro dataset, la clase a la que pertenece y la distancia que existe entre el y nuestra nueva instancia   
    print('Vecino:',(i+1),' ','Ubicacion:',dataset[i][16],' ','Clase:',dataset[i][14],'Distancia:',dataset[i][15])


#En esta funcion  recibimos como parametros los vecinos que se consideraron
#y calculamos cuantos de ellos pertenecen a una clase    
def Numerosdevecinosdeunaclase(dataset,NumerokVecinos):
    clase0=0#contador para la clase 0
    clase1=0#contador para la clase 1
    clase2=0#contador para la clase 2
    clase3=0#contador para la clase 3
    clase4=0#contador para la clase 4
    clase5=0#contador para la clase 5
    clase6=0#contador para la clase 6
    clase7=0#contador para la clase 7
    clase8=0#contador para la clase 8
    clase9=0#contador para la clase 9
    #En el ciclo recorremos a i desde 0 hasta el numero de vecinos que hemos designado
    for i in range(0,NumerokVecinos):
        #En esta condicion tomaremos en cuenta la clase que se encuentra en el dataset y la compararemos con un valor a 0        
        if(dataset[i][14]==0):
            #Si la condicion se cumple incrementaremos el contador en uno para determinar cuantas de las instancias que tomamos para compararr pertenencen a la clase
            clase0=clase0+1
        #En esta condicion tomaremos en cuenta la clase que se encuentra en el dataset y la compararemos con un valor a 1
        if(dataset[i][14]==1):
            #Si la condicion se cumple incrementaremos el contador en uno para determinar cuantas de las instancias que tomamos para compararr pertenencen a la clase
            clase1=clase1+1
       #En esta condicion tomaremos en cuenta la clase que se encuentra en el dataset y la compararemos con un valor a2
        if(dataset[i][14]==2):
            #Si la condicion se cumple incrementaremos el contador en uno para determinar cuantas de las instancias que tomamos para compararr pertenencen a la clase
            clase2=clase2+1
        #En esta condicion tomaremos en cuenta la clase que se encuentra en el dataset y la compararemos con un valor a 3
        if(dataset[i][14]==3):
            #Si la condicion se cumple incrementaremos el contador en uno para determinar cuantas de las instancias que tomamos para compararr pertenencen a la clase
            clase3=clase3+1
        #En esta condicion tomaremos en cuenta la clase que se encuentra en el dataset y la compararemos con un valor a 4
        if(dataset[i][14]==4):
            #Si la condicion se cumple incrementaremos el contador en uno para determinar cuantas de las instancias que tomamos para compararr pertenencen a la clase
            clase4=clase4+1
       #En esta condicion tomaremos en cuenta la clase que se encuentra en el dataset y la compararemos con un valor a 5
        if(dataset[i][14]==5):
            #Si la condicion se cumple incrementaremos el contador en uno para determinar cuantas de las instancias que tomamos para compararr pertenencen a la clase
            clase5=clase5+1
        #En esta condicion tomaremos en cuenta la clase que se encuentra en el dataset y la compararemos con un valor a 6
        if(dataset[i][14]==6):
            #Si la condicion se cumple incrementaremos el contador en uno para determinar cuantas de las instancias que tomamos para compararr pertenencen a la clase
            clase6=clase6+1
       #En esta condicion tomaremos en cuenta la clase que se encuentra en el dataset y la compararemos con un valor a 7
        if(dataset[i][14]==7):
            #Si la condicion se cumple incrementaremos el contador en uno para determinar cuantas de las instancias que tomamos para compararr pertenencen a la clase
            clase7=clase7+1
       #En esta condicion tomaremos en cuenta la clase que se encuentra en el dataset y la compararemos con un valor a 8
        if(dataset[i][14]==8):
            #Si la condicion se cumple incrementaremos el contador en uno para determinar cuantas de las instancias que tomamos para compararr pertenencen a la clase
            clase0=clase8+1
        #En esta condicion tomaremos en cuenta la clase que se encuentra en el dataset y la compararemos con un valor a 9
        if(dataset[i][14]==9):
            #Si la condicion se cumple incrementaremos el contador en uno para determinar cuantas de las instancias que tomamos para compararr pertenencen a la clase
            clase9=clase9+1            
    print('\n')    
    print('Total de instancias que pertenecen a la clase 0: ',clase0)#Imprimimos cuantos de los vecinos  pertenecen a la clase 0   
    print('Total de instancias que pertenecen a la clase 1: ',clase1)#Imprimimos cuantos de los vecinos  pertenecen a la clase 1
    print('Total de instancias que pertenecen a la clase 2: ',clase2)#Imprimimos cuantos de los vecinos  pertenecen a la clase 2
    print('Total de instancias que pertenecen a la clase 3: ',clase3)#Imprimimos cuantos de los vecinos  pertenecen a la clase 3
    print('Total de instancias que pertenecen a la clase 4: ',clase4)#Imprimimos cuantos de los vecinos  pertenecen a la clase 4
    print('Total de instancias que pertenecen a la clase 5: ',clase5)#Imprimimos cuantos de los vecinos  pertenecen a la clase 5
    print('Total de instancias que pertenecen a la clase 6: ',clase6)#Imprimimos cuantos de los vecinos  pertenecen a la clase 6
    print('Total de instancias que pertenecen a la clase 7: ',clase7)#Imprimimos cuantos de los vecinos  pertenecen a la clase 7
    print('Total de instancias que pertenecen a la clase 8: ',clase8)#Imprimimos cuantos de los vecinos  pertenecen a la clase 8
    print('Total de instancias que pertenecen a la clase 9: ',clase9)#Imprimimos cuantos de los vecinos  pertenecen a la clase 9
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

#Mandamos llamar la funcion para obtener el resultado que se produjo en ella
KNN(dataset,NumerokVecinos,Dimensiones,FilaEntreColumna,AreaDeLaFigura,NumeroDeCambiosFilaUcCuarto,NumeroDeCambiosFilaCentral,NumeroDeCambiosFilaTresCuartos,NumeroDeCambiosColumnasaUCuarto,NumeroDeCambiosColumnCentral,NumeroDeCambiosColumnaTresCuartos,NumeroPixelesColumnaUnCuarto,NumeroPixelesColumnaCentral,NumeroPixelesColumnaTresCuartos,NumeroPixelesFilaUnCuarto,NumeroPixelesFilaCentral,NumeroPixelesFilaTresCuartos)
Descripcion(dataset,NumerokVecinos)    
Numerosdevecinosdeunaclase(dataset,NumerokVecinos)
