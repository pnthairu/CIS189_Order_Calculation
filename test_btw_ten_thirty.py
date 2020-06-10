"""
Program: test_btw_ten_thirty.py
Author: Paul Thairu
Last date modified: 06/10/2020

The purpose of this program is to calculate discount based on coupons and percentage discount
for item price which is between 10 and 30 dollars.
The program calculates the discount amount
add shipping cost
then calculate tax
then finally give the final sales price
"""
import unittest
from store import test_price_under_between_ten_thirty_calc


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(test_price_under_between_ten_thirty_calc.calculate_price(15.63), 15.99, 5, 20)


if __name__ == '__main__':
    unittest.main()
