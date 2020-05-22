#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Manu
#
# Created:     10/03/2020
# Copyright:   (c) Manu 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import zipfile
import os
import sys

rutazip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Zips\02197706_MESA.zip'
rutaunzip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Unzips\02197706_MESA.zip'
fileUnzip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Unzips\07027706.DAT'

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
       cont = 0
       for linea in fitxer:

            if linea[11:13] == '99' and linea[9:11] !='99':
                llista = []
                llista.append(linea[14:64].strip())
                llista.append(linea[9:11])
                print(llista)
                cont+=1
       print(cont)

except OSError as e:
    print('Imposible abrir fichero ' + pathFitxer)