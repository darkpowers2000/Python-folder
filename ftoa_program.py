def ftoa(f):
    # Handle sign
    sign = ""
    if f < 0:
        sign = "-"
        f = -f

    # Integer part
    ipart = int(f)
    frac = f - ipart

    # Convert integer part to string manually
    int_str = ""
    if ipart == 0:
        int_str = "0"
    else:
        while ipart > 0:
            int_str = chr(ord('0') + ipart % 10) + int_str
            ipart //= 10

    # Convert fractional part (limit to 6 digits)
    if frac > 0:
        frac_str = "."
        for _ in range(6):
            frac *= 10
            digit = int(frac)
            frac_str += chr(ord('0') + digit)
            frac -= digit

        # Trim trailing zeros
        frac_str = frac_str.rstrip("0")
        if frac_str == ".":
            frac_str = ""
    else:
        frac_str = ""

    return sign + int_str + frac_str


# Test program
x = float(input("Enter a number: "))
s = ftoa(x)

print("The number is", " ".join(s))
