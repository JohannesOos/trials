
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")



# create again
db=connection.geo_trial

#drop existing collection
db.trial_one.drop()

#use the set up trial database
geo = db.trial_one

#insert first coordinate
for a in range(10):
    for b in range(10):
        for c in range(10):
#            geo.insert_one({"loc" : { "lng" : a , "lat" : b }, "height": c })
        # better to be don ewith list
            geo.insert_one({"loc" : [a,b], "height": c })
        

    


