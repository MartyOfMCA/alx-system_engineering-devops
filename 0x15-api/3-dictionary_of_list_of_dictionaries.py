#!/usr/bin/python3
"""
This module retrieves data from a REST API
and export the data to a JSON file.
"""
from requests import get
from json import dumps


if (__name__ == "__main__"):
    empid = 0

    emp_url = f"https://jsonplaceholder.typicode\
.com/users/"
    username = ""
    details, emp_details_list = [], []
    todos, emp_details, emp_details_dict = {}, {}, {}

    with get(emp_url) as response:
        if (response.status_code == 200):

            for user in response.json():
                username = user.get("username")
                empid = user.get("id")
                tasks_url = f"https://jsonplaceholder.typicode\
.com/users/{empid}/todos/"

                with get(tasks_url) as response:
                    if (response.status_code == 200):
                        todos = response.json()

                        emp_details_list = []
                        emp_details_dict = {}

                        for todo in todos:
                            emp_details_dict["username"] =\
                                username
                            emp_details_dict["task"] =\
                                todo.get("title")
                            emp_details_dict["completed"] =\
                                todo.get("completed")

                            emp_details_list.append(emp_details_dict)
                            emp_details_dict = {}

                        emp_details[empid] = emp_details_list

    with open(f"todo_all_employees.json", "w",
              encoding="utf-8") as file:
        file.write(dumps(emp_details))
