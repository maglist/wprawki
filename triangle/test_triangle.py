import unittest
from triangle import triangle


class MyTestCase(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(triangle(6, 6, 6), "Equilateral triangle", msg="Check equilateral triangle")
        self.assertEqual(triangle(14, 14, 10), "Isosceles triangle", msg="Check isosceles triangle")
        self.assertEqual(triangle(3,4,5), "Scalene triangle", msg="Check scalene triangle")

    def test_negative(self):
        self.assertEqual(triangle(-7, 7, 9), "wrong parameters", msg="check negative values")
        self.assertEqual(triangle(2, 2, 9), "wrong parameters", msg="check triangle rule")
        self.assertEqual(triangle(2, 2, 4), "wrong parameters", msg="check triangle rule")
        self.assertEqual(triangle("g", 3, 7), "wrong parameters", msg="check whether values are integers")
        self.assertEqual(triangle(6.0, 7.2, 5), "wrong parameters", msg="check whether values are integers")
        self.assertEqual(triangle(2, 0, 2), "wrong parameters", msg="check whether values are greater than zero")
        # self.assertEqual(triangle(2, 2), "incorect amount of values", msg="check amount of values")
        # self.assertEqual(triangle(4, 5, 3, 8), "incorect amount of values", msg="check amount of values")


if __name__ == '__main__':
    unittest.main()
