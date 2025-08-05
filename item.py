from tensorflow.python.ops.metrics_impl import false_negatives
from datetime import datetime


class Item:
    def __init__(self, item_name, time_due):
        self.item_name = item_name
        # self.time_created=time_created
        self.time_due = time_due
        self.time_finished = 0
        self.completed = False
        self.on_time = False

    def complete_item(self):
        if (input("Did you finish this task, yes or no? ") == "yes"):
            self.completed = True
            self.time_finished = datetime.now()

    def late_work_check(self):
        if self.time_due >= self.time_finished:
            self.on_time = True

    def __str__(self):
        return ("Task Name: " + self.item_name + "Due Date: " + self.time_due + "Completion Status: " + (
            "Complete" if self.completed else "Incomplete"))
