# Get all uncompleted tasks

import requests
import pprint

import config

url_habitica_api = "https://habitica.com/api/v2/"

user_id = config.habitica_user_id
api_token = config.habitica_api_token

headers = {
    'x-api-key': api_token,
    'x-api-user': user_id
}


def get_uncompleted():
    r = requests.get(''.join((url_habitica_api, 'user/tasks')), headers=headers)
    tasks_list = r.json()
    for task in tasks_list:
        if task['type'] == 'todo' and task['completed'] == False:
            print task
            # print task['text']
            # print ''.join(('    ', task['type']))
    # pprint.pprint( r.json() )
