import sys
import json
from pathlib import Path
from platformdirs import user_data_dir

APP_NAME = "task_manager"
DATA_FILE = "data.json"


def get_task_file():
    data_dir = Path(user_data_dir(APP_NAME))
    data_dir.mkdir(parents=True, exist_ok=True)

    tasks_file = data_dir / DATA_FILE

    if not tasks_file.exists():
        tasks_file.write_text("[]")

    return tasks_file


def load_tasks():
    tasks_file = get_task_file()

    with open(tasks_file, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    tasks_file = get_task_file()

    with open(tasks_file, "w") as f:
        json.dump(tasks, f, indent=4)


def delete_task_file():
    tasks_file = get_task_file()

    if tasks_file.exists():
        tasks_file.unlink()
        print("Deleted:", tasks_file)
    else:
        print("File does not exist")


def add_task(input_task_list):
    task = " ".join(input_task_list)

    if not task:
        print("Task cannot be empty")
        return

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)

    print(f'Added task: "{task}"')


class Task_Manager:
    def __init__(self, commands):
        self.commands = commands
        self.command_execute()

    def command_execute(self):
        if not self.commands:
            print("Usage:")
            print("  task-manager read")
            print("  task-manager add <task>")
            print("  task-manager reset")
            return

        command = self.commands[0]

        if command == "read":
            tasks = load_tasks()

            if not tasks:
                print("No tasks found.")
                return

            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

        elif command == "add":
            add_task(self.commands[1:])

        elif command == "reset":
            delete_task_file()

        else:
            print(f"Unknown command: {command}")


def main():
    commands = sys.argv[1:]
    Task_Manager(commands)