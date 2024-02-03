import json

def save_file(contact: dict, filename: str):
            with open(filename, "a") as f: #a means append. so makes it if it already exists, otherwise edits
                json.dump(contact, f)

def signups(name, email):
    # name = input("What is your contact name? ")
    # email = input("What is your contact's email?")

    #defining an object
    contact = {
        "name" : name,
        "email" : email,
    }
    save_file(contact, "signups.json")