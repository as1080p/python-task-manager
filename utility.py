import datetime
import json
import os

FILE_NAME = 'tasks.json'
ID_FILE = 'task_id.txt'

def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as file:
        json.dump(tasks, file, indent=4)

def load_last_id():
    if os.path.exists(ID_FILE):
        with open(ID_FILE, 'r') as file:
            return int(file.read().strip())
    return 0

def save_last_id(task_id):
    with open(ID_FILE, 'w') as file:
        file.write(str(task_id))