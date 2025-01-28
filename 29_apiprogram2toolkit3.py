import math
year_over_forecast = float($$request["year_over_forecast"]) / 100
sales_year = int($$result[25]["field_value"])
sales_baseline = int($$result[26]["field_value"])
#year_over_baseline = float($$result[29]["field_value"])

ayear_over_baseline = (sales_baseline / sales_year - 1) * 100
year_over_baseline = round(ayear_over_baseline, 1)
asales_forecast = sales_baseline * (1 + year_over_forecast) ** 3
sales_forecast  = int(math.ceil(asales_forecast ))

final_output = dict()
final_output["sales_forecast"] = sales_forecast
final_output["year_over_baseline"] = year_over_baseline

final_output["sales_year"] = $$result[25]["field_value"]
final_output["sales_baseline"] = $$result[26]["field_value"]

%%response%% = final_output


[{
    "$match": {
        "toolkit": "Program2Toolkit3"
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
sales_year = int($$request["sales_year"])
sales_baseline = int($$request["sales_baseline"])
year_over_baseline = float($$request["year_over_baseline"])

#year_over_baseline = sales_baseline / sales_year - 1
asales_forecast = sales_baseline * (1 + year_over_forecast) ** 3
sales_forecast  = int(math.ceil(asales_forecast ))

final_output = dict()
final_output["sales_forecast"] = sales_forecast
final_output["year_over_baseline"] = year_over_baseline
final_output["sales_year"] = $$request["sales_year"]
final_output["sales_baseline"] = $$request["sales_baseline"]
final_output["year_over_baseline"] = $$request["year_over_baseline"]

%%response%% = final_output
