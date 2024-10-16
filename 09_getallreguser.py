#>>>>> Actual Raw Query Builder used in getallreguser >>>>>>>>>
[
    {
        "$group": {
            "_id": "$email",
            "count": { "$sum": 1 }
        }
    },
    {
        "$count": "totalRegUsers"
    }
]