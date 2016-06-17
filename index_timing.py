
import pymongo
import sys
import time 

#start timer
t0 = time.time()

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

#time creation of conention
t1 = time.time()


# get a handle to the th new sample database and coleltion
connection.drop_database("new_test")

t2 = time.time()

db=connection.new_test
co = db.index_text
# get time for creaetion (is lazy so nothing shoudl have happend)
t3 = time.time()

for a in range(100):
    for b in range(10):
        for c in range(10):
            co.insert_one({"a":a, "b": b, "c":c})

#inserted the 10,000 documents
t4 = time.time()

#def find():
#
#    print "reporting for duty"
#    
#    
#
#    query = {"year":2000}
#    #projection = {}
#    #projection = {"year":1, "score":1}
#    #e from the year 2013 that is rated PG-13 and won no awards?
##    a = de.find(query)
##    return a
#
#    a = de.find(query)
#    print type(a)
#    return a.explain()
#    #print a
#    
##    id_field = 0
#    #counter = 0
##    for c in a:
###        if len(c['countries']) >=2:
###            if c['countries'][1] == "Sweden":
###                counter +=1
###        c_id = c['student_id']
###        c_ob = c['_id']
###        if c_id == id_field:
###            grades.delete_one({'_id': c_ob})
###            
###        id_field = c_id
###
##        print c
#      
#    #b = de.find_one()
#
##    print b
#    #print de.find_one().pretty()
##    try:
##        grades.delete_many(query)
##    except Exception as e:
##        print "Unexpected error:", type(e), e
#
#
#print ('Pos path creation', time.time() - t0)        
#
#print find()
#
#print ('Pos path creation', time.time() - t0)
#
#a = find()