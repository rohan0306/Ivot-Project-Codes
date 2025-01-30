import math

year_over_forecast = float($$request["year_over_forecast"]) / 100
cogs_sales_forecast = float($$request["cogs_sales_forecast"]) /100

sales_year = int($$request["sales_year"])
sales_baseline = int($$request["sales_baseline"])
year_over_baseline = float($$request["year_over_baseline"])
cog_sold_year = int($$request["cog_sold_year"])
cog_sold_baseline = int($$request["cog_sold_baseline"])
cogs_sales_year = float($$request["cogs_sales_year"])
#cogs_sales_baseline = float($$request["cogs_sales_baseline"])
#cogs_sales_forecast = float($$request["cogs_sales_forecast"])
gross_profit_year = int($$request["gross_profit_year"])
gross_profit_baseline = int($$request["gross_profit_baseline"])
gross_margin_year = float($$request["gross_margin_year"])
gross_margin_baseline = float($$request["gross_margin_baseline"])

#year_over_baseline = sales_baseline / sales_year - 1
asales_forecast = sales_baseline * (1 + year_over_forecast) ** 3
sales_forecast  = int(math.ceil(asales_forecast ))

acogs_sales_baseline = (cog_sold_baseline / sales_baseline) * 100
cogs_sales_baseline = round(acogs_sales_baseline, 1)


acog_sold_forecast = sales_forecast * cogs_sales_baseline
#print("Initial COGS (using baseline):", cog_sold_forecast)  # Should use baseline (0.15)

# If there's an explicit switch to using the forecast, update cog_sold_forecast
use_forecast = True  # Set to True only when you want to use cogs_sales_forecast

if use_forecast:
    acog_sold_forecast = sales_forecast * cogs_sales_forecast 

cog_sold_forecast = math.floor(acog_sold_forecast)

#cog_sold_forecast =  sales_forecast * cogs_sales_baseline
#cog_sold_forecast = sales_forecast * cogs_sales_forecast
#cog_sold_forecast = sales_forecast * year_over_forecast
#cog_sold_forecast = math.floor(acog_sold_forecast)  # Rounds down to the nearest thousand

agross_profit_forecast = sales_forecast - acog_sold_forecast
gross_profit_forecast = round(agross_profit_forecast)

agross_margin_forecast = gross_profit_forecast / sales_forecast 
gross_margin_forecast = round(agross_margin_forecast * 100,1) # Converts 0.133 to 13.3

final_output = dict()
final_output["sales_forecast"] = sales_forecast
final_output["cog_sold_forecast"] = cog_sold_forecast
final_output["gross_profit_forecast"] = gross_profit_forecast
final_output["gross_margin_forecast"] = gross_margin_forecast
final_output["cogs_sales_baseline"] = cogs_sales_baseline

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

%%response%% = final_output





[{
    "$match": {
        "toolkit": "Program2Toolkit4"
    }
},
{
    "$project": {
        "field_name": 1,
        "field_value": 1,
        "_id": 0
    }
}]






import math

year_over_forecast = float($$request["year_over_forecast"]) / 100
cogs_sales_forecast = float($$request["cogs_sales_forecast"]) /100

sales_year = int($$request["sales_year"])
sales_baseline = int($$request["sales_baseline"])
year_over_baseline = float($$request["year_over_baseline"])
cog_sold_year = int($$request["cog_sold_year"])
cog_sold_baseline = int($$request["cog_sold_baseline"])
cogs_sales_year = float($$request["cogs_sales_year"])
#cogs_sales_baseline = float($$request["cogs_sales_baseline"])
#cogs_sales_forecast = float($$request["cogs_sales_forecast"])
gross_profit_year = int($$request["gross_profit_year"])
gross_profit_baseline = int($$request["gross_profit_baseline"])
gross_margin_year = float($$request["gross_margin_year"])
gross_margin_baseline = float($$request["gross_margin_baseline"])

#year_over_baseline = sales_baseline / sales_year - 1
asales_forecast = sales_baseline * (1 + year_over_forecast) ** 3
sales_forecast  = int(math.ceil(asales_forecast ))

acogs_sales_baseline = (cog_sold_baseline / sales_baseline) * 100
cogs_sales_baseline = round(acogs_sales_baseline, 1)


acog_sold_forecast = sales_forecast * cogs_sales_baseline
#print("Initial COGS (using baseline):", cog_sold_forecast)  # Should use baseline (0.15)

# If there's an explicit switch to using the forecast, update cog_sold_forecast
use_forecast = True  # Set to True only when you want to use cogs_sales_forecast

if use_forecast:
    acog_sold_forecast = sales_forecast * cogs_sales_forecast 

cog_sold_forecast = math.floor(acog_sold_forecast)

#cog_sold_forecast =  sales_forecast * cogs_sales_baseline
#cog_sold_forecast = sales_forecast * cogs_sales_forecast
#cog_sold_forecast = sales_forecast * year_over_forecast
#cog_sold_forecast = math.floor(acog_sold_forecast)  # Rounds down to the nearest thousand

agross_profit_forecast = sales_forecast - acog_sold_forecast
gross_profit_forecast = round(agross_profit_forecast)

agross_margin_forecast = gross_profit_forecast / sales_forecast 
gross_margin_forecast = round(agross_margin_forecast * 100,1) # Converts 0.133 to 13.3

final_output = dict()
final_output["sales_forecast"] = sales_forecast
final_output["cog_sold_forecast"] = cog_sold_forecast
final_output["gross_profit_forecast"] = gross_profit_forecast
final_output["gross_margin_forecast"] = gross_margin_forecast
final_output["cogs_sales_baseline"] = cogs_sales_baseline

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

%%response%% = final_output

