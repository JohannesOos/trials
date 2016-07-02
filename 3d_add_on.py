
"""
this is a trial file
purpose is to use mongodbs geospaial index
and at the same time extend it to 3d 
mongodb does nto support this,
so a pymongo script will simulate this
it is importnat to make sure that all 
computation is done on the server
and not on the machine the pythn script runs
"""

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
    #check if all 3d coordinates
    if len(a) != 3 or len(b) !=3 or len(c) != 3:
        return "not 3d coordinates"
      
    #check if a and b in same z coordinate
    if a[2] != b [2]:
        return "a and b not in same plane - check needed"
        
    #create pymongoe in box statement
    corner1 = [a[0], a[1]]
    corner2 = [b[0], b[1]]
    pipe_rectangle = [{"$match": {name_2d: {"$within": {"$box": [corner1, corner2]}}}}]
    
    
    # check if c is under or over a-b plane and adjust bounds accordingly
    #define low ang height points
    low = c[2]
    high = a[2]
    #if it is the other way around then swap high and low
    if a[2]< low:
        low = a[2]
        high = c[2]
        
    # create lower boundary
    lower = [{"$match": {name_height: { "$gte": low}}}]
    
    # create upper boundary
    upper = [{"$match": {name_height: { "$lte": high}}}]
    
    #create pymongo height check pipeline
    pipe_height = lower + upper
    
    #create pymongo complete check
    pipeline = pipe_rectangle + pipe_height
    
    return pipeline
    

#adjsut function later
def insert_3d(position, name_2d = "loc", name_height = "height"):
    """
    input a 3d position of form list [a,b,c]
    returns a document for insert statement
    """
    
    #check if 3d coord
    if len(position) != 3:
        return "not 3d coordinates"
    
    #create document
    doc = {name_2d : [position[0],position[1]], name_height: position[2]}
    
    return doc
           
    


################################
#create some tests

################################

#define if test shoudl be done
test = True

#if we want to test the tests shoudl be run
if test:

    #create the three points which make the cuboid
    search = [[2,2,2.5], [3,3,2.5],[2,2,4]]
    #create pipeline through defined functions
    pipe =  rec_3d_pipe(search[0],search[1],search[2])
    
    print pipe
    
    #run aggregation pipeline    
    for place in geo.aggregate(pipe):
        print place
        
    #insert test     
    geo.insert_one(insert_3d([11,11,11]))
        




