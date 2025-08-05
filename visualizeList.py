from toDoList import ToDoList
import matplotlib.pyplot as plt

class visualizeList:
    def __init__(self, toDoListItem ):
        self.toDoListItem = toDoListItem
        completedNames = ""
        incompleteNames = ""


    def namesOfItems(self):
        currentList = self.toDoListItem
        for i in range(len(currentList.completed_items)):
            self.completedNames += currentList.completed_items[i].item_name+"\n"
        for i in range(len(currentList.items)):
            self.incompleteNames+= currentList.completed_items[i].item_name+"\n"

    def pieChartVisualize(self):
        fig, ax = plt.subplots(figsize=(10, 5))


        labels = 'Not Completed', 'Completed'
        currentList = self.toDoListItem
        notComplete = len(currentList.items)-currentList.how_many_completed

        items = self.incompleteNames, self.completedNames
        sizes = [notComplete, currentList.how_many_completed]

        wedges, texts = ax.pie(sizes, labels=labels)
        ax.legend(wedges, items,
                  title="Items",
                  loc="right",
                  bbox_to_anchor=(1, 0, 0.6, 1))
        ax.set_title("Today's To Do List")
