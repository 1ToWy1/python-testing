class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        task_name = task.strip()
        if not task_name:
            print("Ошибка: Название задачи не может быть пустым.")
            return

        if task_name in self.tasks:
            print(f"Задача '{task_name}' уже есть в списке.")
            return

        self.tasks[task_name] = False
        print(f"Задача '{task_name}' успешно добавлена.")

    def complete_task(self, task):
        task_name = task.strip()
        if task_name not in self.tasks:
            print(f"Ошибка: Задача '{task_name}' не существует.")
            return

        self.tasks[task_name] = True
        print(f"Задача '{task_name}' отмечена как выполненная.")

    def remove_task(self, task):
        task_name = task.strip()
        if task_name not in self.tasks:
            print(f"Ошибка: Задача '{task_name}' не существует.")
            return

        del self.tasks[task_name]
        print(f"Задача '{task_name}' успешно удалена.")

    def list_tasks(self):
        if not self.tasks:
            print("Список задач пуст.")
            return

        print("\n--- Список задач ---")
        for task, is_completed in self.tasks.items():
            status_symbol = "[✓]" if is_completed else "[ ]"
            print(f"{status_symbol} {task}")


if __name__ == "__main__":
    todo = ToDoList()

    todo.add_task("Купить продукты")
    todo.add_task("Изучить ООП в Python")
    todo.add_task("Сделать уборку")

    todo.list_tasks()

    todo.complete_task("Изучить ООП в Python")
    todo.complete_task("Полететь в космос")

    todo.remove_task("Сделать уборку")
    todo.remove_task("Помыть машину")

    todo.list_tasks()
