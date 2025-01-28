import json
import re

#filter_request = cache["question_filter_request"]

if isinstance(cache["question_filter_request"], str):
    filter_request = json.loads(cache["question_filter_request"])  # Parse the string into a dictionary
else:
    filter_request = cache["question_filter_request"]  # Use it directly as it's already a dictionary

question  = None
status = None
published = None

# Correctly check for keys in filter_request
if "question" in filter_request:
    question  = filter_request["question"]

if "status" in filter_request:
    status = filter_request["status"]
	
if "published" in filter_request:
    published = filter_request["published"]

query = []

# Add filter for toolkit
if question is not None and len(question) > 0:
    escaped_question = re.escape(question)
    condition = dict({})
    condition["$match"] = dict({})
    condition["$match"]["question"] = {
        "$regex": escaped_question,  
        "$options": "i"  
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
