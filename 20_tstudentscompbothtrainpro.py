#>>>>>>>>Actual Raw Builder Query used in tstudentscompletedbothtrainprogram >>>>>>>>

[
    {
        "$match": {
            "status": "Completed"
        }
    },
    {
        "$group": {
            "_id": "$user_email",
            "status": { "$first": "$status" }, 
            "training_program_name": { "$first": "$training_program_name" },
            "training_id": { "$first": "$training_id" },
            "user_email": { "$first": "$user_email" },
            "start_time": { "$first": "$start_time" },      
            "end_time": { "$first": "$end_time" },  
            "completion_time": { "$first": "$completion_time" },          
            "percent_completion": { "$first": "percent_completion" },
            "campaign": { "$first": "campaign" },              
            "completedPrograms": { "$addToSet": "$training_program_name" }
        }
    },
    {
        "$match": {
            "completedPrograms": { "$size": 2 }
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
            "completedPrograms": 1
        }
    }
]


