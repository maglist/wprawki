import unittest
from find_unique_element import find_uniq


class MyTestCase(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(find_uniq([1, 3, 1, 1, 1]), 3, msg="check list of integers")
        self.assertEqual(find_uniq([0.7, 0.7, 0.4]), 0.4, msg="check list of floats-last element is unique")
        self.assertEqual(find_uniq([1, 0.6, 1, 1, 1]), 0.6, msg="check list of mix int + float")
        self.assertEqual(find_uniq([-1, -0.8, -1, -1, -1]), -0.8, msg="check list of negative mix inf + float")
        self.assertEqual(find_uniq([2, 7, 7]), 2, msg="check list - first element is unique")

    def test_negative(self):
        self.assertEqual(find_uniq(["a", "a", "c", "a"]), "Wrong type of input", msg="check behaviour for strings")
        self.assertEqual(find_uniq([3, "!", "!", "!"]), "Wrong type of input",
                         msg="check behaviour for strings and numbers")
        self.assertEqual(find_uniq([3.1, 3.1, 3.1, 3.1]), "Lack of unique element",
                         msg="check list without unique element")


if __name__ == '__main__':
    unittest.main()
