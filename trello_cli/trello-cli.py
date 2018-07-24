import requests
import json
from pprint import pprint
from getpass import getpass
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8000/"

class User():
    def __init__(self):
        name=self.name


class Users:

    #returns list of usernames
    def get_user_list(self):
        res = requests.get(BASE_URL + 'api/users')
        # print(res.text)
        data = json.loads(str(res.text))
        username_list = list()
        for line in data:
            username_list.append(line['username'])
        print("[username]")
        return username_list

    def login(self):
        username = input("Enter username: ")
        password = getpass("Enter Password: ")
        return username, password


class Boards():

    def get_board_list(self):
        res = requests.get(BASE_URL + 'api/boards')
        # print(res.text)
        data = json.loads(str(res.text))
        boardname_list = list()
        for line in data:
            boardname_list.append((line['id'],line['name']))
        print('[board id, name]')
        return boardname_list


    def create_board(self, username, password):
        name=input('Enter name for baord: ')
        d1 = {'name' : name}
        r = requests.post('http://127.0.0.1:8000/api/boards/', data=d1 ,auth=HTTPBasicAuth(username, password))
        print("status",r.status_code)

class Lists():
    def get_task_list(self):
        res = requests.get(BASE_URL + 'api/tasks')
        # print(res.text)
        data = json.loads(str(res.text))
        taskname_list = list()
        for line in data:
            taskname_list.append((line['id'],line['name']))
        print('[task id, task name]')
        return taskname_list

    def create_task(self):
        print("List of available boards:")
        b1 = Boards()
        for item in b1.get_board_list():
            print(item[0], item[1])
        board_id = int(input("select a board id from above list: "))
        name = input("enter the name for task: ")
        d1 = {'name' : name, 'board': board_id}
        r = requests.post('http://127.0.0.1:8000/api/tasks/', data=d1)
        print("status", r.status_code)


class Cards():

    def get_card_list(self):
        res = requests.get(BASE_URL + 'api/cards')
        # print(res.text)
        data = json.loads(str(res.text))
        cardname_list = list()
        for line in data:
            cardname_list.append((line['name'], line['description']))
        print('[card name, card description]')
        return cardname_list

    def create_card(self):
        print("List of available tasks(id): ")
        t1 = Lists()
        for item in t1.get_task_list():
            print(item[0], item[1])
        task = input("select a task from the above list: ")
        name = input("enter the name for card: ")
        description = input("enter some description for card: ")

        d1 = {'name' : name, 'task_list': task, 'description' : description}
        r = requests.post('http://127.0.0.1:8000/api/cards/', data=d1)
        print("status", r.status_code)


def main():
    command_list = ['list boards', 'create board', 'list users', 'list tasks', 'create task', 'list cards', 'create card']
    print("Welcome to Trello")
    print("Commands available:\n")
    for i,command in enumerate(command_list):
        print(command)
    choice = input("\nEnter a command: " )
    if (choice == "list users"):
        u1 = Users()
        pprint(u1.get_user_list())
    elif (choice == "list boards"):
        b1 = Boards()
        pprint(b1.get_board_list())
    elif (choice == "list tasks"):
        t1 = Lists()
        pprint(t1.get_task_list())
    elif (choice == "list cards"):
        c1 = Cards()
        pprint(c1.get_card_list())
    elif (choice == "create board"):
        u1 = Users()
        username, password = u1.login()
        b1 = Boards()
        b1.create_board(username, password)
        print("board created")
    elif (choice == "create task"):
        t1 = Lists()
        t1.create_task()
        print("print task created")
    elif (choice == "create card"):
        c1 = Cards()
        c1.create_card()
        print("card created")
    else:
        print("please enter a valid command from above list\n")

if __name__ == '__main__':
    while True:
        main()
        print("\n\n")
