#>>>>>>>Actual Raw Builder Query used for Onboarding Quiz Count>>>>>>>>>>

[
    {
      "$match": {
            "quiz_type": "Onboarding Quiz"
       }
    },
    {
     "$count": "onboarding_count"
    }
]