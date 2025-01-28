import json
import re

#filter_request = cache["filter_request"]

if isinstance(cache["filter_request"], str):
    filter_request = json.loads(cache["filter_request"])  # Parse the string into a dictionary
else:
    filter_request = cache["filter_request"]  # Use it directly as it's already a dictionary

program_header = None
status = None
published = None

# Correctly check for keys in filter_request
if "program_header" in filter_request:
    program_header = filter_request["program_header"]
	
if "status" in filter_request:
    status = filter_request["status"]
	
if "published" in filter_request:
    published = filter_request["published"]

query = []

# Add filter for toolkit
if program_header is not None and len(program_header) > 0:
    escaped_program_header = re.escape(program_header)
    condition = dict({})
    condition["$match"] = dict({})
    condition["$match"]["program_header"] = {
        "$regex": escaped_program_header,  # Remove anchors
        "$options": "i"  # Case-insensitive search
    }
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
