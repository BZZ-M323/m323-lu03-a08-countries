import json
import unittest
from main import filter_european_countries, filter_large_population_countries, transform_to_name_and_capital, transform_to_name_and_area, analyze_countries


class TestMainFunctions(unittest.TestCase):

    def test_filter_european_countries(self):
        country1 = {
            'name': 'Germany',
            'region': 'Europe',
            'population': 83000000,
            'area': 357022,
        }
        country2 = {
            'name': 'India',
            'region': 'Asia',
            'population': 1393409038,
            'area': 3287263,
        }
        self.assertTrue(filter_european_countries(country1))
        self.assertFalse(filter_european_countries(country2))

    def test_filter_large_population_countries(self):
        country1 = {
            'name': 'Germany',
            'region': 'Europe',
            'population': 83000000,
            'area': 357022,
        }
        country2 = {
            'name': 'Iceland',
            'region': 'Europe',
            'population': 368010,
            'area': 103000,
        }
        self.assertTrue(filter_large_population_countries(country1))
        self.assertFalse(filter_large_population_countries(country2))

    def test_transform_to_name_and_capital(self):
        country = {
            'name': 'Germany',
            'capital': 'Berlin',
            'region': 'Europe',
            'population': 83000000,
            'area': 357022,
        }
        self.assertEqual(
            transform_to_name_and_capital(country),
            {'name': 'Germany', 'capital': 'Berlin'},
        )

    def test_transform_to_name_and_area(self):
        country = {
            'name': 'Germany',
            'capital': 'Berlin',
            'region': 'Europe',
            'population': 83000000,
            'area': 357022,
        }
        self.assertEqual(
            transform_to_name_and_area(country), {'name': 'Germany', 'area': 357022}
        )

    def test_analyze_countries(self):
        # Test with real data
        with open('countries_data.json', 'r', encoding='utf-8') as file:
            real_data = json.load(file)

        result1 = analyze_countries(real_data, filter_european_countries, lambda x: x)
        self.assertTrue(all(country['region'] == 'Europe' for country in result1))

        result2 = analyze_countries(
            real_data, filter_large_population_countries, lambda x: x
        )
        self.assertTrue(all(country['population'] > 10000000 for country in result2))
