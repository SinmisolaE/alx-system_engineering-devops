#!/usr/bin/python3
""" extending task0 to export data in the CSV format"""
import sys
import csv
import requests

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    to_do = requets.get(url + "todos", params={"userId": sys.argv[1]}).json()
    complete = [task.get("title") for task in to_do if task.get("completed") is True]

    userId = sys.argv[1]
    with open("{}.csv".format(userId)) as f:
        writ = csv.writer(f, quoting=QUOTE_ALL)
        [writ.writer([userId, user.get(name), t.get("completed"), t.get("title")])
         for t in to_do]
