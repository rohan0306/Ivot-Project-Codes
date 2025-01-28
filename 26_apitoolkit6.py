shares_outstanding_one_value = int($$result[6]["field_value"])
market_price_value = int($$result[8]["field_value"])  
sales_value = int($$result[12]["field_value"])
cogs_value = int($$result[14]["field_value"])  
sales_market_value = int($$result[18]["field_value"])
general_value = int($$result[20]["field_value"])  
depre_value = int($$result[26]["field_value"])  
shares_outstanding_value = int($$result[34]["field_value"])                           

gross_profit_value = sales_value - cogs_value

operating_value = gross_profit_value - sales_market_value - general_value

tax_value = operating_value * 0.21

ocf_value = operating_value - tax_value + depre_value

annual_ocf_value = ocf_value * 4

baseline_v_value = annual_ocf_value * 25

baseline_per_share = int(baseline_v_value / shares_outstanding_value)

final_output = dict()
final_output["gross_profit_value"] =gross_profit_value
final_output["operating_value"]=operating_value
final_output["tax_value"]=tax_value
final_output["ocf_value"]=ocf_value
final_output["annual_ocf_value"]=annual_ocf_value
final_output["baseline_v_value"]=baseline_v_value
final_output["baseline_per_share"]=baseline_per_share

final_output["shares_outstanding_one_value"] = $$result[6]["field_value"]
final_output["shares_outstanding_value"] = $$result[34]["field_value"]
final_output["market_price_value"] = $$result[8]["field_value"]
final_output["sales_value"] = $$result[12]["field_value"]
final_output["cogs_value"] = $$result[14]["field_value"]
final_output["sales_market_value"] = $$result[18]["field_value"]
final_output["general_value"] = $$result[20]["field_value"]
final_output["depre_value"] = $$result[26]["field_value"]

%%calculate%% = final_output


[{
    "$match": {
      "toolkit": "Toolkit6"
    }
},
{
    "$project": {
        "field_name": 1,
        "field_value": 1,
        "_id": 0
    }
}]










shares_outstanding_one_value = int($$request["shares_outstanding_one_value"])
market_price_value = int($$request["market_price_value"])  
sales_value = int($$request["sales_value"])
cogs_value = int($$request["cogs_value"])  
sales_market_value = int($$request["sales_market_value"])
general_value = int($$request["general_value"])  
depre_value = int($$request["depre_value"])  
shares_outstanding_value = int($$request["shares_outstanding_value"])                           

gross_profit_value = sales_value - cogs_value

operating_value = gross_profit_value - sales_market_value - general_value

tax_value = operating_value * 0.21

ocf_value = operating_value - tax_value + depre_value

annual_ocf_value = ocf_value * 4

baseline_v_value = annual_ocf_value * 25

baseline_per_share = int(baseline_v_value / shares_outstanding_value)

final_output = dict()
final_output["gross_profit_value"] =gross_profit_value
final_output["operating_value"]=operating_value
final_output["tax_value"]=tax_value
final_output["ocf_value"]=ocf_value
final_output["annual_ocf_value"]=annual_ocf_value
final_output["baseline_v_value"]=baseline_v_value
final_output["baseline_per_share"]=baseline_per_share

final_output["lesson_header"] = $$request["lesson_header"]
final_output["company"] = $$request["company"]
final_output["company_name"] = $$request["company_name"]
final_output["symbol"] = $$request["symbol"]
final_output["symbol_name"] = $$request["symbol_name"]
final_output["shares_outstanding_one"] = $$request["shares_outstanding_one"]
final_output["shares_outstanding_one_value"] = $$request["shares_outstanding_one_value"]
final_output["market_price"] = $$request["market_price"]
final_output["market_price_value"] = $$request["market_price_value"]
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
final_output["baseline_value"] = $$request["baseline_value"]
final_output["shares_outstanding"] = $$request["shares_outstanding"]
final_output["shares_outstanding_value"] = $$request["shares_outstanding_value"]
final_output["baseline_value_per_share"] = $$request["baseline_value_per_share"]

%%calculate%% = final_output
