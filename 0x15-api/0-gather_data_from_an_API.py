#!/usr/bin/python3
"""
For a given employee ID, returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/todos/" + sys.argv[1]
    req = requests.get(url)
    res = req.json()
    usr = res.get("name")

    url = "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    req = requests.get(url)
    tot = 0
    done = 0
    tasks = []
    for task in req.json():
        if task.get("completed"):
            done += 1
            tasks.append(task.get("title"))
        tot += 1
    print("Employee {} is done with task({}/{}):".format(usr, done, tot))
    for task in tasks:
        print("\t {}".format(task))
