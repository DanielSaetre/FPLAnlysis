#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
import requests
from datetime import datetime
import json

def get(url):
    response = requests.get(url)
    return json.loads(response.content)

response = get('https://fantasy.premierleague.com/api/bootstrap-static/')
response.keys()

players = response['elements']
teams = response['teams']
events = response['events']

players_df = pd.DataFrame(players)
teams_df = pd.DataFrame(teams)
events_df = pd.DataFrame(events)

# Some basic cleaning
events_df['deadline_time'] = pd.to_datetime(events_df['deadline_time'])
events_df['deadline_time'] = events_df['deadline_time'].dt.tz_localize(None)

# Save to files
players_df.to_csv (r'C:\Users\danie\OneDrive\Documents\PythonProjects\FPL Analysis\datafiles\players_df.csv', index = False, header=True)
teams_df.to_csv (r'C:\Users\danie\OneDrive\Documents\PythonProjects\FPL Analysis\datafiles\teams_df.csv', index = False, header=True)
events_df.to_csv (r'C:\Users\danie\OneDrive\Documents\PythonProjects\FPL Analysis\datafiles\events_df.csv', index = False, header=True)

### Get all fixtures ###
test_url = 'https://fantasy.premierleague.com/api/fixtures/'
response = get(test_url)
fixtures_df_test = pd.DataFrame(response)
fixtures_df_test.to_csv (r'C:\Users\danie\OneDrive\Documents\PythonProjects\FPL Analysis\datafiles\fixtures_df_test.csv', index = False, header=True)

#### Get my fantasy team lineup
now = datetime.now()
my_team_id = '204252'
current_gw = events_df[events_df['deadline_time'] < now]['id'].max()

my_team_url = 'https://fantasy.premierleague.com/api/entry/{}/event/{}/picks/'.format(my_team_id,str(current_gw))

my_team = get(my_team_url)['picks']
my_team_df = pd.DataFrame(my_team)

my_team_df.to_csv (r'C:\Users\danie\OneDrive\Documents\PythonProjects\FPL Analysis\datafiles\my_team_df.csv', index = False, header=True)





