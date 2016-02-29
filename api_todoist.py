# Get all uncompleted tasks

import todoist
import json
import inspect
from datetime import datetime
from dateutil.parser import parse
import pprint

import config
#
# - Recuperer les taches dans chaque projet qui sont uncompleted
# - Filtrer les taches et recuperer seulement le nom des taches
#  TODO: Catch the error is error_tag: AUTH_INVALID_TOKEN

def get_uncompleted():
    api = todoist.TodoistAPI(config.todoist_api_token)
    myTasks = api.query(['view all'])[0]

    data = myTasks['data']

    for project in data:
        print project['project_name']
        for task in project['uncompleted']:
            if task['checked'] == 0:
                print " - " + task['content']
            else:
                print " - COMPLETED BUT STILL FETCHED: " + task['content']
