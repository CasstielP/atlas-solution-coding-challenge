import re
import pandas as pd

file_path = 'w_data.dat'

with open(file_path, 'r') as file:
    data = file.readlines()

day_numbers = []
max_temps = []
min_temps= []

line_pattern = re.compile(r"\s*(\d+)\s+(\d+)\s+(\d+)")


for line in data:
    match = line_pattern.match(line)

    if match:
        day = int(match.group(1))
        max_temp = int(match.group(2))
        min_temp = int(match.group(3))
        day_numbers.append(day)
        max_temps.append(max_temp)
        min_temps.append(min_temp)



        
weather_data = pd.DataFrame({
            'Day': day_numbers,
            'Max Temp': max_temps,
            'Min Temp': min_temps
        })

 
weather_data['Temp Spread'] = weather_data['Max Temp'] - weather_data['Min Temp']


min_spread_row = weather_data.loc[weather_data['Temp Spread'].idxmin()]

print(min_spread_row)

