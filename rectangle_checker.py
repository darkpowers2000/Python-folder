def read_rectangle(label):
    """Reads center coordinates, width, and height for a rectangle."""
    print(f"Enter {label}'s data:")
    x, y = eval(input("  Center (x, y): "))
    width, height = eval(input("  Width and height: "))
    return x, y, width, height


def is_inside(r1, r2):
    """Returns True if rectangle r2 is completely inside r1."""
    x1, y1, w1, h1 = r1
    x2, y2, w2, h2 = r2

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    return dx + w2 / 2 <= w1 / 2 and dy + h2 / 2 <= h1 / 2


def is_overlapping(r1, r2):
    """Returns True if rectangles r1 and r2 overlap."""
    x1, y1, w1, h1 = r1
    x2, y2, w2, h2 = r2

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    return dx < (w1 + w2) / 2 and dy < (h1 + h2) / 2


def main():
    r1 = read_rectangle("r1")
    r2 = read_rectangle("r2")

    if is_inside(r1, r2):
        print("\nr2 is inside r1")
    elif is_overlapping(r1, r2):
        print("\nr2 overlaps r1")
    else:
        print("\nr2 does not overlap r1")


if __name__ == "__main__":
    main()
