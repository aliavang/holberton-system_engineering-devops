#!/usr/bin/python3
"""
Export data in the JSON format
"""
import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    req = requests.get(url)
    res = req.json()
    usr = res.get("username")

    url = "https://jsonplaceholder.typicode.com/todos?userId=" + sys.argv[1]
    req = requests.get(url)
    res = req.json()
    j_dict = {}
    n_list = []
    with open(sys.argv[1] + '.json', 'w') as data:
        for item in res:
            j_data = {}
            if sys.argv[1] == str(item.get("userId")):
                stat = item.get("completed")
                title = item.get("title")
                j_data.update({"task": title, "completed": stat,
                               "username": usr})
                n_list.append(j_data)
        j_dict[sys.argv[1]] = n_list
        json.dump(j_dict, data)
