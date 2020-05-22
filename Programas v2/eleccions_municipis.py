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

'''Rutas'''

rutazip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Zips\02197706_MESA.zip'
rutaunzip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Unzips\02197706_MESA.zip'
fileUnzip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Unzips\05027706.DAT'

dirActual = os.path.dirname(rutazip) # Directorio archivo cotenedor zip
print(dirActual)
nomFitxerZip = '02197706_MESA.zip'
dirUnzip = os.path.dirname (rutaunzip ) # Nombre archivo a tratar
pathFitxerZip = os.path.join(dirActual,nomFitxerZip) # Directorio donde descomprimir
print(dirUnzip)

'''Tramiento Archivo'''

with zipfile.ZipFile(pathFitxerZip,'r') as zipRef: # Abrir archivo en modo lectura
     zipRef.extractall(dirUnzip) # Descompresion archivo en carpeta definida en ruta

pathFitxer = fileUnzip

'''Conexion con BBDD'''

cnx = mysql.connector.connect(host='192.168.255.131',user='perepi',password='pastanaga',
      database='eleccions_generals2')
cursor = cnx.cursor()

try: # Creacion de excepcion
   with open (pathFitxer,'r') as fitxer: # abrir archivo .DAT en modo lectura
       for linea in fitxer: # Bucle para leer linea a linea archivo .DAT
            llista = []
            llista.append(linea[136:141])# Numero mesas
            llista.append(linea[128:136])# Poblacion
            llista.append(linea[141:149])# Censo
            llista.append(linea[205:213])# Votos candidaturas
            llista.append(linea[189:197])# Votos blanco
            llista.append(linea[197:205])# Votos nulos
            insert_comunitats_autonomes = ('INSERT INTO eleccions_municipis (eleccio_id, municipi_id, num_meses, '
                                           'poblacio, cens, vots_candidatures, vots_blanc, vots_nuls) '
                                           'VALUES (1, %s, %s, %s, %s, %s, %s)')
            cursor.execute(insert_comunitats_autonomes, llista) # Insertamos en tabla de BBDD
except OSError as e: # Resolucion excepcion
    print('Imposible abrir fichero ' + pathFitxer)

'''Cerramos conexion BBDD'''

cnx.commit()
cursor.close()
cnx.close()
