#!/bin/python3

import argparse
import requests

BASE_URL = "https://gitignore.io/"
API_URL = BASE_URL + "api/"
LIST_URL = API_URL + "list"


def _get_list():
    req = requests.get(LIST_URL)
    options_list = []
    for line in req.text.split("\n"):
        options_list += line.split(",")
    return options_list


def _search(term):
    options_list = _get_list()
    return [option for option in options_list if term in option]


def _get_gitignore(options):
    req = requests.get(API_URL + ",".join(options))
    return req.text


def main():
    parser = argparse.ArgumentParser(
        description="Download .gitignore files from gitignore.io")
    parser.add_argument("languages", metavar="lang", type=str, nargs='*',
                        help="language, IDE or OS to include in the .gitignore file")
    parser.add_argument("--list", "-l", action="store_true",
                        help="list all language, IDE or OS options")
    parser.add_argument("--search", "-s", type=str,
                        help="search list of options and print found matches")
    parser.add_argument("--file", "-f", type=str,
                        default=".gitignore", help="specify which file to write to")
    args = parser.parse_args()

    if args.list:
        print("\n".join(_get_list()))
    elif args.search:
        print("\n".join(_search(args.search.lower())))
    elif args.languages:
        with open(args.file, "w+") as gitignore:
            gitignore.write(_get_gitignore(
                [lang.lower() for lang in args.languages]))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
