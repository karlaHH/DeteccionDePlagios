




import os 

import matplotlib.image as mpimg 

import csv

import math                           


data=[]                               
                      







def caracteristica1(img, tamImg): 

    resu=0

    alto=len(img)                    

    ancho=int(tamImg/alto)

    for al in range(alto):

        for an in range(ancho): 

            num=(int(img[al][an])) 

            if num==1:               

                resu=resu+1          

    resu=(resu/tamImg)               

    return resu                      








def caracteristica2(img, tamImg):

    alto=len(img) 

    ancho=int(tamImg/alto)

    resu=ancho/alto

    return resu                  








def caracteristica3(img, tamImg):

    alto=len(img)

    ancho=int(tamImg/alto)

    dista=int(ancho/2)

    numuns=0 

    for al in range(alto):

        compara=(int(img[al][dista]))

        if compara==1:

            numuns=numuns+1 

    return numuns/alto                      
    







def caracteristica4(img, tamImg):
 
    alto=len(img)

    ancho=int(tamImg/alto) 

    dista=int(ancho/4)

    numuns=0    
 
    for al in range(alto):

        compara=(int(img[al][dista]))   

        if compara==1:

            numuns=numuns+1 

                    
    return numuns/alto                      







def caracteristica5(img, tamImg):            

    alto=len(img)
 
    ancho=int(tamImg/alto)  

    dista=int((int(ancho/4))*3)

    numuns=0
 
    for al in range(alto):

        compara=(int(img[al][dista]))

        if compara==1:

            numuns=numuns+1 

    return numuns/alto                      

       




 

def caracteristica6(img, tamImg): 

    alto=len(img)
 
    ancho=int(tamImg/alto)
 
    altu=int(alto/2) 

    numuns=0
 
    for alt in range(alto):

        for anch in range(ancho):

            if alt==altu:

                compara=(int(img[altu][anch]))

                if compara==1:

                    numuns=numuns+1

    return numuns/ancho                            








def caracteristica7(img, tamImg):

    alto=len(img)

    ancho=int(tamImg/alto)

    altu=int(alto/4)

    numuns=0

    for alt in range(alto):

        for anch in range(ancho):

            if alt==altu:   

                compara=(int(img[altu][anch]))

                if compara==1:

                    numuns=numuns+1

    return numuns/ancho                             







def caracteristica8(img, tamImg):

    alto=len(img)

    ancho=int(tamImg/alto)

    altu=int((int(alto/4))*3)

    numuns=0 

    for alt in range(alto):

        for anch in range(ancho):

            if alt==altu:

                compara=(int(img[altu][anch]))

                if compara==1:

                    numuns=numuns+1

    return numuns/ancho                             








def caracteristica9(img, tamImg):

    alto=len(img)

    ancho=int(tamImg/alto)

    dista=int(ancho/2)

    numuns=0

    val=0

    for al in range(alto):

        compara=(int(img[al][dista]))

        if compara!=val:

            numuns=numuns+1

            val=(int(img[al][dista]))

    return numuns                               








def caracteristica10(img, tamImg):

    alto=len(img)

    ancho=int(tamImg/alto)

    dista=int(ancho/4)

    numuns=0

    val=0 

    for al in range(alto):

        compara=(int(img[al][dista]))

        if compara!=val:

            numuns=numuns+1

            val=(int(img[al][dista]))

    return numuns                               







def caracteristica11(img, tamImg):

    alto=len(img)

    ancho=int(tamImg/alto)

    dista=int((int(ancho/4))*3)

    numuns=0

    val=0

    for al in range(alto):

        compara=(int(img[al][dista]))

        if compara!=val:

            numuns=numuns+1

            val=(int(img[al][dista]))

    return numuns                               








def caracteristica12(img, tamImg):

    alto=len(img)

    ancho=int(tamImg/alto)

    altu=int(alto/2)

    numuns=0

    val=0 

    for alt in range(alto):

        for anch in range(ancho):

            if alt==altu:

                compara=(int(img[altu][anch]))

                if compara!=val:  

                    numuns=numuns+1

                    val=(int(img[altu][anch]))

    return numuns                                   








def caracteristica13(img, tamImg):

    alto=len(img)

    ancho=int(tamImg/alto)

    altu=int(alto/4)

    numuns=0 

    val=0

    for alt in range(alto):

        for anch in range(ancho):

            if alt==altu:

                compara=(int(img[altu][anch]))

                if compara!=val:

                    numuns=numuns+1

                    val=(int(img[altu][anch]))

    return numuns                                   








def caracteristica14(img, tamImg):

    alto=len(img)

    ancho=int(tamImg/alto)

    altu=int((int(alto/4))*3)

    numuns=0

    val=0

    for alt in range(alto):

        for anch in range(ancho):

            if alt==altu:

                compara=(int(img[altu][anch]))

                if compara!=val:

                    numuns=numuns+1

                    val=(int(img[altu][anch]))

    return numuns                                   







def generarArchivo(datset):

    dataSet=datset

    csvsalida=open('DataSet.csv','w',newline='')

    salida=csv.writer(csvsalida)


    salida.writerow(["Caracteristica 1","Caracteristica 2","Caracteristica 3","Caracteristica 4","Caracteristica 5","Caracteristica 6","Caracteristica 7","Caracteristica 8","Caracteristica 9","Caracteristica 10","Caracteristica 11","Caracteristica 12","Caracteristica 13","Caracteristica 14","Número"])      

    salida.writerows(dataSet)    
    del salida

    csvsalida.close()

    print('El dataset se genero exitosamente')      
    







def kNN(img, numVeci):

    img=mpimg.imread(img) 

    mat=[]

    knn=[] 

    tamImg=img.size

    for x in range(1736+1):

        mat.append(['']*15)

    for x in range(1736):  

        knn.append(['']*3)

    reader = csv.reader(open('DataSet.csv'))

    for index,row in enumerate(reader): 

        for cont in range(15):

            mat[index][cont]=row[cont]      

    i2P1=caracteristica1(img, tamImg)              
    i2P2=caracteristica2(img, tamImg)              
    i2P3=caracteristica3(img, tamImg)               
    i2P4=caracteristica4(img, tamImg)              
    i2P5=caracteristica5(img, tamImg)              
    i2P6=caracteristica6(img, tamImg)               
    i2P7=caracteristica7(img, tamImg)               
    i2P8=caracteristica8(img, tamImg)               
    i2P9=caracteristica9(img, tamImg)               
    i2P10=caracteristica10(img, tamImg)             
    i2P11=caracteristica11(img, tamImg)             
    i2P12=caracteristica12(img, tamImg)             
    i2P13=caracteristica13(img, tamImg)             
    i2P14=caracteristica14(img, tamImg)             
    


    for val in range(1736):

        p1=float(mat[val+1][0])              
        p2=float(mat[val+1][1])              
        p3=float(mat[val+1][2])              
        p4=float(mat[val+1][3])              
        p5=float(mat[val+1][4])              
        p6=float(mat[val+1][5])              
        p7=float(mat[val+1][6])              
        p8=float(mat[val+1][7])              
        p9=float(mat[val+1][8])              
        p10=float(mat[val+1][9])             
        p11=float(mat[val+1][10])            
        p12=float(mat[val+1][11])            
        p13=float(mat[val+1][12])            
        p14=float(mat[val+1][13])            
        

        dist= math.sqrt(((p1-i2P1)**2)+((p2-i2P2)**2)+((p3-i2P3)**2)+((p4-i2P4)**2)+((p5-i2P5)**2)+((p6-i2P6)**2)+((p7-i2P7)**2)+((p8-i2P8)**2)+((p9-i2P9)**2)+((p10-i2P10)**2)+((p11-i2P11)**2)+((p12-i2P12)**2)+((p13-i2P13)**2)+((p14-i2P14)**2))

        knn[val][0]=val+1

        knn[val][1]=dist 

        knn[val][2]=mat[val+1][14]          
     


    res=[]  

    for x in range(numVeci):

        res.append([0.0]*3)                 

    for i in range(numVeci):

        temp = knn[0][1]

        numero = len(knn) 

        for j in range(numero):

            if(knn[j][1] < temp): 

                temp = knn[j][1]

                apun=j

            if (j+1==numero):

                res[i][0] = knn[apun][0]

                res[i][1] = knn[apun][1]

                res[i][2] = knn[apun][2]

                knn.pop(apun)

    return res                              
        
    




    
def crearDataSet():                                         
    for i in range(1736):                                 
        data.append([0.0]*15)                               
    rootDir = 'DatosPrueba'                                 
    nameima=''                                              
    x=0                                                     
    y=0                                                     
    for dirName, subdirList, fileList in os.walk(rootDir):  
        num=str(dirName)+'  '                               
        for fname in fileList:                              
            nameima=dirName+"/"+fname                       
            img = mpimg.imread(nameima)                     
            tamImg=img.size                                  
            data[x][y]=caracteristica1(img, tamImg)               
            y=y+1                                           
            data[x][y]=caracteristica2(img, tamImg)               
            y=y+1                                           
            data[x][y]=caracteristica3(img, tamImg)               
            y=y+1                                           
            data[x][y]=caracteristica4(img, tamImg)               
            y=y+1                                           
            data[x][y]=caracteristica5(img, tamImg)               
            y=y+1                                           
            data[x][y]=caracteristica6(img, tamImg)               
            y=y+1                                           
            data[x][y]=caracteristica7(img, tamImg)               
            y=y+1                                           
            data[x][y]=caracteristica8(img, tamImg)               
            y=y+1                                           
            data[x][y]=caracteristica9(img, tamImg)               
            y=y+1                                           
            data[x][y]=caracteristica10(img, tamImg)              
            y=y+1                                           
            data[x][y]=caracteristica11(img, tamImg)              
            y=y+1                                           
            data[x][y]=caracteristica12(img, tamImg)              
            y=y+1                                           
            data[x][y]=caracteristica13(img, tamImg)              
            y=y+1                                           
            data[x][y]=caracteristica14(img, tamImg)              
            y=y+1                                           
            data[x][y]=num[12]                         
            y=0                                             
            x=x+1                                           
        if num[12]!=' ':                                    
            print('Carpeta/ %s' % num[12])     
    return data                                             
    







if __name__ == "__main__":

            

            

            nomImg=input('Ingrese el nombre de la imagen a buscar: ')

            numVeci=int(input('Ingrese el número de vecinos: ')) 

            mat=kNN(nomImg, numVeci) 

            for va in range(numVeci):

                vecino=va+1 

                print("\n Vecino # ", vecino)

                print( " Posición en DataSet: \n", mat[va][0],"\n Distancia euclidiana: \n",mat[va][1],"\n Clase: \n",mat[va][2])  
                print("-----------------------")
            print("La imagen pertenece a la clase :",mat[va][2])
            
            
