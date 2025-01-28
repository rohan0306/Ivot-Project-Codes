import math

company_value = "$$Company_Name"
symbol_value = "$$Company_Symbol"
price_value = float($$Price)
company_logo = "$$Company_Logo"

growth_rate_quarter_27 = float($$request["growth_rate_quarter_27"]) / 100
#percent_sales_quarter_27 = float($$request["percent_sales_quarter_27"]) / 100
request = $$request
percent_sales_quarter_27_str = request["percent_sales_quarter_27"]

# Check if the value is not empty before converting
#if percent_sales_quarter_27_str:
#    percent_sales_quarter_27 = float(percent_sales_quarter_27_str) / 100
#else:
#    percent_sales_quarter_27 = 0.0  # Default value if the input is empty or missing

#price_value = float($$raw_asset[0]["Price"])
ashares_value = float($$raw_finance_24[0]["Fully_diluted_shares_outstanding_m"]) 
shares_value = math.ceil(ashares_value) 

extra_q1_quarter_22 = float($$raw_finance_q1_22[0]["Quarterly_Operating_Cash_Flow_m"])
extra_q1_quarter_23 = float($$raw_finance_q1_23[0]["Quarterly_Operating_Cash_Flow_m"])
                            
extra_fully_q3_22 = float($$raw_finance_q3_22[0]["Fully_diluted_shares_outstanding_m"])
                          
aextra_fully_q3_24 = float($$raw_finance_24[0]["Fully_diluted_shares_outstanding_m"])
extra_fully_q3_24 = math.ceil(aextra_fully_q3_24)                           
                          
cash_and_cash_quarter_23 = float($$raw_finance_23[0]["Cash_and_Cash_Equivalents_m"]) 

longterm_invest_quarter_23 = float($$raw_finance_23[0]["Longterm_Investments_m"]) 
                                   
alongterm_debt_quarter_23 = float($$raw_finance_23[0]["Longterm_Debt_m"]) 
longterm_debt_quarter_23 = math.floor(alongterm_debt_quarter_23) 


acash_and_cash_quarter_24 = float($$raw_finance_24[0]["Cash_and_Cash_Equivalents_m"]) 
cash_and_cash_quarter_24 = math.floor(acash_and_cash_quarter_24)

alongterm_invest_quarter_24 = float($$raw_finance_24[0]["Longterm_Investments_m"])
longterm_invest_quarter_24 = math.ceil(alongterm_invest_quarter_24)
                                   
alongterm_debt_quarter_24 = float($$raw_finance_24[0]["Longterm_Debt_m"]) 
longterm_debt_quarter_24 = math.floor(alongterm_debt_quarter_24) 


asales_quarter_23 = float($$raw_finance_23[0]["Total_Sales_m"]) 
sales_quarter_23 = math.floor(asales_quarter_23)

sales_quarter_23_a = float($$raw_finance_23[0]["Store_Operating_Expenses_m"]) 
sales_quarter_23_b = float($$raw_finance_23[0]["Product_and_Distribution_Costs_m"]) 
                           
acogs_quarter_23 = float($$raw_finance_23[0]["Total_CostofGoods_m"])
cogs_quarter_23 = math.ceil(acogs_quarter_23)
                        
asales_quarter_24 = float($$raw_finance_24[0]["Total_Sales_m"]) 
sales_quarter_24 = math.ceil(asales_quarter_24)

sales_quarter_24_a = float($$raw_finance_24[0]["Store_Operating_Expenses_m"]) 
sales_quarter_24_b = float($$raw_finance_24[0]["Product_and_Distribution_Costs_m"]) 
                           
cogs_quarter_24 = float($$raw_finance_24[0]["Total_CostofGoods_m"]) 
                        
ageneral_admin_quarter_23 = float($$raw_finance_23[0]["General__Administrative_m"])
general_admin_quarter_23 = math.floor(ageneral_admin_quarter_23) 

selling_market_quarter_23 = float($$raw_finance_23[0]["Selling__Marketing_m"])
                                  
research_development_quarter_23 = float($$raw_finance_23[0]["Research__Development_m"])
                                        
aother_quarter_23 = float($$raw_finance_23[0]["Other_m"])
other_quarter_23 = math.ceil(aother_quarter_23) 

adepreciation_quarter_23  = float($$raw_finance_23[0]["Depreciation_m"])
depreciation_quarter_23 = math.ceil(adepreciation_quarter_23) 


general_admin_quarter_24 = float($$raw_finance_24[0]["General__Administrative_m"])
 
selling_market_quarter_24 = float($$raw_finance_24[0]["Selling__Marketing_m"])
                                  
research_development_quarter_24 = float($$raw_finance_24[0]["Research__Development_m"])
                                        
aother_quarter_24 = float($$raw_finance_24[0]["Other_m"])
other_quarter_24 = math.ceil(aother_quarter_24) 

adepreciation_quarter_24  = float($$raw_finance_24[0]["Depreciation_m"])
depreciation_quarter_24 = math.floor(adepreciation_quarter_24) 

amkt_cap_value = price_value * ashares_value
mkt_cap_value = math.floor(amkt_cap_value)

asales_quarter_27 = asales_quarter_24 * ( 1 + growth_rate_quarter_27)**3
sales_quarter_27 = math.ceil(asales_quarter_27)

agross_profit_quarter_23 = asales_quarter_23 - acogs_quarter_23
gross_profit_quarter_23  = math.ceil(agross_profit_quarter_23)

agross_profit_quarter_24 = asales_quarter_24 - cogs_quarter_24
gross_profit_quarter_24  = math.ceil(agross_profit_quarter_24)

apercent_sales_quarter_23 = (acogs_quarter_23 / asales_quarter_23) *100
percent_sales_quarter_23 = round(apercent_sales_quarter_23)
#percent_sales_quarter_23 = math.ceil(apercent_sales_quarter_23)

apercent_sales_quarter_24 = (cogs_quarter_24 / asales_quarter_24) * 100
percent_sales_quarter_24 = round(apercent_sales_quarter_24)
#percent_sales_quarter_24 = math.ceil(apercent_sales_quarter_24)

# Check if the value is not empty before converting
if percent_sales_quarter_27_str != "":
    percent_sales_quarter_27 = float(percent_sales_quarter_27_str) / 100
else:
    percent_sales_quarter_27 =  float(apercent_sales_quarter_24) / 100 # Default value if the input is empty or missing

acogs_quarter_27 = asales_quarter_27 * percent_sales_quarter_27


cogs_quarter_27 = math.floor(acogs_quarter_27)

agross_profit_quarter_27 = asales_quarter_27 - acogs_quarter_27
gross_profit_quarter_27  = math.ceil(agross_profit_quarter_27)


general_admin_percent_quarter_24 = general_admin_quarter_24 / asales_quarter_24
general_admin_quarter_27 = asales_quarter_27 * general_admin_percent_quarter_24

selling_market_percent_quarter_24 = selling_market_quarter_24 / asales_quarter_24
selling_market_quarter_27 = asales_quarter_27 * selling_market_percent_quarter_24

research_development_percent_quarter_24 = research_development_quarter_24 / asales_quarter_24
research_development_quarter_27 = asales_quarter_27 * research_development_percent_quarter_24

other_percent_quarter_24 = aother_quarter_24 / asales_quarter_24
other_quarter_27 = asales_quarter_27 * other_percent_quarter_24


aoperating_profit_quarter_23 = agross_profit_quarter_23 - ageneral_admin_quarter_23 - selling_market_quarter_23 - research_development_quarter_23 - aother_quarter_23
operating_profit_quarter_23  = math.ceil(aoperating_profit_quarter_23)
tax_quarter_23 = aoperating_profit_quarter_23 * 0.21
aquarterly_operating_quarter_23 = aoperating_profit_quarter_23 - tax_quarter_23 + adepreciation_quarter_23
quarterly_operating_quarter_23 = round(aquarterly_operating_quarter_23)

aoperating_profit_quarter_24 = agross_profit_quarter_24 - general_admin_quarter_24 - selling_market_quarter_24 - research_development_quarter_24 - aother_quarter_24
operating_profit_quarter_24 = math.ceil(aoperating_profit_quarter_24)
tax_quarter_24 = aoperating_profit_quarter_24 * 0.21
aquarterly_operating_quarter_24 = aoperating_profit_quarter_24 - tax_quarter_24 + adepreciation_quarter_24
quarterly_operating_quarter_24 = math.floor(aquarterly_operating_quarter_24)

aoperating_profit_quarter_27 = agross_profit_quarter_27 - general_admin_quarter_27 - selling_market_quarter_27 - research_development_quarter_27 - other_quarter_27
operating_profit_quarter_27 = math.ceil(aoperating_profit_quarter_27)
tax_quarter_27 = aoperating_profit_quarter_27 * 0.21
aquarterly_operating_quarter_27 = aoperating_profit_quarter_27 - tax_quarter_27 + adepreciation_quarter_24
quarterly_operating_quarter_27 = math.floor(aquarterly_operating_quarter_27)

operating_cash_quarter_23 = round((extra_q1_quarter_23 / extra_q1_quarter_22 - 1) * 100)

operating_cash_quarter_24 = round((aquarterly_operating_quarter_24 / aquarterly_operating_quarter_23 - 1) * 100)

#operating_cash_quarter_27 = ((aquarterly_operating_quarter_27 / aquarterly_operating_quarter_24 - 1 ) **1/3)
operating_cash_quarter_27 = round(((aquarterly_operating_quarter_27 / aquarterly_operating_quarter_24 - 1 ) **1/3) * 100)


annual_operating_run_rate_quarter_23 = aquarterly_operating_quarter_23 * 4   #Not to show on screen
acash_flow_value_quarter_23 = annual_operating_run_rate_quarter_23 / 0.04
cash_flow_value_quarter_23 = math.ceil(acash_flow_value_quarter_23)
anet_cash_quarter_23 = cash_and_cash_quarter_23 + longterm_invest_quarter_23 - alongterm_debt_quarter_23
net_cash_quarter_23 = int(anet_cash_quarter_23)
aenterprise_value_quarter_23 = acash_flow_value_quarter_23 + anet_cash_quarter_23
enterprise_value_quarter_23 = math.floor(aenterprise_value_quarter_23)
aenterprise_quarter_23 = aenterprise_value_quarter_23 / extra_fully_q3_22 #Quarterlies
enterprise_quarter_23 = math.ceil(aenterprise_quarter_23)

annual_operating_run_rate_quarter_24 = aquarterly_operating_quarter_24 * 4   #Not to show on screen
acash_flow_value_quarter_24 = annual_operating_run_rate_quarter_24 / 0.04
cash_flow_value_quarter_24 = math.ceil(acash_flow_value_quarter_24)
anet_cash_quarter_24 = acash_and_cash_quarter_24 + alongterm_invest_quarter_24 - alongterm_debt_quarter_24
net_cash_quarter_24 = int(anet_cash_quarter_24)
aenterprise_value_quarter_24 = acash_flow_value_quarter_24 + anet_cash_quarter_24
enterprise_value_quarter_24 = math.ceil(aenterprise_value_quarter_24)
aenterprise_quarter_24 = aenterprise_value_quarter_24 / aextra_fully_q3_24 #Quarterlies
enterprise_quarter_24 = math.ceil(aenterprise_quarter_24)

annual_operating_run_rate_quarter_27 = aquarterly_operating_quarter_27 * 4   #Not to show on screen
acash_flow_value_quarter_27 = annual_operating_run_rate_quarter_27 / 0.04
cash_flow_value_quarter_27 = math.floor(acash_flow_value_quarter_27)
anet_cash_quarter_27 = acash_and_cash_quarter_24 + alongterm_invest_quarter_24 - alongterm_debt_quarter_24
net_cash_quarter_27 = int(anet_cash_quarter_27)
aenterprise_value_quarter_27 = acash_flow_value_quarter_27 + anet_cash_quarter_27
enterprise_value_quarter_27 = math.floor(aenterprise_value_quarter_27)
aenterprise_quarter_27 = aenterprise_value_quarter_27 / aextra_fully_q3_24 #Quarterlies
enterprise_quarter_27 = math.ceil(aenterprise_quarter_27)

implied_quarter_23 = round((aenterprise_quarter_23 / price_value - 1) * 100)
implied_quarter_24 = round((aenterprise_quarter_24 / price_value - 1) * 100)
implied_quarter_27 = round((aenterprise_quarter_27 / price_value - 1) * 100)

#implied_quarter_23 = round((enterprise_quarter_23 / price_value - 1)* 100,1)
#implied_quarter_24 = round((enterprise_quarter_24 / price_value - 1)* 100,1)
#implied_quarter_27 = round((enterprise_quarter_27 / price_value - 1)* 100,1)

operating_margin_quarter_23 = round((aoperating_profit_quarter_23 / asales_quarter_23) * 100)

operating_margin_quarter_24 = round((aoperating_profit_quarter_24 / asales_quarter_24) * 100)

operating_margin_quarter_27 = round((aoperating_profit_quarter_27 / asales_quarter_27) * 100) 


growth_rate_quarter_24  = round((asales_quarter_24 / asales_quarter_23 - 1) * 100)
#growth_rate_quarter_24 = math.ceil(agrowth_rate_quarter_24)

#cogs_quarter_27 =  sales_quarter_27 * percent_sales_quarter_27


gross_margin_quarter_23 = round((agross_profit_quarter_23 / asales_quarter_23) * 100)
gross_margin_quarter_24 = round((agross_profit_quarter_24 / asales_quarter_24) * 100)
gross_margin_quarter_27 = round((agross_profit_quarter_27 / asales_quarter_27) * 100)

final_output = dict()

final_output["company_value"] = company_value
final_output["symbol_value"] = symbol_value
final_output["price_value"] = price_value
final_output["company_logo"] = company_logo
final_output["mkt_cap_value"] = mkt_cap_value

final_output["sales_quarter_27"] = sales_quarter_27

final_output["growth_rate_quarter_24"] = growth_rate_quarter_24

final_output["cogs_quarter_27"] = cogs_quarter_27

#final_output["price_value"] = $$raw_asset[0]["Price"]
final_output["shares_value"] = shares_value

final_output["quarterly_operating_quarter_23"] = quarterly_operating_quarter_23
final_output["quarterly_operating_quarter_24"] = quarterly_operating_quarter_24
final_output["quarterly_operating_quarter_27"] = quarterly_operating_quarter_27

final_output["operating_cash_quarter_23"] = operating_cash_quarter_23
final_output["operating_cash_quarter_24"] = operating_cash_quarter_24
final_output["operating_cash_quarter_27"] = operating_cash_quarter_27

final_output["enterprise_quarter_23"] = enterprise_quarter_23
final_output["enterprise_quarter_24"] = enterprise_quarter_24
final_output["enterprise_quarter_27"] = enterprise_quarter_27

final_output["implied_quarter_23"] = implied_quarter_23
final_output["implied_quarter_24"] = implied_quarter_24
final_output["implied_quarter_27"] = implied_quarter_27

final_output["sales_quarter_23"] = sales_quarter_23
final_output["sales_quarter_24"] = sales_quarter_24

final_output["cogs_quarter_23"] = cogs_quarter_23
final_output["cogs_quarter_24"] = cogs_quarter_24

final_output["percent_sales_quarter_23"] = percent_sales_quarter_23
final_output["percent_sales_quarter_24"] = percent_sales_quarter_24

final_output["gross_profit_quarter_23"] = gross_profit_quarter_23
final_output["gross_profit_quarter_24"] = gross_profit_quarter_24
final_output["gross_profit_quarter_27"] = gross_profit_quarter_27

final_output["gross_margin_quarter_23"] = gross_margin_quarter_23
final_output["gross_margin_quarter_24"] = gross_margin_quarter_24
final_output["gross_margin_quarter_27"] = gross_margin_quarter_27

final_output["operating_profit_quarter_23"] = operating_profit_quarter_23
final_output["operating_profit_quarter_24"] = operating_profit_quarter_24
final_output["operating_profit_quarter_27"] = operating_profit_quarter_27

final_output["operating_margin_quarter_23"] = operating_margin_quarter_23
final_output["operating_margin_quarter_24"] = operating_margin_quarter_24
final_output["operating_margin_quarter_27"] = operating_margin_quarter_27

final_output["cash_flow_value_quarter_23"] = cash_flow_value_quarter_23
final_output["cash_flow_value_quarter_24"] = cash_flow_value_quarter_24
final_output["cash_flow_value_quarter_27"] = cash_flow_value_quarter_27

final_output["net_cash_quarter_23"] = net_cash_quarter_23
final_output["net_cash_quarter_24"] = net_cash_quarter_24
final_output["net_cash_quarter_27"] = net_cash_quarter_27

final_output["enterprise_value_quarter_23"] = enterprise_value_quarter_23
final_output["enterprise_value_quarter_24"] = enterprise_value_quarter_24
final_output["enterprise_value_quarter_27"] = enterprise_value_quarter_27

final_output["fully_diluted_quarter_23"] = $$raw_finance_q3_22[0]["Fully_diluted_shares_outstanding_m"]
final_output["fully_diluted_quarter_24"] = extra_fully_q3_24
final_output["fully_diluted_quarter_27"] = extra_fully_q3_24

final_output["implied_value_per_quarter_23"] = enterprise_quarter_23
final_output["implied_value_per_quarter_24"] = enterprise_quarter_24
final_output["implied_value_per_quarter_27"] = enterprise_quarter_27

final_output["tax_quarter_27"] = tax_quarter_27

#final_output["company_value"] = $$request["company_value"]

%%response%% = final_output