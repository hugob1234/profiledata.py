info = {
    "name": "",
    "surname": "",
    "age": "",
    "email": "",
}
score = 0

while True:
    option = input("Enter what option you would like to choose from (name/surname/age/email/end/change/confirm)")

    if option == "end":
        break

    while ((option != "name") and (option != "surname") and (option != "age") and (option != "email") and (option != "end") and (option != "confirm") and (option != "change")):
        option = input("Error , option not found enter option you want again (name/surname/age/email/end/change/confirm)")

    if option == "name":
        if info[option] == "":
            n = input("Enter your name: ")
            info[option] = n
            print("Added your name")
            score += 1
            print(info)
        else:
            print("Slot already full")

    elif option == "surname":
        if info[option] == "":
            n = input("Enter your surname: ")
            info[option] = n
            print("Successfully added ")
            print(info)
            score += 1
        else:
            print("Slot already full")

    elif option == "age":
        if info[option] == "":
            n = input("Enter your age: ")
            info[option] = n
            print("Successfully added ")
            print(info)
            score += 1
        else:
            print("Slot already full")

    elif option == "email":
        if info[option] == "":
            n = input("Enter your email: ")
            info[option] = n
            print("Successfully added ")
            print(info)
            score += 1
        else:
            print("Slot already full")
            
    elif option == "change":
        n = input("which field you would like to change? ")
        if n != "":
            info[option] = ""
            new = input("new content: ")
            info[n] = new
            print(info)
        else:
            print("Already empty.")

    if option == "confirm":
        if score == 4:
            print(info)
            print("Data has been successfully added")
            with open("profile.txt", "w") as file:
                for x, y in info.items():
                    file.write(f"{x}: {y}\n")
            break
        else:
            print("You haven't filled all the slots in yet")
