from item import Item
from toDoList import ToDoList
import datetime
from visualizeList import visualizeList

task_list = ToDoList()
running = True
while running:
    print("\nHello!")
    start = input('[1] Add task \n[2] See list \n[3] Visualize in chart \n[4] Quit \nWhat would you like to do? ')
    if start.lower() == "1":
        new_name = input("\nWhat would you like the name of this task to be? ")
        print("Set the date for your task")
        hour = int(input("What hour is this task due?(0-23) "))
        minute = int(input("What minute is this task due?(0-59) "))
        second = int(input("What second is this task due?(0-59) "))
        new_due = datetime.time(hour, minute, second)
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
