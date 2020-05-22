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
fileUnzip = r'C:\Users\Manu\Desktop\Git BBDD\Python\Python pruebas\Unzips\04027706.DAT'

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

cnx = mysql.connector.connect(host='192.168.255.131',user='perepi',password='pastanaga',
      database='eleccions_generals2')
cursor = cnx.cursor()

try: # Creacion de excepcion
   with open (pathFitxer,'r') as fitxer: # abrir archivo .DAT en modo lectura
       for linea in fitxer: # Bucle para leer linea a linea archivo .DAT
            llista = []
            llista1 = []
            llista1.append(linea[25:50].strip()) # Nombre candidato
            for elemento in llista1:# Bucle para leer linea a linea archivo .DAT
                        llista.append(elemento)
            llista.append(linea[22:24]) # Codigo candidatura
            llista.append(linea[24:25]) # Orden candidato
            llista.append(linea[9:11]) # Codigo ine provincia
            llista.append(linea[15:21]) # Codigo ine municipio
            insert_candidats = ('INSERT INTO candidats (nom_complet, num_ordre, tipus, provincia_id, candidatura_id) VALUES (%s, %s, %s,%s, %s)')
            cursor.execute(insert_candidats, llista) # Insertamos en tabla de BBDD
except OSError as e: # Resolucion excepcion
    print('Imposible abrir fichero ' + pathFitxer)

'''Cerramos conexion BBDD'''

cnx.commit()
cursor.close()
cnx.close()
