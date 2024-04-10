def display_menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()

def encode(password):
    password_list = []
    for digit in password:
        password_list += digit
    password_list = list(map(int, password_list))
    encoded_password_list = [x + 3 for x in password_list]
    encoded_password = "".join(map(str, encoded_password_list))
    return encoded_password

def main():
    while True:
        display_menu()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")
        if choice == 2:
            print()
        else:
            break


if __name__ == "__main__":
    main()

