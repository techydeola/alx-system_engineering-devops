#!/usr/bin/python3
""" This is a module that consumes an API """


if __name__ == ('__main__'):
    import csv
    import json
    import requests
    import sys

    employee_id = sys.argv[1]
    response = requests.get("https://jsonplaceholder.typicode.com/users/" +
                            f"{employee_id}")
    data = response.json()
    username = data['username']

    todo_resp = requests.get("https://jsonplaceholder.typicode.com/users/" +
                             f"{employee_id}/todos")
    todo_data = todo_resp.json()
    my_list = []
    for task in todo_data:
        my_dict = {"task": task['title'], "completed": task['completed'],
                   "username": username}
        my_list.append(my_dict)
    json_dict = {f"{employee_id}": my_list}

    with open(f'{employee_id}.json', 'w') as file:
        file.write(json.dumps(json_dict))
