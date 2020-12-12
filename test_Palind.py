import Palind
import unittest

class test_Palind(unittest.TestCase):
    def test_check(self):
        self.assertEqual(Palind.pa("anna"), "anna")
    
    def test_check2(self):
        self.assertEqual(Palind.pa("racecar"),"racecar")

    def test_check3(self):
        self.assertEqual(Palind.pa("level"), "level")

    def test_check4(self):
        self.assertEqual(Palind.pa("radar"), "radar")

    def test_check5(self):
        self.assertEqual(Palind.pa("rotor"), "rotor")

if __name__ == "__main__":
    unittest.main()
