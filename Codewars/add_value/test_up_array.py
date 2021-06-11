import unittest
from up_array import up_array


class MyTestCase(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(up_array([0]), [1], msg="check list of one integer")
        self.assertEqual(up_array([6]), [7], msg="check list of one integer")
        self.assertEqual(up_array([9]), [1, 0], msg="check list of one integer - result: 2 elements")
        self.assertEqual(up_array([1, 9]), [2, 0], msg="check list of two integers")
        self.assertEqual(up_array([1, 1]), [1, 2], msg="check list of the same two integers")
        self.assertEqual(up_array([7, 9, 2, 5]), [7, 9, 2, 6], msg="check list of four integers")
        self.assertEqual(up_array([9, 9, 9]), [1, 0, 0, 0], msg="check list of three integers - result: 4 elements")
        self.assertEqual(up_array([9, 7, 6, 0, 3, 1, 8, 4, 6, 7, 5, 2]), [9, 7, 6, 0, 3, 1, 8, 4, 6, 7, 5, 3],
                         msg="check long list - all single digits include")

    def test_random_length(self):
        def get_random_data():
            from random import randint
            length = randint(5, 100)
            random_input = [randint(0, 9) for i in range(length)]
            tmp = "".join([str(el) for el in random_input])
            expected_output = [int(el) for el in list(str(int(tmp) + 1))]
            return random_input, expected_output
        for tc_num in range(10):
            input_data, output_data = get_random_data()
            self.assertEqual(up_array(input_data), output_data, msg="check random long data")

    def test_negative(self):
        self.assertEqual(up_array([-1]), None, msg="check list of one negative integer")
        self.assertEqual(up_array([-2, 9, 6, 3]), None, msg="check list of integers with one negative")
        self.assertEqual(up_array([7, 9, -3, 5]), None, msg="check list of integers with one negative")
        self.assertEqual(up_array([4, 6.9, 5, 0.8]), None, msg="check list of integers and floats")
        self.assertEqual(up_array(["u", 6.9, "&", 0.8]), None, msg="check list of strings and floats")
        self.assertEqual(up_array(["a", "6.9", 5, 2, 6]), None, msg="check list of integers and strings")
        self.assertEqual(up_array([10, 7, 44, 6]), None, msg="check list of non single digits")
        self.assertEqual(up_array([]), None, msg="check empty list")


if __name__ == '__main__':
    unittest.main()
