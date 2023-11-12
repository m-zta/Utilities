"""
This script takes a set of tasks and a set of workers and divides the tasks randomly among the workers.
"""

import sys
import random

def print_dict(dictionary):
    """ Print the dictionary """

    print(50 * "=")
    print("Results:\n")

    for key in dictionary:
        print(f"{key}: {dictionary[key]}")


def divide_tasks(workers, tasks):
    """ For each worker create a list of tasks """

    # Create a dictionary of workers
    worker_dict = {}
    for worker in workers:
        worker_dict[worker] = []

    # Divide the tasks
    while len(tasks) > 0:
        for worker in worker_dict:
            task = random.choice(tasks)
            worker_dict[worker].append(task)
            tasks.remove(task)

            if len(tasks) == 0:
                break

    return worker_dict 


def get_items(name):
    print(f"Enter the {name}. Press enter without typing anything to stop.")

    # Get the tasks
    count = 1
    tasks = []
    while True:
        print(tasks)
        task = input(f"{count}: ")

        if task == '':
            break
        
        tasks.append(task)
        count += 1

    # Return the tasks
    return tasks

def main():
    """ Main function """

    # Get the tasks
    tasks = get_items("tasks")
    # tasks = ["Document", "Editor", "EnumCommands", "Index", "Logger", "InputOutput", "OutputFormat", "Parser", "Starter"]

    # Get the workers
    workers = get_items("workers")
    # workers = ["Worker1", "Worker2", "Worker3", "Worker4"]

    # Divide the tasks
    worker_dict = divide_tasks(workers, tasks)

    # Print the results
    print_dict(worker_dict)

if __name__ == '__main__':
    main()
