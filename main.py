from item import Item
from toDoList import ToDoList
from visualizeList import visualizeList

task_list = ToDoList()
while True:
    print("\nHello! What would you like to do?")
    start = input('Enter "add task," "see list," or "visualize." ')

    if start.lower() == "add task":
        new_name = input("\nWhat would you like the name of this task to be? ")
        new_due = int(input("What would you like to set the due date as? "))
        new_item = Item(new_name, new_due)
        task_list.items.append(new_item)
        print("\nThe task has been added to your to-do list!")

    if start.lower() == "see list":
        print("\nHere is your current list of to-dos:")
        for item in task_list.items:
            print(f"\t{item.item_name}, due at {item.time_due}")