from math import sqrt

def main():
    # Header
    print("=" * 28)
    print(f"{'Number':<10} {'Square Root':>15}")
    print("=" * 28)

    # Rows
    for n in range(0, 21, 2):
        print(f"{n:<10} {sqrt(n):>15.4f}")

    print("=" * 28)

if __name__ == "__main__":
    main()
