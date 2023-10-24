#!/usr/bin/python3
"""
This module retrieves data from a REST API.
"""
from requests import get
from sys import argv
import csv


if (__name__ == "__main__"):
    empid = argv[1]
    emp_url = f"https://jsonplaceholder.typicode\
.com/users/{empid}"
    tasks_url = f"https://jsonplaceholder.typicode\
.com/users/{empid}/todos/"
    username = ""
    todos, item = [], []

    with get(emp_url) as response:
        if (response.status_code == 200):
            username = response.json().get("username")

    with get(tasks_url) as response:
        if (response.status_code == 200):
            todos = response.json()

    with open(f"{empid}.csv", "w", encoding="utf-8") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            item.append(empid)
            item.append(username)
            item.append(todo.get("completed"))
            item.append(todo.get("title"))
            writer.writerow(item)
            item = []
