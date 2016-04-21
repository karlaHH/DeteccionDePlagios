
 

from PIL import Image

import matplotlib.image as mpimg

import os

import csv





def RazonFilasColumnas(numfilas,numcolumnas):
    
    razonfilascolumnas = numfilas/numcolumnas
    
    return razonfilascolumnas





def AreaBlancosNegros(imagenmatriz,numfilas,numcolumnas):
    
    contadorceros = 0
    
    contadorunos = 0
    
    razonesarea = []
    
    for x in range(numfilas):
        
        for y in range(numcolumnas):
            
            if(imagenmatriz[x][y]==0):
                
                contadorceros = contadorceros + 1
            else:
                
                contadorunos = contadorunos + 1
    
    razonunos = contadorceros/(numfilas*numcolumnas)
    
    razonceros = contadorunos/(numfilas*numcolumnas)
    
    razonesarea = [razonunos,razonceros]
    
    return razonesarea





def AreaMitadSuperiorBlancosNegros(imagenmatriz,numfilas,numcolumnas):
    
    contadorceros = 0
    
    contadorunos = 0
    
    razonesareamitad = []
    
    mitadfilas = int(numfilas/2)
    
    for x in range(mitadfilas):
        
        for y in range(numcolumnas):
            
            if(imagenmatriz[x][y]==0):
                
                contadorceros = contadorceros + 1
            else:
                
                contadorunos = contadorunos + 1
    
    razonunos = contadorunos/(mitadfilas*numcolumnas)
    
    razonceros = contadorceros/(mitadfilas*numcolumnas)
    
    razonesareamitad = [razonunos,razonceros]
    
    return razonesareamitad
    




def AreaCuartoSuperiorBlancosNegros(imagenmatriz,numfilas,numcolumnas):
    
    contadorceros = 0
    
    contadorunos = 0
    
    razonesareacuarto = []
    
    cuartofilas = int(numfilas/4)
    
    for x in range(cuartofilas):
        
        for y in range(numcolumnas):
            
            if(imagenmatriz[x][y]==0):
                
                contadorceros = contadorceros + 1
            else:
                
                contadorunos = contadorunos + 1
    
    razonunos = contadorunos/(cuartofilas*numcolumnas)
    
    razonceros = contadorceros/(cuartofilas*numcolumnas)
    
    razonesareacuarto = [razonunos,razonceros]
    
    return razonesareacuarto
    




def AreaTresCuartoSuperiorBlancosNegros(imagenmatriz,numfilas,numcolumnas):
    
    contadorceros = 0
    
    contadorunos = 0
    
    razonesareatrescuarto = []
    
    trescuartofilas = int((numfilas/4)*3)
    
    for x in range(trescuartofilas):
        
        for y in range(numcolumnas):
            
            if(imagenmatriz[x][y]==0):
                
                contadorceros = contadorceros + 1
            else:
                
                contadorunos = contadorunos + 1
    
    razonunos = contadorunos/(trescuartofilas*numcolumnas)
    
    razonceros = contadorceros/(trescuartofilas*numcolumnas)
    
    razonesareatrescuarto = [razonunos,razonceros]
    
    return razonesareatrescuarto
   




def RazonMitadVertical(imagenmatriz,numfilas,numcolumnas):
    
    contadorunos = 0
    
    mitadcolumnas = int(numcolumnas/2)
    
    for x in range(numfilas):
        
        if(imagenmatriz[x][mitadcolumnas]==1):
            
            contadorunos += 1
    
    razon = contadorunos/numfilas
    
    return razon





def RazonMitadHorizontal(imagenmatriz,numfilas,numcolumnas):
    
    contadorunos = 0
    
    mitadfilas = int(numfilas/2)
    
    for x in range(numcolumnas):
        
        if(imagenmatriz[mitadfilas][x]==1):
            
            contadorunos += 1
    
    razon = contadorunos/numcolumnas
    
    return razon





def RazonCuartoVertical(imagenmatriz,numfilas,numcolumnas):
    
    contadorunos = 0
    
    cuartocolumnas = int(numcolumnas/4)
    
    for x in range(numfilas):
        
        if(imagenmatriz[x][cuartocolumnas]==1):
            
            contadorunos += 1
    
    razon = contadorunos/numfilas
    
    return razon





def RazonCuartoHorizontal(imagenmatriz,numfilas,numcolumnas):
    
    contadorunos = 0
    
    cuartofilas = int(numfilas/4)
    
    for x in range(numcolumnas):
        
        if(imagenmatriz[cuartofilas][x]==1):
            
            contadorunos += 1
    
    razon = contadorunos/numcolumnas
    
    return razon
   





def RazonTresCuartoVertical(imagenmatriz,numfilas,numcolumnas):
    
    contadorunos = 0
    
    trescuartocolumnas = int((numcolumnas/4)*3)
    
    for x in range(numfilas):
        
        if(imagenmatriz[x][trescuartocolumnas]==1):
            
            contadorunos += 1
    
    razon = contadorunos/numfilas
    
    return razon





def RazonTresCuartoHorizontal(imagenmatriz,numfilas,numcolumnas):
    
    contadorunos = 0
    
    trescuartofilas = int((numfilas/4)*3)
    
    for x in range(numcolumnas):
         
        if(imagenmatriz[trescuartofilas][x]==1):
            
            contadorunos += 1
    
    razon = contadorunos/numcolumnas
    
    return razon
   




def CortesMitadVertical(imagenmatriz,numfilas,numcolumnas):
    
    apuntadoractual = 0
    
    apuntadordelantero = 0
    
    cortes = 0
    
    filauno = 0
    
    mitadcolumnas = int(numcolumnas/2)
    
    for x in range(numfilas):
        
        apuntadoractual = imagenmatriz[x][mitadcolumnas]
        
        if(x<numfilas-1):
            
            apuntadordelantero = imagenmatriz[x+1][mitadcolumnas]
            
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (filauno==0 and imagenmatriz[0][mitadcolumnas]==1)):
                
                cortes = cortes + 1
                
                filauno = filauno + 1
    
    return cortes
    





def CortesMitadHorizontal(imagenmatriz,numfilas,numcolumnas):
    
    apuntadoractual = 0
    
    apuntadordelantero = 0
    
    cortes = 0
    
    columnauno = 0
    
    mitadfilas = int(numfilas/2)
    
    for x in range(numcolumnas):
        
        apuntadoractual = imagenmatriz[mitadfilas][x]
        
        if(x<numcolumnas-1):
            
            apuntadordelantero = imagenmatriz[mitadfilas][x+1]
            
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (columnauno==0 and imagenmatriz[mitadfilas][0]==1)):
                
                cortes = cortes + 1
                
                columnauno = columnauno + 1
    
    return cortes






def CortesCuartoVertical(imagenmatriz,numfilas,numcolumnas):
    
    apuntadoractual = 0
    
    apuntadordelantero = 0
    
    cortes = 0
    
    filauno = 0
    
    cuartocolumnas = int(numcolumnas/4)
    
    for x in range(numfilas):
        
        apuntadoractual = imagenmatriz[x][cuartocolumnas]
        
        if(x<numfilas-1):
            
            apuntadordelantero = imagenmatriz[x+1][cuartocolumnas]
            
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (filauno==0 and imagenmatriz[0][cuartocolumnas]==1)):
                
                cortes = cortes + 1
                
                filauno = filauno + 1
    
    return cortes
            





def CortesCuartoHorizontal(imagenmatriz,numfilas,numcolumnas):
    
    apuntadoractual = 0
    
    apuntadordelantero = 0
    
    cortes = 0
    
    columnauno = 0
    
    cuartofilas = int(numfilas/4)
    
    for x in range(numcolumnas):
        
        apuntadoractual = imagenmatriz[cuartofilas][x]
        
        if(x<numcolumnas-1):
            
            apuntadordelantero = imagenmatriz[cuartofilas][x+1]
            
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (columnauno==0 and imagenmatriz[cuartofilas][0]==1)):
                
                cortes = cortes + 1
                
                columnauno = columnauno + 1
    
    return cortes
            





def CortesTresCuartosVertical(imagenmatriz,numfilas,numcolumnas):
    
    apuntadoractual = 0
    
    apuntadordelantero = 0
    
    cortes = 0
    
    filauno = 0
    
    cuartocolumnas = int((numcolumnas/4)*3)
    
    for x in range(numfilas):
        
        apuntadoractual = imagenmatriz[x][cuartocolumnas]
        
        if(x<numfilas-1):
            
            apuntadordelantero = imagenmatriz[x+1][cuartocolumnas]
            
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (filauno==0 and imagenmatriz[0][cuartocolumnas]==1)):
                
                cortes = cortes + 1
                
                filauno = filauno + 1
    
    return cortes
            





def CortesTresCuartosHorizontal(imagenmatriz,numfilas,numcolumnas):
    
    apuntadoractual = 0
    
    apuntadordelantero = 0
    
    cortes = 0
    
    columnauno = 0
    
    cuartofilas = int((numfilas/4)*3)
    
    for x in range(numcolumnas):
        
        apuntadoractual = imagenmatriz[cuartofilas][x]
        
        if(x<numcolumnas-1):
            
            apuntadordelantero = imagenmatriz[cuartofilas][x+1]
            
            if((apuntadordelantero!=apuntadoractual and apuntadordelantero==1) or (columnauno==0 and imagenmatriz[cuartofilas][0]==1)):
                
                cortes = cortes + 1
                
                columnauno = columnauno + 1
    
    return cortes





def CruzBlancosNegros(imagenmatriz,numfilas,numcolumnas):   
    
    contadorcerosvertical = 0
    
    contadorunosvertical = 0
    
    contadorceroshorizontal = 0
    
    contadorunoshorizontal = 0
    
    razonescruz = []
    
    mitadfilas = int(numfilas/2)
    
    mitadcolumnas = int(numcolumnas/2)
    
    for x in range(numfilas):
        
        if(imagenmatriz[x][mitadcolumnas]==0):
            
            contadorcerosvertical = contadorcerosvertical + 1
        else:
            
            contadorunosvertical = contadorunosvertical + 1
    
    for y in range(numcolumnas):
        
        if(imagenmatriz[mitadfilas][y]==0):
            
            contadorceroshorizontal = contadorceroshorizontal + 1
        else:
            
            contadorunoshorizontal = contadorunoshorizontal + 1
    
    razonblancos = (contadorcerosvertical + contadorceroshorizontal)/(numcolumnas+numfilas)  
    
    razonnegros = (contadorunosvertical + contadorunoshorizontal)/(numcolumnas+numfilas)
    
    razonescruz = [razonblancos,razonnegros]
    
    return razonescruz        






def DiferenciaMitadArea(imagenmatriz,numfilas,numcolumnas):
    
    contadorcerosmitad = 0
    
    contadorunosmitad = 0
    
    mitadcolumnas = int(numcolumnas/2)
    
    contadorceros = 0
    
    contadorunos = 0
    
    for x in range(numfilas):
        
        for y in range(mitadcolumnas,numcolumnas):
            
            if(imagenmatriz[x][y]==0):
                
                contadorceros = contadorceros + 1
            else:
                
                contadorunos = contadorunos + 1
    
    for x in range(numfilas):
        
        for y in range(mitadcolumnas):
            
            if(imagenmatriz[x][y]==0):
                
                contadorcerosmitad = contadorcerosmitad + 1
            else:
                 
                contadorunosmitad = contadorunosmitad + 1
    
    diferenciaunos = (contadorunosmitad*2)/contadorunos
    
    return diferenciaunos
    





def DiferenciaMitadAreaHorizontal(imagenmatriz,numfilas,numcolumnas):
    
    contadorcerosmitad = 0
    
    contadorunosmitad = 0
    
    mitadfilas = int(numfilas/2)
    
    contadorceros = 0
    
    contadorunos = 0
    
    for x in range(mitadfilas,numfilas):
        
        for y in range(numcolumnas):
            
            if(imagenmatriz[x][y]==0):
                
                contadorceros = contadorceros + 1
            else:
                
                contadorunos = contadorunos + 1
    
    for x in range(mitadfilas):
        
        for y in range(numcolumnas):
            
            if(imagenmatriz[x][y]==0):
                
                contadorcerosmitad = contadorcerosmitad + 1
            else:
                 
                contadorunosmitad = contadorunosmitad + 1
    
    diferenciaunos = (contadorunosmitad*2)/contadorunos
    
    return diferenciaunos
    




def LeerImagen(ruta):
    
    parametrosimagen = []
    
    imagenjpg = Image.open(ruta)
    
    imagenmatriz = mpimg.imread(ruta)
    
    numcolumnas, numfilas = imagenjpg.size
    
    parametrosimagen = [imagenmatriz,numfilas,numcolumnas]
    
    return parametrosimagen
    


def main():
    
    datasetfila = []
    
    rootDir= './dataset/'
    
    f = open('data.csv','w',newline='')
    
    documento = csv.writer(f,delimiter=',')
    
    for dirName, subdirList, fileList in os.walk(rootDir):
        
        print('Procesando clase: %s' % dirName)
        
        for fname in fileList:
            
            ruta = dirName + '/' + fname
            
            clase = dirName[10]
            
            
            li = LeerImagen(ruta)
            rfc = RazonFilasColumnas(li[1],li[2])
            abc = AreaBlancosNegros(li[0],li[1],li[2])
            amsbn = AreaMitadSuperiorBlancosNegros(li[0],li[1],li[2])
            acsbn = AreaCuartoSuperiorBlancosNegros(li[0],li[1],li[2])
            atcsbn = AreaTresCuartoSuperiorBlancosNegros(li[0],li[1],li[2])
            rmh = RazonMitadHorizontal(li[0],li[1],li[2])
            rmv = RazonMitadVertical(li[0],li[1],li[2])
            rch = RazonCuartoHorizontal(li[0],li[1],li[2])
            rcv = RazonCuartoVertical(li[0],li[1],li[2])
            rtch = RazonTresCuartoHorizontal(li[0],li[1],li[2])
            rtcv = RazonTresCuartoVertical(li[0],li[1],li[2])
            cmv = CortesMitadVertical(li[0],li[1],li[2])
            cmh = CortesMitadHorizontal(li[0],li[1],li[2])
            ccv = CortesCuartoVertical(li[0],li[1],li[2])
            cch = CortesCuartoHorizontal(li[0],li[1],li[2])
            ctcv = CortesTresCuartosVertical(li[0],li[1],li[2])
            ctch = CortesTresCuartosHorizontal(li[0],li[1],li[2])
            cbn = CruzBlancosNegros(li[0],li[1],li[2])
            dma = DiferenciaMitadArea(li[0],li[1],li[2])
            dmah = DiferenciaMitadAreaHorizontal(li[0],li[1],li[2])
            
            datasetfila.append([rfc,abc[0],amsbn[0],acsbn[0],atcsbn[0],rmh,rmv,rch,rcv,rtch,rtcv,cmv,cmh,ccv,cch,ctcv,ctch,cbn[0],dma,dmah,clase])
    
    documento.writerows(datasetfila)
    
    f.close()




 

import csv

import math

import ocr_dataset as ocrds






def nuevaInstanciaK():
    
    imagen = str(input('\nNúmero a identificar: '))
    
    k = int(input('\nNúmero de vecinos: '))
    
    print('\nObteniendo características de imagen...')
    
    ruta = './test/' + imagen + '.png'
    
    
    
    li = ocrds.LeerImagen(ruta)
    rfc = ocrds.RazonFilasColumnas(li[1],li[2])
    abc = ocrds.AreaBlancosNegros(li[0],li[1],li[2])
    amsbn = ocrds.AreaMitadSuperiorBlancosNegros(li[0],li[1],li[2])
    acsbn = ocrds.AreaCuartoSuperiorBlancosNegros(li[0],li[1],li[2])
    atcsbn = ocrds.AreaTresCuartoSuperiorBlancosNegros(li[0],li[1],li[2])
    rmh = ocrds.RazonMitadHorizontal(li[0],li[1],li[2])
    rmv = ocrds.RazonMitadVertical(li[0],li[1],li[2])
    rch = ocrds.RazonCuartoHorizontal(li[0],li[1],li[2])
    rcv = ocrds.RazonCuartoVertical(li[0],li[1],li[2])
    rtch = ocrds.RazonTresCuartoHorizontal(li[0],li[1],li[2])
    rtcv = ocrds.RazonTresCuartoVertical(li[0],li[1],li[2])
    cmv = ocrds.CortesMitadVertical(li[0],li[1],li[2])
    cmh = ocrds.CortesMitadHorizontal(li[0],li[1],li[2])
    ccv = ocrds.CortesCuartoVertical(li[0],li[1],li[2])
    cch = ocrds.CortesCuartoHorizontal(li[0],li[1],li[2])
    ctcv = ocrds.CortesTresCuartosVertical(li[0],li[1],li[2])
    ctch = ocrds.CortesTresCuartosHorizontal(li[0],li[1],li[2])
    cbn = ocrds.CruzBlancosNegros(li[0],li[1],li[2])
    dma = ocrds.DiferenciaMitadArea(li[0],li[1],li[2])
    dmah = ocrds.DiferenciaMitadAreaHorizontal(li[0],li[1],li[2])
    
    nuevainstancia = [rfc,abc[0],amsbn[0],acsbn[0],atcsbn[0],rmh,rmv,rch,rcv,rtch,rtcv,cmv,cmh,ccv,cch,ctcv,ctch,cbn[0],dma,dmah,k]
    
    return nuevainstancia





def cargarDataset(nombrearchivo):
    
    with open(nombrearchivo, 'r') as csvfile:
        
        lineas = csv.reader(csvfile)
        
        dataset = list(lineas)
        
        contadorinstancias = 0
        
        for x in range(len(dataset)):
            
            contadorinstancias = contadorinstancias + 1
            
            for y in range(21):
                
                if(y<20):
                    
                    dataset[x][y] = float(dataset[x][y])
                else:
                    
                    dataset[x][y] = dataset[x][y]
        
        print("============ Información del Dataset ============")
        print("\tNúmero de Instancias: " + str(contadorinstancias))
        print("\tNúmero de Características por Instancia: 20")
        print("\tNúmero de Clases: 10")
        print("\tNombre de Clases: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}")
    
    return dataset






def calcularDistancia(dataset,ni):
    
    print('\nCalculando distancias...')
    
    distancias = []
    
    
    for x in range(len(dataset)):
        
        distancias.append([math.sqrt(pow((dataset[x][0] - float(ni[0])),2)+pow((dataset[x][1]-float(ni[1])),2)+pow((dataset[x][2]-float(ni[2])),2)+pow((dataset[x][3]-float(ni[3])),2)+pow((dataset[x][4]-float(ni[4])),2)+pow((dataset[x][5]-float(ni[5])),2)+pow((dataset[x][6]-float(ni[6])),2)+pow((dataset[x][7]-float(ni[7])),2)+pow((dataset[x][8]-float(ni[8])),2)+pow((dataset[x][9]-float(ni[9])),2)+pow((dataset[x][10]-float(ni[10])),2)+pow((dataset[x][11]-float(ni[11])),2)+pow((dataset[x][12]-float(ni[12])),2)+pow((dataset[x][13]-float(ni[13])),2)+pow((dataset[x][14]-float(ni[14])),2)+pow((dataset[x][15]-float(ni[15])),2)+pow((dataset[x][16]-float(ni[16])),2)+pow((dataset[x][17]-float(ni[17])),2)+pow((dataset[x][18]-float(ni[18])),2)+pow((dataset[x][19]-float(ni[19])),2)),dataset[x][20],x+1])
    
    temp = 0
    
    tam = len(distancias)
    
    for i in range(1, tam):
        
        for j in range(0,tam-1):
            
            
            if(distancias[j]>distancias[j+1]):
               
               temp = distancias[j+1]
               
               distancias[j+1] = distancias[j]
               
               distancias[j] = temp
    
    return distancias     






def clasificarInstancia(distancias,ni):
    print('\nObteniendo distancias mas cercanas...')
    
    contadorinstancias = 1
    
    contadorcero = 0
    contadoruno = 0
    contadordos = 0
    contadortres = 0
    contadorcuatro = 0
    contadorcinco = 0
    contadorseis= 0
    contadorsiete = 0
    contadorocho = 0
    contadornueve = 0
    
    print('\n')
    print('     K      |       Distancia     |Clase|Fila|')
    print('----------------------------------------------')
    
    for x in range(int(ni[20])):
        print('Instancia '+str(contadorinstancias)+" = "+str(distancias[x]))
        
        contadorinstancias = contadorinstancias + 1
        
        if(distancias[x][1]=='0'):
            contadorcero += 1
        if(distancias[x][1]=='1'):
            contadoruno += 1
        if(distancias[x][1]=='2'):
            contadordos += 1
        if(distancias[x][1]=='3'):
            contadortres += 1
        if(distancias[x][1]=='4'):
            contadorcuatro += 1
        if(distancias[x][1]=='5'):
            contadorcinco += 1
        if(distancias[x][1]=='6'):
            contadorseis += 1
        if(distancias[x][1]=='7'):
            contadorsiete += 1
        if(distancias[x][1]=='8'):
            contadorocho += 1
        if(distancias[x][1]=='9'):
            contadornueve += 1
    
    clases = []
    
    clases = [contadorcero,contadoruno,contadordos,contadortres,contadorcuatro,contadorcinco,contadorseis,contadorsiete,contadorocho,contadornueve]
    
    clasemayor = 0
    
    clasificacion = 0
    for x in range(len(clases)):
        
        if(clases[x] > clasemayor):
            
            clasemayor = clases[x]
            
            clasificacion = x    
    
    
    if(contadorcero>0):
        print('\nClase 0: '+str(contadorcero) + ' Instancias detectadas')
    if(contadoruno>0):
        print('\nClase 1: '+str(contadoruno) + ' Instancias detectadas')
    if(contadordos>0):
        print('\nClase 2: '+str(contadordos) + ' Instancias detectadas')
    if(contadortres>0):
        print('\nClase 3: '+str(contadortres) + ' Instancias detectadas')
    if(contadorcuatro>0):
        print('\nClase 4: '+str(contadorcuatro) + ' Instancias detectadas')
    if(contadorcinco>0):
        print('\nClase 5: '+str(contadorcinco) + ' Instancias detectadas')
    if(contadorseis>0):
        print('\nClase 6: '+str(contadorseis) + ' Instancias detectadas')
    if(contadorsiete>0):
        print('\nClase 7: '+str(contadorsiete) + ' Instancias detectadas')
    if(contadorocho>0):
        print('\nClase 8: '+str(contadorocho) + ' Instancias detectadas')
    if(contadornueve>0):
        print('\nClase 9: '+str(contadornueve) + ' Instancias detectadas')
    
    print('\n\nCaracter predicho: ' + str(clasificacion))



ds = cargarDataset("data.csv")

nik = nuevaInstanciaK()    

cd = calcularDistancia(ds,nik)

clasificarInstancia(cd,nik)


