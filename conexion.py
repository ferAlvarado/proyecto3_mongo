import pymongo
import sys
import re
import xml.sax
import os
from datetime import datetime
import xmltodict
import json



"""Vrear conexión con mongo"""
##con = pymongo.MongoClient()
##db=con.proyecto3
##
##nombre_coleccion=input("Ingrese el nombre de la coleccion: ")
##db.create_collection(nombre_coleccion)
##print(db.collection_names())


"""Leer archivos xml"""
path= "/home/fernanda/Documents/Bases/Proyecto3/reuters21578"
contenido = os.listdir("/home/fernanda/Documents/Bases/Proyecto3/reuters21578")


##archivo=os.path.join(path, 'reut2-017.xml')
##print(archivo)
####f = open(archivo, 'r')
####
####xml = f.read()
##with open(archivo, "r",encoding='utf-8', errors='ignore') as f:    # notice the "rb" mode
##        print("hola")
##        #d = xmltodict.parse(f, xml_attribs=xml_attribs)
##        #return json.dumps(d, indent=4)
###f.close()

for filename in contenido:
    archivo=os.path.join(path,filename) 
    with open(archivo, "r",encoding='utf-8', errors='ignore') as f:
        print()
