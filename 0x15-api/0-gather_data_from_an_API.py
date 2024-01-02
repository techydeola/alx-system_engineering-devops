#!/usr/bin/python3
""" This is a module that consumes an API """


if __name__ == ('__main__'):
    import json
    import requests
    import sys

    employee_id = sys.argv[1]
    response = requests.get("https://jsonplaceholder.typicode.com/users/" +
                            f"{employee_id}")
    data = response.json()
    name = data['name']

    todo_resp = requests.get("https://jsonplaceholder.typicode.com/users/" +
                             f"{employee_id}/todos")
    todo_data = todo_resp.json()

    all_task = 0
    completed_task = 0

    for task in todo_data:
        if task['completed'] is True:
            completed_task += 1
        all_task += 1

    print(f"Employee {name} is done with tasks" +
          f"({completed_task}/{all_task}):")
    for task in todo_data:
        if task['completed'] is True:
            title = task['title']
            print(f"\t{title}")
