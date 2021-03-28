import os
import json



def add_account(username, password): #treba dodati pogoje za dobro geslo in username
    with open(os.path.join(os.getcwd(),'..', "database", "accounts.json"), "r") as file:
        accounts = json.load(file)
        new_account = {"username": username, "password" : password, "graphs" : []}
        accounts['people'].append(new_account)  
        json.dump(accounts, file, indent = 4)

def correct_password(username, password):
    with open(os.path.join(os.getcwd(),'..', "database", "accounts.json"), "r") as file:
        logins = json.load(file)
    for login in logins:
        if login['username'] == username and login['password'] == password:
            return True
    return False

