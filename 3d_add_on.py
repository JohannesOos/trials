
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")



# define database
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
            geo.insert_one({"loc" : [a,b], "height": c})

#create index       
geo.create_index( [( "loc", "2d" ) ])

# create pipeline for aggregation
pipeline_1 = [{"$match": {"loc": {"$within": {"$box": [[3, 3], [5, 5]]}}}}]
pipeline_2 = [{"$match": {"height": { "$lte": 5}}}]
pipeline_3 = [{"$match": {"height": { "$gte": 4}}}]

#query for 2d results
for place in geo.aggregate(pipeline_1):
    print place
    
print "first query done"
    
#query for 3d results
for place in geo.aggregate(pipeline_1 + pipeline_2+ pipeline_3):
    print place


        




