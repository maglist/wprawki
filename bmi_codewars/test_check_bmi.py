import unittest
from bmi import check_bmi

def get_weight(bmi):
    h = 1.7
    w = bmi * h**2
    return w

class MyTestCase(unittest.TestCase):
    def test_boundary_values(self):
        self.assertEqual(check_bmi(get_weight(18.50), 1.7), "Underweight", msg="check bmi for underweight")
        self.assertEqual(check_bmi(get_weight(18.51), 1.7), "Normal", msg="check bmi for normal")
        self.assertEqual(check_bmi(get_weight(25.0), 1.7), "Normal", msg="check bmi for normal")
        self.assertEqual(check_bmi(get_weight(25.01), 1.7), "Overweight", msg="check bmi for overweight")
        self.assertEqual(check_bmi(get_weight(30.0), 1.7), "Overweight", msg="check bmi for overweight")
        self.assertEqual(check_bmi(get_weight(30.01), 1.7), "Obese", msg="check bmi for obese")

    def test_values_positive(self):
        """
        Normal values for weight and height
        """
        self.assertEqual(check_bmi(32, 1.5), "Underweight", msg="check bmi for underweight")
        self.assertEqual(check_bmi(30, 0.9), "Obese", msg="check bmi for obese")
        self.assertEqual(check_bmi(75, 1.9), "Normal", msg="check bmi for normal")
        self.assertEqual(check_bmi(69, 1.65), "Overweight", msg="check bmi for overweight")

    def test_values_negative(self):
        self.assertEqual(check_bmi(22, 0), "Wrong value", msg="check bmi for wrong value")
        self.assertEqual(check_bmi(0, 0), "Wrong value", msg="check bmi for wrong value")
        self.assertEqual(check_bmi(0, 0.6), "Wrong value", msg="check bmi for wrong value")
        self.assertEqual(check_bmi(-22, 1.7), "Wrong value", msg="check bmi for wrong value")
        self.assertEqual(check_bmi(-33, 0), "Wrong value", msg="check bmi for wrong value")
        self.assertEqual(check_bmi(22, -2.1), "Wrong value", msg="check bmi for wrong value")
        self.assertEqual(check_bmi(0, -1.4), "Wrong value", msg="check bmi for wrong value")


if __name__ == '__main__':
    unittest.main()



