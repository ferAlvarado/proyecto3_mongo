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

def conexionBD(nombre_coleccion):
    con = pymongo.MongoClient()
    db=con.proyecto3
    record1=db.create_collection(nombre_coleccion)
    return record1
def conexionBDexistente(nombre_coleccion):
    con = pymongo.MongoClient()
    db=con.proyecto3
    record1= pymongo.collection.Collection(db, nombre_coleccion)
    return record1

def cleanList(i,Key):
    if i[Key] is not None:
        if 'D' in i[Key]:
            temp = i[Key]['D']
            del i[Key]['D']
            i.update({Key:temp})


def busqueda1(base):
    print('\n',"======= Busqueda 1: TOPICS que contienen sugar, PLACES que contienen indonesia =======", '\n', '------------------------------------------------------' )
    query = base.find({'TOPICS': 'sugar','PLACES': 'indonesia'})
    for x in query:
        print(x['@NEWID'], ": ", x['TEXT']['TITLE'], '\n', '------------------------------------------------------' )
def busqueda2(base):
    print('\n',"======= Busqueda 2: BODY que contienen colombia y coffee =======", '\n', '------------------------------------------------------' )
    query = base.find({ '$text': { '$search': "\"coffee\" \"colombia\"" } })
    for x in query:
        print(x['@NEWID'], ": ", x['TEXT']['TITLE'], '\n', '------------------------------------------------------' )

def xmlTOjson(path,contenido,base):
    documentos=[]
    for filename in contenido:
        if filename.endswith('.xml'):
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
    print("Datos cargados.")
    return documentos

def crearIndices(base):
    base.create_index([("TOPICS",pymongo.ASCENDING)])
    base.create_index([("PLACES",pymongo.ASCENDING)])
    base.create_index([("PEOPLE",pymongo.ASCENDING)])
    base.create_index([("ORGS",pymongo.ASCENDING)])
    base.create_index([("EXCHANGES",pymongo.ASCENDING)])
    base.create_index([("TEXT.TITLE",pymongo.TEXT),("TEXT.BODY",pymongo.TEXT)])
    print("Indices creados")
        
    #"/home/fernanda/Documents/Bases/Proyecto3/reuters21578"

def main(ruta):
    path= ruta
    contenido = os.listdir(ruta)
    nombre_coleccion=input("Ingrese el nombre de la coleccion: ")
    try:
        DBconn=conexionBD(nombre_coleccion)
        documentos= xmlTOjson(path,contenido,DBconn)
        crearIndices(DBconn)
    except:
        print("Coleccion con ese nombre ya existe")
        DBconn = conexionBDexistente(nombre_coleccion)
    busqueda1(DBconn)
    busqueda2(DBconn)

main('E:\\Desktop\\proyecto3_mongo\\reuters21578')
