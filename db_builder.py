from pymongo import MongoClient
import csv

server = MongoClient()#'149.89.150.100')
print server
db = server.mongeese 
print db

# peeps - name, age, id

f1 = open('peeps.csv')

d1 = csv.DictReader(f1)

peeps = db.peeps
print peeps
dict = {}

print "step 1"

for key in d1:
    doc = { 'name': key['name'], 'age': key['age'], 'id': key['id'] }
    print doc
    peeps.insert_one( doc )

print "step 2"
'''
f2 = open('courses.csv')

d2  = csv.DictReader(f2)

courses = db.courses

print "step 3"

for key in d2:
    doc = { 'code': key['code'], 'mark': key['mark'], 'id': key['id'] }
    courses.inert_one( doc )

print "step 4"
'''
