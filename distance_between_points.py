def get_float(prompt):
    """Safely get a floating‑point number from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    print("Distance Between Two Points Calculator")
    print("-------------------------------------")

    # Get validated input
    x1 = get_float("Enter x1: ")
    y1 = get_float("Enter y1: ")
    x2 = get_float("Enter x2: ")
    y2 = get_float("Enter y2: ")

    # Compute the distance
    distance = pow((x2 - x1)**2 + (y2 - y1)**2, 0.5)

    # Display the result
    print(f"\nThe distance between the two points is: {distance:.4f}")

# Run the program
main()
