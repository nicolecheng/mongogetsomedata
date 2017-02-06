from pymongo import MongoClient
import csv

server = MongoClient()#'149.89.150.100')
#print server

db = server.mongeese 
#print db

# peeps - name, age, id

f1 = open('peeps.csv')

d1 = csv.DictReader(f1)

peeps = db.peeps

dict = {}

for key in d1:
    doc = { 'name': key['name'], 'age': key['age'], '_id': key['id'] }
    #print doc
    peeps.insert_one( doc )

f2 = open('courses.csv')

d2  = csv.DictReader(f2)

courses = db.courses

for key in d2:
    db.peeps.update(
        { _id: key["id"]},
        { $set : {"%s".format(key["course"]): key["mark"] } }
        )
    
