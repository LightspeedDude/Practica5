import Pali
import unittest

class test_Palindromo(unittest.TestCase):
    def test_check(self):
        self.assertEqual(Pali.pa("anna"), "anna")

    def test_check2(self):
        self.assertEqual(Pali.pa("racecar"), "racecar")
    
    def test_check3(self):
        self.assertEqual(Pali.pa("level"), "level")
    
    def test_check4(self):
        self.assertEqual(Pali.pa("mom"), "mom")
    
    def test_check5(self):
        self.assertEqual(Pali.pa("wow"), "wow")


if __name__ == '__main__':
    unittest.main()