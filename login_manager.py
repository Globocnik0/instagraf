import os
import json
import re

class User:

    def __init__(self, username, password = None):
        self.username = username
        self.password = password

    def add_account(self): #treba dodati pogoje za dobro geslo in username
        with open(os.path.join(os.getcwd(), "database", "accounts.json"), "r+") as file:
            accounts = json.load(file)
            new_account = {"username": self.username, "password" : self.password, "graphs" : []}
            accounts['people'].append(new_account) 
            file.seek(0)
            json.dump(accounts, file, indent = 2)

    def correct_password(self):
        with open(os.path.join(os.getcwd(), "database", "accounts.json"), "r") as file:
            logins = json.load(file)
        for login in logins['people']:
            if login['username'] == self.username and login['password'] == self.password:
                return True
        return False

    def username_exists(self):
        with open(os.path.join(os.getcwd(), "database", "accounts.json"), "r") as file: #get file directory
            logins = json.load(file)
        for login in logins['people']:
            if login['username'] == self.username:
                return True
        return False

    def valid_characters(self):
        if re.search("^[A-Za-z0-9]*$", self.username) and re.search("^[A-Za-z0-9]*$", self.password):
            return True
        return False 
    


#dealing with graphs and .json
def add_graph_to_account(username, filename, title, x_label, y_label, fit):
    with open(os.path.join(os.getcwd(), "database", "accounts.json"), "r+") as file:
        accounts = json.load(file)
        new_graph = {'filename': filename, 'title': title, 'x_label': x_label, 'y_label': y_label, 'fit': fit}
        for user in accounts['people']:
            if user['username'] == username:
                user['graphs'].append(new_graph)
        file.seek(0)
        json.dump(accounts, file, indent = 2)

def read_graphs_from_account(username):
    with open(os.path.join(os.getcwd(), "database", "accounts.json"), "r") as file:
        accounts = json.load(file)
        for user in accounts['people']:
            if user['username'] == username:
                return user['graphs']