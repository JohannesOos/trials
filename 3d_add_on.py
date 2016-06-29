
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")



# define database
db=connection.geo_trial

#drop existing collection
db.trial_one.drop()

#use the set up trial database
geo = db.trial_one

#insert 1000 3d coordinates with 0-10 all combos
for a in range(10):
    for b in range(10):
        for c in range(10):
#            geo.insert_one({"loc" : { "lng" : a , "lat" : b }, "height": c })
        # better to be don ewith list
            geo.insert_one({"loc" : [a,b], "height": c})

#create 2d index   (sphere if earth surface / 2d if plane)    
geo.create_index( [( "loc", "2d" ) ])

# create pipeline for aggregation
pipeline_1 = [{"$match": {"loc": {"$within": {"$box": [[3, 3], [5, 5]]}}}}]
pipeline_2 = [{"$match": {"height": { "$lte": 5}}}]
pipeline_3 = [{"$match": {"height": { "$gte": 4}}}]

#query for 2d results
for place in geo.aggregate(pipeline_1):
    print place
    
print "2d query done"
    
#query for 3d results
for place in geo.aggregate(pipeline_1 + pipeline_2+ pipeline_3):
    print place
    
print "3d query done"
    
def rec_3d_pipe(a,b,c, name_2d = "loc", name_height = "height"):
    """
    input: 
    3 points of form ([[a1,a2,a3], [b1,b2,b3], [c1,c2,c3]])
    to create cuboid --> shaoe to be inspected
    name of sphere document and height document
    database must have coordinates of form ({"loc" : [a,b], "height": c})
    return: a translated aggregation pipeline
    """
    #input validation
    if len(a) != 3 or len(b) !=3 or len(c) != 3:
        return "not 3d coordinates"
        
    if a[2] != b [2]:
        return "a and b not in same plane - check needed"
        
    
        
    

    



search = [[2,2,2], [3,3,2],[2,2,4]]
print rec_3d_pipe(search[0],search[1],search[2])

        




