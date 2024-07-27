"""
Justin Nguyen
[COP3502C] - Lab 9, main.py

Objective: Create a looping menu, with options: encode, decode, and exit.
"""
# IMPORTS
from functions import encode # import decode later


# MAIN FUNCTION
def main():

    menu_is_active = True
    menu = ("Menu\n"
            "-------------\n"
            "1. Encode\n"
            "2. Decode\n"
            "3. Quit\n")

    while menu_is_active:
        print(menu)
        choice = int(input("Please enter an option: "))

        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded_pass = encode(password)
            print("Your password has been encoded and stored!")

        elif choice == 2:
            pass

        elif choice == 3:
            menu_is_active = False

        print()

if __name__ == "__main__":
    main()