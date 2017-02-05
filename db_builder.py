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
    doc = { 'name': key['name'], 'age': key['age'], 'id': key['id'] }
    peeps.insert_one( doc )


f2 = open('courses.csv')

d2  = csv.DictReader(f2)

courses = db.courses

for key in d2:
    doc = { 'code': key['code'], 'mark': key['mark'], 'id': key['id'] }
    courses.inert_one( doc )
