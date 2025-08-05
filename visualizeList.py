from toDoList import ToDoList
import matplotlib.pyplot as plt

class visualizeList:
    def __init__(self, arrToDoList):
        self.arrToDoList = arrToDoList


    def pieChartVisualize(self, listNum):
        fig, ax = plt.subplots(figsize=(10, 5))


        labels = 'Not Completed', 'Completed'
        currentList = self.arrToDoList[listNum]
        notComplete = len(currentList.items)-currentList.how_many_completed


        sizes = [notComplete, currentList.how_many_completed]

        wedges, texts = ax.pie(sizes, labels=labels)
        ax.legend(wedges, labels,
                  title="Items",
                  loc="right",
                  bbox_to_anchor=(1, 0, 0.6, 1))
        ax.set_title("Today's To Do List")





v = visualizeList(6)

v.pieChartVisualize(6)
plt.show()
