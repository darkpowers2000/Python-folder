def kg_to_lb(kg):
    """Convert kilograms to pounds."""
    return kg * 2.2

def lb_to_kg(lb):
    """Convert pounds to kilograms."""
    return lb / 2.2

def print_tables():
    # Table headers
    header_left = "Kilograms"
    header_right = "Pounds"
    header_left2 = "Pounds"
    header_right2 = "Kilograms"

    print(f"{header_left:<12}{header_right:<12} | {header_left2:<12}{header_right2:<12}")
    print("-" * 55)

    # Generate rows
    for i in range(1, 11):
        kg = i
        lb_from_kg = kg_to_lb(kg)

        lb = i * 5
        kg_from_lb = lb_to_kg(lb)

        print(f"{kg:<12}{lb_from_kg:<12.1f} | {lb:<12}{kg_from_lb:<12.2f}")

# Run the program
print_tables()
