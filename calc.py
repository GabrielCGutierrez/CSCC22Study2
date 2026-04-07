import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(4, add(2, 2))

    def test_subtract(self):
        self.assertEqual(2, subtract(4, 2))

    def test_multiply(self):
        self.assertEqual(8, multiply(2, 4))

    def test_divide(self):
        self.assertEqual(2, divide(4, 2))
        with self.assertRaises(ZeroDivisionError):
            divide(1, 0)

def add(a, b):
    return a + b

def subtract(a, b): 
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b   

if __name__ == '__main__':
    unittest.main()