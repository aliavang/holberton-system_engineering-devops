#!/usr/bin/python3
"""
Export data in the CSV format
"""
import csv
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
    with open(sys.argv[1] + '.csv', 'w') as data:
        file = csv.writer(data, quoting=csv.QUOTE_ALL)
        for item in res:
            if sys.argv[1] == str(item.get("userId")):
                stat = item.get("completed")
                title = item.get("title")
                file.writerow([sys.argv[1], usr, stat, title])
