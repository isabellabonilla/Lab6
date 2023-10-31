#Isabella Bonilla

def encode(password):
    new_password = ''

    for value in password:
        new_password = new_password + str((int(value) + 3) % 10)

    return new_password


if __name__ == '__main__':
    user_input = 0
    run = True

    while run:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        user_input = input("\nPlease enter an option: ")

        if user_input == "1":
            password = input("Please enter a password to encode: ")
            encode(password)
            print("Your password has been encoded and stored!")

        elif user_input == '2':
            pass

        elif user_input == '3':
            run = False