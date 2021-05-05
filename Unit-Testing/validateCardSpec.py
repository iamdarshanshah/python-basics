import unittest

from validateCard import *


class CardValidationTest(unittest.TestCase):

    def setUp(self):
        print('Setup')

    def test_validateCard_valid(self):
        result = validateCard(date(2021, 5, 5))
        self.assertEqual('Valid', result)

    def test_validateCard_expired(self):
        result = validateCard(date(2020, 5, 5))
        self.assertEqual('Expired', result)

    def test_validateCardException_expired(self):
        with self.assertRaises(RuntimeError):
            validateCardException(date(2020, 5, 5))

    def test_validateCardException_valid(self):
        with self.assertRaises(RuntimeError):
            validateCardException(date(2022, 5, 5))

    def tearDown(self): print('Tear Down')


if __name__ == '__main__':
    unittest.main()
