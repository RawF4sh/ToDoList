from item import Item
from toDoList import ToDoList
from visualizeList import visualizeList

task_list = ToDoList()
while True:
    start = input("Hello! What would you like to do? ")
    if start.lower() == "add task":
        new_name = str(input("What would you like the name of this task to be? "))
        new_due = int(input("What would you like to set the due date as? "))
        new_item = Item(new_name, new_due)
        task_list.items.append(new_item)
        print("The task has been added to your to-do list!")