
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")


# use the correct database
db=connection.geo_trial

#use the set up trial database
geo = db.trial_one

#insert first coordinate
geo.insert_one({"loc" : { "lng" : 0.1 , "lat" : 0.1 }})


