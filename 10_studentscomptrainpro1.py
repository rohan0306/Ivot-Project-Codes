#Actual Raw Builder Query used to get studentscompleted trainingprogram1 >>>>>>>
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



