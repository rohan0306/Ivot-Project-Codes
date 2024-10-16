#>>>>>>>>> Actual Raw Builder Query used in studentscompletedbothtrainingprogram >>>>>>>>

[
    {
        "$match": {
            "status": "Completed"
        }
    },
    {
        "$group": {
            "_id": "$user_email",  
            "completedPrograms": { "$addToSet": "$training_program_name" } 
        }
    },
    {
        "$match": {
            "completedPrograms": {
                "$size": 2  
            }
        }
    },
    {
        "$count": "studentsCompletedBoth"  
    }
]


