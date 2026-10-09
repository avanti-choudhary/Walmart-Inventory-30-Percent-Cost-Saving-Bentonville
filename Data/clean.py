import pandas as pd

# Step 1: Load the Walmart data
df = pd.read_csv('Walmart_sample.csv')
print("Original data loaded:")
print(df.head())

# Step 2: Sort data - VERY important for LAG() window function
# We sort by Store, Product, and Date so LAG can see previous week
df = df.sort_values(['Store_ID', 'Product_ID', 'Date'])

# Step 3: LAG() - Get previous week's sales (SQL: LAG(Weekly_Sales) OVER...)
df['Prev_Week_Sales'] = df.groupby(['Store_ID', 'Product_ID'])['Weekly_Sales'].shift(1)

# Step 4: Calculate Sales Change %
df['Sales_Change'] = (df['Weekly_Sales'] - df['Prev_Week_Sales']) / df['Prev_Week_Sales']

# Step 5: CORE LOGIC - 30% Cost Reduction Strategy
# If sales dropped more than 10%, we reduce next inventory by 30%
# This is how Walmart saves inventory cost in Bentonville stores
def calculate_new_inventory(row):
    if pd.isna(row['Sales_Change']):
        return row['Inventory_Level']
    if row['Sales_Change'] < -0.10:  # Sales dropped 10%
        return row['Inventory_Level'] * 0.7  # 30% reduction
    else:
        return row['Inventory_Level']

df['New_Inventory'] = df.apply(calculate_new_inventory, axis=1)

# Step 6: Calculate Cost Before vs After - For interview proof
df['Old_Cost'] = df['Inventory_Level'] * df['Cost']
df['New_Cost'] = df['New_Inventory'] * df['Cost']
df['Cost_Saved'] = df['Old_Cost'] - df['New_Cost']

# Step 7: Save cleaned file for dashboard
df.to_csv('inventory_cost.csv', index=False)

print("\n--- 30% Reduction Logic Applied ---")
print(df[['Store_ID','Product_ID','Date','Weekly_Sales','Prev_Week_Sales','Sales_Change','Inventory_Level','New_Inventory']])

total_old = df['Old_Cost'].sum()
total_new = df['New_Cost'].sum()
total_saved = total_old - total_new
percent_saved = (total_saved / total_old) * 100

print(f"\nTotal Old Cost: ${total_old}")
print(f"Total New Cost: ${total_new}")
print(f"Total Saved: ${total_saved} ({percent_saved:.2f}%)")
print("\nFile saved as inventory_cost.csv")