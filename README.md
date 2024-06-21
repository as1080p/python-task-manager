# Task Manager using Python
## Overview
This project is a command-line application built in Python that allows users to manage their tasks efficiently. It provides functionalities to create, read, update, and delete tasks, as well as to sort and filter tasks based on various criteria such as due date, priority level, and status (pending/completed).

## Features
* CRUD Operations: Perform Create, Read, Update, and Delete operations on tasks.
* Sorting: Sort tasks by due date, priority level, or status.
* Filtering: Filter tasks to display only pending or completed tasks.
* Unique Task IDs: Automatically assigns unique IDs to each task to ensure identification.
* Data Persistence: Utilizes JSON file storage to persist tasks between sessions.
* User-Friendly Interface: Simple command-line interface with clear prompts for user interaction.

## Project Structure
- main.py: Entry point that handles user input and manages the application flow.
- operations.py: Contains the Operations class with methods for task management operations.
- utility.py: Provides utility functions for loading and saving tasks to a JSON file.
- tasks.json: Stores the list of tasks.
- task_id.txt: Keeps track of the last used task ID to ensure uniqueness.

## Getting Started
To run the Task Manager:
1. Clone the repository: git clone
2. Navigate to the project directory: cd Task-Manager
3. Run python main.py to start the application.
4. Follow the prompts to manage your tasks efficiently.

## License
This project is licensed under the MIT License.


