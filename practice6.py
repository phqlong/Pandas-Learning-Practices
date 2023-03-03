# # Practice 6
# Analyze sales trends by product category, region, and month and make recommendations
import random
import pandas as pd
import matplotlib.pyplot as plt

import statsmodels.api as sm
from statsmodels.formula.api import ols


# Define the product categories, regions, and months
product_categories = ['Electronics', 'Clothing']
regions = ['North', 'South']
months = ['Jan', 'Feb', 'Mar']

# Generate sales data for each product category, region, and month
sales_data = []
for product in product_categories:
    for region in regions:
        for month in months:
            sales = random.randint(5000, 15000)  # Generate random sales amount between 5000 and 15000 dollars
            sales_data.append([product, region, month, sales])

# Convert the sales data to a pandas DataFrame
columns = ['Product Category', 'Region', 'Month', 'Sales ($)']
sales_df = pd.DataFrame(sales_data, columns=columns)

# Converting Month to datetime
sales_df["Month"] = pd.to_datetime(sales_df["Month"], format="%b").dt.month
sales_df

# Group data by Product Category, Region, and Month
sales_df = sales_df.groupby(["Product Category", "Region", 'Month'])["Sales ($)"].sum().reset_index()


# ## Exploratory Data Analysis

# Plot Line chart for each combination of ["Product Category", "Region"] by Month
plt.figure(figsize=(12, 6))
for category in sales_df["Product Category"].unique():
    for region in sales_df["Region"].unique():
        data = sales_df[(sales_df["Product Category"] == category) & (sales_df["Region"] == region)]
        plt.plot(data["Month"], data["Sales ($)"], label=f"{category} ({region})")
        
plt.legend()
plt.title("Sales Trends by Product Category and Region")
plt.xlabel("Month")
plt.ylabel("Sales ($)")
plt.show()


# ## Two-way ANOVA test

# Perform two-way ANOVA  with two categorical independent variables, "Product Category" and "Region," 
# and one continuous dependent variable: Month
model = ols("Q('Sales ($)') ~ C(Q('Product Category')) + C(Region)", data=sales_df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)
print(anova_table)

"""
# The "sum_sq" column represents the sum of squares, which is a measure of the variation in the data that can be attributed to each source of variation.
# The "df" column represents the degrees of freedom for each source of variation, which is the number of independent observations minus the number of parameters estimated from the data.
# The "F" column represents the F-statistic, which is the ratio of the variation between groups to the variation within groups.
# The "PR(>F)" column represents the p-value, which is the probability of observing a F-statistic as large or larger than the observed value if the null hypothesis is true.
# In this table, the null hypothesis for each factor is that there is no significant effect on the dependent variable. The p-values for both factors are greater than the significance level of 0.05, indicating that there is not enough evidence to reject the null hypothesis. Therefore, it can be concluded that there is no significant interaction between "Product Category" and "Region" and neither "Product Category" nor "Region" has a significant main effect on the dependent variable. The majority of the variation in the dependent variable is due to the residual term, which represents unexplained variation or random error.
"""

"""
# **Recommendations:** Based on the analysis, we can make recommendations to improve sales. For example, if we identify a seasonal pattern in sales, we can adjust our marketing and promotional activities accordingly. If we find that certain product categories or regions are performing better than others, we can focus our resources on those areas. Additionally, if we find that there are significant differences in sales between different product categories and regions, we can adjust our pricing or product offerings to better match the preferences of our customers in those areas.
"""