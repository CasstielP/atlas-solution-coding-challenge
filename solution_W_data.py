# import re, regex module from python
import re
# import pandas module for display data
import pandas as pd

file_path = 'w_data.dat'

# open file path and store to var: data
with open(file_path, 'r') as file:
    data = file.readlines()


# declare var lists to append the appropriate regex pattern groups
day_numbers = []
max_temps = []
min_temps= []

# create the regex pattern accordingly
# groups: date, max temp, min temp
line_pattern = re.compile(r"\s*(\d+)\s+(\d+)\s+(\d+)")


# iterate through var: data and parse each line with line_pattern
for line in data:
    match = line_pattern.match(line)
# when match found, append each group to the lists accordingly
    if match:
        day = int(match.group(1))
        max_temp = int(match.group(2))
        min_temp = int(match.group(3))
        day_numbers.append(day)
        max_temps.append(max_temp)
        min_temps.append(min_temp)



# create pandas dataframe to display data
weather_data = pd.DataFrame({
            'Day': day_numbers,
            'Max Temp': max_temps,
            'Min Temp': min_temps
        })

# create new column to store the temp spread
weather_data['Temp Spread'] = weather_data['Max Temp'] - weather_data['Min Temp']

# declare new var to store the row with min temp spread
min_spread_row = weather_data.loc[weather_data['Temp Spread'].idxmin()]

print(min_spread_row)
