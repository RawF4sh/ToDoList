from toDoList import ToDoList
import matplotlib.pyplot as plt

class visualizeList:
    def __init__(self, arrToDoList):
        self.arrToDoList = arrToDoList


    def pieChartVisualize(self, listNum):
        labels = 'Not Completed', 'Completed'
        sizes = [len(self.arrToDoList[listNum])-self.arrToDoList[listNum].how_many_completed, self.arrToDoList[listNum].how_many_completed]

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels)



