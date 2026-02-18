def get_int(prompt):
    """Safely get an integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative number.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def main():
    print("Minutes to Years and Days Converter")
    print("----------------------------------")

    minutes = get_int("Enter the number of minutes: ")

    # Constants
    minutes_per_day = 60 * 24
    minutes_per_year = minutes_per_day * 365

    # Calculations
    years = minutes // minutes_per_year
    remaining_minutes = minutes % minutes_per_year
    days = remaining_minutes // minutes_per_day

    # Output
    print(f"\n{minutes} minutes is approximately {years} years and {days} days")

# Run the program
main()
