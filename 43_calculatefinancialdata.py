#Calculate Financial Data Original Logic as 1 	January 2025 only accept csv as a input 

import pandas as pd
import numpy as np
import json

# Load the data into a DataFrame

# Check if cache["request"] is already a dictionary or needs to be parsed
if isinstance(cache["request"], str):
    request = json.loads(cache["request"])  # Parse the string into a dictionary
else:
    request = cache["request"]  # Use it directly as it's already a dictionary

df = pd.DataFrame(request)

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(0, inplace=True)


df = df[df['asset_class'].notnull() & (df['asset_class'].str.strip() != '')]

#df = pd.DataFrame(data)

# Shift sales values by four quarters back (one year)
df['Sales_Last_Year'] = df['Total_Sales_m'].shift(4).fillna(0)

# Calculate YOY Growth
df['Growth_rate__YOY'] = np.where(
    df['Sales_Last_Year'] != 0,
    (df['Total_Sales_m'] / df['Sales_Last_Year']) - 1,
    0
)
# Calculate Store_Operating_Expenses__of_Sales
df['Store_Operating_Expenses__of_Sales'] = df['Store_Operating_Expenses_m'] / df['Total_Sales_m']
#df['Store_Operating_Expenses__of_Sales'] = (df['Store_Operating_Expenses__of_Sales_raw'] * 100).round(1)

# Calculate Product_and_Distribution_Costs__of_Sales
df['Product_and_Distribution_Costs__of_Sales'] = df['Product_and_Distribution_Costs_m'] / df['Total_Sales_m']
#df['Product_and_Distribution_Costs__of_Sales'] = (df['Product_and_Distribution_Costs__of_Sales_raw'] * 100).round(1)

# Calculate Total_CostofGoods_m
df['Total_CostofGoods_m'] = df['Store_Operating_Expenses_m'] + df['Product_and_Distribution_Costs_m'] + df['Depreciation_and_Amortization_Expenses_m']
#df['Total_CostofGoods_m'] = (df['Total_CostofGoods_m_raw'] * 100 / 100).round().astype(int)


df['Total_CostofGoods_m'] = pd.to_numeric(df['Total_CostofGoods_m'], errors='coerce')
df['Total_Sales_m'] = pd.to_numeric(df['Total_Sales_m'], errors='coerce')

# Calculate Product_and_Distribution_Costs__of_Sales
df['COGS__of_sales_raw'] = df['Total_CostofGoods_m'] / df['Total_Sales_m']
df['COGS__of_sales'] = (df['COGS__of_sales_raw'] * 100).round(1)


# Convert columns to numeric, handling any non-numeric values by setting them as NaN
df['Total_Sales_m'] = pd.to_numeric(df['Total_Sales_m'], errors='coerce')
df['Total_CostofGoods_m'] = pd.to_numeric(df['Total_CostofGoods_m'], errors='coerce')

# Calculate Gross Profit (Total Sales - Cost of Goods)
df['Total_Gross_Profit_m'] = df['Total_Sales_m'] - df['Total_CostofGoods_m']

# Calculate the percentage and round the result
#df['Total_Gross_Profit_m'] = (df['Total_Gross_Profit_m_raw'] * 100 / 100).round().astype(int)


df['Total_Gross_Profit_m'] = pd.to_numeric(df['Total_Gross_Profit_m'], errors='coerce')
df['Total_Sales_m'] = pd.to_numeric(df['Total_Sales_m'], errors='coerce')

# Calculate Product_and_Distribution_Costs__of_Sales
df['Gross_Margin__of_Sales'] = df['Total_Gross_Profit_m'] / df['Total_Sales_m']
#df['Gross_Margin__of_Sales'] = (df['Gross_Margin__of_Sales_raw'] * 100).round(1)

df['SM__of_Sales'] = df['Selling__Marketing_m'] / df['Total_Sales_m']

df['RD__of_Sales'] = df['Research__Development_m'] / df['Total_Sales_m']

df['General__Administrative_m'] = pd.to_numeric(df['General__Administrative_m'], errors='coerce')
df['Total_Sales_m'] = pd.to_numeric(df['Total_Sales_m'], errors='coerce')

# Calculate Product_and_Distribution_Costs__of_Sales
df['GA__of_Sales'] = df['General__Administrative_m'] / df['Total_Sales_m']
#df['GA__of_Sales'] = (df['GA__of_Sales_raw'] * 100).round(1)

df['Other_m'] = pd.to_numeric(df['Other_m'], errors='coerce')
df['Total_Sales_m'] = pd.to_numeric(df['Total_Sales_m'], errors='coerce')

# Calculate Product_and_Distribution_Costs__of_Sales
df['Other__of_Sales'] = df['Other_m'] / df['Total_Sales_m']
#df['Other__of_Sales'] = (df['Other__of_Sales_raw'] * 100).round(1)

df['Total_Gross_Profit_m'] = pd.to_numeric(df['Total_Gross_Profit_m'], errors='coerce')
df['General__Administrative_m'] = pd.to_numeric(df['General__Administrative_m'], errors='coerce')
df['Selling__Marketing_m'] = pd.to_numeric(df['Selling__Marketing_m'], errors='coerce')
df['Research__Development_m'] = pd.to_numeric(df['Research__Development_m'], errors='coerce')
df['Other_m'] = pd.to_numeric(df['Other_m'], errors='coerce')

# Calculate Total_CostofGoods_m
df['Operating_Profit_m'] = df['Total_Gross_Profit_m'] - df['General__Administrative_m'] - df['Selling__Marketing_m'] - df['Research__Development_m'] - df['Other_m']
#df['Operating_Profit_m'] = (df['Operating_Profit_m_raw'] * 100 / 100).round().astype(int)


# Calculate Product_and_Distribution_Costs__of_Sales
df['Operating_Margin__of_Sales'] = df['Operating_Profit_m'] / df['Total_Sales_m']
#df['Operating_Margin__of_Sales'] = (df['Operating_Margin__of_Sales_raw'] * 100).round(1)


# Calculate Product_and_Distribution_Costs__of_Sales
df['Taxes_21'] = df['Operating_Profit_m'] * 0.21
#df['Taxes_21'] = (df['Taxes_21_raw']* 100 / 100).round().astype(int)


# Convert all columns to numeric, handling non-numeric values
# Ensure columns are numeric, converting non-numeric values to NaN
df[['Operating_Profit_m', 'Taxes_21', 'Depreciation_m']] = df[['Operating_Profit_m', 'Taxes_21', 'Depreciation_m']].apply(pd.to_numeric, errors='coerce')

# Calculate the raw cash flow values
df['Quarterly_Operating_Cash_Flow_m'] = df['Operating_Profit_m'] - df['Taxes_21'] + df['Depreciation_m']


# Ensure columns are numeric
df['Quarterly_Operating_Cash_Flow_m'] = pd.to_numeric(df['Quarterly_Operating_Cash_Flow_m'], errors='coerce')

# Shift sales values by four quarters back (one year)
df['Sales_Current_Year'] = df['Quarterly_Operating_Cash_Flow_m'].shift(4).fillna(0)

# Calculate YOY Growth
df['Percent_Change'] = np.where(
    df['Sales_Current_Year'] != 0,
    (df['Quarterly_Operating_Cash_Flow_m'] / df['Sales_Last_Year']) - 1,
    0
)

# Calculate Product_and_Distribution_Costs__of_Sales
df['Annualized_OCF_m'] = df['Quarterly_Operating_Cash_Flow_m'] * 4


# Calculate Total_CostofGoods_m
df['Net_Cash_m'] = df['Cash_and_Cash_Equivalents_m'] + df['Longterm_Investments_m'] - df['Longterm_Debt_m']
#df['Net_Cash_m'] = (df['Net_Cash_m_raw'] * 100 / 100).round().astype(int)

# Calculate Product_and_Distribution_Costs__of_Sales
df['Perpetuity_Value_4_raw'] = df['Annualized_OCF_m'] / 0.4
df['Perpetuity_Value_4'] = df['Perpetuity_Value_4_raw']* 100 / 10


df['Net_Cash_m1'] = df['Net_Cash_m'] 


# Ensure that the values are numeric
df['Perpetuity_Value_4'] = pd.to_numeric(df['Perpetuity_Value_4'], errors='coerce')
#df['Net_Cash_m_raw'] = pd.to_numeric(df['Net_Cash_m_raw'], errors='coerce')

# Calculate Enterprise Value dynamically for each row
df['Enterprise_Value_m'] = df['Perpetuity_Value_4'] + df['Net_Cash_m1']
#df['Enterprise_Value_m'] = (df['Enterprise_Value_m_raw']* 100 / 10).round().astype(int)

# Ensure that the columns are numeric
df['Enterprise_Value_m'] = pd.to_numeric(df['Enterprise_Value_m'], errors='coerce')
df['Fully_diluted_shares_outstanding_m'] = pd.to_numeric(df['Fully_diluted_shares_outstanding_m'], errors='coerce')

# Perform the division for Implied Value Per Share
df['Implied_Value_Per_Share_raw'] = df['Enterprise_Value_m'] / df['Fully_diluted_shares_outstanding_m']
df['Implied_Value_Per_Share_raw'] = df['Implied_Value_Per_Share_raw'].where(df['Fully_diluted_shares_outstanding_m'] != 0, 0)
df['Implied_Value_Per_Share'] = (df['Implied_Value_Per_Share_raw'] * 100) / 100


final_output = dict()

final_output["SM__of_Sales"] = df['SM__of_Sales'].tolist()
final_output["RD__of_Sales"] = df['RD__of_Sales'].tolist()

final_output["Growth_rate__YOY"] = df['Growth_rate__YOY'].tolist()
final_output["Store_Operating_Expenses__of_Sales"] = df['Store_Operating_Expenses__of_Sales'].tolist()
final_output["Product_and_Distribution_Costs__of_Sales"] = df['Product_and_Distribution_Costs__of_Sales'].tolist()
final_output["Total_CostofGoods_m"] = df['Total_CostofGoods_m'].tolist()
final_output["COGS__of_sales"] = df['COGS__of_sales'].tolist()
final_output["Total_Gross_Profit_m"] = df['Total_Gross_Profit_m'].tolist()
final_output["Gross_Margin__of_Sales"] = df['Gross_Margin__of_Sales'].tolist()
final_output["GA__of_Sales"] = df['GA__of_Sales'].tolist()
final_output["Other__of_Sales"] = df['Other__of_Sales'].tolist()
final_output["Operating_Profit_m"] = df['Operating_Profit_m'].tolist()
final_output["Operating_Margin__of_Sales"] = df['Operating_Margin__of_Sales'].tolist()
final_output["Taxes_21"] = df['Taxes_21'].tolist()
final_output["Quarterly_Operating_Cash_Flow_m"] = df['Quarterly_Operating_Cash_Flow_m'].tolist()
final_output["Percent_Change"] = df['Percent_Change'].tolist()
final_output["Annualized_OCF_m"] = df['Annualized_OCF_m'].tolist()
final_output["Net_Cash_m"] = df['Net_Cash_m'].tolist()
final_output["Perpetuity_Value_4"] = df['Perpetuity_Value_4'].tolist()
final_output["Net_Cash_m1"] = df['Net_Cash_m1'].tolist()
final_output["Enterprise_Value_m"] = df['Enterprise_Value_m'].tolist()
final_output["Implied_Value_Per_Share"] = df['Implied_Value_Per_Share'].tolist()

result = [ '_id', 'asset_class', 'Financial_Term', 'Total_Sales_m',
'Store_Operating_Expenses_m', 'Product_and_Distribution_Costs_m', 
'Depreciation_and_Amortization_Expenses_m',
    'General__Administrative_m', 'Other_m', 'Depreciation_m', 'Cash_and_Cash_Equivalents_m', 'Longterm_Investments_m', 'Longterm_Debt_m', 'Fully_diluted_shares_outstanding_m',
'Growth_rate__YOY', 'Store_Operating_Expenses__of_Sales', 
    'Product_and_Distribution_Costs__of_Sales','Total_CostofGoods_m','COGS__of_sales','Total_Gross_Profit_m','Gross_Margin__of_Sales',
    'GA__of_Sales','Other__of_Sales', 'Operating_Profit_m', 'Operating_Margin__of_Sales',
    'Taxes_21', 'Quarterly_Operating_Cash_Flow_m', 'Percent_Change',
    'Annualized_OCF_m', 'Net_Cash_m', 'Perpetuity_Value_4','Net_Cash_m1',
    'Enterprise_Value_m', 'Implied_Value_Per_Share', 'Selling__Marketing_m', 'Research__Development_m',
    'SM__of_Sales', 'RD__of_Sales']

df = df[result]

# Convert DataFrame to an array of JSON objects
final_output = df.to_dict(orient='records')

result = json.dumps(final_output, allow_nan=True)
cache["response"]= final_output

[ 	{ 		"_id": "", 		"asset_class": "TSLA", 		"Financial_Term": "Q1-2023", 		"Total_Sales_m": 100, 		"Store_Operating_Expenses_m": 100, 		"Product_and_Distribution_Costs_m": 0, 		"Depreciation_and_Amortization_Expenses_m": 0, 		"Selling__Marketing_m": 100, 		"Research__Development_m": 0, 		"General__Administrative_m": 100, 		"Other_m": 0, 		"Depreciation_m": 0, 		"Cash_and_Cash_Equivalents_m": 0, 		"Longterm_Investments_m": 0, 		"Longterm_Debt_m": 0, 		"Fully_diluted_shares_outstanding_m": 0 	} ]