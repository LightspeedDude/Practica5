import Palind
import unittest

class test_Palind(unittest.TestCase):
    def test_check(self):
        self.assertEqual(Palind.po("anna"), "anna")
    
    def test_check2(self):
        self.assertEqual(Palind.po("level"), "level")
    
    def test_check3(self):
        self.assertEqual(Palind.po("racecar"), "racecar")
    
    def test_check4(self):
        self.assertEqual(Palind.po("wow"), "wow")
    
    def test_check5(self):
        self.assertEqual(Palind.po("madam"), "madam")

if __name__ == "__main__":
    unittest.main()