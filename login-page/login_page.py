# Login page welcome
print("Welcome to my login page")
print("\n")
print("If you login then press 1 or sign up to press 2")

# user inputs
user_choice = int(input("If you login then press 1 or sign up to press 2 : "))

# Sign up section
if user_choice == 2:
    fast_name = input("Enter your name: ")
    last_name = input("Enter your last name: ")
    moblie_num = input("Enter your mobile number: ")
    email_add = input("Enter your Email address: ")
    user_name = input("Create a username: ")
    password = input("Create a strong password: ")
    retype_password = input("Retype This password: ")

    if retype_password != password:
        print("Password is not matched!")
    else:
        print("\nYou have successfully created an account!!")
        print("Name:", fast_name, last_name)
        print("Mobile:", moblie_num)
        print("Email:", email_add)

        # File Handling (save info)
        with open("login.txt", "w") as f:
            f.write(user_name + "\n")
            f.write(password + "\n")

# login section code
elif user_choice == 1:
    login_username = input("Enter your username: ")
    login_password = input("Enter your Password: ")

    # Check user password
    with open("login.txt", "r") as f:
        saved_username = f.readline().strip()
        saved_password = f.readline().strip()

    if login_username == saved_username and login_password == saved_password:
        print("Login successful!")
    else:
        print("Wrong username or password, please try again!")	