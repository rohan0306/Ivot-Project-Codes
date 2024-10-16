#>>>>>>>>>>Actual Dynamic Logic used in Table Get registered user in a single day>>>>>>>>>
import time
import json


current_time_millis = int(time.time() * 1000)
one_day_millis = 24 * 60 * 60 * 1000  
one_day_ago_millis = current_time_millis - one_day_millis


query = [
    {
        "$match": {
            "created_date_millis": {
                "$gte": one_day_ago_millis,  
                "$lte": current_time_millis  
            }
        }
    },
    {
        "$project": {
            "_id": 0,                
            "first_name": 1,
    "last_name": 1,
    "email": 1,       
    "language": 1,
    "contact_no": 1,   
    "status": 1,         
    "university": 1,
    "address": 1,
    "dob": 1,
    "city": 1, 
    "country": 1,
        }
    }
]

query_string = json.dumps(query)

%%query%% = query_string



