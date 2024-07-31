import sqlite3
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

def create_task(description):
    cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, 0)", (description,))
    conn.commit()
def list_tasks():
    cursor.execute("SELECT id, description, completed FROM tasks")
    tasks = cursor.fetchall()
    for task in tasks:
        print(f"ID: {task[0]}, Description: {task[1]}, Completed: {'Yes' if task[2] else 'No'}")
def mark_completed(task_id):
    cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    
list_tasks()