units_sold_daily = float($$request["units_sold_daily"])
var_cost_per_unit = float($$result[16]["field_value"])
fix_cost_per_month = int($$result[22]["field_value"])    
fix_cost_per_quarter = int($$result[23]["field_value"])
fix_cost_per_year = int($$result[24]["field_value"])

units_sold_monthly = units_sold_daily  * 30

units_sold_quarterly = units_sold_daily  * 90

units_sold_yearly = units_sold_quarterly * 3

var_cost_per_month = units_sold_monthly * var_cost_per_unit 

var_cost_per_quarter = units_sold_quarterly * var_cost_per_unit 

var_cost_per_year = var_cost_per_quarter * 3

fix_cost_per_unit = round(fix_cost_per_quarter / units_sold_quarterly, 2) if units_sold_quarterly != 0 else 0

total_cost_per_unit = round(fix_cost_per_unit +  var_cost_per_unit,2)

total_cost_per_month = var_cost_per_month + fix_cost_per_month

total_cost_per_quarter = fix_cost_per_quarter + var_cost_per_quarter

total_cost_per_year = fix_cost_per_year + var_cost_per_year

final_output = dict()
final_output["units_sold_monthly"]=units_sold_monthly
final_output["units_sold_quarterly"]=units_sold_quarterly
final_output["units_sold_yearly"]=units_sold_yearly
final_output["var_cost_per_month"]=var_cost_per_month
final_output["var_cost_per_quarter"]=var_cost_per_quarter
final_output["var_cost_per_year"]=var_cost_per_year
final_output["fix_cost_per_unit"]=fix_cost_per_unit
final_output["total_cost_per_unit"]=total_cost_per_unit
final_output["total_cost_per_month"]=total_cost_per_month
final_output["total_cost_per_quarter"]=total_cost_per_quarter
final_output["total_cost_per_year"]=total_cost_per_year

final_output["var_cost_per_unit"] = $$result[16]["field_value"]
final_output["fix_cost_per_month"] = $$result[22]["field_value"]
final_output["fix_cost_per_quarter"] = $$result[23]["field_value"]
final_output["fix_cost_per_year"] = $$result[24]["field_value"]

%%response%% = final_output




[
  {
    "$match": {
      "toolkit": "Toolkit4"
    }
  },
  {
    "$project": {
       "field_name" : 1,
       "field_value" : 1,
       "_id": 0
    }
  }
]













units_sold_daily = float($$request["units_sold_daily"])
var_cost_per_unit = float($$request["var_cost_per_unit"])
fix_cost_per_month = int($$request["fix_cost_per_month"])    
fix_cost_per_quarter = int($$request["fix_cost_per_quarter"])
fix_cost_per_year = int($$request["fix_cost_per_year"])

units_sold_monthly = units_sold_daily  * 30

units_sold_quarterly = units_sold_daily  * 90

units_sold_yearly = units_sold_quarterly * 3

var_cost_per_month = units_sold_monthly * var_cost_per_unit 

var_cost_per_quarter = units_sold_quarterly * var_cost_per_unit 

var_cost_per_year = var_cost_per_quarter * 3

fix_cost_per_unit = round(fix_cost_per_quarter / units_sold_quarterly, 2) if units_sold_quarterly != 0 else 0

total_cost_per_unit = round(fix_cost_per_unit +  var_cost_per_unit,2)

total_cost_per_month = var_cost_per_month + fix_cost_per_month

total_cost_per_quarter = fix_cost_per_quarter + var_cost_per_quarter

total_cost_per_year = fix_cost_per_year + var_cost_per_year

final_output = dict()
final_output["units_sold_monthly"]=units_sold_monthly
final_output["units_sold_quarterly"]=units_sold_quarterly
final_output["units_sold_yearly"]=units_sold_yearly
final_output["var_cost_per_month"]=var_cost_per_month
final_output["var_cost_per_quarter"]=var_cost_per_quarter
final_output["var_cost_per_year"]=var_cost_per_year
final_output["fix_cost_per_unit"]=fix_cost_per_unit
final_output["total_cost_per_unit"]=total_cost_per_unit
final_output["total_cost_per_month"]=total_cost_per_month
final_output["total_cost_per_quarter"]=total_cost_per_quarter
final_output["total_cost_per_year"]=total_cost_per_year


final_output["lesson_header"] = $$request["lesson_header"]
final_output["daily"] = $$request["daily"]
final_output["monthly"] = $$request["monthly"]
final_output["quarterly"] = $$request["quarterly"]
final_output["yearly"] = $$request["yearly"]
final_output["units_sold"] = $$request["units_sold"]
final_output["cost_of_goods"] = $$request["cost_of_goods"]
final_output["per_unit"] = $$request["per_unit"]
final_output["per_month"] = $$request["per_month"]
final_output["per_quarter"] = $$request["per_quarter"]
final_output["per_year"] = $$request["per_year"]
final_output["variable_costs"] = $$request["variable_costs"]
final_output["var_cost_per_unit"] = $$request["var_cost_per_unit"]
final_output["fixed_costs"] = $$request["fixed_costs"]
final_output["fix_cost_per_month"] = $$request["fix_cost_per_month"]
final_output["fix_cost_per_quarter"] = $$request["fix_cost_per_quarter"]
final_output["fix_cost_per_year"] = $$request["fix_cost_per_year"]
final_output["total_costs"] = $$request["total_costs"]

%%response%% = final_output
