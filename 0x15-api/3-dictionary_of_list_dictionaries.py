#!/usr/bin/python3
"""
Export data in the JSON format
"""
import json
import requests


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users/"
    req = requests.get(url)
    res = req.json()

    j_dict = {}
    for user in res:
        n_list = []
        url2 = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            user.get("id"))
        req2 = requests.get(url2)
        res2 = req2.json()
        for item in res2:
            j_data = {}
            usr = user.get("username")
            title = item.get("title")
            stat = item.get("completed")
            j_data.update({"username": usr, "task": title,
                          "completed": stat})
            n_list.append(j_data)
        j_dict[user.get("id")] = n_list
    with open('todo_all_employees.json', 'w') as data:
        json.dump(j_dict, data)
