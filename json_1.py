import json

filename = "user.json"

def check_user():
    try:
        with open(filename) as f:
            user = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user

def create_user():
    user = input("Enter your name")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(user,f,ensure_ascii=False)
    return welcome_user()

def welcome_user():
    user = input("Enter your login")
    if user == check_user():
        print("Wellcome ",user)
    elif check_user()==None:
        user = create_user()
    else:
        print("Sorry you have not roots to acces")

welcome_user()





'''def create_user():
    #create user
    user = welcome_user()
    if user:
        print( "Wellcome" + user)
    with open(filename,"w",encoding="utf-8") as f:
        json.dump(user,f, ensure_ascii=False)



def welcome_user():
    #welcome user
    try:
        with open(filename) as f:
            user = json.load(f)
    except FileNotFoundError():
        return None
    else:
        return user


welcome_user()'''
