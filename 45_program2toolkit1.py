[{
    "$match": {
        "toolkit": "Program2Toolkit1"
    }
},
{
    "$project": {
        "field_name": 1,
        "field_value": 1,
        "_id": 0
    }
}]


#analyst_name = str($$request["analyst_name"])
market_px_value = int($$request["market_px_value"])
shares_value = int($$request["shares_value"])
                                    
market_cap_value = market_px_value * shares_value

final_output = dict()
final_output["market_cap_value"]=market_cap_value

final_output["lesson_header"] = $$request["lesson_header"]
final_output["ivot_forecaster"] = $$request["ivot_forecaster"]
final_output["name"] = $$request["name"]
final_output["symbol"] = $$request["symbol"]
final_output["latest"] = $$request["latest"]
final_output["next_report"] = $$request["next_report"]
final_output["company_name"] = $$request["company_name"]
final_output["symbol_name"] = $$request["symbol_name"]
final_output["latest_value"] = $$request["latest_value"]
final_output["next_report_value"] = $$request["next_report_value"]
final_output["analyst"] = $$request["analyst"]
final_output["shares"] = $$request["shares"]
final_output["market_px"] = $$request["market_px"]
final_output["market_cap"] = $$request["market_cap"]
#final_output["analyst_name"] = $$request["analyst_name"]
final_output["shares_value"] = $$request["shares_value"]
final_output["market_px_value"] = $$request["market_px_value"]

%%calculated%% = final_output 
