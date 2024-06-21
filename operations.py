import datetime
import json
import os
from utility import load_tasks,save_tasks,load_last_id, save_last_id

class Operations:

    def generate_task_id():
        task_id = load_last_id() + 1
        save_last_id(task_id)
        return task_id
    
    def add_task(tasks):
        task_id = Operations.generate_task_id()
        description = input('Enter task description: ')
        due_date = input('Enter due date (YYYY-MM-DD): ')
        try:
            due_date = datetime.datetime.strptime(due_date, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format! Please enter date in YYYY-MM-DD format.")
            return
        if due_date < datetime.date.today():
            print("Due date cannot be in the past! Please enter a valid due date.")
            return
        priority = input('Enter priority from high to low(1-5): ')
        status = 'pending'
        
        task = {
            'task_id': task_id,
            'description': description,
            'due_date': due_date.isoformat(),
            'priority': priority,
            'status': status
        }
        tasks.append(task)
        save_tasks(tasks)

    def view_tasks(tasks):
        for task in tasks:
            print(f"ID: {task['task_id']}, Description: {task['description']}, Due Date: {task['due_date']}, Priority: {task['priority']}, Status: {task['status']}")

    def update_task(tasks):
        task_id = int(input('Enter task ID to update: '))
        for task in tasks:
            if task['task_id'] == task_id:
                print(f"ID: {task['task_id']}, Description: {task['description']}, Due Date: {task['due_date']}, Priority: {task['priority']}, Status: {task['status']}")
                task['description'] = input('Enter new description: ')
                new_dueDate = input('Enter new due date (YYYY-MM-DD): ')
                new_dueDate = datetime.datetime.strptime(new_dueDate, '%Y-%m-%d').date()
                task['due_date'] = new_dueDate.isoformat()
                task['priority'] = input('Enter new priority (1-5): ')
                task['status'] = input('Enter new status (pending/completed): ')
                save_tasks(tasks)
                return
        print(f"Task with ID {task_id} not found.")

    def delete_task(tasks):
        task_id = int(input('Enter task ID to delete: '))
        tasks = [task for task in tasks if task['task_id'] != task_id]
        save_tasks(tasks)
        return tasks

    def DisplayTasks(tasks):
        for task in tasks:
            print(f"Task ID: {task['task_id']}")
            print(f"Description: {task['description']}")
            print(f"Due Date: {task['due_date']}")
            print(f"Priority: {task['priority']}")
            print(f"Status: {task['status']}")
            print()

    def DueDateSort(tasks):
        return sorted(tasks, key=lambda x: datetime.datetime.strptime(x['due_date'], '%Y-%m-%d').date())

    def PrioritySort(tasks):
        return sorted(tasks, key=lambda x: x['priority'])

    def StatusSort(tasks):
        return sorted(tasks, key=lambda x: x['status'])

    def PendingFilter(tasks):
        return [task for task in tasks if task['status'] == 'pending' and datetime.datetime.strptime(task['due_date'], '%Y-%m-%d').date() >= datetime.date.today()]

    def CompletedFilter(tasks):
        return [task for task in tasks if task['status'] == 'completed']


