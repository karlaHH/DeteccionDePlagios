
 

import os                             

import matplotlib.image as mpimg      

import csv                            

import math                           



datS=[]                               

tamMat=1726                          







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
    
        
    




def crearDataSet():                                         

    for i in range(tamMat):                                 

        datS.append([0.0]*15)                               
        
    carpPrin = 'DatosPrueba'                                
    
    nameima=''                                              
    
    x=0                                                     
    
    y=0                                                     
    
    for dirName, subdirList, fileList in os.walk(carpPrin): 
    
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
            
            datS[x][y]=num[12]                              
            
            y=0                                             
            
            x=x+1                                           
            
    print('DataSet creado\n')                                 
    
    return datS                                             
    






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
    
        dist= math.sqrt(((float(mat[val+1][0])-i2P1)**2)+((float(mat[val+1][1])-i2P2)**2)+((float(mat[val+1][2])-i2P3)**2)+((float(mat[val+1][3])-i2P4)**2)+((float(mat[val+1][4])-i2P5)**2)+((float(mat[val+1][5])-i2P6)**2)+((float(mat[val+1][6])-i2P7)**2)+((float(mat[val+1][7])-i2P8)**2)+((float(mat[val+1][8])-i2P9)**2)+((float(mat[val+1][9])-i2P10)**2)+((float(mat[val+1][10])-i2P11)**2)+((float(mat[val+1][11])-i2P12)**2)+((float(mat[val+1][12])-i2P13)**2)+((float(mat[val+1][13])-i2P14)**2))
        
        knn[val][0]=val+1                   
        
        knn[val][1]=dist                   
        
        knn[val][2]=mat[val+1][14]          
        
    ce=0
    
    un=0
    
    do=0
    
    tr=0
    
    cu=0
    
    ci=0
    
    se=0
    
    si=0
    
    oc=0
    
    nu=0
    
    i=0
    while (i < numVeci):                
    
        j=0
        temp = knn[0][1]                    
        
        numero = len(knn)                   
        
        while (j < numero):             
        
            if(knn[j][1] < temp):           
            
                temp = knn[j][1]            
                
                apun=j                      
                
            if (j+1==numero):               
            
                print("Num. vecino: ",i+1," Posición en D.S: ", knn[apun][0]," Distancia Euclidiana: ",knn[apun][1]," Clase: ",knn[apun][2])  
                
                if knn[apun][2]=='0':
                    
                    ce=ce+1
                    
                elif knn[apun][2]=='1':
                    
                    un=un+1
                    
                elif knn[apun][2]=='2':
                    
                    do=do+1
                    
                elif knn[apun][2]=='3':
                    
                    tr=tr+1
                    
                elif knn[apun][2]=='4':
                    
                    cu=cu+1
                    
                elif knn[apun][2]=='5':
                    
                    ci=ci+1
                    
                elif knn[apun][2]=='6':
                    
                    se=se+1
                    
                elif knn[apun][2]=='7':
                    
                    si=si+1
                    
                elif knn[apun][2]=='8':
                    
                    oc=oc+1
                    
                elif knn[apun][2]=='9':
                    
                    nu=nu+1
                    
                knn.pop(apun)               
                
            j=j+1
            
        i=i+1
        
    print('-----------------------------------------------------------------------------------------------------')
    print('\nInstancias   Clase   Vecinos cercano')
    print('166          Ceros:   ',ce)
    print('183          Unos:    ',un)
    print('230          Dos:     ',do)
    print('155          Tres:    ',tr)
    print('160          Cuatros: ',cu)
    print('175          Cincos:  ',ci)
    print('168          Seis:    ',se)
    print('155          Sietes:  ',si)
    print('172          Ochos:   ',oc)
    print('162          Nueves:  ',nu)
    
    arre=[[ce,'Cero'],[un,'Uno'],[do,'Dos'],[tr,'Tres'],[cu,'Cuatro'],[ci,'Cinco'],[se,'Seis'],[si,'Siete'],[oc,'Ocho'],[nu,'Nueve']]
    
    temp=arre[0][0]
    
    nu=''
    
    for a in range(10):
        
        if temp < arre[a][0]:
            
            temp=arre[a][0]
            
            num=arre[a][1]
            
    print('-----------------------------------------------------------------------------------------------------')
    print('La imagen pertenece a la clase: ',num)
    print('-----------------------------------------------------------------------------------------------------')
    






if __name__ == "__main__":                                                   

    os.system('cls')                                                         
    
    while True:                                                              
    
        print('Ingrese una opción')                                       
        
        print('1.-Buscar un número')                                
        
        print('2.-Crear Data Set')                                           
        
        print('3.-Salir')                                                    
        
        opcion=int(input('¿Qué opción eliges?: '))                           
        
        if opcion==1:                                                        
        
            nomImg=input('Ingrese el nombre de la imagen a buscar: ')        
            
            numVeci=int(input('Ingrese el número de vecinos: '))             
            
            nomImg=nomImg+".png"                                             
            
            print('-----------------------------------------------------------------------------------------------------')
            print('\n#Instancias en data set: 1726\n#Propiedades: 14\n#Clases: 10\nClases: 0,1,2,3,4,5,6,7,8,9\n')
            print('-----------------------------------------------------------------------------------------------------')
            
            kNN(nomImg, numVeci)                                         
            
            print('\n')
            
        elif opcion==2:                                                      
        
            data=crearDataSet()                                              
            
            generarArchivo(data)                                             
            
        elif opcion==3:                                                      
        
            break                                                            
            
        else:                                                                
        
            print('La opcion ingresada no existe\n')                    
            
            
