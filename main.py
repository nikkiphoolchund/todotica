# coding: utf8

import json
import inspect
import sys
import os
import logging
import pickle

# Requirements libs

from mako.template import Template
import argparse

# Project libs

import api_todoist
import api_habitica
from Task import Task


# - TODO: Recuperer les taches dans chaque projet qui sont uncompleted
# - TODO: Filtrer les taches et recuperer seulement le nom des taches
# - TODO: Export file_tasks to Gist / Save into it automatically, so can be anywhere => Useless if web server :)
# - TODO: If a task has disappeared, it could either mean it has been completed OR it has been deleted. Manage the cases.
# - TODO: Create classes to transfer a Habitica or Todoist task into a todotica task class
# - TODO: Create an file which stores all the objects instead of a raw file => See Pickle

# print api_todoist.get_uncompleted()

# - Get all tasks from Habitica

# print api_habitica.get_uncompleted()

def main():
    # Log init
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger()

    # Variables
    store_tasks_dump_name = "file_tasks.p"
    store_tasks_html_name = "file_tasks.html"
    tasks_file_template_name = "file_tasks_template.mako"

    # Command Line parsing init
    parser = argparse.ArgumentParser(description='Synchronize your TODOist with your habiTICA :)')

    parser.add_argument('-d', '--debug', help='Set the debug mode for more informations', action='store_const', const=True)

    # parser.add_argument('-', '--gff3', help='Directory where to put the foo.txt')

    # Get the args passed in parameter
    args = parser.parse_args()

    # TODO:
    # 1. If not file tasks_synchronized, then first time launch (print it) => Retrieve all tasks uncompleted from todoist
    #   and from habitica, and synchronize bidirectionnaly (only add). Plus, add all tasks synchronized into the file_tasks
    # 2. If file_tasks exists, then check every task in file_tasks against habitica and todoist. Complete them on the other side, if they still exists
    #   and remove it from the file_tasks file
    # 3. If file_tasks exists, then check if a task is new in habitica or todoist. If so, add it into the file, and create it into the other todo management

    # TODO: Remove when tests finished
    tasks = []
    # task_one = Task("Task One", "31/12/1987")
    # task_two = Task("Task Two", "19/09/1990")
    #
    # tasks.append(task_one)
    # tasks.append(task_two)

    # Get all the habitica tasks into Task objects
    habitica_tasks = api_habitica.get_uncompleted()
    for h_task in habitica_tasks:
        tasks.append(h_task)

    # Get all the todoist tasks into Task objects
    todoist_tasks = api_todoist.get_uncompleted()
    for t_task in todoist_tasks:
        tasks.append(t_task)

    # Save sync tasks to pickle object (for reusability)
    pickle.dump(tasks, open('file_tasks.p', 'wb'))

    # Save sync tasks to HTML (for readability)
    myTemplate = Template(filename=tasks_file_template_name)
    tasks_file_template_rendered = myTemplate.render(tasks=tasks)

    with open(store_tasks_html_name, "w+") as file_tasks:
        file_tasks.write(tasks_file_template_rendered.encode('utf-8'))


if __name__ == "__main__":
    main()
