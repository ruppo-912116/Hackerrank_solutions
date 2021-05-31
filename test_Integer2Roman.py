import unittest
import Integer2Roman

class TestInteger2Roman(unittest.TestCase):
    def test_integertoRoman(self):
        integer = 1994
        roman = "MCMXCIV"
        self.assertEqual(roman, Integer2Roman.IntegertoRoman(integer))

if __name__ == "__main__":
    unittest.main()