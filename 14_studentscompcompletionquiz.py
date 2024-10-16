#>>>>>>>Actual Raw Builder Query used in Completion Quiz Count

[
    {
      "$match": {
            "quiz_type": "Completion Quiz"
       }
    },
    {
     "$count": "completion_count"
    }
]