# from item import Item

class ToDoList:
    def __init__(self):
        self.items = []
        self.how_many_completed = 0

    def CheckComplete(self):
        for item in self.items:
            if item.complete: #change when I have access to
                self.how_many_completed+=1