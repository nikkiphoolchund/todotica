

class Task:
    ### Agnostic Todotica class

    def __init__(self, name, due_date):
        self.name = name    # instance variable unique to each instance
        self.due_date = due_date

    def __str__(self):
        return u"Task name is: {0}, and Due Date is: {1}".format(self.name, self.due_date)

    def __repr__(self):
        return u"Task name is: {0}, and Due Date is: {1}".format(self.name, self.due_date)