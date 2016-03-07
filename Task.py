import datetime
from dateutil import parser

class Task:
    ### Agnostic Todotica class

    # TODO: Create two sub-classes: One for Habitica and one for Todoist => So can retrieve where does the task comes from

    def __init__(self, name, due_date):
        self.name = name    # instance variable unique to each instance
        # TODO: Ask a specific format for these due_dates, which will be handled in sub-classes
        # Date has to manage UTC => See tzinfo. Use datetime.datetime
        if due_date != None:
            parsed_due_date = parser.parse(due_date)
            self.due_date = parsed_due_date
        else:
            self.due_date = due_date