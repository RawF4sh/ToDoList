from toDoList import ToDoList
import matplotlib.pyplot as plt

class visualizeList:
    def __init__(self, toDoListItem ):
        self.toDoListItem = toDoListItem
        #self.completedNames = ""
        #self.incompleteNames = ""


    #def setNamesOfItems(self):

        #currentList = self.toDoListItem
        #for i in range(len(currentList.completed_items)):
            #self.completedNames += currentList.completed_items[i].item_name+"\n"
        #for i in range(len(currentList.items)):
           # self.incompleteNames+= currentList.items[i].item_name+"\n"

    def pieChartVisualize(self):
        fig, ax = plt.subplots(figsize=(10, 5))

        #Labels for pi chart and legend
        labels = ['Not Completed', 'Completed']
        currentList = self.toDoListItem

        #items = [self.incompleteNames, self.completedNames]

        #How many not complete and complete items
        sizes = [len(currentList.items), currentList.how_many_completed]

        #Creates the pie charts with the pie chart labels and percentages
        wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

        #Creates a legend
        ax.legend(wedges, labels,
                  title="Items",
                  loc="right",
                  bbox_to_anchor=(1, 0, 0.6, 1))

        #Title
        ax.set_title("Today's To Do List")

        #Shows the Window
        plt.show()
