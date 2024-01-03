#!/usr/bin/python3
""" This is a module stores all employees data from an API to json """


if __name__ == ('__main__'):
    import csv
    import json
    import requests

    response = requests.get("https://jsonplaceholder.typicode.com/users/")
    data = response.json()
    id_list = []
    for user in data:
        employee_id = user['id']
        id_list.append(employee_id)

    todo_resp = requests.get("https://jsonplaceholder.typicode.com/todos")
    todo_data = todo_resp.json()
    json_dict = {}

    for user_id in id_list:
        my_list = []
        for user_todo in todo_data:
            if user_id == user_todo['userId']:
                for item in data:
                    if user_id == item['id']:
                        username = item['username']
                my_dict = {f"username": username, "task": user_todo['title'],
                           "completed": user_todo['completed']}
                my_list.append(my_dict)
        json_dict.update({f"{user_id}": my_list})

    with open(f'todo_all_employees.json', 'w') as file:
        file.write(json.dumps(json_dict))
