import json

#filter_request = cache["filter_request"]

if type(cache["filter_request"]) == str:
    filter_request = json.loads(cache["filter_request"])  # Parse the string into a dictionary
else:
    filter_request = cache["filter_request"]  # Use it directly as it's already a dictionary

media_name = None
folder = None

# Correctly check for keys in filter_request
if "media_name" in filter_request:
    media_name = filter_request["media_name"]

if "folder" in filter_request:
    folder = filter_request["folder"]


query = []

# Add filter for media_name and description combined
if (media_name is not None and len(media_name) > 0):
    condition = dict({})
    condition["$match"] = dict({})
    condition["$match"]["$or"] = [{"media_name": 
	{
	"$regex": media_name,
	"$options": "i"
	}},
	{"description": {
	"$regex": media_name,
	"$options": "i"
	}}]
    
    query.append(condition)

# Add filter for folder
if folder is not None and len(folder) > 0:
    condition = dict({})
    condition["$match"] = dict({})
    condition["$match"]["folder"] = dict({})
    condition["$match"]["folder"]["$in"] = folder
    query.append(condition)

cache["query"] = json.dumps(query)