from item import Item
from toDoList import ToDoList
from visualizeList import visualizeList

task_list = ToDoList()
running = True
while running:
    print("\nHello!")
    start = input('[1] Add task \n[2] Remove task \n[3] Complete task \n[4] See list \n[5] Visualize in chart \n[6] Quit \nWhat would you like to do? ')
    if start.lower() == "1":
        new_name = input("\nWhat would you like the name of this task to be? ")
        new_due = int(input("What would you like to set the due date as? "))
        new_item = Item(new_name, new_due)
        task_list.items.append(new_item)
        print("\nThe task has been added to your to-do list!")

    elif start == "2":
        counter = 0
        for length in task_list.items:
            print(f"[{counter}] {length.item_name}")
            counter+=1
        remove = int(input("Which task would you like to remove? "))
        del task_list.items[remove]

    elif start == "3":
        counter = 0
        for length in task_list.items:
            print(f"[{counter}] {length.item_name}")
            counter += 1
        done = int(input("Which task have you completed?"))
        task_list.items[done].complete_item()
        task_list.CheckComplete()


    elif start.lower() == "4":
        print("\nHere is your current list of to-dos:")
        for item in task_list.items:
            print(f"\t{item.item_name}; due at {item.time_due}")


    #elif start.lower() == "3":
        #VISUALIZE: needs filling in lol

    elif start == "5":
        print("\nAll set? See you next time!")
        running = False

    else:
        print("\nPlease enter a valid input")