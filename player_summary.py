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

#### Getting player summary data
def get_player_summary(player_id):
    url = 'https://fantasy.premierleague.com/api/element-summary/' + str(player_id) + '/' 
    response = get(url)
    fixtures = response['fixtures']
    history = response['history']
    history_past = response['history_past']
    return [fixtures, history, history_past]

fixtures, history, history_past = get_player_summary(100)

fixtures_df = pd.DataFrame(fixtures)
history_df = pd.DataFrame(history)
history_past_df = pd.DataFrame(history_past)

fixtures_df.to_csv (r'C:\Users\danie\OneDrive\Documents\PythonProjects\FPL Analysis\datafiles\fixtures_df.csv', index = False, header=True)
history_df.to_csv (r'C:\Users\danie\OneDrive\Documents\PythonProjects\FPL Analysis\datafiles\history_df.csv', index = False, header=True)
history_past_df.to_csv (r'C:\Users\danie\OneDrive\Documents\PythonProjects\FPL Analysis\datafiles\history_past_df.csv', index = False, header=True)

