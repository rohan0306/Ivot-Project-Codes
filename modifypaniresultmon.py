result_response = [
  {
    "_id": {
      "$oid": "6708622950fa2e616ef1a170"
    },
    "student_email": "rohan.ghume@datamoulds.com",
    "student_id": 1,
    "student_name": "Rohan Ghume",
    "quiz_id": 2,
    "quiz_name": "PRE-TRAINING TEST",
    "start_time": "2024-09-02T01:15:33.246660",
    "end_time": "2024-09-02T01:20:12.574343",
    "answers": [
      {
        "question": "<p>When did humans first start using coin based money?</p>",
        "expected_answers": [
          "3,000 years ago"
        ],
        "actual_answers": [
          "3,000 years ago"
        ],
        "is_correct": "Yes"
      },
      {
        "question": "<p><span style=\"color: rgb(0, 0, 0); background-color: transparent;\">Mack’s Coffee Shop is solely owned by Mack. Mack is considering selling his shop. You are considering buying the shop. Mack is selling the shop for $100 per share and there are 10,000 shares outstanding.</span></p><p><span style=\"color: rgb(0, 0, 0); background-color: transparent;\">﻿If you buy a share in Mack’s shop, what do you own? (choose as many as you want)</span></p>",
        "expected_answers": [
          "A right to your share of the company’s profits",
          "A right to take your share of profits whenever you want"
        ],
        "actual_answers": [
          "A right to your share of the company’s profits",
          "A right to take your share of profits whenever you want"
        ],
        "is_correct": "Yes"
      },
      {
        "question": "<p>How does a government control the supply of its currency?</p>",
        "expected_answers": [
          "Both",
          "By issuing more of its currency",
          "By removing currency from the system?"
        ],
        "actual_answers": [
          "Both",
          "By issuing more of its currency",
          "By removing currency from the system?"
        ],
        "is_correct": "Yes"
      }
    ],
    "correct_count": 3,
    "incorrect_count": 0,
    "score": 100,
    "percent": "1.0",
    "completion_time": 4.66,
    "status": "PASSED",
    "user_id": 27217,
    "srno": 50,
    "training_id": 1,
    "created_by": 27217,
    "created_date": "2024-10-10T23:24:25.902900",
    "created_date_label": "2024-10-10 23:24:25",
    "created_date_millis": 1728602665902.9
  }
]

final_result = {}

for quiz in result_response:
    if isinstance(quiz, dict) and "training_id" in quiz and "quiz_name" in quiz and "student_email" in quiz and "student_name" in quiz and "score" in quiz and "correct_count" in quiz and "incorrect_count" in quiz:
        
        training_id = quiz["training_id"]
        quiz_name = quiz["quiz_name"]
        student_email = quiz["student_email"]
        student_name = quiz["student_name"]
        score = quiz["score"]
        correct_count = quiz["correct_count"]
        incorrect_count = quiz["incorrect_count"]
        total_attempt = correct_count + incorrect_count
        total_score = f"{correct_count}/{total_attempt}" if total_attempt > 0 else f"{correct_count}/0"  # Handling zero attempts

        if training_id not in final_result:
            final_result[training_id] = {
                "quiz_name": quiz_name,
                "students": []
            }

        final_result[training_id]["students"].append({
            "student_name": student_name,
            "student_email": student_email,
            "score": score,
            "marked": "✅" if student_email in [r["student_email"] for r in result_response] else "❎",
            "total_score": total_score  # Store formatted score
        })

final_output = final_result

print(final_result)
