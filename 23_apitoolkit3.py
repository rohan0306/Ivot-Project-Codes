import math
units_two = float($$request["units_two"])
sale_four = float($$request["sale_four"])               
unit_one = int($$final_result[10]["field_value"])
sale_one = float($$final_result[11]["field_value"])
units_one = int($$final_result[12]["field_value"])
day_two = int($$final_result[15]["field_value"])
day_three = int($$final_result[21]["field_value"])
day_four = int($$final_result[27]["field_value"])
day_five = int($$final_result[33]["field_value"])

sales_one = float(sale_one * units_one)
aunit_two = sale_four / day_four / sale_one
unit_two = math.ceil(aunit_two)
asale_two = aunit_two * sale_one
sale_two = math.ceil(asale_two)
sales_two = units_two * sales_one
aunit_three = day_three * aunit_two
unit_three = int(aunit_three)
#unit_three = math.ceil(aunit_three)
asale_three = aunit_three * sale_one
sale_three = math.ceil(asale_three)
units_three = day_three * units_two
sales_three = units_three * sales_one
unit_four =  int(day_four * aunit_two)
#unit_four = math.ceil(aunit_four)
units_four = day_four * units_two
sales_four = units_four * sales_one
unit_five = int(day_five * aunit_two)
#unit_five = math.ceil(aunit_five)
asale_five = unit_five * sale_one
sale_five = math.ceil(asale_five)
units_five = day_five * units_two
sales_five = units_five * sales_one 

final_output = dict()
final_output["sales_one"]=sales_one
final_output["unit_two"]=unit_two
final_output["sale_two"]=sale_two
final_output["sales_two"]=sales_two
final_output["unit_three"]=unit_three
final_output["sale_three"]=sale_three
final_output["units_three"]=units_three
final_output["sales_three"]=sales_three
final_output["unit_four"]=unit_four
final_output["units_four"]=units_four
final_output["sales_four"]=sales_four
final_output["unit_five"]=unit_five
final_output["sale_five"]=sale_five
final_output["units_five"]=units_five
final_output["sales_five"]=sales_five

final_output["unit_one"] = $$final_result[10]["field_value"]
final_output["sale_one"] = $$final_result[11]["field_value"]
final_output["units_one"] = $$final_result[12]["field_value"]
final_output["day_two"] = $$final_result[15]["field_value"]
final_output["day_three"] = $$final_result[21]["field_value"]
final_output["day_four"] = $$final_result[27]["field_value"]
final_output["day_five"] = $$final_result[33]["field_value"]

%%result%% = final_output






import math
units_two = int($$request["units_two"])
sale_four = int($$request["sale_four"])               
unit_one = int($$request["unit_one"])
sale_one = float($$request["sale_one"])
units_one = int($$request["units_one"])
day_two = int($$request["day_two"])
day_three = int($$request["day_three"])
day_four = int($$request["day_four"])
day_five = int($$request["day_five"])

sales_one = float(sale_one * units_one)
aunit_two = sale_four / day_four / sale_one
unit_two = math.ceil(aunit_two)
asale_two = aunit_two * sale_one
sale_two = math.ceil(asale_two)
sales_two = units_two * sales_one
aunit_three = day_three * aunit_two
unit_three = int(aunit_three)
#unit_three = math.ceil(aunit_three)
asale_three = aunit_three * sale_one
sale_three = math.ceil(asale_three)
units_three = day_three * units_two
sales_three = units_three * sales_one
unit_four =  int(day_four * aunit_two)
#unit_four = math.ceil(aunit_four)
units_four = day_four * units_two
sales_four = units_four * sales_one
unit_five = int(day_five * aunit_two)
#unit_five = math.ceil(aunit_five)
asale_five = unit_five * sale_one
sale_five = math.ceil(asale_five)
units_five = day_five * units_two
sales_five = units_five * sales_one 

final_output = dict()
final_output["sales_one"]=sales_one
final_output["unit_two"]=unit_two
final_output["sale_two"]=sale_two
final_output["sales_two"]=sales_two
final_output["unit_three"]=unit_three
final_output["sale_three"]=sale_three
final_output["units_three"]=units_three
final_output["sales_three"]=sales_three
final_output["unit_four"]=unit_four
final_output["units_four"]=units_four
final_output["sales_four"]=sales_four
final_output["unit_five"]=unit_five
final_output["sale_five"]=sale_five
final_output["units_five"]=units_five
final_output["sales_five"]=sales_five

final_output["lesson_header"] = $$request["lesson_header"]
final_output["company_name"] = $$request["company_name"]
final_output["year"] = $$request["year"]
final_output["baseline"] = $$request["baseline"]
final_output["day"] = $$request["day"]
final_output["unit"] = $$request["unit"]
final_output["sale"] = $$request["sale"]
final_output["units"] = $$request["units"]
final_output["sales"] = $$request["sales"]
final_output["avg"] = $$request["avg"]
final_output["unit_one"] = $$request["unit_one"]
final_output["sale_one"] = $$request["sale_one"]
final_output["units_one"] = $$request["units_one"]
final_output["per_day"] = $$request["per_day"]
final_output["day_two"] = $$request["day_two"]
final_output["units_two"] = $$request["units_two"]
final_output["per_month"] = $$request["per_month"]
final_output["day_three"] = $$request["day_three"]
final_output["per_quarter"] = $$request["per_quarter"]
final_output["day_four"] = $$request["day_four"]
final_output["sale_four"]= $$request["sale_four"]
final_output["per_year"] = $$request["per_year"]
final_output["day_five"] = $$request["day_five"]

%%result%% = final_output
