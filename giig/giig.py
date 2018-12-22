#!/bin/python3

import requests

BASE_URL = "https://gitignore.io/"
API_URL = BASE_URL + "api/"
LIST_URL = API_URL + "list"


def get_list():
    req = requests.get(LIST_URL)
    options_list = []
    for line in req.text.split("\n"):
        options_list += line.split(",")
    return options_list


def search(term):
    options_list = get_list()
    return [option for option in options_list if term in option]


def get_gitignore(options):
    req = requests.get(API_URL + ",".join(options))
    return req.text
