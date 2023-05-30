import unittest
from main import quadcc

class quadtest(unittest.TestCase):
    def test_ab_zero(self):
        res = quadcc(0, 0, 5)
        self.assertEqual(res, (None, None))

    def test_solution_one(self):
        res = quadcc(1, 6, 9)
        self.assertEqual(res, (-3, None))

    def test_solution_double(self):
        res = quadcc(4, 12, 8)
        self.assertEqual(res, (-1, -2))

    def test_solution_d_less_than_zero(self):
        res = quadcc(2, 3, 3)
        self.assertEqual(res, (None, None))


if __name__ == '__main__':
    unittest.main()