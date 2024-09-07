import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

df = pd.read_csv("datasets/output.csv")
df['renewable_percentage'] = pd.to_numeric(df['renewable_percentage'], errors='coerce')

renewable_percentage = df.groupby('country')['renewable_percentage'].mean()

desired_countries = ['Mexico', 'Japan', 'United States', 'Iceland']

percentages = {country: renewable_percentage.loc[country] if country in renewable_percentage.index else 0 for country in desired_countries}

categories = list(percentages.keys())
values = list(percentages.values())
colors = ['#4f518c', '#907ad6', '#DABFFF', '#2c2a4a']  

radius = 0
bar_width = 0.2
edge_color = 'lightgray'

fig, ax = plt.subplots(figsize=(12, 7))

for i, (value, color) in enumerate(zip(values, colors)):
    x = i
    rect = patches.FancyBboxPatch(
        (x - bar_width / 2, 0),  
        bar_width, value, 
        boxstyle=f"round,pad=0.05,rounding_size={radius}", 
        edgecolor=edge_color,
        facecolor=color,
        linewidth=1
    )
    ax.add_patch(rect)

for i, value in enumerate(values):
    plt.text(i, value + 1, f'{value:.2f}%', ha='center', va='bottom', fontsize=12, color='black', fontweight='bold')

plt.xticks(ticks=np.arange(len(categories)), labels=categories, rotation=45, fontsize=12, fontweight='bold')

plt.xlabel('Países', fontsize=14, fontweight='bold')
plt.ylabel('Porcentaje (%)', fontsize=14, fontweight='bold')
plt.title('Porcentaje de Energía Renovable por País', fontsize=16, fontweight='bold')

plt.grid(axis='y', linestyle='--', alpha=0.6)

plt.xlim(-0.5, len(categories) - 0.5)
plt.ylim(0, max(values) + 10)

plt.axhline(0, color='black', linewidth=0.8)

plt.tight_layout()

plt.show()
