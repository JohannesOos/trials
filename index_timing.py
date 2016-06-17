
import pymongo
#import sys
import time 
#import random

#start timer
t0 = time.time()

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

#time creation of conention
t1 = time.time()
print "conenction takes s: " + str(t1-t0)
t1 = time.time()

# get a handle to the th new sample database and coleltion
connection.drop_database("new_test")

t2 = time.time()
print "droppung takes s: " + str(t2-t1)
t2 = time.time()

db=connection.new_test
co = db.index_text
# get time for creaetion (is lazy so nothing shoudl have happend)
t3 = time.time()

print "creation takes s: " + str(t3-t2)

t3 = time.time()

for a in range(100):
    for b in range(10):
        for c in range(10):
            co.insert_one({"a":a, "b": b, "c":c})

#inserted the 10,000 documents
t4 = time.time()
print "inserting takes s: " + str(t4-t3)
t4 = time.time()

#create test docs

doc1 = co.find({"a":50, "b": 5, "c":5})

t5 = time.time()
print "fidn in the middle: " + str(t5-t4)
t5 = time.time()

doc2 = co.find({"a":0, "b": 0, "c":0})

t6 = time.time()
print "fidn at start: " + str(t6-t5)
t6 = time.time()


doc3 = co.find({"a":99, "b": 9, "c":9})

t7 = time.time()
print "fidn at end: " + str(t7-t6)
t7 = time.time()

doc4 = co.find({"c":9})

t8 = time.time()
print "find single c: " + str(t8-t7)
t8 = time.time()

    

