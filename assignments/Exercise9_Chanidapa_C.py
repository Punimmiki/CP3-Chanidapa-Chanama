usernameInput = input("Username : ")
passwordInput = input("Password : ")
while usernameInput != "admin" or passwordInput != "1234":
    print("Wrong username or password!")
    usernameInput = input("Username : ")
    passwordInput = input("Password : ")
print("Welcome", usernameInput, "!")
