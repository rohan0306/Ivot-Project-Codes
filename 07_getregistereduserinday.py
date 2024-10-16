#>>>>>>>>Actual Code used in Dynamic Logic of Get registered user in a single day>>>

import time
import json

# Convert time to milliseconds
current_time_millis = int(time.time() * 1000)
one_day_millis = 24 * 60 * 60 * 1000  # Milliseconds in one day

# Time ranges
one_day_ago_millis = current_time_millis - one_day_millis

query=[]

condition=dict({})
condition["$match"]=dict({})
condition["$match"]["created_date_millis"]=dict({})
condition["$match"]["created_date_millis"]["$gte"]=one_day_ago_millis
condition["$match"]["created_date_millis"]["$lte"]=current_time_millis
query.append(condition)

count_condition=dict({})
count_condition["$count"]="one_day_ago_count"
query.append(count_condition)

print(query)
%%query%%=json.dumps(query)



# import time
# import json

# #convert time to milliseconds
# current_time_millis = int(time.time() * 1000)
# one_day_millis = 24 * 60 * 60 * 1000

# one_day_ago_millis = current_time_millis - one_day_millis

# query = []

# condition = dict({})
# condition["$match"] = dict({})
# condition["$match"]["created_date_millis"] = dict({})
# condition["$match"]["created_date_millis"]["$gte"] = one_day_ago_millis
# condition["$match"]["created_date_millis"]["lte"] = current_time_millis
# query.append(condition)

# count_condition = dict({})
# count_condition["$count"] = "one_day_ago_count"
# query.append(count_condition)

# %%query%% = json.dumps(query)

