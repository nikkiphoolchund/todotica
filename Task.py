

class Task:
    ### Agnostic Todotica class

    def __init__(self, name, due_date):
        self.name = name    # instance variable unique to each instance
        self.due_date = due_date