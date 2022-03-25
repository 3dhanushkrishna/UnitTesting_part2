import unittest
def list():
    mylist=[1,2,3,4,'dhanush']
    return mylist
class mylistchecker(unittest.TestCase):
    def test_mylist1(self):
        element = 23
        self.assertIn(element, list())

    def test_mylist2(self):
        element = 23
        self.assertNotIn(element, list())
if __name__=="__main__":
    unittest.main()