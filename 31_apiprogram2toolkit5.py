import math

year_over_forecast = float($$request["year_over_forecast"]) / 100
cogs_sales_forecast = float($$request["cogs_sales_forecast"]) /100

sales_year = int($$request["sales_year"])
sales_baseline = int($$request["sales_baseline"])
year_over_baseline = float($$request["year_over_baseline"])
cog_sold_year = int($$request["cog_sold_year"])
cog_sold_baseline = int($$request["cog_sold_baseline"])
cogs_sales_year = float($$request["cogs_sales_year"])
net_cash_forecast = int($$request["net_cash_forecast"])
                        
sales_market_baseline = int($$request["sales_market_baseline"])
general_admin_baseline = int($$request["general_admin_baseline"])
                        
#cogs_sales_baseline = float($$request["cogs_sales_baseline"])
#cogs_sales_forecast = float($$request["cogs_sales_forecast"])
                            
gross_profit_year = int($$request["gross_profit_year"])
gross_profit_baseline = int($$request["gross_profit_baseline"])
gross_margin_year = float($$request["gross_margin_year"])
gross_margin_baseline = float($$request["gross_margin_baseline"])
                              
                              
depreciation= int($$request["depreciation"])                              
shares_outstanding_value_forecast = int($$request["shares_outstanding_value_forecast"])
market_px_value= int($$request["market_px_value"]) 
quarterly_operating_cash_flow_quarter_24 = int($$request["quarterly_operating_cash_flow_quarter_24"]) 
                              
#operating_profit_forecast = int($$request["operating_profit_forecast"])

#year_over_baseline = sales_baseline / sales_year - 1
asales_forecast = sales_baseline * (1 + year_over_forecast) ** 3
sales_forecast  = int(round(asales_forecast ))

acogs_sales_baseline = (cog_sold_baseline / sales_baseline) * 100
cogs_sales_baseline = round(acogs_sales_baseline,1)


acog_sold_forecast = sales_forecast * cogs_sales_baseline
#print("Initial COGS (using baseline):", cog_sold_forecast)  # Should use baseline (0.15)

# If there's an explicit switch to using the forecast, update cog_sold_forecast
use_forecast = True  # Set to True only when you want to use cogs_sales_forecast

if use_forecast:
    acog_sold_forecast = sales_forecast * cogs_sales_forecast 

cog_sold_forecast = round(acog_sold_forecast)

#cog_sold_forecast = int(cog_sold_baseline / sales_baseline * sales_forecast)
#cog_sold_forecast = math.floor(acog_sold_forecast / 1000) * 1000  # Rounds down to the nearest thousand

agross_profit_forecast = sales_forecast - cog_sold_forecast
gross_profit_forecast = round(agross_profit_forecast)

agross_margin_forecast = gross_profit_forecast / sales_forecast 
gross_margin_forecast = round(agross_margin_forecast * 100,1) # Converts 0.133 to 13.3

sales_percent_baseline = sales_market_baseline / sales_baseline

sales_market_forecast = sales_forecast * sales_percent_baseline 

general_percent_baseline = general_admin_baseline / sales_baseline

general_admin_forecast = sales_forecast * general_percent_baseline

aoperating_profit_forecast = agross_profit_forecast - sales_market_forecast - general_admin_forecast
operating_profit_forecast = round(aoperating_profit_forecast)

aoperating_margin_forecast	= operating_profit_forecast / sales_forecast
operating_margin_forecast	= round(aoperating_margin_forecast * 100,1)

atax_forecast = operating_profit_forecast * 0.21
tax_forecast = round(atax_forecast)
aquarterly_operating_cash_forecast = operating_profit_forecast - atax_forecast +  depreciation
quarterly_operating_cash_forecast = round(aquarterly_operating_cash_forecast)
raw_annual_cash_flow_forecast = aquarterly_operating_cash_forecast * 4
annual_cash_flow_forecast = round(raw_annual_cash_flow_forecast )
cash_flow_value_forecast = raw_annual_cash_flow_forecast / 0.04
aenterprise_value_forecast	= cash_flow_value_forecast / shares_outstanding_value_forecast
enterprise_value_forecast = round(aenterprise_value_forecast)  # Rounds to the nearest integer

aimplied_forecast = (aenterprise_value_forecast / market_px_value - 1) * 100
implied_forecast = round(aimplied_forecast,1)  # Gives 28.8

operating_cash_flow_growth_quarter_27 = round((quarterly_operating_cash_forecast / quarterly_operating_cash_flow_quarter_24 - 1) * 100,1)

new_enterprise_value_forecast = cash_flow_value_forecast + net_cash_forecast

final_output = dict()
final_output["sales_forecast"] = sales_forecast
final_output["cog_sold_forecast"] = cog_sold_forecast
final_output["gross_profit_forecast"] = gross_profit_forecast
final_output["gross_margin_forecast"] = gross_margin_forecast
final_output["cogs_sales_baseline"] = cogs_sales_baseline

final_output["operating_profit_forecast"] = operating_profit_forecast

final_output["operating_margin_forecast"] = operating_margin_forecast

final_output["sales_market_forecast"] = sales_market_forecast
final_output["sales_percent_baseline"] = sales_percent_baseline
#final_output["sales_percent_forecast"] = sales_percent_forecast

final_output["general_admin_forecast"] = general_admin_forecast
final_output["general_percent_baseline"] = general_percent_baseline
#final_output["general_percent_forecast"] = general_percent_forecast

final_output["new_enterprise_value_forecast"] = new_enterprise_value_forecast

final_output["tax_forecast"] = tax_forecast
final_output["quarterly_operating_cash_forecast"] = quarterly_operating_cash_forecast
final_output["annual_cash_flow_forecast"] = annual_cash_flow_forecast
final_output["cash_flow_value_forecast"] = cash_flow_value_forecast
final_output["enterprise_value_forecast"] = enterprise_value_forecast

final_output["implied_forecast"] = implied_forecast

final_output["operating_cash_flow_growth_quarter_27"] = operating_cash_flow_growth_quarter_27

final_output["sales_year"] = $$request["sales_year"]
final_output["sales_baseline"] = $$request["sales_baseline"]
final_output["year_over_baseline"] = $$request["year_over_baseline"]
final_output["cog_sold_year"] = $$request["cog_sold_year"]
final_output["cog_sold_baseline"] = $$request["cog_sold_baseline"]
final_output["cogs_sales_year"] = $$request["cogs_sales_year"]
#final_output["cogs_sales_baseline"] = $$request["cogs_sales_baseline"]
final_output["cogs_sales_forecast"] = $$request["cogs_sales_forecast"]

final_output["gross_profit_year"] = $$request["gross_profit_year"]
final_output["gross_profit_baseline"] = $$request["gross_profit_baseline"]
final_output["gross_margin_year"] = $$request["gross_margin_year"]
final_output["gross_margin_baseline"] = $$request["gross_margin_baseline"]
#final_output["operating_profit_forecast"] = $$request["operating_profit_forecast"]

final_output["sales_market_baseline"] = $$request["sales_market_baseline"]
final_output["general_admin_baseline"] = $$request["general_admin_baseline"]

final_output["depreciation"] = $$request["depreciation"]
final_output["shares_outstanding_value_forecast"] = $$request["shares_outstanding_value_forecast"]
final_output["market_px_value"] = $$request["market_px_value"]

final_output["quarterly_operating_cash_flow_quarter_24"] = $$request["quarterly_operating_cash_flow_quarter_24"]

%%response%% = final_output




