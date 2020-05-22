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

'''Rutas'''

rutazip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Zips\02197706_MESA.zip'
rutaunzip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Unzips\02197706_MESA.zip'
fileUnzip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Unzips\05027706.DAT'

dirActual = os.path.dirname(rutazip) # Directorio archivo cotenedor zip
print(dirActual)
nomFitxerZip = '02197706_MESA.zip' # Nombre archivo a tratar
dirUnzip = os.path.dirname (rutaunzip ) # Directorio donde descomprimir
pathFitxerZip = os.path.join(dirActual,nomFitxerZip) # Ruta archivo a tratar
print(dirUnzip)

'''Tramiento Archivo'''

with zipfile.ZipFile(pathFitxerZip,'r') as zipRef: # Abrir archivo en modo lectura
     zipRef.extractall(dirUnzip) # Descompresion archivo en carpeta definida en ruta

pathFitxer = fileUnzip

'''Conexion con BBDD'''

cnx = mysql.connector.connect(host='192.168.255.133',user='perepi',password='pastanaga',
      database='eleccions_generals2')
cursor = cnx.cursor()

try: # Creacion de excepcion
   with open (pathFitxer,'r') as fitxer: # abrir archivo .DAT en modo lectura
       for linea in fitxer: # Bucle para leer linea a linea archivo .DAT
            llista = []
            llista.append(linea[18:118].strip()) # Nombre municipio
            llista.sort() # Ordenar lista
            llista.append(linea[13:16]) # Codigo Ine municipio
            llista.append(linea[11:13]) # Codigo Ine provincia
            insert_municipis = ('INSERT INTO municipis (nom, codi_ine_municipi, provincia_id) VALUES (%s, %s, %s)')
            cursor.execute(insert_municipis, llista) # Insertamos en tabla de BBDD
except OSError as e: # Resolucion excepcion
    print('Imposible abrir fichero ' + pathFitxer)

'''Cerramos conexion BBDD'''

cnx.commit()
cursor.close()
cnx.close()
