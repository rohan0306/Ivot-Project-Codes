import json
import datetime

filter_request=$$quiz_filter_request

quiz=None
student_email=None
start_date=None
end_date=None

if "quiz" in filter_request:
	quiz=filter_request["quiz"]
if "student_email" in filter_request:
	student_email=filter_request["student_email"]
if "from_date" in filter_request:
	start_obj=filter_request["from_date"] +" 00:00:00"
	start_date_obj=datetime.datetime.strptime(start_obj,"%Y-%m-%d %H:%M:%S")
	start_date=start_date_obj.timestamp() * 1000
if "to_date" in filter_request:
	end_obj=filter_request["to_date"] +" 23:59:59"
	end_date_obj=datetime.datetime.strptime(end_obj,"%Y-%m-%d %H:%M:%S")
	end_date=end_date_obj.timestamp() * 1000

query=[]

if start_date is not None:
	condition=dict({})
	condition["$match"]=dict({})
	condition["$match"]["created_date_millis"]=dict({})
	condition["$match"]["created_date_millis"]["$gte"]=start_date
	query.append(condition)

if end_date is not None:
	condition=dict({})
	condition["$match"]=dict({})
	condition["$match"]["created_date_millis"]=dict({})
	condition["$match"]["created_date_millis"]["$lte"]=end_date
	query.append(condition)

if quiz is not None and len(quiz)>0:
	condition=dict({})
	condition["$match"]=dict({})
	condition["$match"]["quiz_id"]=dict({})
	condition["$match"]["quiz_id"]=quiz[0]
	query.append(condition)
	
if student_email is not None:
	condition=dict({})
	condition["$match"]=dict({})
	condition["$match"]["student_email"]=dict({})
	condition["$match"]["student_email"]=student_email
	query.append(condition)

%%query%%=json.dumps(query)


