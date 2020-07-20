#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
import requests
from datetime import datetime
import json

#### Get my fantasy team lineup
now = datetime.now()
my_team_id = '204252'
current_gw = events_df[events_df['deadline_time'] < now]['id'].max()

my_team_url = 'https://fantasy.premierleague.com/api/entry/{}/event/{}/picks/'.format(my_team_id,str(current_gw))

my_team = get(my_team_url)['picks']
my_team_df = pd.DataFrame(my_team)

my_team_df.to_csv (r'C:\Users\danie\OneDrive\Documents\PythonProjects\FPL Analysis\datafiles\my_team_df.csv', index = False, header=True)


