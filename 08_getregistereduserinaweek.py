#Actual Dynamic Logic Used for getregistereduserinaweek >>>>>>>>>>>

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

count_condition=dict({})
count_condition["$count"]="one_week_ago_count"
query.append(count_condition)

%%query%%=json.dumps(query)