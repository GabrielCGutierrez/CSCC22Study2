import unittest

class TestPalindrome(unittest.TestCase):
    def test_isPalindrome(self):
        self.assertTrue(isPalindrome(self, "racecar"))

def isPalindrome(self, s):
    if s[::-1] == s:
        return True
    else:
        return False

if __name__ == '__main__':
    unittest.main()

