import json
import re

#filter_request = cache["quiz_filter_request"]

if isinstance(cache["quiz_filter_request"], str):
    filter_request = json.loads(cache["quiz_filter_request"])  # Parse the string into a dictionary
else:
    filter_request = cache["quiz_filter_request"]  # Use it directly as it's already a dictionary

quiz_name = None
published = None

# Correctly check for keys in filter_request
if "quiz_name" in filter_request:
    quiz_name = filter_request["quiz_name"]
	
# Correctly check for keys in filter_request
if "published" in filter_request:
    published = filter_request["published"]

query = []

# Add filter for toolkit
if quiz_name is not None and len(quiz_name) > 0:
    escaped_quiz_name = re.escape(quiz_name)
    condition = dict({})
    condition["$match"] = dict({})
    condition["$match"]["quiz_name"] = {
        "$regex": escaped_quiz_name,  
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

