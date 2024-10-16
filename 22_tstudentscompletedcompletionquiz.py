#>>>> Actual Raw Builder Query used tgetstudentscompletedcompletionquiz >>>>>>

[
    {
        "$match": {
            "quiz_type": "Completion Quiz"
        }
    },
    {
        "$project": {
            "_id": 0,
            "quiz_id": 1,
            "quiz_name": 1,
            "quiz_type": 1,
            "quiz_completion_time": 1,
            "user_name": 1,
            "user_email": 1,
            "start_time": 1,
            "end_time": 1,
            "language": 1,
            "campaign": 1,
        }
    }
]
