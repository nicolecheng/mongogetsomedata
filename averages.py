'''Using python and the database from the previous assignment write a program to do the following:
Compute the average for each student.
Display each students name, id and average.'''

from pymongo import MongoClient
import csv

server = MongoClient()#'149.89.150.100')
db = server.mongeese
thepeeps = db.thepeeps

#{name, age, id, classes:[code:mark]}

people = thepeeps.find()#{'classes'})

for a in people:
    print a
    name = a['name']
    id = a['_id']
    classes = a['classes']
    sum = 0
    count = 0
    for m in classes:
        sum += int(classes[m])
        count += 1
    print name+","+str(id)+","+str(float(sum)/float(count))
