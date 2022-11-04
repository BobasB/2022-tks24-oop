import unittest
from lab import Rocket

class TestRocket(unittest.TestCase):
    def setUp(self) -> None:
        #print("Цей метод запускається перед кожним тестом")
        self.name = "Falcon 9"
        self.mass = 549054
        self.obj = Rocket(self.name, self.mass)
    
    def tearDown(self) -> None:
        del self.obj
        
    def testConverter(self):
        self.assertEqual(self.mass * 2.20462262, self.obj.convert())
    
    def testProperty(self):
        self.assertIn(self.name, self.obj.get_info)
        self.assertIn(str(self.mass), self.obj.get_info)

    def testPropertyEn(self):
        self.assertIn(f"{self.obj.convert()} фунтів", self.obj.get_info_en)

    def testMassNotZero(self):
        with self.assertRaises(AssertionError):
            Rocket("None", -1)
        
        with self.assertRaises(AssertionError):
            Rocket(None, 20)


if __name__ == "__main__":
    unittest.main(verbosity=2)