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

"""Crear conexión con mongo"""

def conexionBD():
    con = pymongo.MongoClient()
    db=con.proyecto3
    nombre_coleccion=input("Ingrese el nombre de la coleccion: ")
    record1=db.create_collection(nombre_coleccion)
    return record1

def cleanList(i,Key):
    if i[Key] is not None:
        if 'D' in i[Key]:
            temp = i[Key]['D']
            del i[Key]['D']
            i.update({Key:temp})

"""Leer archivos xml"""

def xmlTOjson(path,contenido,base):
    documentos=[]
    for filename in contenido:
        archivo=os.path.join(path,filename)
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
            parsed=json.loads(jsonString)
            base.insert(parsed)
    return documentos

def crearIndices(base):
    base.create_index([("TOPICS",pymongo.ASCENDING)])
    base.create_index([("PLACES",pymongo.ASCENDING)])
    base.create_index([("PEOPLE",pymongo.ASCENDING)])
    base.create_index([("ORGS",pymongo.ASCENDING)])
    base.create_index([("EXCHANGES",pymongo.ASCENDING)])
    base.create_index([("TITLE",pymongo.TEXT)])
    base.create_index([("BODY",pymongo.TEXT)])
    
#"/home/fernanda/Documents/Bases/Proyecto3/reuters21578"

def main(ruta):
    path= ruta
    contenido = os.listdir(ruta)
    record1=conexionBD()
    documentos= xmlTOjson(path,contenido,record1)
    print("Carga terminada")
    crearIndices(record1)
    print("Indices creados")
