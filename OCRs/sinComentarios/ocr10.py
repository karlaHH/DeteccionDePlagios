
 


import os                             
import matplotlib.image as mpimg      
import csv                            
import math                           


datS=[]                               
tamMat=2380                          






def propiedad1(img, tImTo):          
    resu=0                           
    alto=len(img)                    
    ancho=int(tImTo/alto)            
    for al in range(alto):           
        for an in range(ancho):      
            num=(int(img[al][an]))   
            if num==1:               
                resu=resu+1          
    resu=(resu/tImTo)                
    return resu                      






def propiedad2(img, tImTo):    
    alto=len(img)              
    ancho=int(tImTo/alto)      
    resu=ancho/alto            
    return resu                






def propiedad3(img, tImTo):                 
    alto=len(img)                           
    ancho=int(tImTo/alto)                   
    dista=int(ancho/2)                      
    numuns=0                                
    for al in range(alto):                  
        compara=(int(img[al][dista]))       
        if compara==1:                      
            numuns=numuns+1                 
    return numuns/alto                      
    





def propiedad4(img, tImTo):                 
    alto=len(img)                           
    ancho=int(tImTo/alto)                   
    dista=int(ancho/4)                      
    numuns=0                                
    for al in range(alto):                  
        compara=(int(img[al][dista]))       
        if compara==1:                      
            numuns=numuns+1                 
    return numuns/alto                      
    





def propiedad5(img, tImTo):                 
    alto=len(img)                           
    ancho=int(tImTo/alto)                   
    dista=int((int(ancho/4))*3)             
    numuns=0                                
    for al in range(alto):                  
        compara=(int(img[al][dista]))       
        if compara==1:                      
            numuns=numuns+1                 
    return numuns/alto                      

       




def propiedad6(img, tImTo):                         
    alto=len(img)                                   
    ancho=int(tImTo/alto)                           
    altu=int(alto/2)                                
    numuns=0                                        
    for alt in range(alto):                         
        for anch in range(ancho):                   
            if alt==altu:                           
                compara=(int(img[altu][anch]))      
                if compara==1:                      
                    numuns=numuns+1                 
    return numuns/ancho                             






def propiedad7(img, tImTo):                         
    alto=len(img)                                   
    ancho=int(tImTo/alto)                           
    altu=int(alto/4)                                
    numuns=0                                        
    for alt in range(alto):                         
        for anch in range(ancho):                   
            if alt==altu:                           
                compara=(int(img[altu][anch]))      
                if compara==1:                      
                    numuns=numuns+1                 
    return numuns/ancho                             






def propiedad8(img, tImTo):                         
    alto=len(img)                                   
    ancho=int(tImTo/alto)                           
    altu=int((int(alto/4))*3)                       
    numuns=0                                        
    for alt in range(alto):                         
        for anch in range(ancho):                   
            if alt==altu:                           
                compara=(int(img[altu][anch]))      
                if compara==1:                      
                    numuns=numuns+1                 
    return numuns/ancho                             






def propiedad9(img, tImTo):                     
    alto=len(img)                               
    ancho=int(tImTo/alto)                       
    dista=int(ancho/2)                          
    numuns=0                                    
    val=0                                       
    for al in range(alto):                      
        compara=(int(img[al][dista]))           
        if compara!=val:                        
            numuns=numuns+1                     
            val=(int(img[al][dista]))           
    return numuns                               






def propiedad10(img, tImTo):                    
    alto=len(img)                               
    ancho=int(tImTo/alto)                       
    dista=int(ancho/4)                          
    numuns=0                                    
    val=0                                       
    for al in range(alto):                      
        compara=(int(img[al][dista]))           
        if compara!=val:                        
            numuns=numuns+1                     
            val=(int(img[al][dista]))           
    return numuns                               






def propiedad11(img, tImTo):                    
    alto=len(img)                               
    ancho=int(tImTo/alto)                       
    dista=int((int(ancho/4))*3)                 
    numuns=0                                    
    val=0                                       
    for al in range(alto):                      
        compara=(int(img[al][dista]))           
        if compara!=val:                        
            numuns=numuns+1                     
            val=(int(img[al][dista]))           
    return numuns                               






def propiedad12(img, tImTo):                        
    alto=len(img)                                   
    ancho=int(tImTo/alto)                           
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






def propiedad13(img, tImTo):                        
    alto=len(img)                                   
    ancho=int(tImTo/alto)                           
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






def propiedad14(img, tImTo):                        
    alto=len(img)                                   
    ancho=int(tImTo/alto)                           
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
  
  




def kNN(img, numVeci):                      
    img=mpimg.imread(img)                   
    mat=[]                                  
    knn=[]                                  
    tImTo=img.size                          
    for x in range(tamMat+1):               
        mat.append(['']*15)                 
    for x in range(tamMat):                 
        knn.append(['']*3)                  
    reader = csv.reader(open('DataSet.csv')) 
    for index,row in enumerate(reader):      
        for cont in range(15):              
            mat[index][cont]=row[cont]      
    
    i2P1=propiedad1(img, tImTo)               
    i2P2=propiedad2(img, tImTo)               
    i2P3=propiedad3(img, tImTo)               
    i2P4=propiedad4(img, tImTo)               
    i2P5=propiedad5(img, tImTo)               
    i2P6=propiedad6(img, tImTo)               
    i2P7=propiedad7(img, tImTo)               
    i2P8=propiedad8(img, tImTo)               
    i2P9=propiedad9(img, tImTo)               
    i2P10=propiedad10(img, tImTo)             
    i2P11=propiedad11(img, tImTo)             
    i2P12=propiedad12(img, tImTo)             
    i2P13=propiedad13(img, tImTo)             
    i2P14=propiedad14(img, tImTo)             
    
    
    for val in range(tamMat):                
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
    for i in range(tamMat):                                 
        datS.append([0.0]*15)                               
    rootDir = 'DatosPrueba'                                 
    nameima=''                                              
    x=0                                                     
    y=0                                                     
    for dirName, subdirList, fileList in os.walk(rootDir):  
        num=str(dirName)+'  '                               
        for fname in fileList:                              
            nameima=dirName+"/"+fname                       
            img = mpimg.imread(nameima)                     
            tImTo=img.size                                  
            datS[x][y]=propiedad1(img, tImTo)               
            y=y+1                                           
            datS[x][y]=propiedad2(img, tImTo)               
            y=y+1                                           
            datS[x][y]=propiedad3(img, tImTo)               
            y=y+1                                           
            datS[x][y]=propiedad4(img, tImTo)               
            y=y+1                                           
            datS[x][y]=propiedad5(img, tImTo)               
            y=y+1                                           
            datS[x][y]=propiedad6(img, tImTo)               
            y=y+1                                           
            datS[x][y]=propiedad7(img, tImTo)               
            y=y+1                                           
            datS[x][y]=propiedad8(img, tImTo)               
            y=y+1                                           
            datS[x][y]=propiedad9(img, tImTo)               
            y=y+1                                           
            datS[x][y]=propiedad10(img, tImTo)              
            y=y+1                                           
            datS[x][y]=propiedad11(img, tImTo)              
            y=y+1                                           
            datS[x][y]=propiedad12(img, tImTo)              
            y=y+1                                           
            datS[x][y]=propiedad13(img, tImTo)              
            y=y+1                                           
            datS[x][y]=propiedad14(img, tImTo)              
            y=y+1                                           
            datS[x][y]=num[12]+'´s'                         
            y=0                                             
            x=x+1                                           
        
          
    return datS                                             
    
     





if __name__ == "__main__":                                              
    os.system('cls')                                                    
    while True:                                                         
        print('\n___________Bienvenido usuario______________')            
        print('|                                         |')            
        print('|    1.-Generar el archivo CSV (DataSet)  |')            
        print('|    2.-Buscar un número por KNN          |')            
        print('|    3.-Salir del programa                |')            
        print('|_________________________________________|')            
        opcion=int(input('|¿Qué opción eliges?:                     |>')) 
        if opcion==1:                                                   
            print('Procesando informacion ...')                         
            data=crearDataSet()                                         
            generarArchivo(data)                                        
            print ('Se leyeron: ',tamMat,' datos\nSe definieron 14 instancias\nSe definieron 10 clases\nLas clases son: 0,1,2,3,4,5,6,7,8,9' )  
        elif opcion==2:                                                
            nomImg=input('Ingrese el nombre de la imagen a comparar sin extension: ') 
            numVeci=int(input('Ingrese el número de vecinos K: '))     
            nomImg=nomImg+".png"                                       
            mat=kNN(nomImg, numVeci)                                   
            for va in range(numVeci):                                  
                print("Num. vecino: ",va+1,"\n Posición en DataSet: ", mat[va][0]+1,"\n Clase: ",mat[va][2],"\n Distancia: ",mat[va][1]+0.3431100858184699)  
            print('\nTu imagen es de clase',mat[va][2])
            print('Proceso finalizado\n')                              
        elif opcion==3:                                                
            print('Programa finalizado\n')                             
            break                                                      
        else:                                                          
            print('No has ingresado una opcion valida\n')              
            
