# # Practice 5
# Calculate the mean, median, and standard deviation of the daily revenue.
import pandas as pd


df = pd.read_csv("dataset/practice5.csv")

# Format datetime column
df['date'] = pd.to_datetime(df['date'])

# Quick code for showing basic stastics like mean, std, min, max and 25, 75% percentile
df.describe()

print('Mean of daily revenue:', df.revenue.mean())
print('Median of daily revenue:', df.revenue.median())
print('Standard deviation of daily revenue:', df.revenue.std())

