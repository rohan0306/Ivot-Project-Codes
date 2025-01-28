import json
import re

#filter_request = cache["filter_request"]

if isinstance(cache["filter_request"], str):
    filter_request = json.loads(cache["filter_request"])  # Parse the string into a dictionary
else:
    filter_request = cache["filter_request"]  # Use it directly as it's already a dictionary

course_header = None
published = None

# Correctly check for keys in filter_request
if "course_header" in filter_request:
    course_header = filter_request["course_header"]
	
# Correctly check for keys in filter_request
if "published" in filter_request:
    published = filter_request["published"]

query = []

# Add filter for toolkit
if course_header is not None and len(course_header) > 0:
    escaped_course_header = re.escape(course_header)
    condition = dict({})
    condition["$match"] = dict({})
    condition["$match"]["course_header"] = {
        "$regex": escaped_course_header,  
        "$options": "i"  
    }
    query.append(condition)
	
# Add filter for toolkit
if published is not None and len(published) > 0:
    condition = dict({})
    condition["$match"] = dict({})
    condition["$match"]["published"] = dict({})
    condition["$match"]["published"]= published
    query.append(condition)
	
cache["query"]= json.dumps(query)
#%%query%% = json.dumps(query)
