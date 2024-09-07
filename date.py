import pandas as pd
from datetime import datetime
import calendar

df = pd.read_csv("datasets/output.csv")

start_timestamp = 1454306399 
rows_per_period = 32

def generate_unix_timestamps(start_ts, total_rows, rows_per_period):
    timestamps = []
    current_ts = start_ts
    
    for i in range(total_rows):
        date = datetime.utcfromtimestamp(current_ts)
        timestamps.append(current_ts)

        if (i + 1) % rows_per_period == 0:
            current_ts = start_ts
        else:
            if date.month == 12: 
                next_month = datetime(date.year + 1, 1, 1, date.hour, date.minute, date.second)
            else:  
                next_month = datetime(date.year, date.month + 1, 1, date.hour, date.minute, date.second)
            last_day = calendar.monthrange(next_month.year, next_month.month)[1]
            next_month = next_month.replace(day=last_day)
            current_ts = int(next_month.timestamp())

    return timestamps

df['date'] = generate_unix_timestamps(start_timestamp, len(df), rows_per_period)

df.to_csv('output.csv', index=False)

print("DataFrame saved to 'output.csv'.")
