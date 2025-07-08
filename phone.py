def add_digits_until_single(n):
    # Keep summing digits until n is a single digit
    while n > 9:
        total = 0
        while n > 0:
            total += n % 10  # Add the last digit
            n //= 10         # Remove the last digit
        n = total
    return n

def main():
    print("Welcome! 😊")
    print("Enter any 10-digit number, and I'll add its digits until only a single digit remains.")
    
    number_str = input("Please type your 10-digit number: ")
    
    # Input validation
    if not (number_str.isdigit() and len(number_str) == 10):
        print("Oops! Please enter exactly 10 digits.")
        return
    
    number = int(number_str)
    result = add_digits_until_single(number)
    print(f"The single-digit sum of your number is: {result}")

if __name__ == "__main__":
    main()

# This code defines a function to repeatedly sum the digits of a number until a single digit is obtained.