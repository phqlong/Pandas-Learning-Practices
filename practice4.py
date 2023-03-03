# # Practice 4
# Purchase frequency (average days between purchases of each customer)

import pandas as pd


df = pd.read_csv("dataset/practice4.csv")

# Format datetime column
df['date'] = pd.to_datetime(df['date'])

# Sort df by customer_id and date
df = df.sort_values(by=["customer_id", "date"]).reset_index(drop=True)

# Calculate interval days between purchased days for each customer
df['interval'] = df.groupby('customer_id')['date'].diff(periods=1).dt.days

# Calculate purchase frequency (mean interval days between 2 purchases)
purchase_frequency = df.groupby('customer_id')['interval'].mean()
purchase_frequency