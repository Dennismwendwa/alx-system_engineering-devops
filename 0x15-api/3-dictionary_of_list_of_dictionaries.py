#!/usr/bin/python3
"""This script exports all employees data to json file"""
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 1:
        print("Usage: python3 3-dictionary_of_list_of_dictionaries.py")
        sys.exit(1)

    def get_data(res, par=None):
        """get user"""
        url = "https://jsonplaceholder.typicode.com/"
        url += res

        if par:
            url += ("?" + par[0] + "=" + par[1])

        re = requests.get(url)

        re = re.json()
        return re

    data_e = {}
    users = get_data("users")
    for user in users:
        user_id = user["id"]
        data_e.update({user_id: []})
        tasks_by_user = get_data("todos", ("userId", str(user_id)))
        for task in tasks_by_user:
            data_e[user_id].append({"username": user["username"],
                                    "task": task["title"],
                                    "completed": task["completed"]})


    with open("todo_all_employees.json", mode="w") as json_file:
        json.dump(data_e, json_file)  # added indent=4 better format

    print("Data exported to todo_all_employees.json")
