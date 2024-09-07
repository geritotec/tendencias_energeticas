import pandas as pd

df = pd.read_csv("datasets/output.csv")

renewable_change = df.groupby('country')['renewables'].agg(['first', 'last'])
renewable_change['increase'] = renewable_change['last'] - renewable_change['first']

max_increase_country = renewable_change['increase'].idxmax()
max_increase_value = renewable_change['increase'].max()

print(f"País con mayor incremento de energías renovables:  {max_increase_country} ({max_increase_value} GWh).")