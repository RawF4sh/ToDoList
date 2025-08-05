from item import Item

class ToDoList:
    def __init__(self):
        self.items = []
        self.how_many_completed = 0

    #Function to check if an item (a task) is complete
    def CheckComplete(self):
        for item in self.items:
            if item.complete: #change when I have access to
                self.how_many_completed+=1

    #Function to add an item (task) to the list of items (the whole to-do list)
    def AddItem(self, Item):
        self.items.append(Item) #Does this work? Appending the whole class?

    def __str__(self):
        return f"There are {len(self.items)} tasks on the to-do list. {self.how_many_completed} of those tasks has been completed."
