#>>>>>>>Original code used in Dynamic logic "Result Monitoring">>>>>>>>>>

input= $$result_response
final_output = dict()

if len(input) > 0:
    total = input[0]["correct_count"]+input[0]["incorrect_count"]
    final_output["Student Name"] = input[0]["student_name"]
    final_output["Quiz Name"] = input[0]["quiz_name"]
    final_output["Quiz Taken"] = "✔️"
    final_output["Score"] = str(input[0]["correct_count"]) + "/" + str(total)
    final_output["Percent %"] = str(input[0]["score"]) + "%"

%%final_output%%= [final_output]


#>>>>Code with comment to understand>>>>>>>
# result = [
#   {
#     "student_email": "rohan.ghume@datamoulds.com",
#     "student_name": "Rohan Ghume",
#     "quiz_name": "PRE-TRAINING TEST",
#     "correct_count": 3,
#     "incorrect_count": 0,
#     "score": 100
#   }
# ]

# final_output = dict()                            #empty dictionary is created named "final_output"
# if len(result) > 0:
#     total = result[0]["correct_count"] + result[0]["incorrect_count"]   #Calculating
#     final_output["Student Email"] = result[0]["student_email"]          #"student_email" is directly fetched from "result" 
#     final_output["Student Name"] = result[0]["student_name"]           #"student_name" is directly fetched from "result"
#     final_output["Quiz Name"] = result[0]["quiz_name"]                 #"quiz_name" is directly fetched from "result"
#     final_output["Quiz Taken"] = "✔️"                                 #it is directly marked
#     final_output["Score"] = str(result[0]["correct_count"]) + "/" + str(total)  #format used to display score
#     final_output["Percent"] = str(result[0]["score"]) + "%"            #it is directly fetched from result and percentage sign is marked

# print(final_output)









# >>>>>>>>>>>>>>Raw Builder Query Rohan>>>>>>>>>>>>>>>>>>>>
# [
#     {
#         "$sort": {
#             "created_at": -1
#         }
#     },
#     {
#         "$group": {
#             "_id": "$student_email",
#             "student_name": { "$first": "$student_name" },
#             "correct_count": { "$first": "$correct_count" },
#             "incorrect_count": { "$first": "$incorrect_count" },
#             "score": { "$first": "$score" },
#             "quiz_id": { "$first": "$quiz_id" },
#             "quiz_name": { "$first": "$quiz_name" }
#         }
#     },
#     {
#         "$project": {
#             "_id": 0,
#             "student_email": "$_id",
#             "student_name": 1,
#             "correct_count": 1,
#             "incorrect_count": 1,
#             "score": 1,
#             "quiz_id": 1,
#             "quiz_name": 1
#         }
#     }
# ]

# >>>>>>>>>>>>>>>>Raw Builder Query Rikhil Sir>>>>>>>>>>>>>>>>>>
# [
#   {
#     "$match":
#       {
#         "quiz_name": %quiz_name%,
#         "training_id": %training_id%,
#       },
#   },
#   {
#     "$sort":
#       {
#         "created_date_label": -1,
#       },
#   },
  
# ]


