def indexOf(s1, s2):
    """Return the starting index of s1 in s2, or -1 if not found."""
    return s2.find(s1)

def main():
    print("=== Substring Checker ===")
    print("This program finds the starting index of one string inside another.\n")

    s1 = input("Enter the first string (the substring to search for): ").strip()
    s2 = input("Enter the second string (the text to search in): ").strip()

    result = indexOf(s1, s2)

    print("\n--- Result ---")
    print(f'indexOf("{s1}", "{s2}") is {result}')
    print("-------------------------")

if __name__ == "__main__":
    main()
