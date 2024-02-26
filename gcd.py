# Define a function to calculate the greatest common divisor (GCD) of two numbers
def gcd():
    """
    Function to calculate the greatest common divisor (GCD) of two numbers
    """
    # Prompt the user to enter the first number
    a = int(input("Enter the first number: "))
    # Prompt the user to enter the second number
    b = int(input("Enter the second number: "))
    # Call the calculate_gcd function to find the GCD
    result = calculate_gcd(a, b)
    # Print the result
    print("The GCD of", a, "and", b, "is", result)

# Define a function to recursively calculate the GCD using Euclid's algorithm
def calculate_gcd(a, b):
    """
    Function to recursively calculate the GCD using Euclid's algorithm
    """
    # Base case: if b is 0, return a
    if b == 0:
        return a
    # Recursive case: call calculate_gcd with b and a % b
    else:
        return calculate_gcd(b, a % b)

# Call the gcd function to execute the GCD calculation
gcd()

# The time complexity of the calculate_gcd function using Euclid's algorithm is O(log min(a, b)).
# This is because the Euclidean algorithm for finding the greatest common divisor 
# has a logarithmic time complexity based on the smaller of the two input numbers.

# step-by-step flow for the calculate_gcd(48, 18) using the calculate_gcd function:

# Initial call: calculate_gcd(48, 18)
# Since b (18) is not 0, we proceed to the else block.
# Next call: calculate_gcd(18, 48 % 18) => calculate_gcd(18, 12)
# Since b (12) is not 0, we proceed to the else block.
# Next call: calculate_gcd(12, 18 % 12) => calculate_gcd(12, 6)
# Since b (6) is not 0, we proceed to the else block.
# Next call: calculate_gcd(6, 12 % 6) => calculate_gcd(6, 0)
# Now, b (0), so the base case is triggered and we return a (6).
# Therefore, the result of calculate_gcd(48, 18) is 6, as the greatest common divisor (GCD) of 48 and 18.


