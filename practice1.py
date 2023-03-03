# # Practice 1
# Create two DataFrames
# Then merges these two DataFrames using the 'Name' column as the key, and outputs the following merged DataFrame which includes their Name, Age and Occupation:

import pandas as pd
from datetime import date

#Create a dictionary with some sample data
Info_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Dave','Eva','Kevin'],
    'Birth_Date': ['1991-12-01', '1980-01-11', '1987-01-01', '1966-01-18', '1996-10-10', '1999-11-11']}

Occupation_data = {
    'Name': ['Alice', 'Bob', 'Eve', 'Eva', 'Kevin'],
    'Occupation': ['Engineer', 'Doctor', 'Teacher', 'Student', 'Student']}


#Create a dataframe from the dictionary
Info_df = pd.DataFrame(Info_data)
Occupation_df = pd.DataFrame(Occupation_data)

def merging(df1, df2, key, how="inner"):
    merged_df = df1.merge(df2, on=key, how=how)
    
    # Calculate age and add it to the merged dataframe
    merged_df['Birth_Date'] = pd.to_datetime(merged_df['Birth_Date'])
    merged_df['Age'] = date.today().year - merged_df['Birth_Date'].dt.year
    merged_df = merged_df.drop(columns=['Birth_Date'])

    return merged_df


# If we want to merge and remain all values in Info_df
merged_df = merging(Info_df, Occupation_df, key="Name", how="left")
merged_df

# Else If we want to merge and remove all rows contain null 
merged_df = merging(Info_df, Occupation_df, key="Name", how="inner")
merged_df