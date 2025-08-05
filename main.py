from item import Item
from toDoList import ToDoList
from visualizeList import visualizeList

task_list = ToDoList()
running = True
while running:
    print("\nHello!")
    start = input('[1] Add task \n[2] See list \n[3] Visualize in chart \n[4] Quit \nWhat would you like to do? ')
    if start.lower() == "1":
        new_name = input("\nWhat would you like the name of this task to be? ")
        new_due = int(input("What would you like to set the due date as? "))
        new_item = Item(new_name, new_due)
        task_list.items.append(new_item)
        print("\nThe task has been added to your to-do list!")

    elif start.lower() == "2":
        print("\nHere is your current list of to-dos:")
        for item in task_list.items:
            print(f"\t{item.item_name}; due at {item.time_due}")

    #elif start.lower() == "3":
        #VISUALIZE: needs filling in lol

    elif start == "4":
        print("\nAll set? See you next time!")
        running = False

    else:
        print("\nPlease enter a valid input")