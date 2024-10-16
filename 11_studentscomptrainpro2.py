#>>>>>>>>> Actual Raw Builder Query used in getstudentscompletedtrainingprogram2 >>>>>>>>
# Just change the default value in "request" flow variable

[
    {
        "$match": {
            "training_program_name": %training_program_name%,
            "status": "Completed"  
        }
    },
    {
        "$count": "totalCompletedStudents"   
    }
]


