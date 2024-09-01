import unittest

from city_functions import city_functions

class CitesTestCase(unittest.TestCase):

    def test_city_country(self):
        santiago_chile = city_functions('santiago', 'chile',5000000)
        self.assertEqual(santiago_chile, 'Santiago, Chile - 5000000')


if __name__ == "__main__":
    unittest.main()
