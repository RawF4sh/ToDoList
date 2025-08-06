from item import Item

class ToDoList:
    def __init__(self):
        self.items = []
        self.completed_items = []
        self.how_many_completed = 0

    #Function to check if an item (a task) is complete
    def CheckComplete(self):
        for item in self.items:
            if item.completed:
                self.how_many_completed+=1
                self.completed_items.append(self.items[item])
                del self.items[item]

    #Function to add an item (task) to the list of items (the whole to-do list)
    def AddItem(self, Item):
        self.items.append(Item)

    def RemoveItem(self, index):
        del self.items[index]

    #Cool lil thing so that it prints when an instance of the class is printed
    def __str__(self):
        return f"There are {len(self.items)} tasks on the to-do list. {self.how_many_completed} of those tasks has been completed."