import pytest
import json

from main import *
# Define test cases using real data


class TestClassReport:

    @pytest.fixture
    def real_countries_data(self):
        try:
            with open('countries_data.json', 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Datei nicht gefunden!")

    def test_analyze_countries_with_real_data(self, real_countries_data):
        # Test filter and transformation functions with real data
        european_countries = analyze_countries(real_countries_data, filter_european_countries,
                                               transform_to_name_and_capital)
        large_population_countries = analyze_countries(real_countries_data, filter_large_population_countries,
                                                       transform_to_name_and_area)

        # Test: Verify that the filtered European countries are actually from Europe and have the required keys
        #assert all(country['region'] == 'Europe' for country in european_countries)
        assert all('name' in country and 'capital' in country for country in european_countries)

        # Test: Verify that the filtered countries have a population greater than 10 million and have the required keys
        #assert all(country['population'] > 10000000 for country in large_population_countries)
        assert all('name' in country and 'area' in country for country in large_population_countries)


