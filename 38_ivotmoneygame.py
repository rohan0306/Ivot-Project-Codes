import json

request = cache["request"]

if isinstance(request, str):
    request = json.loads(request)

begin_value = float(request["begin_value"])
end_value = float(request["end_value"])
int_rate_value = float(request["int_rate_value"]) / 100
bonus_value = float(request["bonus_value"])
monthly_income_value = float(request["monthly_income_value"])

dec_one_value = float(request["dec_one_value"])
dec_two_value = float(request["dec_two_value"])
dec_three_value = float(request["dec_three_value"])

lifestyle_dec_one = float(request["lifestyle_dec_one"])
lifestyle_dec_two = float(request["lifestyle_dec_two"])
lifestyle_dec_three = float(request["lifestyle_dec_three"])

habits_dec_one = float(request["habits_dec_one"])
habits_dec_two = float(request["habits_dec_two"])
habits_dec_three = float(request["habits_dec_three"])

impulse_dec_one = float(request["impulse_dec_one"])
impulse_dec_two = float(request["impulse_dec_two"])
impulse_dec_three = float(request["impulse_dec_three"])

total_value = dec_one_value + dec_two_value + dec_three_value
remaining_value = bonus_value - total_value

total_months_lost_value = (end_value - begin_value)  # Total number of months
# Future Value Calculation (Without PV)
alost_value = -total_value * (1 + int_rate_value) ** total_months_lost_value
#lost_value = (-total_value * ((1 + int_rate_value ) ** total_months_lost_value - 1) / int_rate_value)
lost_value = round(alost_value)

awealth_value = bonus_value * ( 1 + int_rate_value)**(end_value - begin_value) + alost_value
wealth_value = round(awealth_value)

lifestyle_total = lifestyle_dec_one + lifestyle_dec_two + lifestyle_dec_three
lifestyle_remaining = monthly_income_value - lifestyle_total

monthly_rate_lifestyle_lost = int_rate_value / 12  # Monthly interest rate
total_months_lifestyle_lost = (end_value - begin_value) * 12  # Total number of months
# Future Value Calculation (Without PV)
alifestyle_lost = (-lifestyle_total * ((1 + monthly_rate_lifestyle_lost) ** total_months_lifestyle_lost - 1) / monthly_rate_lifestyle_lost)
lifestyle_lost = round(alifestyle_lost)

habits_total = (habits_dec_one + habits_dec_two + habits_dec_three) * 30
habits_remaining  = lifestyle_remaining - habits_total

monthly_rate_habits_lost = int_rate_value / 12  # Monthly interest rate
total_months_habits_lost = (end_value - begin_value) * 12  # Total number of months
# Future Value Calculation (Without PV)
ahabits_lost = (-habits_total * ((1 + monthly_rate_habits_lost) ** total_months_habits_lost - 1) / monthly_rate_habits_lost)
habits_lost = round(ahabits_lost)

impulse_total = impulse_dec_one + impulse_dec_two + impulse_dec_three
impulse_remaining = habits_remaining - impulse_total

monthly_rate_impulse_lost = int_rate_value / 12  # Monthly interest rate
total_months_impulse_lost = (end_value - begin_value) * 12  # Total number of months
# Future Value Calculation (Without PV)
aimpulse_lost = (-impulse_total * ((1 + monthly_rate_impulse_lost) ** total_months_impulse_lost - 1) / monthly_rate_impulse_lost)
impulse_lost = round(aimpulse_lost)

total_spend = lifestyle_total + habits_total + impulse_total

remaining_spend = impulse_remaining

alost_wealth = alifestyle_lost + ahabits_lost + aimpulse_lost
lost_wealth = round(alost_wealth)

monthly_rate_funds_wealth = int_rate_value / 12  # Monthly interest rate
total_months_funds_wealth = (end_value - begin_value) * 12  # Total number of months
# Future Value Calculation (Without PV)
afunds_wealth = (monthly_income_value * ((1 + monthly_rate_funds_wealth) ** total_months_funds_wealth - 1) / monthly_rate_funds_wealth)
funds_wealth = round(afunds_wealth + alost_wealth)

final_output = dict()
final_output["total_value"] = total_value
final_output["remaining_value"] = remaining_value
final_output["lost_value"] = lost_value
final_output["wealth_value"] = wealth_value

final_output["lifestyle_total"] = lifestyle_total
final_output["lifestyle_remaining"] = lifestyle_remaining
final_output["lifestyle_lost"] = lifestyle_lost

final_output["habits_total"] = habits_total
final_output["habits_remaining"] = habits_remaining
final_output["habits_lost"] = habits_lost

final_output["impulse_total"] = impulse_total
final_output["impulse_remaining"] = impulse_remaining
final_output["impulse_lost"] = impulse_lost

final_output["total_spend"] = total_spend
final_output["remaining_spend"] = remaining_spend
final_output["lost_wealth"] = lost_wealth
final_output["funds_wealth"] = funds_wealth

final_output["int_rate_value"] = request["int_rate_value"] 
final_output["bonus_value"] = request["bonus_value"] 
final_output["dec_one_value"] = request["dec_one_value"] 
final_output["dec_two_value"] = request["dec_two_value"] 
final_output["dec_three_value"] = request["dec_three_value"] 

final_output["lifestyle_dec_one"] = request["lifestyle_dec_one"] 
final_output["lifestyle_dec_two"] = request["lifestyle_dec_two"] 
final_output["lifestyle_dec_three"] = request["lifestyle_dec_three"] 

final_output["habits_dec_one"] = request["habits_dec_one"] 
final_output["habits_dec_two"] = request["habits_dec_two"] 
final_output["habits_dec_three"] = request["habits_dec_three"] 

final_output["impulse_dec_one"] = request["impulse_dec_one"] 
final_output["impulse_dec_two"] = request["impulse_dec_two"] 
final_output["impulse_dec_three"] = request["impulse_dec_three"] 

cache["response"]= final_output

