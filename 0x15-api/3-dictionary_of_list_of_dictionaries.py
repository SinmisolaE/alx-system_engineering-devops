#!/usr/bin/python3
"""  task #0, extend your Python script to export data in the JSON format"""
import sys
import requests
import json

if __name == '__main__':
    userId = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json") as f:
        f.dump({u.id: [{
		"username": u.get(name),
		"task": t.get("title"),
		"completed": t.get("completed")
		} for t in requests.get(url + "todos",
					param={"userId": u.id})]
		for u in users, f)
