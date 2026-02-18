def letter_to_keypad_number():
    print("Phone Keypad Letter Mapper")
    print("-" * 32)

    keypad = {
        '2': "ABC",
        '3': "DEF",
        '4': "GHI",
        '5': "JKL",
        '6': "MNO",
        '7': "PQRS",
        '8': "TUV",
        '9': "WXYZ"
    }

    user_input = input("Enter a single letter: ").strip()

    # Validate input
    if len(user_input) != 1 or not user_input.isalpha():
        print(f"'{user_input}' is an invalid input")
        return

    letter = user_input.upper()

    # Find the corresponding number
    for number, letters in keypad.items():
        if letter in letters:
            print(f"The corresponding number is {number}")
            return

    # If somehow not found (shouldn't happen with A–Z)
    print(f"'{user_input}' is an invalid input")


# Run the program
letter_to_keypad_number()
