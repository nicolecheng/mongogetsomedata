from pymongo import MongoClient
import csv

server = MongoClient('149.89.150.100')
db = server.mongeese
thepeeps = db.thepeeps

#{name, age, id, classes:[code:mark]}

people = thepeeps.find()#{'classes'})

for a in people:
    #print a
    name = a['name']
    id = a['_id']
    classes = a['classes']
    sum = 0
    count = 0
    for m in classes:
        #print m.values()
        sum += int(m.values()[0])
        count += 1
    print name+","+str(id)+","+str(float(sum)/float(count))

ts = open('teachers.csv')
t = csv.DictReader(ts)
teachers = db.teachers

listODocs = []
for key in t:
    doc = { 'code': key['code'], 'teacher': key['teacher'], 'period': key['period'] }
    listODocs.append(doc)

for a in listODocs:
#    students = thepeeps.find({'classes.code' : a['code']})
# let's just find the students. his code makes no sense

    studs = []
    listOStudents = thepeeps.find()
    for z in listOStudents:
        for b in z:
            if b == 'classes':
                for c in z['classes']:
                    for d in c:
                        if d == a['code']:
                            studs.append(z)
                

    ls = []
    for key in studs:
        ls.append(key['_id'])
    a['students'] = ls

for a in listODocs:
    teachers.insert_one(a)

#to test:
#for a in listODocs:
#    print a

