#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_max_integer(self):
        self.assertEqual(max_integer([5, 6, 9]), 9)
        self.assertEqual(max_integer([5, 9, 5]), 9)
        self.assertEqual(max_integer([100]), 100)
        self.assertEqual(max_integer([5.2, 6.7, 9.3]), 9.3)
        self.assertEqual(max_integer([-5, -6, -9]), -5)
        self.assertEqual(max_integer([-5.2, -6.7, -9.3]), -5.2)
        self.assertEqual(max_integer("123453276921"), "9")
        self.assertEqual(max_integer('abc'), 'c')
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer([None]), None)
        self.assertEqual(max_integer([[5, 6, 7], [5, 6, 7]]), [5, 6, 7])
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([7, 1, 10, 16, None])


if __name__ == "__main__":
    unittest.main()
