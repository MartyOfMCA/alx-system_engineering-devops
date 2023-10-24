#!/usr/bin/python3
"""
This module retrieves data from a REST API.
"""
from requests import get
from sys import argv


if (__name__ == "__main__"):
    empid = argv[1]
    emp_url = f"https://jsonplaceholder.typicode\
.com/users/{empid}"
    tasks_url = f"https://jsonplaceholder.typicode\
.com/users/{empid}/todos/"
    emp_name, completed, total = "", 0, 0
    todos = []

    with get(emp_url) as response:
        if (response.status_code == 200):
            emp_name = response.json().get("name")

    with get(tasks_url) as response:
        if (response.status_code == 200):
            todos = response.json()
            for todo in todos:
                if (todo.get("completed")):
                    completed += 1

    total = len(todos)
    print(f"Employee {emp_name} is done \
with tasks({completed}/{total}):")
    for todo in todos:
        if (todo.get("completed")):
            print(f"\t {todo.get('title')}")
