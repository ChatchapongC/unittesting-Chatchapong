import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())
        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(1, 0)
        self.assertEqual("1/0", f.__str__())

    def test_negative_number(self):
        self.assertEqual(Fraction(1,2),Fraction(-6, -12))
        self.assertEqual(Fraction(-1,4),Fraction(-4,16))
        self.assertNotEqual(Fraction(5,-7),Fraction(5, 7))

    def test_not_int_input(self):
        with self.assertRaises(TypeError):
            frc = Fraction(1.5,0)

    # Here is an example, but you must add more test cases.  
    # The test requires that your __eq__ is correct.
    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        self.assertEqual(Fraction(-5,6), Fraction(-1,3)+Fraction(-1,2))

    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        a = Fraction(1,0)
        b = Fraction(-1,0)
        c = Fraction(0)
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        self.assertFalse(a == b)
        self.assertFalse(a.__eq__(b))
        self.assertFalse((b == c))
        self.assertFalse((b.__eq__(c)))

    def test_mul(self):
        self.assertEqual(Fraction(3,2), Fraction(3,5)*Fraction(5,2))
        self.assertEqual(Fraction(0), Fraction(0)*Fraction(0))
