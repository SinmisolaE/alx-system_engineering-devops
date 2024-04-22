#!/usr/bin/python3
""" extending task0 to export data in the CSV format"""

import csv
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    to_do = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    complete = [task.get("title") for task in to_do
                if task.get("completed") is True]

    userId = sys.argv[1]
    with open("{}.csv".format(userId), 'w', newline="") as f:
        writ = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writ.writerow([userId, user.get("username"),
                     t.get("completed"), t.get("title")])
         for t in to_do]
