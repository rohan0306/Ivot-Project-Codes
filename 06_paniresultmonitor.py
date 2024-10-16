input = [
  {
    "student_email": "rohan.ghume@datamoulds.com",
    "student_name": "Rohan Ghume",
    "quiz_name": "PRE-TRAINING TEST",
    "correct_count": 3,
    "incorrect_count": 0,
    "score": 100
  }
]
final_output = dict()

if len(input) > 0:
    total = input[0]["correct_count"]+input[0]["incorrect_count"]
    final_output["Student Name"] = input[0]["student_name"]
    final_output["Quiz Name"] = input[0]["quiz_name"]
    final_output["Quiz Taken"] = "✔️"
    final_output["Score"] = str(input[0]["correct_count"]) + "/" + str(total)
    final_output["Percent %"] = str(input[0]["score"]) + "%"

print(final_output)



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






# key_value_output = ""

# for quiz in result_response:
#     if isinstance(quiz, dict) and "training_id" in quiz and "quiz_name" in quiz and "student_email" in quiz and "student_name" in quiz and "score" in quiz and "correct_count" in quiz and "incorrect_count" in quiz:
        
#         training_id = quiz.get("training_id")
#         quiz_name = quiz.get("quiz_name")
#         student_email = quiz.get("student_email")
#         student_name = quiz.get("student_name")
#         score = quiz.get("score")
#         correct_count = quiz.get("correct_count")
#         incorrect_count = quiz.get("incorrect_count")
#         total_attempt = correct_count + incorrect_count
#         total_score = str(correct_count) + "/" + str(total_attempt) if total_attempt > 0 else str(correct_count) + "/0"  

#         marked = "✅" if student_email in [r.get("student_email") for r in result_response] else "❎"

        
#         key_value_output += "Student Name: " + str(student_name) + "\n"
#         key_value_output += "Marked: " + marked + "\n"
#         key_value_output += "Score: " + str(score) + "\n"
#         key_value_output += "Total Score: " + total_score + "\n"
#         key_value_output += "-" * 40 + "\n"  
        
# # Print or return the formatted key-value pairs
# final_output = key_value_output
# print(final_output)
