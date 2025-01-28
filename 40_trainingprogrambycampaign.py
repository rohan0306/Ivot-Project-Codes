training_programs = cache["response"]
existing_student = cache["existing_student_object"]
active_subscription_ids=[]
if "subscriptions" in existing_student and (existing_student["subscriptions"] != "" or len(existing_student["subscriptions"]) > 0):
    for item in existing_student["subscriptions"]:
        if item["status"] == "Active":
            active_subscription_ids.append(item["product_id"])

subscribed=[]

for training_program in training_programs:
    if "product_ids" in training_program and len(training_program["product_ids"]) > 0:
        if "subscriptions" in existing_student and (existing_student["subscriptions"] != "" or len(existing_student["subscriptions"]) > 0):
            training_program["is_subscribed"]  = False
            for item in active_subscription_ids:
                if item in training_program["product_ids"]:
                    training_program["is_subscribed"]  = True
                    break                
        subscribed.append(training_program)    
    else:
        subscribed.append(training_program)

cache["training_programs"] = subscribed