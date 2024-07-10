MIN_BASE = int(input('Enter the minimum base value: '))
MAX_BASE = int(input('Enter the maximum base value: '))

def convert_base(number, from_base, to_base):
    if from_base != 10:
        number_in_decimal = int(number, from_base)
    else:
        number_in_decimal = int(number)

    if to_base != 10:
        result = ""
        negative = False
        if number_in_decimal < 0:
            negative = True
            number_in_decimal = -number_in_decimal

        while number_in_decimal > 0:
            remainder = number_in_decimal % to_base
            if remainder < 10:
                result = str(remainder) + result
            else:
                result = chr(55 + remainder) + result
            number_in_decimal //= to_base
        return ('-' if negative else '') + (result or "0")
    else:
        return str(number_in_decimal)

def get_valid_base(prompt, attempt_limit=3):
    attempts = 0
    while attempts < attempt_limit:
        try:
            base = int(input(prompt))
            if MIN_BASE <= base <= MAX_BASE:
                return base
            else:
                print(f"Base must be between {MIN_BASE} and {MAX_BASE}.")
        except ValueError:
            print("Base must be a number.")
        attempts += 1
    return None

def main():
    while True:
        print("\nType 'exit' to quit the program.")
        number = input("Enter the number to convert: ").strip()
        if number.lower() == 'exit':
            break

        from_base = get_valid_base(f"Enter the base of the input number ({MIN_BASE}-{MAX_BASE}): ")
        if from_base is None:
            print("Too many invalid attempts. Please try again.")
            continue

        to_base = get_valid_base(f"Enter the base to convert to ({MIN_BASE}-{MAX_BASE}): ")
        if to_base is None:
            print("Too many invalid attempts. Please try again.")
            continue

        result = convert_base(number, from_base, to_base)
        print(f"Converted number: {result}")

if __name__ == "__main__":
    main()