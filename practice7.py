# # Practice 7
# Analyze customer purchasing behavior
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dataset/customer_purchases.csv')

# ## 1. Average purchase amount for each product category
df.groupby('Product Category')['Purchase Amount ($)'].mean()

# ## 2. Average age and income of customers who make purchases in each product category
# Drop duplicates ['Customer ID', 'Product Category'] for make sure each customer for each product appears once
df.drop_duplicates(['Customer ID', 'Product Category']).groupby('Product Category')[['Age', 'Income ($)']].mean()

# ## 3. Gender distribution of customers in each product category
gender_distribution = df.drop_duplicates(['Customer ID', 'Product Category'])                        .groupby('Product Category').agg({'Gender': 'value_counts'})                        .rename({'Gender': 'count'}, axis=1)                        .reset_index(drop=False)
gender_distribution

# Pivot the DataFrame to get the desired format for plotting
gender_distribution = gender_distribution.pivot(index='Product Category', columns='Gender', values='count')
gender_distribution


ax = gender_distribution.plot(kind='bar', rot=0, stacked=False)
ax.set_xlabel('Product Category')
ax.set_ylabel('Count')
ax.set_title('Gender Distribution of Customers by Product Category')
plt.show()


# ## 4. Check if any customers make multiple purchases for same product category 
# Average time between purchases and average purchase amount?

# Check duplicates of 'Customer ID' and 'Product Category'
duplicates = df.duplicated(['Customer ID', 'Product Category'], keep=False)

# Get all multiple purchases by duplicates mask
multiple_purchases = df[duplicates].copy()
multiple_purchases

# Calculate the interval time between purchases for each customer/product category combination
multiple_purchases['interval_time'] = multiple_purchases.groupby(['Customer ID', 'Product Category'])['Purchase Date'].diff(periods=1)

# Calculate the average time between purchases and average purchase amount for each customer/product category combination
multiple_purchases = multiple_purchases.groupby(['Customer ID', 'Product Category']).agg({'interval_time': 'mean', 'Purchase Amount ($)': 'mean'})
multiple_purchases


# ## 5. Average purchase amount each month & Seasonal trends in purchasing behavior?

# Convert the Purchase Date column to a datetime data type
# Note that because SQL Server, the default zero date is January 1, 1900
# So I assume Purchase Date is number of dates since this day  
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'], unit='D', origin='1900-01-01')

# Add a Month column
df['Month'] = df['Purchase Date'].dt.month

# Group the data by month and calculate the average purchase amount for each month
avg_month_purchase = df.groupby('Month')['Purchase Amount ($)'].mean()
avg_month_purchase

avg_month_purchase.plot.line(title='Average purchase amount each month')

"""
# From the above chart, purchase in Feb is the highest, compare to Jan and Mar. 
# However, the provided data of average purchase each month is not sufficient to make a conclusion about seasonal trends as it only provides information about three months. 
# We need more data, preferably for a longer time period, to analyze seasonal trends in purchasing behavior.
"""