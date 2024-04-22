#!/usr/bin/python3
""" extend your Python script to export data in the JSON format"""
import sys
import json
import requests

if __name__ == '__main__':
    userId = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url + "users/{}".format(userId)).json()
    to_do = requests.get(url + "todos", params={"userId": userId}).json()

    with open("{}.json".format(userId)) as f:
        json.dump({userId: [{
		"task": t.get("title"),
		"completed": t.get("completed"),
		"username": user.name
		} for t in to_do]}, f)
