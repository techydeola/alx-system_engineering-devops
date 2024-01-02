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
    name = data['username']

    todo_resp = requests.get("https://jsonplaceholder.typicode.com/users/" +
                             f"{employee_id}/todos")
    todo_data = todo_resp.json()

    with open('USER_ID.csv', 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        for data in todo_data:
            my_list = [str(data['userId']),
                       str(name),
                       str(data['completed']),
                       str(data['title'])]
            writer.writerow(my_list)
