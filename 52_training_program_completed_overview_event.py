#Get Training Program Name from Training ID---------------------
[
{
"$match":{
"srno":%training_id%
}
},
{
"$project":{
"_id":0,
"program_header":1
}
}
]

#Get Campaign From User Email----------------------------------
[
{
"$match":{
"email":%user_email%
}
},
{
"$project":{
"_id":0,
"campaign":1
}
}
]

#Mapp All The Fields
user_email = cache["user_email"]
training_id = cache["training_id"]
campaign = cache["student_detail"]
current_date = cache["current_date"]["datetime"]
training_program_name = cache["training_program_details"]

output = dict()
output["training_id"] = training_id
output["training_program_name"] = training_program_name[0]["program_header"]
output["campaign"] = campaign[0]["campaign"]
output["status"] = "Completed"
output["start_time"] = current_date
output["end_time"] = current_date
output["user_email"] = user_email
output["percent_completion"] = 100
output["event_type"] = "Training Program Completed"

cache["user_training_program_details"] = output