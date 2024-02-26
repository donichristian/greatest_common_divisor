import unittest

# Define the function to calculate the greatest common divisor (GCD) of two numbers
def gcd(a, b):
    """
    Function to calculate the greatest common divisor (GCD) of two numbers

    Args:
    a (int): The first number
    b (int): The second number

    Returns:
    int: The greatest common divisor of the two numbers
    """
    print(f"Calculating gcd of {a} and {b}")  # Print statement for debugging
    # Base case: if b is 0, return a
    if b == 0:
        return a
    # Recursive case: call calculate_gcd with b and a % b
    else:
        return gcd(b, a % b)

# Define a class for unit testing the gcd function
class TestGCDFunction(unittest.TestCase):
    """
    Class for unit testing the gcd function
    """

    def test_gcd(self):
        """
        Test the gcd function
        """
        result1 = gcd(10, 25)
        print(f"Result of gcd(10, 25): {result1}")  # Print the result of the first test
        self.assertEqual(result1, 5)  # Test 1: expected result: 5
        
        result2 = gcd(14, 28)
        print(f"Result of gcd(14, 28): {result2}")  # Print the result of the second test
        self.assertEqual(result2, 14)  # Test 2: expected result: 14

        result3 = gcd(21, 14)
        print(f"Result of gcd(21, 14): {result3}")  # Print the result of the third test
        self.assertEqual(result3, 7)  # Test 3: expected result: 7

if __name__ == '__main__':
    unittest.main()