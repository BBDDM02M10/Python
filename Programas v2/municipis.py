#-------------------------------------------------------------------------------
# Name:        módulo1
# Purpose:
#
# Author:      Manu
#
# Created:     14/03/2020
# Copyright:   (c) Manu 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import zipfile
import os
import sys
import mysql.connector

rutazip = r'C:\Users\Manu\Desktop\Python\Zips\02197706_MESA.zip'
rutaunzip = r'C:\Users\Manu\Desktop\Python\Unzips\02197706_MESA.zip'
fileUnzip = r'C:\Users\Manu\Desktop\Python\Unzips\05027706.DAT'

dirActual = os.path.dirname(rutazip)
print(dirActual)
nomFitxerZip = '02197706_MESA.zip'
dirUnzip = os.path.dirname (rutaunzip )
pathFitxerZip = os.path.join(dirActual,nomFitxerZip)
print(dirUnzip)


with zipfile.ZipFile(pathFitxerZip,'r') as zipRef:
     zipRef.extractall(dirUnzip)

pathFitxer = fileUnzip

cnx = mysql.connector.connect(host='192.168.255.133',user='perepi',password='pastanaga',
      database='eleccions_generals2')
cursor = cnx.cursor()

try:
   with open (pathFitxer,'r') as fitxer:

       for linea in fitxer:
            llista = []
            #CD = (linea[8:14])
            llista.append(linea[18:118].strip())
            llista.append(linea[11:13])
            llista.append(linea[13:16])
            llista.append(linea[16:18])
            insert_municipis = ('INSERT INTO municipis (nom, codi_ine, provincia_id, districte) VALUES (%s, %s, %s, %s)')
            cursor.execute(insert_municipis, llista)
            #print(llista)

except OSError as e:
    print('Imposible abrir fichero ' + pathFitxer)

cnx.commit()
cursor.close()
cnx.close()
