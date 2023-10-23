#!/usr/bin/python3
"""This script send request to get employees done data"""
import requests
import sys


def get_employee_progress(employee_id):
    """this method sends http request to get response data"""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        user_data = user_response.json()
        todo_data = todo_response.json()

        if (user_response.status_code == 200 and
                todo_response.status_code == 200):
            employee_name = user_data["name"]

            done_tasks = [
                task["title"] for task in todo_data if task["completed"]
            ]
            total_tasks = len(todo_data)

            results = (
                f"Employee {employee_name} is done with tasks "
                f"({len(done_tasks)}/{total_tasks}):"
            )
            print(results)

            for task_title in done_tasks:
                print(f"\t{task_title}")
        else:
            print("Request failed")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
    else:
        employee_id = int(sys.argv[1])
        get_employee_progress(employee_id)