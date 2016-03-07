# coding: utf8
# Get all uncompleted tasks

import todoist
import json
import inspect
from datetime import datetime
import pprint

from Task import Task

import config
#
# - Recuperer les taches dans chaque projet qui sont uncompleted
# - Filtrer les taches et recuperer seulement le nom des taches
#  TODO: Catch the error is error_tag: AUTH_INVALID_TOKEN

def get_uncompleted():
    tasks_uncompleted = []

    api = todoist.TodoistAPI(config.todoist_api_token)
    myTasks = api.query(['view all'])[0]

    data = myTasks['data']

    for project in data:
        for task in project['uncompleted']:
            if task['checked'] == 0:
                # print " - " + task['content']
                new_task = Task(task['content'], task['due_date_utc'])
                # print u" - {0}".format(new_task)
                tasks_uncompleted.append(new_task)
            # else:
                # print " - COMPLETED BUT STILL FETCHED: " + task['content']

        return tasks_uncompleted

if __name__ == "__main__":
    print get_uncompleted()
