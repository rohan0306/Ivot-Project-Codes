import math
investment_commitment_input = float($$request["investment_commitment_input"]) / 100
total_income_value = int($$result[17]["field_value"])
debt_payment_dollars = int($$result[23]["field_value"])
fixed_expenses_total_fixed = int($$result[42]["field_value"])
variable_expenses_total_variable = int($$result[61]["field_value"])
pharmacy_dollars = int($$result[9]["field_value"])
income_two_dollars = int($$result[12]["field_value"])
income_three_dollars = int($$result[15]["field_value"])    
rent_value = int($$result[26]["field_value"])
utilities_value = int($$result[29]["field_value"])
phone_value = int($$result[32]["field_value"])
car_value = int($$result[35]["field_value"])
monthly_value = int($$result[38]["field_value"])  
fixed_expenses_rent = int($$result[27]["field_value"])
fixed_expenses_utilities = int($$result[30]["field_value"])
fixed_expenses_phone = int($$result[33]["field_value"])
fixed_expenses_car = int($$result[36]["field_value"])
fixed_expenses_monthly = int($$result[39]["field_value"])  
groceries_value = int($$result[45]["field_value"])
eating_value = int($$result[48]["field_value"])
travel_value = int($$result[51]["field_value"])
entertainment_value = int($$result[54]["field_value"])
health_value = int($$result[57]["field_value"])                   
variable_expenses_groceries = int($$result[46]["field_value"])
variable_expenses_eating = int($$result[49]["field_value"])
variable_expenses_travel = int($$result[52]["field_value"])
variable_expenses_entertainment = int($$result[55]["field_value"])
variable_expenses_health = int($$result[58]["field_value"]) 

final_total_income = pharmacy_dollars + income_two_dollars + income_three_dollars
investment_commitment_dollars = investment_commitment_input * total_income_value
variable_expenses_total_expenses = investment_commitment_dollars + debt_payment_dollars + fixed_expenses_total_fixed + variable_expenses_total_variable
atotal_expenses_value =  (variable_expenses_total_expenses / total_income_value) * 100
total_expenses_value = math.ceil(atotal_expenses_value)
variable_expenses_monthly_profit = total_income_value - variable_expenses_total_expenses
amonthly_profit_value = (variable_expenses_monthly_profit / total_income_value) * 100
monthly_profit_value = math.ceil(amonthly_profit_value)
final_total_fixed_expenses = rent_value + utilities_value + phone_value + car_value + monthly_value
final_total_fixed_expenses_value = fixed_expenses_rent  + fixed_expenses_utilities  + fixed_expenses_phone + fixed_expenses_car + fixed_expenses_monthly
final_total_variable_expenses = groceries_value + eating_value + travel_value + entertainment_value + health_value
final_total_variable_expenses_value = variable_expenses_groceries + variable_expenses_eating + variable_expenses_travel + variable_expenses_entertainment + variable_expenses_health

final_output = dict()
final_output["investment_commitment_dollars"] = investment_commitment_dollars
final_output["variable_expenses_total_expenses"] = variable_expenses_total_expenses
final_output["total_expenses_value"] = total_expenses_value
final_output["variable_expenses_monthly_profit"] = variable_expenses_monthly_profit
final_output["monthly_profit_value"] = monthly_profit_value
final_output["final_total_income"] = final_total_income
final_output["final_total_fixed_expenses"] = final_total_fixed_expenses
final_output["final_total_fixed_expenses_value"] = final_total_fixed_expenses_value
final_output["final_total_variable_expenses"] = final_total_variable_expenses
final_output["final_total_variable_expenses_value"] = final_total_variable_expenses_value

final_output["total_income_value"] = $$result[17]["field_value"]
final_output["debt_payment_dollars"] = $$result[23]["field_value"]
final_output["fixed_expenses_total_fixed"] = $$result[42]["field_value"]
final_output["variable_expenses_total_variable"] = $$result[61]["field_value"]

%%response%% = final_output















#Old Correct Code
import math
investment_commitment_input = float($$request["investment_commitment_input"]) / 100
total_income_value   = int($$request["total_income_value"])
debt_payment_dollars = int($$request["debt_payment_dollars"])
fixed_expenses_total_fixed = int($$request["fixed_expenses_total_fixed"])
variable_expenses_total_variable = int($$request["variable_expenses_total_variable"])
pharmacy_dollars = int($$request["pharmacy_dollars"])
income_two_dollars = int($$request["income_two_dollars"])
income_three_dollars = int($$request["income_three_dollars"])    
rent_value = int($$request["rent_value"])
utilities_value = int($$request["utilities_value"])
phone_value = int($$request["phone_value"])
car_value = int($$request["car_value"])
monthly_value = int($$request["monthly_value"])  
fixed_expenses_rent = int($$request["fixed_expenses_rent"])
fixed_expenses_utilities = int($$request["fixed_expenses_utilities"])
fixed_expenses_phone = int($$request["fixed_expenses_phone"])
fixed_expenses_car = int($$request["fixed_expenses_car"])
fixed_expenses_monthly = int($$request["fixed_expenses_monthly"])  
groceries_value = int($$request["groceries_value"])
eating_value = int($$request["eating_value"])
travel_value = int($$request["travel_value"])
entertainment_value = int($$request["entertainment_value"])
health_value = int($$request["health_value"])                   
variable_expenses_groceries = int($$request["variable_expenses_groceries"])
variable_expenses_eating = int($$request["variable_expenses_eating"])
variable_expenses_travel = int($$request["variable_expenses_travel"])
variable_expenses_entertainment = int($$request["variable_expenses_entertainment"])
variable_expenses_health = int($$request["variable_expenses_health"]) 

final_total_income = pharmacy_dollars + income_two_dollars + income_three_dollars
investment_commitment_dollars = investment_commitment_input * total_income_value
variable_expenses_total_expenses = investment_commitment_dollars + debt_payment_dollars + fixed_expenses_total_fixed + variable_expenses_total_variable
atotal_expenses_value =  (variable_expenses_total_expenses / total_income_value) * 100
total_expenses_value = math.ceil(atotal_expenses_value)
variable_expenses_monthly_profit = total_income_value - variable_expenses_total_expenses
amonthly_profit_value = (variable_expenses_monthly_profit / total_income_value) * 100
monthly_profit_value = math.ceil(amonthly_profit_value)
final_total_fixed_expenses = rent_value + utilities_value + phone_value + car_value + monthly_value
final_total_fixed_expenses_value = fixed_expenses_rent  + fixed_expenses_utilities  + fixed_expenses_phone + fixed_expenses_car + fixed_expenses_monthly
final_total_variable_expenses = groceries_value + eating_value + travel_value + entertainment_value + health_value
final_total_variable_expenses_value = variable_expenses_groceries + variable_expenses_eating + variable_expenses_travel + variable_expenses_entertainment + variable_expenses_health

final_output = dict()
final_output["investment_commitment_dollars"] = investment_commitment_dollars
final_output["variable_expenses_total_expenses"] = variable_expenses_total_expenses
final_output["total_expenses_value"] = total_expenses_value
final_output["variable_expenses_monthly_profit"] = variable_expenses_monthly_profit
final_output["monthly_profit_value"] = monthly_profit_value
final_output["final_total_income"] = final_total_income
final_output["final_total_fixed_expenses"] = final_total_fixed_expenses
final_output["final_total_fixed_expenses_value"] = final_total_fixed_expenses_value
final_output["final_total_variable_expenses"] = final_total_variable_expenses
final_output["final_total_variable_expenses_value"] = final_total_variable_expenses_value

final_output["total_income_value"] = $$request["total_income_value"]
final_output["debt_payment_dollars"] = $$request["debt_payment_dollars"]
final_output["fixed_expenses_total_fixed"] = $$request["fixed_expenses_total_fixed"]
final_output["variable_expenses_total_variable"] = $$request["variable_expenses_total_variable"]

%%response%% = final_output
