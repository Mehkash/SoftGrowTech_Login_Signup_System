# Login and Signup System

while True:
    print("\n===== Login & Signup System =====")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        file = open("users.txt", "a")
        file.write(username + "," + password + "\n")
        file.close()

        print("Signup Successful!")

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")

        found = False

        try:
            file = open("users.txt", "r")
            users = file.readlines()
            file.close()

            for user in users:
                data = user.strip().split(",")

                if username == data[0] and password == data[1]:
                    found = True
                    break

            if found:
                print("Login Successful!")
            else:
                print("Invalid Username or Password!")

        except:
            print("No users found.")

    elif choice == "3":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")