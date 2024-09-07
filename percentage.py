import pandas as pd

df = pd.read_csv("datasets/output.csv")

df['renewable_percentage'] = (df['renewables'] / (df['non_renewables'] + df['renewables'])) * 100

df.to_csv("datasets/output.csv", index=False)
print("done!")