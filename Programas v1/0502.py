#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Manu
#
# Created:     07/03/2020
# Copyright:   (c) Manu 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import zipfile
import os
import sys

rutazip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Zips\02197706_MESA.zip'
rutaunzip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Unzips\02197706_MESA.zip'
fileUnzip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Unzips\05027706.DAT'

dirActual = os.path.dirname(rutazip)
print(dirActual)
nomFitxerZip = '02197706_MESA.zip'
dirUnzip = os.path.dirname (rutaunzip )
pathFitxerZip = os.path.join(dirActual,nomFitxerZip)
print(dirUnzip)


with zipfile.ZipFile(pathFitxerZip,'r') as zipRef:
     zipRef.extractall(dirUnzip)

pathFitxer = fileUnzip

try:
   with open (pathFitxer,'r') as fitxer:

       for linea in fitxer:
            llista = []
            #CD = (linea[8:14])
            llista.append(linea[136:141])# nº mesas
            llista.append(linea[128:136])# poblacion
            llista.append(linea[141:149])# censo
            llista.append(linea[205:213])# votos candidaturas
            llista.append(linea[189:197])# votos blanco
            llista.append(linea[197:205])# votos nulos
            print(llista)

except OSError as e:
    print('Imposible abrir fichero ' + pathFitxer)
