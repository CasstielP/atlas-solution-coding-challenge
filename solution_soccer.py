# import re, regex module from python
import re
# import pandas module for display data
import pandas as pd

file_path = 'soccer.dat'
# open file path and store to var: data
with open(file_path, 'r') as file:
    data = file.readlines()

# declare var lists to append the appropriate regex pattern groups
team_names = []

scores_for = []

scores_against = []

# create the regex pattern accordingly
# groups: team name, score for, score agianst
line_pattern = re.compile(r'\s*\d+\.\s+(\w+[\w_]*?)\s+\d+\s+\d+\s+\d+\s+\d+\s+(\d+)\s+-\s+(\d+)\s+\d+')

# iterate through var: data and parse each line with line_pattern
for line in data:
    match = line_pattern.match(line)
# when match found, append each group to the lists accordingly
    if match:
        team = match.group(1)
        score_for = int(match.group(2))
        score_against = int(match.group(3))
        team_names.append(team)
        scores_for.append(score_for)
        scores_against.append(score_against)

# create pandas dataframe to display data
team_score_data = pd.DataFrame({
        'Team': team_names,
        'Score For': scores_for,
        'Score Against': scores_against
    })

# create new column and calculate the difference
team_score_data['Score Difference'] = abs(team_score_data['Score For'] - team_score_data['Score Against'])

# declare var to store the row with min score difference
min_difference_row = team_score_data.loc[team_score_data['Score Difference'].idxmin()]


print(min_difference_row)
