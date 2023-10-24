#!/usr/bin/python3
"""
This module retrieves data from a REST API
and export the data to a JSON file.
"""
from requests import get
from sys import argv
from json import dumps


if (__name__ == "__main__"):
    empid = argv[1]
    emp_url = f"https://jsonplaceholder.typicode\
.com/users/{empid}"
    tasks_url = f"https://jsonplaceholder.typicode\
.com/users/{empid}/todos/"
    username = ""
    todos, emp_details_list = [], []
    emp_details, emp_details_dict = {}, {}

    with get(emp_url) as response:
        if (response.status_code == 200):
            username = response.json().get("username")

    with get(tasks_url) as response:
        if (response.status_code == 200):
            todos = response.json()

    for todo in todos:
        emp_details_dict["task"] = todo.get("title")
        emp_details_dict["completed"] = todo.get("completed")
        emp_details_dict["username"] = username
        emp_details_list.append(emp_details_dict)
        emp_details_dict = {}

    emp_details[empid] = emp_details_list

    with open(f"{empid}.json", "w", encoding="utf-8") as file:
        file.write(dumps(emp_details))
