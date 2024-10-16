#  >>>>>>>>>Original Toolkit 1 Code>>>>>>>>>>>>>

ownership_value = int($$request["ownership_value"])
shares_value = int($$request["shares_value"])
price_value = int($$request["price_value"])

market_value = shares_value * price_value

ownership_decimal = ownership_value / 100

shares_owned = ownership_decimal * shares_value 

total_amount_value = shares_owned * price_value

final_output = dict()
final_output["market_value"]=market_value
final_output["shares_owned"]=shares_owned
final_output["total_amount_value"]=total_amount_value
final_output["lesson_header"] = $$request["lesson_header"]
final_output["company"] = $$request["company"]
final_output["company_name"] = $$request["company_name"]
final_output["shares"] = $$request["shares"]
final_output["total_amount"] = $$request["total_amount"]
final_output["symbol"] = $$request["symbol"]
final_output["baseline"] = $$request["baseline"]
final_output["symbol_name"] = $$request["symbol_name"]
final_output["baseline_value"] = $$request["baseline_value"]
final_output["price"] = $$request["price"]
final_output["ownership"] = $$request["ownership"]
final_output["share_calculator"] = $$request["share_calculator"]
final_output["shares1"] = $$request["shares1"]
final_output["shares_value"] = $$request["shares_value"]
final_output["price_value"] = $$request["price_value"]

%%calculated%% = final_output 

