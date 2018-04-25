from pymongo import MongoClient
from bson.json_util import dumps,loads

def mongo_connect(url,port,dbs,collection):
    client = MongoClient(url, port)
    db = client[dbs]
    collection = db[collection]
    return collection


def findAll(client,arrayName):
    cursor = client.find({})
    cursorToList = dumps(cursor)
    listToJson = loads(cursorToList)
    data = {}
    data[arrayName] = listToJson
    return data