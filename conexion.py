import pymongo
con = pymongo.MongoClient()
db=con.proyecto3

nombre_coleccion=input("Ingrese el nombre de la coleccion: ")
db.create_collection(nombre_coleccion)
#db.createCollection(nombre_coleccion)
#collection = db[nombre_coleccion]
#smith = {"last_name": "Smith", "age": 30}
print(db.collection_names())
