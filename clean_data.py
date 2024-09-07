import pandas as pd

df = pd.read_csv('datasets/output.csv')

def clean_numeric_values(value):
    if isinstance(value, str):
        try:
            return float(value.replace(' ', ''))
        except ValueError:
            return value
    else:
        return value

df = df.applymap(clean_numeric_values)

df.to_csv('datasets/output.csv', index=False)

print("Cleaned data saved to datasets/output.csv")
