#>>>>>>Code using max functions in which all training programs is showing>>>>>

quiz_response = [
  {
    "_id": {
      "$oid": "6704ed01bafd26856df7b5d5"
    },
    "quiz_type": "Onboarding Quiz",
    "user_email": "rohan.ghume@datamoulds.com",
    "user_name": "Rohan Ghume"
  },
  {
    "_id": {
      "$oid": "6704ed01bafd26856df7b5db"
    },
    "quiz_type": "Onboarding Quiz",
    "user_email": "rohan.ghume@datamoulds.com",
    "user_name": "Rohan Ghume"
  },
  {
    "_id": {
      "$oid": "6704ed01bafd26856df7b5e1"
    },
    "quiz_type": "Onboarding Quiz",
    "user_email": "rohan.ghume351@datamoulds.com",
    "user_name": "Rohan Ghume"
  },
]
program_response = [
  {
    "_id": {
      "$oid": "670130897f5530943f32d803"
    },
    "status": "Completed",
    "training_id": 1,
    "user_email": "rohan.ghume@datamoulds.com",
    "percent_completion": 100,
    "student_info": {
      "first_name": "Rohan",
      "last_name": "Ghume"
    }
  },
  {
    "_id": {
      "$oid": "6703b7048d815a1e22bd1451"
    },
    "status": "Completed",
    "training_id": 2,
    "user_email": "rohan.ghume@datamoulds.com",
    "percent_completion": 100,
    "student_info": {
      "first_name": "Rohan",
      "last_name": "Ghume"
    }
  }
]

final_status = {}

# Process quiz responses
for quiz in quiz_response:
    if isinstance(quiz, dict) and "user_email" in quiz and "quiz_type" in quiz:
        user_email = quiz["user_email"]
        
        # Initialize final_status for the user if not already done
        if user_email not in final_status:
            final_status[user_email] = {
                "Onboarding Quiz": "❎",
                "Completion Quiz": "❎"
            }

            # Initialize all the training programs with ❎
            max_training_programs = 2
            for i in range(1, max_training_programs + 1):
                final_status[user_email][f"Training {i}"] = "❎"
        
        # Update quiz status based on quiz_type
        if quiz["quiz_type"] == "Onboarding Quiz":
            final_status[user_email]["Onboarding Quiz"] = "✅"
        elif quiz["quiz_type"] == "Completion Quiz":
            final_status[user_email]["Completion Quiz"] = "✅"

# Process program responses
for program in program_response:
    if isinstance(program, dict) and "user_email" in program and "training_id" in program and "status" in program and "percent_completion" in program:
        user_email = program["user_email"]
        training_id = program["training_id"]
        status = program["status"]
        percent_completion = program["percent_completion"]

        # Ensure the user is initialized in final_status
        if user_email not in final_status:
            final_status[user_email] = {
                "Onboarding Quiz": "❎",
                "Completion Quiz": "❎"
            }
            # Initialize all the training programs with ❎
            max_training_programs = 4
            for i in range(1, max_training_programs + 1):
                final_status[user_email][f"Training {i}"] = "❎"

        # Update training status based on completion
        if status == "Completed" and percent_completion == 100:
            final_status[user_email][f"Training {training_id}"] = "✅"
        else:
            final_status[user_email][f"Training {training_id}"] = f"{percent_completion}%"

# Output the final status
print(final_status)