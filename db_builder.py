from pymongo import MongoClient
import csv

server = MongoClient('149.89.150.100')
#print server

db = server.mongeese 
#print db

# peeps - name, age, id

f1 = open('peeps.csv')

d1 = csv.DictReader(f1)

peeps = db.peeps

dict = {}

listODocs = []

for key in d1:
    doc = { 'name': key['name'], 'age': key['age'], '_id': key['id'] }
    listODocs.append(doc)

f2 = open('courses.csv')

d2  = csv.DictReader(f2)

for key in d2:
    for a in listODocs:
        if a['_id'] == key["id"]:
            a[key["code"]] = key['mark']

for a in listODocs:
    peeps.insert_one(a)
