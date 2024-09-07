import pandas as pd

df = pd.read_csv("datasets/output.csv")

max_renewables_index = df['renewables'].idxmax()

max_renewables_country = df.loc[max_renewables_index, 'country']
max_renewables_value = df.loc[max_renewables_index, 'renewables']

print(f"País con la mayor cantidad de energías renovables al final: {max_renewables_country} ({max_renewables_value} GWh).")
