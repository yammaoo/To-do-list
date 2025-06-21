# To-Do List App (Python CLI)

This is a simple and effective command-line To-Do List application built in Python. It allows users to manage their daily tasks with features like due dates, categories, task sorting, and automatic saving/loading.

---

## Key Features

- Add multiple tasks at once with optional due dates and categories
- View all tasks with completion status, due dates, and categories
- Mark tasks as complete or incomplete
- Delete tasks by their number
- Sort tasks by due date, status, or category
- Tasks are saved locally and automatically loaded on next run

---

## How It Works

Upon running the app, you'll interact with a simple menu system in your terminal. You can view your tasks, add new ones, delete, update their status, and sort them for better visibility.

All tasks are saved in a local file named `tasks.json`. This file is automatically created and used by the program to store your task list so your data is preserved between sessions.

---

## Task Information

Each task includes:
- A title (required)
- A due date (optional)
- A category (optional)
- Completion status (complete or incomplete)

---

## Task Sorting Options

You can sort tasks by:
- **Due Date** – Earliest first
- **Status** – Incomplete tasks shown before completed ones
- **Category** – Alphabetical order of categories

---

## Data Storage

The app saves your tasks in a file called `tasks.json`. This file is updated whenever you save or exit the program.

Note: If you are sharing this project publicly, you may want to exclude the `tasks.json` file from version control to protect your personal task data.

---

## Project Structure

- `todo.py` – The main Python file containing all app functionality
- `tasks.json` – Auto-generated file storing your task data
- `README.md` – This documentation

---

## Notes

- No internet connection is required to use this app
- Designed for personal productivity
- Works on any system with Python installed

---

## Future Enhancements

- Graphical user interface (GUI) version
- Task notifications/reminders
- Multi-user support

---
