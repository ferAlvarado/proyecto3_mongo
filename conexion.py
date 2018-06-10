import pymongo
import sys
import re
import xml.sax
import os
from datetime import datetime
import xmltodict
import json
from io import StringIO
import xml.etree.ElementTree as ET

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



"""Leer archivos xml"""
path= "/home/fernanda/Documents/Bases/Proyecto3/reuters21578"
contenido = os.listdir("/home/fernanda/Documents/Bases/Proyecto3/reuters21578")
for filename in contenido:
    archivo=os.path.join(path,filename)
    with open(archivo,encoding='utf-8', errors='ignore') as f:
        xmlreader=f.read()
        try:
            doc=xmltodict.parse(xmlreader)
            j=json.dumps(doc)
            print(j)
        except (ET.ParseError):
            print ("error on row", "column" )
       # jsonString = json.dumps(xmltodict.parse(xmlreader), indent=4)
##Se supone que con esto se convierte a jason, solo que hay que quitar los espacios
 #Unknown y companies de los archivos
 #Esto porque tienen datos irrelevantes y caracteres invalidos       
        
  
    
