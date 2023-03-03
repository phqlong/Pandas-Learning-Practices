# # Practice 8
# Categorize Age to Young (<30), Middle (30-60), and Old (>60)
import pandas as pd

# Create a dictionary of data
data = {'Name': ['John', 'Jane', 'Bob', 'Alice'],
        'Age': [25, 30, 27, 40]}

# Create a DataFrame from the dictionary
df = pd.DataFrame(data)


def categorize_age(age):
    if age<30:
        return 'Young'
    elif age<=60:
        return 'Middle'
    else:
        return 'Old'

df['Category'] = df.Age.apply(categorize_age)
df