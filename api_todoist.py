# Get all uncompleted tasks

import todoist
import json
import inspect
from datetime import datetime
from dateutil.parser import parse
import pprint

#
# - Recuperer les taches dans chaque projet qui sont uncompleted
# - Filtrer les taches et recuperer seulement le nom des taches

def get_uncompleted():
    api = todoist.TodoistAPI('b5d1c0868fda34530315cb2c50c2c8ac6db5cacd')
    myTasks = api.query(['view all'])[0]

    data = myTasks['data']

    for project in data:
        print project['project_name']
        for task in project['uncompleted']:
            if task['checked'] == 0:
                print " - " + task['content']
            else:
                print " - COMPLETED BUT STILL FETCHED: " + task['content']
