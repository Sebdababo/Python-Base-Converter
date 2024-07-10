import string

def convert_base(number, from_base, to_base):
    digits = string.digits + string.ascii_letters + '+/'

    if from_base != 10:
        decimal = 0
        power = 0
        for digit in reversed(str(number)):
            decimal += digits.index(digit) * (from_base ** power)
            power += 1
    else:
        decimal = int(number)

    if to_base == 10:
        return str(decimal)
    else:
        result = ""
        while decimal > 0:
            result = digits[decimal % to_base] + result
            decimal //= to_base
        return result or "0"

while True:
    number = input("Enter the number to convert: ")
    from_base = int(input("Enter the base of the input number (2-64): "))
    to_base = int(input("Enter the base to convert to (2-64): "))

    if from_base < 2 or from_base > 64 or to_base < 2 or to_base > 64:
        print("Base must be between 2 and 64")
        continue

    result = convert_base(number, from_base, to_base)
    print(f"Result: {result}")

    another = input("Do you want to convert another number? (y/n): ")
    if another.lower() != 'y':
        break

print("Thank you for using the base converter!")