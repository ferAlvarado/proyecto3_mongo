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
#path= "/home/fernanda/Desktop"
#archivo=os.path.join(path,"prueba1.xml")

path= "E:\Desktop\proyecto3_mongo\\reuters21578"
archivo=os.path.join(path,"test.xml")

'''
##cleanList: ajusta los valores multiples de los documentos REUTERS
##input i: Documento REUTERS como ordereddict
##input Key: Nombre del campo a ajustar
ej.
 "PLACES": {
                "D": [
                    "usa",
                    "ussr"
                ]
            },
 -->
  "PLACES": [
                "usa",
                "ussr"
            ],
'''
def cleanList(i,Key):
    if i[Key] is not None:
        if 'D' in i[Key]:
            temp = i[Key]['D']
            del i[Key]['D']
            i.update({Key:temp})
    
with open(archivo,encoding='utf-8', errors='ignore') as f:
    xmlreader=f.read()
    doc=xmltodict.parse(xmlreader)
    doc = doc['COLLECTION']['REUTERS']
    for i in doc:
        if 'MKNOTE' in i:
            del i['MKNOTE']
        if 'UNKNOWN' in i:
            del i['UNKNOWN']
        cleanList(i,'PLACES')
        cleanList(i,'TOPICS')
        cleanList(i,'PEOPLE')
        cleanList(i,'ORGS')
        cleanList(i,'EXCHANGES')
        

    jsonString = json.dumps(doc, indent=4)
    print(jsonString)

####mongoimport --db db --collection db --file E:\Desktop\test.json --jsonArray
        
  
    
