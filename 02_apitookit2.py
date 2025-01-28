sales_value = float($$request["sales_value"])
expenses_value = float($$request["expenses_value"])
shares_out_value = int($$result[9]["field_value"])
market_p_value = int($$result[10]["field_value"])

market_v_price = shares_out_value * market_p_value

quarterly_c_flow_value = sales_value - expenses_value

acfrr_value = quarterly_c_flow_value * 4

cash_f_v_value = acfrr_value * 25

cash_f_v_p_s_value = cash_f_v_value / shares_out_value      

implied_return_float = cash_f_v_p_s_value / market_p_value - 1
implied_return_value = round(implied_return_float * 100)

final_output = dict()
final_output["market_v_price"] = market_v_price
final_output["quarterly_c_flow_value"] = quarterly_c_flow_value
final_output["acfrr_value"] = acfrr_value
final_output["cash_f_v_value"] = cash_f_v_value
final_output["cash_f_v_p_s_value"] = cash_f_v_p_s_value
final_output["implied_return_value"] = implied_return_value

final_output["shares_out_value"] = $$result[9]["field_value"]
final_output["market_p_value"] = $$result[10]["field_value"]

%%calculate%% = final_output 






#>>>>>>>>>>Original Code Toolkit 2>>>>>>>>>>

shares_out_value = int($$request["shares_out_value"])
market_p_value = int($$request["market_p_value"])
sales_value = float($$request["sales_value"])
expenses_value = float($$request["expenses_value"])


market_v_price = shares_out_value * market_p_value

quarterly_c_flow_value = sales_value - expenses_value

acfrr_value = quarterly_c_flow_value * 4

cash_f_v_value = acfrr_value * 25

cash_f_v_p_s_value = cash_f_v_value / shares_out_value      

implied_return_float = cash_f_v_p_s_value / market_p_value - 1
implied_return_value = round(implied_return_float * 100)


final_output = dict()
final_output["market_v_price"] = market_v_price
final_output["quarterly_c_flow_value"] = quarterly_c_flow_value
final_output["acfrr_value"] = acfrr_value
final_output["cash_f_v_value"] = cash_f_v_value
final_output["cash_f_v_p_s_value"] = cash_f_v_p_s_value
final_output["implied_return_value"] = implied_return_value
final_output["lesson_header"] = $$request["lesson_header"]
final_output["company"] = $$request["company"]
final_output["company_name"] = $$request["company_name"]
final_output["latest"] = $$request["latest"]
final_output["latest_value"] = $$request["latest_value"]
final_output["symbol"] = $$request["symbol"]
final_output["shares_outstanding"] = $$request["shares_outstanding"]
final_output["shares_out_value"] = $$request["shares_out_value"]
final_output["market_price"] = $$request["market_price"]
final_output["market_p_value"] = $$request["market_p_value"]
final_output["market_value"] = $$request["market_value"]
final_output["quarterly_income_statement"] = $$request["quarterly_income_statement"]
final_output["sales"] = $$request["sales"]
final_output["baseline"] = $$request["baseline"]
final_output["expenses"] = $$request["expenses"]
final_output["quarterly_cash_flow"] = $$request["quarterly_cash_flow"]
final_output["annual_cash_run_rate"] = $$request["annual_cash_run_rate"]
final_output["cash_flow_value"] = $$request["cash_flow_value"]
final_output["cash_flow_value_per_share"] = $$request["cash_flow_value_per_share"]
final_output["implied_return"] = $$request["implied_return"]

%%calculate%% = final_output 