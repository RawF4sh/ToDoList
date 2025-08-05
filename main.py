from item import Item
from toDoList import ToDoList
from datetime import time

dateTime = time(10,30)

while True:
    inp = input("Add Item[1], Quit[2]")
    if inp == "2":
        break
    elif inp == "1":
        hour = input("What hour is it due")
        minute = input("What minute is it due")