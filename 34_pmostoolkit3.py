import math
invested_spent_value = float($$request["invested_spent_value"]) 
years_value = int($$request["years_value"]) 
daily_cost_value = float($$request["daily_cost_value"])        
interest_rate_value = float($$request["interest_rate_value"]) / 100           

afuture_value = invested_spent_value * ((1 + interest_rate_value) **years_value )
future_value = math.floor(afuture_value)
monthly_cost_value = daily_cost_value * 30
annual_cost_value = monthly_cost_value * 12

final_output = dict()
final_output["future_value"] = future_value
final_output["monthly_cost_value"] = monthly_cost_value
final_output["annual_cost_value"] = annual_cost_value

final_output["interest_rate_value"] = $$request["interest_rate_value"]

%%response%% = final_output
