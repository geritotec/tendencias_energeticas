import pandas as pd

df = pd.read_csv("datasets/output.csv")


df['renewable_percentage'] = ( df['renewables']  / (df['non_renewables'] + df['renewables'])) * 100

max_percentage_index = df['renewable_percentage'].idxmax()

max_percentage_country = df.loc[max_percentage_index, 'country']
max_percentage_value = df.loc[max_percentage_index, 'renewable_percentage']

print(f"País con el mayor porcentaje de energía renovable: {max_percentage_country} ({max_percentage_value:.2f}%).")
