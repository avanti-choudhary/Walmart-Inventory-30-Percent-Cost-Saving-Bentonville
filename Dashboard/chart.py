import pandas as pd
import matplotlib.pyplot as plt

# Load your cleaned data
df = pd.read_csv('../data/inventory_cost.csv')

# Sum by Store to show saving
summary = df.groupby('Store_ID')[['Old_Cost','New_Cost']].sum()

# Make bar chart
summary.plot(kind='bar', figsize=(8,5))
plt.title('Walmart Bentonville - Old vs New Inventory Cost')
plt.ylabel('Cost in $')
plt.xlabel('Store ID')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('cost_saving_chart.png')
print("Chart saved as cost_saving_chart.png")
plt.show()