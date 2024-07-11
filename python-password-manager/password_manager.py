from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file: # wb is a special file formatl
        key_file.write(key)

def load_key():
    file =  open("key.key", "rb")
    key = file.read() # rb is a special file format
    file.close()
    return key

master_pwd = input("Master Password : ")
key = load_key() 
fer = Fernet(key)
mode = input("Would you like to - Add New Password or Virew Existing Ones (add, view) or Quit? ")

def view():
    with open("passwords.txt", "r") as f: #with automatically closes the file for us
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|") 
            print("User : ", user, ", Password", fer.decrypt(passw.encode()).decode())
            # .split() finds the character present in the (), splits the unique strings and presents it in form of a list ["a1", "a2", "a3" etc.]
            # user and passw are the elements that have been assigned to be split user, passw = ["user", "passw"]

def add():
    name = input("Account Name : ")
    pwd = input("Password : ")

    with open("passwords.txt", "a") as f: #with automatically closes the file for us
        f.write( name + " | " + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    if mode == "Q":
        break

    if mode == "view":
        view()
        break
    elif mode == "add":
        add()
        break
    else:
        print("Invalid Mode")