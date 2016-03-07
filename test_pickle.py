import pickle

tasks = pickle.load(open('file_tasks.p', 'rb'))

for task in tasks:
    print task.name