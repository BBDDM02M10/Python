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

rutazip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Zips\02197706_MESA.zip'
rutaunzip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Unzips\02197706_MESA.zip'
fileUnzip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Unzips\04027706.DAT'

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
            llista1 = []

            llista1.append(linea[25:50].strip())
            for elemento in llista1:
                        llista.append(elemento)
            llista.append(linea[22:24])
            llista.append(linea[24:25])
            llista.append(linea[9:11])
            llista.append(linea[15:21])
            insert_candidats = ('INSERT INTO candidats (nom_complet, num_ordre, tipus, provincia_id, candidatura_id) VALUES (%s, %s, %s,%s, %s)')
            cursor.execute(insert_candidats, llista)

except OSError as e:
    print('Imposible abrir fichero ' + pathFitxer)

cnx.commit()
cursor.close()
cnx.close()
