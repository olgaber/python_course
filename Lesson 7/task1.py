import unittest


def is_leap_year(yyyy):
    if yyyy % 4 == 0 and yyyy % 100 != 0 or yyyy % 400 == 0:
        return True
    else:
        return False


def is_triangle(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        return True
    else:
        return False


class TasksTests(unittest.TestCase):
    def test_one(self):
        res = is_leap_year(1984)
        self.assertTrue(res, True)

    def test_two(self):
        res = is_leap_year(2021)
        self.assertFalse(res, False)

    def test_three(self):
        res = is_leap_year(1901)
        with self.assertRaises(AssertionError):
            self.assertTrue(res, True)

    def test_four(self):
        res = is_leap_year(2000)
        with self.assertRaises(AssertionError):
            self.assertFalse(res, False)

    def test_a_five(self):
        res = is_triangle(3, 4, 5)
        self.assertTrue(res, True)

    def test_b_six(self):
        res = is_triangle(10, 30, 7)
        with self.assertRaises(AssertionError):
            self.assertTrue(res, False)

    @unittest.expectedFailure(unittest.TestCase)
    def test_c_seven(self):
        res = is_triangle(5, 15, 3)
        self.assertTrue(res, True)


if __name__ == "__main__":
    unittest.main()

