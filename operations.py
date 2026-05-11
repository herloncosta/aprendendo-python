from database import get_connection


def add(title):
    with get_connection() as conn:
        sql = "INSERT INTO tasks (title) VALUES (?)"
        cursor = conn.execute(sql, (title,))
        return cursor.lastrowid


def remove(task_id):
    with get_connection() as conn:
        sql = "DELETE FROM tasks WHERE id = ?"
        cursor = conn.execute(sql, (task_id,))
        return cursor.rowcount > 0


def edit(task_id, new_title):
    with get_connection() as conn:
        sql = "UPDATE tasks SET title = ? WHERE id = ?"
        cursor = conn.execute(sql, (new_title, task_id))
        return cursor.rowcount > 0


def list_one(task_id):
    with get_connection() as conn:
        sql = "SELECT * FROM tasks WHERE id = ?"
        rows = conn.execute(sql, (task_id,))

        for row in rows:
            if (row["completed"] == 1):
                isCompleted = "Sim"
            else:
                isCompleted = "Não"

            print(f'Tarefa: {row["title"]} | Concluída: {isCompleted}')


def mark_completed(task_id):
    with get_connection() as conn:
        sql = "UPDATE tasks SET completed = 1 WHERE id = ?"
        cursor = conn.execute(sql, (task_id,))
        return cursor.rowcount > 0


def mark_uncompleted(task_id):
    with get_connection() as conn:
        sql = "UPDATE tasks SET completed = 0 WHERE id = ?"
        cursor = conn.execute(sql, (task_id,))
        return cursor.rowcount > 0


def list_all():
    with get_connection() as conn:
        sql = "SELECT id, title, completed FROM tasks"
        rows = conn.execute(sql).fetchall()

        for row in rows:
            if (row["completed"] == 1):
                isCompleted = "Sim"
            else:
                isCompleted = "Não"

            print(f'Tarefa: {row["title"]} | Concluída: {isCompleted}')


def list_completed():
    with get_connection() as conn:
        sql = "SELECT id, title, completed FROM tasks WHERE completed = 1"
        rows = conn.execute(sql).fetchall()

        isCompleted = ""

        for row in rows:
            if (row["completed"] == 1):
                isCompleted = "Sim"
            else:
                isCompleted = "Não"

            print(f'Tarefa: {row["title"]} | Concluída: {isCompleted}')


def list_pending():
    with get_connection() as conn:
        sql = "SELECT id, title, completed FROM tasks WHERE completed = 0"
        rows = conn.execute(sql).fetchall()

        isCompleted = ""

        for row in rows:
            if (row["completed"] == 1):
                isCompleted = "Sim"
            else:
                isCompleted = "Não"

            print(f'Tarefa: {row["title"]} | Concluída: {isCompleted}')
