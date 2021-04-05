import os
import json
#naredi class iz tega
#user exists za cookie
#username taken


def add_account(username, password): #treba dodati pogoje za dobro geslo in username
    with open(os.path.join(os.getcwd(),'..', "database", "accounts.json"), "r+") as file:
        accounts = json.load(file)
        new_account = {"username": username, "password" : password, "graphs" : []}
        accounts['people'].append(new_account) 
        file.seek(0)
        json.dump(accounts, file, indent = 2)

def correct_password(username, password):
    with open(os.path.join(os.getcwd(),'..', "database", "accounts.json"), "r") as file:
        logins = json.load(file)
    for login in logins['people']:
        if login['username'] == username and login['password'] == password:
            return True
    return False



def add_graph_to_account(username, filename, title, x_label, y_label, fit):
    with open(os.path.join(os.getcwd(),'..', "database", "accounts.json"), "r+") as file:
        accounts = json.load(file)
        new_graph = {'filename': filename, 'title': title, 'x_label': x_label, 'y_label': y_label, 'fit': fit}
        for user in accounts['people']:
            if user['username'] == username:
                user['graphs'].append(new_graph)
        file.seek(0)
        json.dump(accounts, file, indent = 2)

def read_graphs_from_account(username):
    with open(os.path.join(os.getcwd(),'..', "database", "accounts.json"), "r") as file:
        accounts = json.load(file)
        for user in accounts['people']:
            if user['username'] == username:
                return user['graphs']



