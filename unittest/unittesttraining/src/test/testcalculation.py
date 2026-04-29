import sys
import unittest

from src.calculation import add, sub, mul, div, ne


class TestCalculation(unittest.TestCase):
    def test_add(self):
        res=add(10,20)
        self.assertEqual(30, res, msg='Addition error')

    def test_sub(self):
        res = sub(10,5)
        self.assertEqual(5, res, msg='Subtraion error')

    def test_mul(self):
        res = mul(10, 2)
        self.assertEqual(20, res, msg='Multiplication error')

    def test_div(self):
        res = div(10, 2)
        self.assertEqual(5, res, msg='Division error')

    def test_div1(self):
        with self.assertRaises(ZeroDivisionError, msg='Division error'):
            div(10, 0)

    @unittest.skipIf(sys.version_info[:2] < (3, 13), reason="not impl yet")
    def test_ne(self):
        res = ne(10, 10)
        self.assertFalse(res, msg="10 should equal 10")
