from pymongo import MongoClient
import csv

server = MongoClient(‘149.89.150.100’)
db = server.<team name>

# peeps - name, age, id

f1 = open('peeps.csv')

d1 = csv.DictReader(f1)

peeps = db.peeps

dict = {}

for key in d1:
    doc = { ‘name’: key[0], ‘age’: key[1], 'id': key[2] }

    
    peeps.insert_one( doc )
