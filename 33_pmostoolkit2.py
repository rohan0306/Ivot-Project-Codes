import math
inv_value = float($$request["inv_value"])
investment_commitment_dollars = int($$request["investment_commitment_dollars"]) 
payments_23 = int($$request["payments_23"]) 
payments_33 = int($$request["payments_33"]) 
payments_53 = int($$request["payments_53"]) 
payments_73 = int($$request["payments_73"]) 
c8 = float($$request["c8"]) / 100
return_value = float($$request["return_value"]) / 100
starting_amount = int($$request["starting_amount"]) 
#safety_value_33 = int($$request["safety_value_33"]) 
#safety_value_53 = int($$request["safety_value_53"]) 
#safety_value_73 = int($$request["safety_value_73"]) 
monthly_overhead_23 = int($$request["monthly_overhead_23"]) 
#monthly_overhead_53 = int($$request["monthly_overhead_53"]) 
#monthly_overhead_73 = int($$request["monthly_overhead_73"]) 
inflation_value = float($$request["inflation_value"]) / 100
                                    
#Fields which is to be used for Calculation and not to show on FrontEnd.
monthly_com_23 = investment_commitment_dollars + inv_value
monthly_com_33 = investment_commitment_dollars + inv_value
monthly_com_53 = investment_commitment_dollars + inv_value
monthly_com_73 = investment_commitment_dollars + inv_value

#Simple Interest
c7 = investment_commitment_dollars * 12 + inv_value
c9 = c7 * c8

k7 = c7 * 9
k9 = c9 * 9
k10 = k9 * 5

l9 = c9 * 10
#l10 = l9 + k10

ae7 = c7 * 29
ae9 = ae7 * c8
ae10 = ae9 * 15

af9 = c9 * 30
#af10 = ae10 + af9

ay7 = c7 * 49
ay9 = c9 * 49
ay10 = ay9 * 25

az9 = c9 * 50
#az10 = ay10 + az9

#Total Portfolio 
# Convert annual interest rate to monthly interest rate for 33
monthly_rate_33 = return_value / 12

# Calculate Future Value using numpy_financial's fv function
#future_value_33 = npf.fv(rate=monthly_rate_33, nper=payments_33, pmt=-monthly_com_33, pv=0)
future_value_33 = monthly_com_33 * ((1 + monthly_rate_33)**payments_33 - 1) / monthly_rate_33

# Add the additional amount (E13)
#final_value = future_value_33 + E13

# Convert annual interest rate to monthly interest rate for 53
monthly_rate_53 = return_value / 12

# Calculate Future Value using numpy_financial's fv function
#future_value_53 = npf.fv(rate=monthly_rate_53, nper=payments_53, pmt=-monthly_com_53, pv=0)
future_value_53 = monthly_com_53 * ((1 + monthly_rate_53)**payments_53 - 1) / monthly_rate_53

# Add the additional amount (G13)
#final_value = future_value_53 + starting_amount

# Convert annual interest rate to monthly interest rate for 73
monthly_rate_73 = return_value / 12

# Calculate Future Value using numpy_financial's fv function
#future_value_73 = npf.fv(rate=monthly_rate_73, nper=payments_73, pmt=-monthly_com_73, pv=0)
future_value_73 = monthly_com_73 * ((1 + monthly_rate_73)**payments_73 - 1) / monthly_rate_73

#Calculated Fields and is to be shown on FrontEnd.
total_invested_33 = payments_33 * monthly_com_33
total_invested_53 = payments_53 * monthly_com_53
total_invested_73 = payments_73 * monthly_com_73

atotal_si_33 = l9 + k10
total_si_33 = math.ceil(atotal_si_33)
atotal_si_53 = ae10 + af9
total_si_53 = math.ceil(atotal_si_53)
atotal_si_73 = ay10 + az9
total_si_73 = math.ceil(atotal_si_73)

atotal_portfolio_33 = future_value_33 + starting_amount
total_portfolio_33 = math.ceil(atotal_portfolio_33)
atotal_portfolio_53 = future_value_53 + starting_amount
total_portfolio_53 = math.ceil(atotal_portfolio_53)
atotal_portfolio_73 = future_value_73 + starting_amount
total_portfolio_73  = math.floor(atotal_portfolio_73)

atotal_interest_33 = total_portfolio_33 - total_invested_33
total_interest_33 = math.ceil(atotal_interest_33)
atotal_interest_53 = total_portfolio_53 - total_invested_53
total_interest_53 = math.ceil(atotal_interest_53)
atotal_interest_73 = total_portfolio_73 - total_invested_73
total_interest_73 = math.floor(atotal_interest_73)

atotal_ci_33 = total_interest_33 - total_si_33
total_ci_33 = math.ceil(atotal_ci_33)
atotal_ci_53 = total_interest_53 - total_si_53
total_ci_53 = math.ceil(atotal_ci_53)
atotal_ci_73 = total_interest_73 - total_si_73
total_ci_73 = math.floor(atotal_ci_73)

monthly_overhead_26 = monthly_overhead_23 * (1 + inflation_value) #not to show on frontend
amonthly_overhead_33 = monthly_overhead_26 * 1.02
monthly_overhead_33 = math.floor(amonthly_overhead_33)
monthly_overhead_43 = monthly_overhead_33 * 1.02       #not to show on frontend
amonthly_overhead_53 = monthly_overhead_43 * 1.02
monthly_overhead_53 = math.floor(amonthly_overhead_53)
monthly_overhead_63 = monthly_overhead_53 * 1.02       #not to show on frontend
amonthly_overhead_73 = monthly_overhead_63 * 1.02
monthly_overhead_73 = math.ceil(amonthly_overhead_73)

safety_value_23 = monthly_overhead_23 * 6
asafety_value_33 = amonthly_overhead_33 * 6
safety_value_33 = math.floor(asafety_value_33)
safety_value_53 = monthly_overhead_53 * 6
safety_value_73 = monthly_overhead_73 * 6

safety_net_33 = round((total_portfolio_33 / safety_value_33) * 100) if safety_value_33 > 0 else 0

safety_net_53 = round((total_portfolio_53 / safety_value_53) * 100) if safety_value_53 > 0 else 0
safety_net_73 = round((total_portfolio_73 / safety_value_73) * 100) if safety_value_73 > 0 else 0

aimplied_mi_33 = total_portfolio_33 * 0.1 / 12
implied_mi_33 = math.floor(aimplied_mi_33)
aimplied_mi_53 = total_portfolio_53 * 0.1 / 12
implied_mi_53 = math.floor(aimplied_mi_53)
aimplied_mi_73 = total_portfolio_73 * 0.1 / 12
implied_mi_73 = math.ceil(aimplied_mi_73)

financial_freedom_33 = round((implied_mi_33 / monthly_overhead_33) * 100) if monthly_overhead_33 > 0 else 0
financial_freedom_53 = round((implied_mi_53 / monthly_overhead_53) * 100) if monthly_overhead_53 > 0 else 0
financial_freedom_73 = round((implied_mi_73 / monthly_overhead_73) * 100) if monthly_overhead_73 > 0 else 0

final_output = dict()
final_output["total_invested_33"] = total_invested_33
final_output["total_invested_53"] = total_invested_53
final_output["total_invested_73"] = total_invested_73
final_output["total_si_33"] = total_si_33
final_output["total_si_53"] = total_si_53
final_output["total_si_73"] = total_si_73
final_output["total_ci_33"] = total_ci_33
final_output["total_ci_53"] = total_ci_53
final_output["total_ci_73"] = total_ci_73
final_output["total_interest_33"] = total_interest_33
final_output["total_interest_53"] = total_interest_53
final_output["total_interest_73"] = total_interest_73
final_output["total_portfolio_33"] = total_portfolio_33
final_output["total_portfolio_53"] = total_portfolio_53
final_output["total_portfolio_73"] = total_portfolio_73
final_output["monthly_overhead_33"] = monthly_overhead_33
final_output["monthly_overhead_53"] = monthly_overhead_53
final_output["monthly_overhead_73"] = monthly_overhead_73

final_output["safety_value_23"] = safety_value_23
final_output["safety_value_33"] = safety_value_33
final_output["safety_value_53"] = safety_value_53
final_output["safety_value_73"] = safety_value_73

final_output["safety_net_33"] = safety_net_33
final_output["safety_net_53"] = safety_net_53
final_output["safety_net_73"] = safety_net_73
final_output["implied_mi_33"] = implied_mi_33
final_output["implied_mi_53"] = implied_mi_53
final_output["implied_mi_73"] = implied_mi_73
final_output["financial_freedom_33"] = financial_freedom_33
final_output["financial_freedom_53"] = financial_freedom_53
final_output["financial_freedom_73"] = financial_freedom_73

final_output["investment_commitment_dollars"] = $$request["investment_commitment_dollars"]
final_output["payments_23"] = $$request["payments_23"]
final_output["payments_33"] = $$request["payments_33"]
final_output["payments_53"] = $$request["payments_53"]
final_output["payments_73"] = $$request["payments_73"]
final_output["c8"] = $$request["c8"]
final_output["return_value"] = $$request["return_value"]
final_output["starting_amount"] = $$request["starting_amount"]
final_output["monthly_overhead_23"] = $$request["monthly_overhead_23"]
final_output["inflation_value"] = $$request["inflation_value"]
#final_output["monthly_overhead_53"] = $$request["monthly_overhead_53"]
#final_output["monthly_overhead_73"] = $$request["monthly_overhead_73"]

%%response%% = final_output
