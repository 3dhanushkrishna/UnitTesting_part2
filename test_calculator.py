import Caluclator
import unittest
class check_calculator(unittest.TestCase):
    def test_add(self):
        a=20
        b=10
        c=Caluclator.add(a,b)
        self.assertEqual(a+b,c)

    def test_sub(self):
        a = 20
        b = 10
        c = Caluclator.sub(a, b)
        self.assertEqual(a - b, c)

    def test_mul(self):
        a = 20
        b = 10
        c = Caluclator.mul(a, b)
        self.assertEqual(a * b, c)

    def test_div(self):
        a = 20
        b = 10
        c = Caluclator.div(a, b)
        self.assertEqual(a / b, c)
if __name__=="__main__":
    unittest.main()