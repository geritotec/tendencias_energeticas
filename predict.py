import pandas as pd
from sklearn.linear_model import LinearRegression
from datetime import datetime

df = pd.read_csv("datasets/output.csv")

mexico_df = df[df['country'] == 'Mexico']

mexico_df['date'] = pd.to_datetime(mexico_df['date'], unit='s')

mexico_df['date_num'] = mexico_df['date'].map(pd.Timestamp.toordinal)

X = mexico_df[['date_num']]
y = mexico_df['renewable_percentage']

model = LinearRegression()
model.fit(X, y)

def predict_percentage(year):
    date_num = datetime(year, 1, 1).toordinal()
    prediction = model.predict([[date_num]])
    return prediction[0]

years = [2024, 2033, 2050]
predictions = {year: predict_percentage(year) for year in years}

for year, percentage in predictions.items():
    print(f"Porcentaje predecido para el año {year}: {percentage:.2f}%")
