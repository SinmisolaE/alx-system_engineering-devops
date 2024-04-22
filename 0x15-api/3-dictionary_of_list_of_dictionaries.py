#!/usr/bin/python3
"""  task #0, extend your Python script to export data in the JSON format"""

import requests
import json

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", 'w') as f:
        json.dump({u.get("id"): [{
            "username": u.get("username"),
            "task": t.get("title"),
            "completed": t.get("completed")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, f)
