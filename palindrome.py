import unittest

class TestPalindrome(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertTrue(isPalindrome(self, "racecar"))

def isPalindrome(self, s):
    return s[::-1] == s
     

if __name__ == '__main__':
    unittest.main()

