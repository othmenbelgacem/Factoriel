def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def power(base, exponent):
    return base ** exponent

def main():
    try:
        # Ask the user what operation they want to perform
        operation = input("Choose an operation (factorial or power): ").lower()

        if operation == "factorial":
            # Get user input for the number
            num = int(input("Enter a non-negative integer: "))

            # Check if the input is non-negative
            if num < 0:
                print("Please enter a non-negative integer. Thank you.")
            else:
                result = factorial(num)
                print("The factorial of {} is: {}".format(num, result))

        elif operation == "power":
            # Get user input for the base and exponent
            base = int(input("Enter the base: "))
            exponent = int(input("Enter the exponent: "))
            
            result = power(base, exponent)
            print("{} raised to the power of {} is: {}".format(base, exponent, result))

        else:
            print("Invalid operation. Please choose either 'factorial' or 'power'.")

    except ValueError:
        print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
