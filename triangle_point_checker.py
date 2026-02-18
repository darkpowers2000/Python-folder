def is_point_in_triangle(px, py):
    """Return True if point (px, py) is inside the right triangle."""
    
    # Triangle vertices
    A = (0, 0)
    B = (200, 0)
    C = (0, 100)

    # Cross product helper
    def cross(x1, y1, x2, y2, px, py):
        return (x2 - x1) * (py - y1) - (y2 - y1) * (px - x1)

    c1 = cross(A[0], A[1], B[0], B[1], px, py)
    c2 = cross(B[0], B[1], C[0], C[1], px, py)
    c3 = cross(C[0], C[1], A[0], A[1], px, py)

    return c1 >= 0 and c2 >= 0 and c3 >= 0


def main():
    print("Right Triangle Region Checker")
    print("--------------------------------")
    print("The triangle has vertices at:")
    print("  A = (0, 0)")
    print("  B = (200, 0)")
    print("  C = (0, 100)")
    print()

    # Get user input safely
    try:
        px = float(input("Enter the x-coordinate of your point: "))
        py = float(input("Enter the y-coordinate of your point: "))
    except ValueError:
        print("\nInvalid input. Please enter numeric values.")
        return

    # Determine location
    if is_point_in_triangle(px, py):
        print(f"\nThe point ({px}, {py}) is INSIDE the triangle.")
    else:
        print(f"\nThe point ({px}, {py}) is OUTSIDE the triangle.")


# Run the program
main()
