import unittest
from city_functions import city_function

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        format_name = city_function('santiago','chile')
        self.assertEqual(format_name,'Santiago,Chile')

    def test_city_country_population(self):
        format_name = city_function('santiago','chile',5000000)
        self.assertEqual(format_name,'Santiago,Chile - population 5000000')

unittest.main()