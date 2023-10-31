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
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!")

        elif user_input == "2":
            decoded_pass = decode(encoded_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {decoded_pass}.")

        elif user_input == "3":
            run = False
def decoder(password):
   int_password = int(password)
   decoded_password = ""
   for x in int_password:
       if 3 <= x < 9:
           decoded_password += str(x - 3)
       elif x == 0:
           decoded_password += "7"
       elif x == 1:
           decoded_password += "8"
       elif x == 2:
           decoded_password += "9"
   return decoded_password
