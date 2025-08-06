from item import Item
from toDoList import ToDoList
import datetime
from visualizeList import visualizeList

#Creates the Objects
task_list = ToDoList()
pieChart= visualizeList(task_list)

#Run Until user quits
running = True
while running:
    print("\nHello!")
    #Chose option
    start = input('[1] Add task \n[2] Remove task \n[3] Complete task \n[4] See list \n[5] Visualize in chart \n[6] Quit \nWhat would you like to do? ')

    #Adding a task
    if start.lower() == "1":
        #Takes name
        new_name = input("\nWhat would you like the name of this task to be? ")
        print("\nSet the date for your task")
        #Takes time and creates time object
        hour = int(input("What hour is this task due?(0-23) "))
        minute = int(input("What minute is this task due?(0-59) "))
        second = int(input("What second is this task due?(0-59) "))
        new_due = datetime.time(hour, minute, second)
        #Create Item object with name and time
        new_item = Item(new_name, new_due)
        #Add to toDoList
        task_list.items.append(new_item)
        print("\nThe task has been added to your to-do list!")

    #Remove a task
    elif start == "2":
        counter = 0
        #Print every current item/task
        for length in task_list.items:
            print(f"[{counter}] {length.item_name}")
            counter+=1
        remove = int(input("Which task would you like to remove? "))
        #Removes item
        del task_list.items[remove]

    #Complete a task
    elif start == "3":
        #Print all not completed items
        counter = 0
        for length in task_list.items:
            print(f"[{counter}] {length.item_name}")
            counter += 1
        done = int(input("Which task have you completed?"))
        #completes the item
        task_list.items[done].complete_item()
        task_list.CheckComplete()

    #See List
    elif start.lower() == "4":
        print("\nHere is your current list of to-dos:")
        #Prints everything
        for item in task_list.items:
            print(f"\t{item.item_name}; due at {item.time_due}")

    #Displays Pi Chart
    elif start.lower() == "5":

        pieChart.pieChartVisualize()

    #Quit
    elif start == "6":
        print("\nAll set? See you next time!")
        running = False

    #Wrong input
    else:
        print("\nPlease enter a valid input")
