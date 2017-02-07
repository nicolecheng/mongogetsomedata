'''Using python and the database from the previous assignment write a program to do the following:
Compute the average for each student.
Display each students name, id and average.'''

from pymongo import MongoClient
server = MongoClient('149.89.150.100')
db = server.mongeese
peps = db.peps

#{name, age, id, classes:[code:mark]}

person = peps.find({'classes'})

for a in person:
    print a
