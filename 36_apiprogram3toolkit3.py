import math

company_value = "$$Company_Name"
symbol_value = "$$Company_Symbol"
price_value = float($$Price)
company_logo = "$$Company_Logo"

#company_value = $$request["company_value"]
#price_value= float($$raw_asset[0]["Price"])
ashares_value = float($$raw_finance_24[0]["Fully_diluted_shares_outstanding_m"]) 
shares_value = round(ashares_value) 

growth_rate_quarter_27 = float($$request["growth_rate_quarter_27"]) / 100
#percent_sales_quarter_27 = float($$request["percent_sales_quarter_27"]) / 100
percent_sales_quarter_27_str = $$request["percent_sales_quarter_27"]

asales_quarter_23 = float($$raw_finance_23[0]["Total_Sales_m"]) 
sales_quarter_23 = round(asales_quarter_23)

sales_quarter_23_a = float($$raw_finance_23[0]["Store_Operating_Expenses_m"]) 
sales_quarter_23_b = float($$raw_finance_23[0]["Product_and_Distribution_Costs_m"]) 
                           
acogs_quarter_23 = float($$raw_finance_23[0]["Total_CostofGoods_m"])
cogs_quarter_23 = round(acogs_quarter_23)
                        
asales_quarter_24 = float($$raw_finance_24[0]["Total_Sales_m"]) 
sales_quarter_24 = round(asales_quarter_24)

sales_quarter_24_a = float($$raw_finance_24[0]["Store_Operating_Expenses_m"]) 
sales_quarter_24_b = float($$raw_finance_24[0]["Product_and_Distribution_Costs_m"]) 
                           
cogs_quarter_24 = float($$raw_finance_24[0]["Total_CostofGoods_m"]) 

amkt_cap_value = price_value * ashares_value
mkt_cap_value = round(amkt_cap_value)

asales_quarter_27 = asales_quarter_24 * ( 1 + growth_rate_quarter_27)**3
sales_quarter_27 = round(asales_quarter_27)

growth_rate_quarter_24  = round((asales_quarter_24 / asales_quarter_23 - 1) * 100)
#growth_rate_quarter_24 = math.ceil(agrowth_rate_quarter_24)

#cogs_quarter_27 =  sales_quarter_27 * percent_sales_quarter_27

apercent_sales_quarter_23 = (acogs_quarter_23 / asales_quarter_23) *100
percent_sales_quarter_23 = round(apercent_sales_quarter_23)
#percent_sales_quarter_23 = math.ceil(apercent_sales_quarter_23)

apercent_sales_quarter_24 = (cogs_quarter_24 / asales_quarter_24) * 100
percent_sales_quarter_24 = round(apercent_sales_quarter_24)
#percent_sales_quarter_24 = math.ceil(apercent_sales_quarter_24)

if percent_sales_quarter_27_str:
    percent_sales_quarter_27 = float(percent_sales_quarter_27_str) / 100
else:
    percent_sales_quarter_27 =  apercent_sales_quarter_24 # Default value if the input is empty or missing

acogs_quarter_27 = asales_quarter_27 * percent_sales_quarter_27

cogs_quarter_27 = round(acogs_quarter_27)
#acogs_quarter_27 = asales_quarter_27 * apercent_sales_quarter_24
#print("Initial COGS (using baseline):", cog_sold_forecast)  # Should use baseline (0.15)

# If there's an explicit switch to using the forecast, update cog_sold_forecast
#use_forecast = True  # Set to True only when you want to use cogs_sales_forecast

#if use_forecast:
#    acogs_quarter_27 = asales_quarter_27 * percent_sales_quarter_27


agross_profit_quarter_23 = asales_quarter_23 - acogs_quarter_23
gross_profit_quarter_23  = round(agross_profit_quarter_23)

agross_profit_quarter_24 = asales_quarter_24 - cogs_quarter_24
gross_profit_quarter_24  = round(agross_profit_quarter_24)

agross_profit_quarter_27 = asales_quarter_27 - acogs_quarter_27
gross_profit_quarter_27  = round(agross_profit_quarter_27)

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

final_output["cogs_quarter_27"] = cogs_quarter_27

final_output["growth_rate_quarter_24"] = growth_rate_quarter_24

#final_output["price_value"] = $$raw_asset[0]["Price"]
final_output["shares_value"] = shares_value

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

#final_output["company_value"] = $$request["company_value"]

%%response%% = final_output
