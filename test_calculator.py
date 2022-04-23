import unittest
from calculator import Calculations
from calculator import Helper
from calculator import Parser

class MyTestCase(unittest.TestCase):

    #unit tests
    def test_add(self):
        self.assertEqual(Calculations.add(2,3), 5)

    def test_sub(self):
        self.assertEqual(Calculations.sub(4,3), 1)

    def test_mult(self):
        self.assertEqual(Calculations.mult(4,3), 12)

    def test_div(self):
        self.assertEqual(Calculations.div(4,4), 1)
    
    def test_find_all_operations(self):
        eq = "2*8*2+4/4-3"
        self.assertEqual(Helper.find_all_operations(eq), [1,3,5,7,9])

    def test_recurisvemult(self):
        eq = "2*8*2+4/4-3"
        self.assertEqual(Parser.recursivemult(eq), '32+1-3')

    def test_recursiveadd(self):
        eq = "32+1-3"
        self.assertEqual(Parser.recursiveadd(eq), '30')

    #integration tests
    def test_together(self):
        eq = "2*8*2+4/4-3"
        self.assertEqual(Helper.together(eq), '30')



if __name__ == '__main__':
    unittest.main()