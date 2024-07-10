import string

def convert_base(number, from_base, to_base):
    """Converts a number from one base to another."""
    digits = string.digits + string.ascii_letters + '+/'

    negative = number.startswith('-')
    if negative:
        number = number[1:]

    if any(digit not in digits[:from_base] for digit in number):
        return "Invalid number for the specified base."

    if from_base != 10:
        decimal = sum(digits.index(digit) * (from_base ** power) for power, digit in enumerate(reversed(number)))
    else:
        decimal = int(number)

    if to_base == 10:
        return str(-decimal if negative else decimal)
    else:
        result = ""
        while decimal > 0:
            result = digits[decimal % to_base] + result
            decimal //= to_base
        return ('-' if negative else '') + (result or "0")

def main():
    """Main function to handle user input and base conversion."""
    while True:
        print("\nType 'exit' to quit the program.")
        number = input("Enter the number to convert: ").strip()
        if number.lower() == 'exit':
            break

        try:
            from_base = int(input("Enter the base of the input number (2-64): "))
            to_base = int(input("Enter the base to convert to (2-64): "))
            if from_base < 2 or from_base > 64 or to_base < 2 or to_base > 64:
                print("Base must be between 2 and 64.")
                continue
        except ValueError:
            print("Base must be a number.")
            continue

        result = convert_base(number, from_base, to_base)
        if result.startswith("Invalid"):
            print(result)
        else:
            print(f"Converted number: {result}")

if __name__ == "__main__":
    main()