#>>>>>> Actual dynamic Logic used in tgetstudentscomptrainpro1 >>>>>>>>>>>
# Just change default value of "training_program_name" in "request" flow variable
[
    {
        "$match": {
            "training_program_name": %training_program_name%, 
            "status": "Completed"  
        }
    },
    {
        "$project": {
            "_id": 0,
            "status": 1,
            "training_program_name": 1,
            "training_id": 1,
            "user_email": 1,
            "start_time": 1,
            "end_time": 1,
            "completion_time": 1,
            "percent_completion": 1,
            "campaign": 1,
        }
    }
]
