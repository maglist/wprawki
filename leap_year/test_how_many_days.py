import unittest
from how_many_days import how_many_days


class MyTestCase(unittest.TestCase):
    def test_normal_months(self):
        self.assertEqual(how_many_days(1, 2001), 31, msg="January should have 31 days")
        self.assertEqual(how_many_days(9,1999), 30, msg="September should have 30 days")

    def test_february(self):
        self.assertEqual(how_many_days(2, 2012), 29, msg="2012 is a leap year")
        self.assertEqual(how_many_days(2, 1999), 28, msg="1999 is not a leap year")
        self.assertEqual(how_many_days(2, 752), 29, msg="752 is a leap year")
        self.assertEqual(how_many_days(2, 28), 29, msg="28 is a leap year")



if __name__ == '__main__':
    unittest.main()
