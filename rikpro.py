quizzes=$$quiz_response
trainings=$$program_response

# Combine Data by user_email
combined_data = dict()

# Process quiz information
for quiz in quizzes:
    email = quiz['user_email']
    if email not in combined_data:
        combined_data[email] = dict(
            **{"User Email": email},
            **{"User Name": quiz['user_name']},
            **{"Onboarding Quiz": "❎"},
            **{"Completion Quiz": "❎"}
        )
    
    # Set quiz completion flags
    if quiz['quiz_type'] == 'Onboarding Quiz':
        combined_data[email]['Onboarding_Quiz'] = "✅"
    elif quiz['quiz_type'] == 'Completion Quiz':
        combined_data[email]['Completion_Quiz'] = "✅"

# Process training information
for training in trainings:
    email = training['user_email']
    training_program = training['training_program_name']
    
    # Initialize user's entry if not present
    if email not in combined_data:
        combined_data[email] = dict(
            **{"User Email": email},
            **{"User Name": ''},
            **{"Onboarding Quiz": "❎"},
            **{"Completion Quiz": "❎"}
        )
    
    # Set training program status based on completion
    if training['status'] == 'Completed':
        combined_data[email][training_program] = "✅"
    else:
        combined_data[email][training_program] = "❎"

# Collect all unique training program names
all_training_programs = set()
for training in trainings:
    all_training_programs.add(training['training_program_name'])

# Fill missing training programs with "No"
for email, record in combined_data.items():
    for program in all_training_programs:
        if program not in record:
            record[program] = "❎"

# Convert the combined data into a list
result = list(combined_data.values())
%%final_output%% = result