import datetime
import json
import os
from operations import Operations
from utility import load_tasks,save_tasks

def main():
    tasks = load_tasks()

    while True:
        print('--------TASK MANAGER USING PYTHON--------')
        print('What operation would you like to perform?')
        print('1. Create new tasks')
        print('2. Read tasks')
        print('3. Update tasks')
        print('4. Delete tasks')
        print('5. Exit task manager')
        choice = input('Enter the number:')
        if(choice == '1'):
            Operations.add_task(tasks)
        elif(choice == '2'):
            print('i. Read all tasks')
            print('ii. Sort tasks')
            print('iii. Check pending and completed tasks')
            read_choice = input('Enter your choice:')
            if(read_choice == 'i'):
                Operations.view_tasks(tasks)
            elif(read_choice == 'ii'):
                print('Sort by:')
                print('a. Due Date')
                print('b. Priority')
                print('c. Status')
                sort_choice = input('Enter choice:')
                if(sort_choice == 'a'):
                    print("Tasks sorted by Due Date:")
                    Operations.DisplayTasks(Operations.DueDateSort(tasks))
                elif(sort_choice == 'b'):
                    print("Tasks sorted by Priority:")
                    Operations.DisplayTasks(Operations.PrioritySort(tasks))
                elif(sort_choice == 'c'):
                    print("Tasks sorted by Status:")
                    Operations.DisplayTasks(Operations.StatusSort(tasks))
                else:
                    print('Invalid choice! Please try again.')
            elif(read_choice == 'iii'):
                print('a. Pending tasks')
                print('b. Completed tasks')
                filter_choice = input('Enter choice:')
                if(filter_choice == 'a'):
                    print("Pending Tasks:")
                    Operations.DisplayTasks(Operations.PendingFilter(tasks))
                elif(filter_choice == 'b'):
                    print("Completed Tasks:")
                    Operations.DisplayTasks(Operations.CompletedFilter(tasks))
                else:
                    print('Invalid choice! Please try again.')            
        elif(choice == '3'):
            Operations.update_task(tasks)
        elif(choice == '4'):
            tasks = Operations.delete_task(tasks)
        elif(choice == '5'):
            break
        else:
            print('Invalid choice! Please try again.')

if __name__ == "__main__":
    main()