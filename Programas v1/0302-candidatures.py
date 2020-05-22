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
fileUnzip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Unzips\03027706.DAT'

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
            llista.append(linea[15:64].strip())
            llista.append(linea[64:214].strip())
            llista.append(linea[214:220].strip())
            llista.append(linea[220:226].strip())
            #llista.append(linea)
            print(llista)

except OSError as e:
    print('Imposible abrir fichero ' + pathFitxer)
