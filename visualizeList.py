from toDoList import ToDoList
import matplotlib.pyplot as plt

class visualizeList:
    def __init__(self, arrToDoList):
        self.arrToDoList = arrToDoList


    def pieChartVisualize(self, listNum):
        fig, ax = plt.subplots()

        labels = 'Not Completed', 'Completed'
        currentList = self.arrToDoList[listNum]
        notComplete = len(currentList.items)-currentList.how_many_completed

        sizes = [notComplete, currentList.how_many_completed]

        wedges, texts, autotexts = ax.pie(sizes     , textprops=dict(color="w"))
        ax.set_title("Today's To Do List")


        ax.pie(sizes, labels=labels)



