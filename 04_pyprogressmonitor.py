#>>>>>>>>>>>>>Actual Code of Progress Monitoring in python>>>>>>>>>>>>>

quizzes = [
  {
    "quiz_type": "Onboarding Quiz",
    "user_email": "rohan.ghume@datamoulds.com",
    "user_name": "Rohan Ghume"
  },
  {
    "quiz_type": "Completion Quiz",
    "user_email": "rohanghume351@gmail.com",
    "user_name": "Rohan Ghume"
  },
  {
    "quiz_type": "Onboarding Quiz",
    "user_email": "rohanghume351@gmail.com",
    "user_name": "Rohan Ghume"
  }
]
trainings = [
  {
    "status": "Completed",
    "training_program_name": "IVoT Personal Money System Program",
    "training_id": 1,
    "user_email": "rohan.ghume@datamoulds.com"
  },
  {
    "status": "Completed",
    "training_program_name": "IVoT Personal Money System Program 2",
    "training_id": 2,
    "user_email": "rohan.ghume@datamoulds.com"
  },
  {
    "status": "Pending",
    "training_program_name": "INTRODUCCIÓN A IVoT ACADEMY",
    "training_id": 3,
    "user_email": "rohan.ghume@datamoulds.com"
  }
]

combined_data = dict()

# Process quiz information
for quiz in quizzes:
    email = quiz['user_email']
    if email not in combined_data:
        combined_data[email] = dict()
        combined_data[email]["User Email"]=email
        combined_data[email]["User Name"]=quiz['user_name']
        combined_data[email]["Onboarding Quiz"]="❌"
        combined_data[email]["Completion Quiz"]="❌"
      
    # Set quiz completion flags
    if quiz['quiz_type'] == 'Onboarding Quiz':
        combined_data[email]['Onboarding Quiz'] = "✔️"
    elif quiz['quiz_type'] == 'Completion Quiz':
        combined_data[email]['Completion Quiz'] = "✔️"

# Process training information
for training in trainings:
    email = training['user_email']
    training_program = training['training_program_name']
    
    # Initialize user's entry if not present
    if email not in combined_data:
        combined_data[email] = dict()
        combined_data[email]["User Email"]=email
        combined_data[email]["User Name"]=""
        combined_data[email]["Onboarding Quiz"]="❌"
        combined_data[email]["Completion Quiz"]="❌"
    
    # Set training program status based on completion
    if training['status'] == 'Completed':
        combined_data[email][training_program] = "✔️"
    else:
        combined_data[email][training_program] = "❌"

# Collect all unique training program names
all_training_programs = set()
for training in trainings:
    all_training_programs.add(training['training_program_name'])

# Fill missing training programs with "No"
for email, record in combined_data.items():
    for program in all_training_programs:
        if program not in record:
            record[program] = "❌"

# Convert the combined data into a list
result = list(combined_data.values())
print(result)


#>>>>>>Original Code with comment to understand>>>>>>>>>
# quizzes = [
#   {
#     "quiz_type": "Onboarding Quiz",
#     "user_email": "rohan.ghume@datamoulds.com",
#     "user_name": "Rohan Ghume"
#   },
#   {
#     "quiz_type": "Completion Quiz",
#     "user_email": "rohanghume351@gmail.com",
#     "user_name": "Rohan Ghume"
#   },
#   {
#     "quiz_type": "Onboarding Quiz",
#     "user_email": "rohanghume351@gmail.com",
#     "user_name": "Rohan Ghume"
#   }
# ]
# trainings = [
#   {
#     "status": "Completed",
#     "training_program_name": "IVoT Personal Money System Program",
#     "training_id": 1,
#     "user_email": "rohan.ghume@datamoulds.com"
#   },
#   {
#     "status": "Completed",
#     "training_program_name": "IVoT Personal Money System Program 2",
#     "training_id": 2,
#     "user_email": "rohan.ghume@datamoulds.com"
#   },
#   {
#     "status": "Pending",
#     "training_program_name": "INTRODUCCIÓN A IVoT ACADEMY",
#     "training_id": 3,
#     "user_email": "rohan.ghume@datamoulds.com"
#   }
# ]

# combined_data = dict()                     #created new dictionary to store all output

# for quiz in quizzes:                       # "quiz" is a new variable and "quizzes" is in which data is stored
#     email = quiz["user_email"]             #through this it will check whether user is in database or not
#     if email not in combined_data:         #if user is not in database then what to do
#         combined_data[email] = dict()      #it will check user with email in dictionary
#         combined_data[email]["User Email"] = email        #column of table with new created key 
#         combined_data[email]["User Name"] = quiz["user_name"]  #column of table with variable "quiz" and "user_name" which is already in database
#         combined_data[email]["Onboarding Quiz"]= "❌"           #marked it as wrong   
#         combined_data[email]["Completion Quiz"] = "❌"          #marked it as wrong
    
#     if quiz["quiz_type"] == "Onboarding Quiz":              # "quiz" is a variable and "quiz_type" is a field in a database
#         combined_data[email]["Onboarding Quiz"] = "✔️"     #here "Onboarding quiz" is hardcoded because it will never change
#     if quiz["quiz_type"] == "Completion Quiz":              # "quiz" is a variable and "quiz_type" is a field in a database
#         combined_data[email]["Completion Quiz"] = "✔️"      #here "Completion quiz" is hardcoded because it will never change

# for training in trainings:                   # "training" is a new variable and "trainings" is in which data is stored 
#     email = training["user_email"]           # "email" is a new variable and "user_email" is a  feild in a database and 
#     training_program = training["training_program_name"]      #"training_program" is a new variable and "training_program_name" is a field stored in database
#     if email not in combined_data:           # if user is not in database then what to do
#         combined_data[email] = dict()        #it will check user with email in dict()
#         combined_data[email]["User Email"] = email        #column of table with new created (key)variable
#         combined_data[email]["User Name"] = ""            #from above logic we are getting user name so here no need thats why empty string is passsed
#         combined_data[email]["Onboarding Quiz"] = "❌"
#         combined_data[email]["Completion Quiz"] = "❌"
    
#     if training["status"] == "Completed":                 #in a databse there is a field named "status" where we know it is "completed" or "pending"
#         combined_data[email][training_program] = "✔️"     #here we can't hardcode "training_program_name"  
#     else:                                                 #so that's why we have decalred "training_program"
#         combined_data[email][training_program] = "❌"    #as a variable above so that we directly fetched program name from database


# all_training_programs = set()                       #set is created beacause sometimes user email is not in database so in field it doesn't crossed marked it
# for training in trainings:                          # so this will help us to collect all training program names from database
#     all_training_programs.add(training["training_program_name"])        #it adds all training_program_name" in a set call "all_training_programs" 


# for email, record in combined_data.items():      #it checks user_email in a combined_data dictionary
#     for program in all_training_programs:       #"program" is a new variable in "all_training_programs"
#         if program not in record:               #it checks if "program" is in "record" of combined_data
#             record[program] = "❌"             #if program is not in record then it is set to be marked as "❌" 

# result = list(combined_data.values())
# print(result)



































#>>>>>>>>>>>>Below Code is, in which training_id is directly fetched from training_program no hardcoded>>>>>>>>

# # Debug: Print the content of quiz_response and program_response
# print("quiz_response:", quiz_response)
# print("program_response:", program_response)

# final_status = dict()

# # Ensure quiz_response is not None and is iterable
# if quiz_response:
#     for quiz in quiz_response:
#         print("Processing quiz:", quiz)  # Debug: Show the current quiz being processed
#         if isinstance(quiz, dict) and "user_email" in quiz and "quiz_type" in quiz:
#             user_email = quiz.get("user_email")
#             user_name = quiz.get("user_name", "Unknown")  # Fetch user_name if present, else 'Unknown'

#             if not final_status.get(user_email):
#                 final_status[user_email] = dict(
#                     name=user_name,  # Add the user name to final_status
#                     Onboarding_Quiz="❎",
#                     Completion_Quiz="❎",
#                 )

#             # Mark the quiz completion status
#             if quiz.get("quiz_type") == "Onboarding Quiz":
#                 final_status[user_email]["Onboarding_Quiz"] = "✅"
#             elif quiz.get("quiz_type") == "Completion Quiz":
#                 final_status[user_email]["Completion_Quiz"] = "✅"

# # Ensure program_response is not None and is iterable
# if program_response:
#     for program in program_response:
#         print("Processing program:", program)  # Debug: Show the current program being processed
#         if isinstance(program, dict) and "user_email" in program and "training_id" in program and "status" in program and "percent_completion" in program:
#             user_email = program.get("user_email")
#             training_id = program.get("training_id")
#             status = program.get("status")
#             percent_completion = program.get("percent_completion")
#             student_name = program.get("student_info", dict()).get("first_name", "") + " " + program.get("student_info", dict()).get("last_name", "Unknown")

#             # If user_email is not in final_status, initialize it and add the student name from program
#             if not final_status.get(user_email):
#                 final_status[user_email] = dict(
#                     name=student_name,  # Add student name if present
#                     Onboarding_Quiz="❎",
#                     Completion_Quiz="❎"
#                 )

#             # Update the name if not already present or default value ('Unknown')
#             if final_status[user_email].get("name", "Unknown") == "Unknown":
#                 final_status[user_email]["name"] = student_name

#             # Initialize the specific training_id in final_status if it doesn't exist
#             if not final_status[user_email].get("Training_" + str(training_id)):
#                 final_status[user_email]["Training_" + str(training_id)] = "❎"

#             # Check the training_id and status and update the completion status dynamically
#             if status == "Completed" and percent_completion == 100:
#                 final_status[user_email]["Training_" + str(training_id)] = "✅"
#             else:
#                 final_status[user_email]["Training_" + str(training_id)] = str(percent_completion) + "%"

# # Fetch the training programs from the 'training_programs' database
# training_programs = $$training_programs  # Example: [{"training_id": 1, "training_name": "Training 1"}, ...]

# # Debug: Print the training programs fetched
# print("training_programs:", training_programs)

# # Ensure that all users have training data dynamically based on what's in the database
# for user_email, user_data in final_status.items():
#     # Loop through the training programs from the database
#     for program in training_programs:
#         training_id = program.get("training_id")
#         if not user_data.get("Training_" + str(training_id)):
#             user_data["Training_" + str(training_id)] = "❎"  # Mark as not completed if missing

# # Debug: Print the final result
# print("final_status:", final_status)

# final_output = final_status








