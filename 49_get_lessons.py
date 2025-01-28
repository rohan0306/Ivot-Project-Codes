import json
import re

#filter_request = cache["filter_request"]

if isinstance(cache["filter_request"], str):
    filter_request = json.loads(cache["filter_request"])  # Parse the string into a dictionary
else:
    filter_request = cache["filter_request"]  # Use it directly as it's already a dictionary

lesson_header = None
lesson_type = None
status = None
published = None

# Correctly check for keys in filter_request
if "lesson_header" in filter_request:
    lesson_header = filter_request["lesson_header"]

if "lesson_type" in filter_request:
    lesson_type = filter_request["lesson_type"]
	
if "status" in filter_request:
    status = filter_request["status"]
	
if "published" in filter_request:
    published = filter_request["published"]

query = []

# Add filter for toolkit
if lesson_header is not None and len(lesson_header) > 0:
    escaped_lesson_header = re.escape(lesson_header)
    condition = dict({})
    condition["$match"] = dict({})
    condition["$match"]["lesson_header"] = {
        "$regex": escaped_lesson_header,  
        "$options": "i"  
    }
    query.append(condition)
	
# Add filter for toolkit
if lesson_type is not None and len(lesson_type) > 0:
    condition = dict({})
    condition["$match"] = dict({})
    condition["$match"]["lesson_type"] = dict({})
    condition["$match"]["lesson_type"]= lesson_type
    query.append(condition)
	
# Add filter for toolkit
if status is not None and len(status) > 0:
    condition = dict({})
    condition["$match"] = dict({})
    condition["$match"]["status"] = dict({})
    condition["$match"]["status"]= status
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

