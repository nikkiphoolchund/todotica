import json
import inspect
import api_todoist
import api_habitica
import sys
import argparse
import os
import logging


# - TODO: Recuperer les taches dans chaque projet qui sont uncompleted
# - TODO: Filtrer les taches et recuperer seulement le nom des taches
# - TODO: Export file_tasks to Gist / Save into it automatically, so can be anywhere => Useless if web server :)
# - TODO: If a task has disappeared, it could either mean it has been completed OR it has been deleted. Manage the cases.

# print api_todoist.get_uncompleted()

# - Get all tasks from Habitica

# print api_habitica.get_uncompleted()

def main():
    # Log init
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger()

    # Variables
    store_tasks_file_name = "file_tasks"

    # Command Line parsing init
    parser = argparse.ArgumentParser(description='Synchronize your TODOist with your habiTICA :)')

    parser.add_argument('-d', '--debug', help='Set the debug mode for more informations', action='store_const', const=True)

    # parser.add_argument('-', '--gff3', help='Directory where to put the foo.txt')

    # Get the args passed in parameter
    args = parser.parse_args()

    if args.debug:
        # We clean the content of file_tasks for debug purpose
        log.debug(''.join(["We erase the content of ", store_tasks_file_name, " before writing again"]))
        open(store_tasks_file_name, 'w').close()

    # 1. If not file tasks_synchronized, then first time launch (print it) => Retrieve all tasks uncompleted from todoist
    #   and from habitRica, and synchronize bidirecitonnaly (only add). Plus, add all tasks synchronized into the file_tasks
    # 2. If file_tasks exists, then check every task in file_tasks against habitica and todoist. Complete them on the other side, if they still exists
    #   and remove it from the file_tasks file
    # 3. If file_tasks exists, then check if a task is new in habitica or todoist. If so, add it into the file, and create it into the other todo management
    with open(store_tasks_file_name, "a+") as file_tasks:
        file_tasks.write("Hey!")



if __name__ == "__main__":
    main()