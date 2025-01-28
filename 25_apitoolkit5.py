import math
com_value = float($$request["com_value"])
expected_value = float($$request["expected_value"])              
sales_value = int($$result[4]["field_value"])
cogs_value = int($$result[6]["field_value"])
sales_market_value = int($$result[10]["field_value"])
general_value = int($$result[12]["field_value"])
depre_value = int($$result[18]["field_value"])

gross_profit_value = sales_value - cogs_value

operating_value = gross_profit_value - sales_market_value - general_value

tax_value = operating_value * 0.21

ocf_value = operating_value - tax_value + depre_value

monthly_value = 0
amonthly_value = 0

if com_value == 0 or expected_value == 0:
    
    monthly_value = 0  
else:
    
    amonthly_value = com_value / expected_value  
    monthly_value = math.ceil(amonthly_value)


#amonthly_value = com_value / expected_value
#monthly_value = math.ceil(amonthly_value)

aquarterly_value = amonthly_value * 3
quarterly_value = math.ceil(aquarterly_value)

final_output = dict()
final_output["gross_profit_value"]=gross_profit_value
final_output["operating_value"]=operating_value
final_output["tax_value"]=tax_value
final_output["ocf_value"]=ocf_value
final_output["monthly_value"]=monthly_value
final_output["quarterly_value"]=quarterly_value

final_output["sales_value"] = $$result[4]["field_value"]
final_output["cogs_value"] = $$result[6]["field_value"]
final_output["sales_market_value"] = $$result[10]["field_value"]
final_output["general_value"] = $$result[12]["field_value"]
final_output["depre_value"] = $$result[18]["field_value"]

%%calculate%% = final_output


[
  {
    "$match": {
      "toolkit": "Toolkit5"
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







import math
com_value = float($$request["com_value"])
expected_value = float($$request["expected_value"])              
sales_value = int($$request["sales_value"])
cogs_value = int($$request["cogs_value"])
sales_market_value = int($$request["sales_market_value"])
general_value = int($$request["general_value"])
depre_value = int($$request["depre_value"])

gross_profit_value = sales_value - cogs_value

operating_value = gross_profit_value - sales_market_value - general_value

tax_value = operating_value * 0.21

ocf_value = operating_value - tax_value + depre_value

monthly_value = 0
amonthly_value = 0

if com_value == 0 or expected_value == 0:
    
    monthly_value = 0  
else:
    
    amonthly_value = com_value / expected_value  
    monthly_value = math.ceil(amonthly_value)


#amonthly_value = com_value / expected_value
#monthly_value = math.ceil(amonthly_value)

aquarterly_value = amonthly_value * 3
quarterly_value = math.ceil(aquarterly_value)

final_output = dict()
final_output["gross_profit_value"]=gross_profit_value
final_output["operating_value"]=operating_value
final_output["tax_value"]=tax_value
final_output["ocf_value"]=ocf_value
final_output["monthly_value"]=monthly_value
final_output["quarterly_value"]=quarterly_value

final_output["lesson_header"] = $$request["lesson_header"]
final_output["quarterly_income_statement"] = $$request["quarterly_income_statement"]
final_output["baseline"] = $$request["baseline"]
final_output["sales"] = $$request["sales"]
final_output["sales_value"] = $$request["sales_value"]
final_output["cogs"] = $$request["cogs"]
final_output["cogs_value"] = $$request["cogs_value"]
final_output["gross_profit"] = $$request["gross_profit"]
final_output["sales_market"] = $$request["sales_market"]
final_output["sales_market_value"] = $$request["sales_market_value"]
final_output["general"] = $$request["general"]
final_output["general_value"] = $$request["general_value"]
final_output["operating"] = $$request["operating"]
final_output["tax"] = $$request["tax"]
final_output["depre"] = $$request["depre"]
final_output["depre_value"] = $$request["depre_value"]
final_output["ocf"] = $$request["ocf"]
final_output["calculator"] = $$request["calculator"]
final_output["com"] = $$request["com"]
final_output["com_value"] = $$request["com_value"]
final_output["expected"] = $$request["expected"]
final_output["expected_value"] = $$request["expected_value"]
final_output["monthly"] = $$request["monthly"]
final_output["quarterly"] = $$request["quarterly"]

%%calculate%% = final_output
