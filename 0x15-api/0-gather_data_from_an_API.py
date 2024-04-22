#!/usr/bin/python3
"""using this REST API, for a given employee ID,
    returns information about his/her TODO list progress"""

import requests
import sys

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    to_do = requests.get(url + "todos",
                         params={"userId": sys.argv[1]}).json()
    complete = [task.get("title") for task in to_do
                if task.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(complete), len(to_do)))
    [print("\t {}".format(t)) for t in complete]
