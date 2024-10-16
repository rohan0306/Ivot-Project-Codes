#>>>>>>>>Actual Code used in tgetregistereduserinaweek >>>>>>>>>>>>>>>
import time
import json

# Convert time to milliseconds
current_time_millis = int(time.time() * 1000)
one_day_millis = 24 * 60 * 60 * 1000  # Milliseconds in one day
one_week_millis = 7 * one_day_millis  # Milliseconds in one week

# Time ranges
one_week_ago_millis = current_time_millis - one_week_millis

query=[]

condition=dict({})
condition["$match"]=dict({})
condition["$match"]["created_date_millis"]=dict({})
condition["$match"]["created_date_millis"]["$gte"]=one_week_ago_millis
condition["$match"]["created_date_millis"]["$lte"]=current_time_millis
query.append(condition)

project_condition=dict(({}))
project_condition["$project"] = ({
    "_id" : 0,
    "first_name" : 1,
    "last_name" : 1,
    "email" : 1,
    "language" : 1,
    "contact_no" : 1,
    "status" : 1,
    "university" : 1,
    "address": 1,
    "dob" : 1,
    "city" : 1,
    "country" : 1,    
})
query.append(project_condition)

%%query%%=json.dumps(query)

