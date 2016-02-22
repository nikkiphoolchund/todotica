import json
import inspect
import api_todoist
import api_habitica

# -
# - Recuperer les taches dans chaque projet qui sont uncompleted
# - Filtrer les taches et recuperer seulement le nom des taches

# print api_todoist.get_uncompleted()

# - Get all tasks from Habitica

print api_habitica.get_uncompleted()