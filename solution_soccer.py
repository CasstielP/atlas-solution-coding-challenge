import re
import pandas as pd

file_path = 'soccer.dat'

with open(file_path, 'r') as file:
    data = file.readlines()

team_names = []

scores_for = []

scores_against = []

line_pattern = re.compile(r'\s*\d+\.\s+(\w+[\w_]*?)\s+\d+\s+\d+\s+\d+\s+\d+\s+(\d+)\s+-\s+(\d+)\s+\d+')

for line in data:
    match = line_pattern.match(line)

    if match:
        team = match.group(1)
        score_for = int(match.group(2))
        score_against = int(match.group(3))
        team_names.append(team)
        scores_for.append(score_for)
        scores_against.append(score_against)

team_score_data = pd.DataFrame({
        'Team': team_names,
        'Score For': scores_for,
        'Score Against': scores_against
    })

team_score_data['Score Difference'] = abs(team_score_data['Score For'] - team_score_data['Score Against'])

min_difference_row = team_score_data.loc[team_score_data['Score Difference'].idxmin()]


print(min_difference_row)