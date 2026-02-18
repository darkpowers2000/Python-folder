def main():
    print("Student Major and Status Decoder")
    print("--------------------------------")

    code = input("Enter two characters (e.g., C1, M4, I2): ").strip()

    # Validate length
    if len(code) != 2:
        print("Invalid input. Please enter exactly two characters.")
        return

    major_char = code[0].upper()
    status_char = code[1]

    # Major lookup
    majors = {
        'M': "Mathematics",
        'C': "Computer Science",
        'I': "Information Technology"
    }

    # Status lookup
    statuses = {
        '1': "Freshman",
        '2': "Sophomore",
        '3': "Junior",
        '4': "Senior"
    }

    # Validate major
    if major_char not in majors:
        print("Invalid major code.")
        return

    # Validate status
    if status_char not in statuses:
        print("Invalid status code.")
        return

    # Output result
    print(f"{majors[major_char]} {statuses[status_char]}")

# Run the program
main()
