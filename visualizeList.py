#from toDoList import toDoList
import matplotlib.pyplot as plt

class visualizeList:
    def __init__(self, arrToDoList):
        self.arrToDoList = arrToDoList


    def pieChartVisualize(self, listNum):
        #labels = 'Not Completed', 'Completed'
        #sizes = [len(self.arrToDoList[listNum])-self.arrToDoList[listNum].how_many_complete, self.arrToDoList[listNum].how_many_complete]

       #fig, ax = plt.subplots()
        #ax.pie(sizes, labels=labels)
        labels = 'Complete', 'Incomplete'
        sizes = [5,15]

        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels)


a = visualizeList("f")

a.pieChartVisualize(5)

plt.show()