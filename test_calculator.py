import sys

import Caluclator
import unittest
class check_calculator(unittest.TestCase):
    def setUp(self):
        self.a=10
        self.b=20
        # print("setup print")
    def tearDown(self):
        self.a=0
        self.b=0
        # print("teardowm print")
    def test_add(self):
        # arrage
        # a=20
        # b=10
        # act
        c=Caluclator.add(self.a,self.b)
        # assert
        self.assertEqual(self.a +self. b, self.c)

    def test_sub(self):

        c = Caluclator.sub(self.a, self.b)
        self.assertEqual(self.a - self. b,self. c)
    # @unittest.skipUnless(sys.platform.startswith("linux"),"requires not windows os")
    def test_mul(self):

        c = Caluclator.mul(self.a,self. b)
        self.assertEqual(self.a * self.b,self. c)
    # @unittest.skipIf(sys.platform.startswith("drawim"),"requries maxbook")
    def test_div(self):

        c = Caluclator.div(self.a, self.b)
        self.assertEqual(self.a /self.b, self.c)
if __name__=="__main__":
    unittest.main()