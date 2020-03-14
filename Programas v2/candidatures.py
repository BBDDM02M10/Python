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
import mysql.connector

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

cnx = mysql.connector.connect(host='192.168.255.133',user='perepi',password='pastanaga',
      database='eleccions_generals2')
cursor = cnx.cursor()

try:
   with open (pathFitxer,'r') as fitxer:

       for linea in fitxer:
            llista = []
            llista.append(linea[15:64].strip())
            llista.append(linea[64:214].strip())
            llista.append(linea[220:226])
            llista.append(linea[226:232])
            insert_candidatures = ('INSERT INTO candidatures (eleccio_id, nom_curt, nom_llarg, codi_acumulacio_provincia, codi_acumulacio_ca) VALUES (1,%s, %s, %s, %s)')
            cursor.execute(insert_candidatures, llista)
except OSError as e:
    print('Imposible abrir fichero ' + pathFitxer)

cnx.commit()
cursor.close()
cnx.close()

