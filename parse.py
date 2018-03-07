#!/usr/bin/env python
'''Git script'''
# pylint: disable=invalid-name
# pylint: disable=line-too-long
import getpass
import argparse
import requests


paswd = None
user = None


def show_last():
    """show last Pull"""
    pull = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls', auth=(user, paswd))
    pull_dict = pull.json()
    print("Last PR info")
    print("\tNumber: ", pull_dict[0].get("number"))
    print("\tStatus: ", pull_dict[0].get("state"))
    print("\tTitle: ", pull_dict[0].get("title"))
    print("\tCreated: ", pull_dict[0].get("created_at"))
    print("\tUser: ", pull_dict[0].get("user").get("login"))
    print("\tBaseRepo: ", pull_dict[0].get("base").get("label"))


def show_user_PR(num):
    """show user PR"""
    pull = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls', auth=(user, paswd))
    pull_dict = pull.json()
    index = pull_dict[0].get("number") - num
    print("\tReal Number: ", pull_dict[index].get("number"))
    print("\tUser: ", pull_dict[index].get("user").get("login"))


def show_all(num):
    """show all PR in repo"""
    pull = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls?per_page='+str(num), auth=(user, paswd))
    pull_dict = pull.json()
    for i in pull_dict:
        print("\t", i.get("title"))


def show_closed():
    """show closed PR"""
    pull = requests.get("https://api.github.com/repos/alenaPy/devops_lab/pulls?state=closed", auth=(user, paswd))
    pull_dict = pull.json()
    for one in pull_dict:
        print("\tTitle: ", one.get("title"))
        print("\t\tUser:    ", one.get("user").get("login"))
        print("\t\tCreated: ", one.get("created_at"))
        print("\t\tClosed:  ", one.get("closed_at"))


def show_rep():
    """show repos"""
    pull = requests.get("https://api.github.com/users/alenaPy/repos", auth=(user, paswd))
    pull_dict = pull.json()
    for one in pull_dict:
        print("\tName: ", one.get("name"))


def parse_arg():
    """parser commandline arguments"""
    parser = argparse.ArgumentParser(description="Get GIT info", epilog='LIngBY ® ©')
    parser.add_argument('-v', '--version', action='version', help="Shows program's version", version="1.2.0 Closed Beta Trial")
    parser.add_argument('-u', required=True, dest='user', help='User Login')
    argroup = parser.add_mutually_exclusive_group()
    argroup.add_argument('-num', type=int, help='List user and real number PullRequest')
    argroup.add_argument('-title', type=int, help='Show titles last <num> PullRequests')
    argroup.add_argument('-lastPR', action='store_true', help='List last PR info')
    argroup.add_argument('-closed', action='store_true', help='List closed PullRequests')
    argroup.add_argument('-repos', action='store_true', help='List Repos')
    return parser.parse_args()


args = parse_arg()
user = args.user
paswd = getpass.getpass()
if args.num:
    show_user_PR(args.num)
if args.title:
    show_all(args.title)
if args.lastPR:
    show_last()
if args.closed:
    show_closed()
if args.repos:
    show_rep()
