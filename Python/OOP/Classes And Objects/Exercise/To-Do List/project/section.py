from project.task import Task

class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for k in range(0, len(self.tasks)):
            if self.tasks[k].name == task_name:
                self.tasks[k].completed = True
                return f"Completed task {task_name}"
        
        return f"Could not find task with the name {task_name}"

    def clean_section(self):
        k = 0
        removedTasks = 0

        while k < len(self.tasks):
            if self.tasks[k].completed == True:
                removedTasks += 1
                del self.tasks[k]
            else:
                k += 1

        return f"Cleared {removedTasks} tasks."

    def view_section(self):
        output = f"Section {self.name}:\n"
        
        for k in range(0, len(self.tasks)):
            output += self.tasks[k].details()

            if k != len(self.tasks) - 1:
                output += "\n"
        
        return output