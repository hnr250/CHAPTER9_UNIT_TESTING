import unittest
import roman2

class ToRomanBadInput(unittest.TestCase):
    def test_too_large(self):
        '''to_roman powinna zglosic wyjatek przy zbyt duzym parametrze'''
        self.assertRaises(roman2.OutOfRangeError, roman2.to_roman, 4000)

if __name__ == '__main__':
    unittest.main()