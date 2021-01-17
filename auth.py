import csv

def main():
    with open("users.txt","r") as file:
        file_reader = csv.reader(file)
        user_find(file_reader)
        file.close()

def user_find(file):
    user = input("Enter your username: ")
    for row in file:
        if row[0] == user:
            print("username found", user)
            user_found = [row[0],row[1]]
            pass_check(user_found)
            break
        else:
            print("not found")

def pass_check(user_found):
    user = input("enter your password: ")
    if user_found[1] == user:
        print("password match")
    else:
        print("password not match")
        user_find(file_reader)

main()
