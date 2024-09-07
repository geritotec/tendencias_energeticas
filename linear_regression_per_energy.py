import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib.patches as patches


df = pd.read_csv('datasets/output.csv')
mexico_df = df[df['country'] == 'Mexico']

mexico_df['date'] = pd.to_datetime(mexico_df['date'], unit='s')
mexico_df['date_num'] = mexico_df['date'].map(pd.Timestamp.toordinal)

X = mexico_df[['date_num']] 
y = mexico_df['electricity_consumed'] 

model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)

fig, ax = plt.subplots(figsize=(10, 6))
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(0.5)
ax.spines['bottom'].set_linewidth(0.5)

fig.patch.set_facecolor('#e0e0e0')
ax.set_facecolor('#f0f0f0')

ax.plot(mexico_df['date'], y, color='#007acc', marker='o', linestyle='-', linewidth=2, markersize=7, label='Datos')

ax.plot(mexico_df['date'], predictions, color='#ff4500', linewidth=2, label='Regresión lineal')

for date, value in zip(mexico_df['date'], y):
    ax.add_patch(patches.Circle((date, value), radius=0.3, color='#ffffff', edgecolor='#007acc', linewidth=2, alpha=0.8))

ax.tick_params(axis='both', which='major', labelsize=12, width=0.5)
ax.xaxis.set_tick_params(width=0.5)
ax.yaxis.set_tick_params(width=0.5)

ax.set_xlabel('Fecha', fontsize=14, weight='bold')
ax.set_ylabel('GWh', fontsize=14, weight='bold')
ax.set_title(f'Consumo de energía en México', fontsize=16, weight='bold')

ax.legend()
ax.grid(True, linestyle='--', alpha=0.7)

plt.show()
