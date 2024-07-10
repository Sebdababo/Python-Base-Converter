def convert_base(number, from_base, to_base):
    decimal = int(str(number), from_base)
    
    if to_base == 10:
        return str(decimal)
    elif to_base == 16:
        return hex(decimal)[2:].upper()
    else:
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while decimal > 0:
            result = digits[decimal % to_base] + result
            decimal //= to_base
        return result or "0"

while True:
    number = input("Enter the number to convert: ")
    from_base = int(input("Enter the base of the input number (2-36): "))
    to_base = int(input("Enter the base to convert to (2-36): "))

    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        print("Base must be between 2 and 36")
        continue

    result = convert_base(number, from_base, to_base)
    print(f"Result: {result}")

    another = input("Do you want to convert another number? (y/n): ")
    if another.lower() != 'y':
        break

print("Thank you for using the base converter!")