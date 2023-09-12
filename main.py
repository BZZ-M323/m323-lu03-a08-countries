import json

def filter_european_countries(country):
    """
    Filter European countries from the list.

    Args:
    - country: A dictionary representing a country

    Returns:
    - True if the country is in Europe, otherwise False
    """
    return country['region'] == 'Europe'


def filter_large_population_countries(country):
    """
    Filter countries with a population of more than 10 million.

    Args:
    - country: A dictionary representing a country

    Returns:
    - True if the country has a population of more than 10 million, otherwise False
    """
    return country['population'] > 10000000


def transform_to_name_and_capital(country):
    """
    Transform the country dictionary so that only the name and the capital are returned.

    Args:
    - country: A dictionary representing a country

    Returns:
    - A dictionary with the name and the capital of the country
    """
    return {'name': country['name'], 'capital': country['capital']}


def transform_to_name_and_area(country):
    """
    Transform the country dictionary so that only the name and the area are returned.

    Args:
    - country: A dictionary representing a country

    Returns:
    - A dictionary with the name and the area of the country
    """
    return {'name': country['name'], 'area': country['area']}


def analyze_countries(data, filter_func, transform_func):
    """
    Analyze a list of country data. Uses 'filter_func' to filter and 'transform_func' to transform the country data.

    Args:
    - data: List of countries as dictionaries
    - filter_func: Function to filter the countries
    - transform_func: Function to transform the country data

    Returns:
    - List of transformed country data
    """
    return [transform_func(country) for country in data if filter_func(country)]


if __name__ == '__main__':
    """ Hauptfunktion zum Ausführen des Programms """
    # TODO: JSON-Datei (countries_data.json) öffnen und Daten laden
    countries_data = None
    try:
        with open('countries_data.json', 'r', encoding='utf-8') as file:
            countries_data = json.load(file)
    except FileNotFoundError:
        print("Datei nicht gefunden!")

    # Europäische Länder filtern und nach Name und Hauptstadt transformieren
    european_countries = analyze_countries(countries_data, filter_european_countries, transform_to_name_and_capital)
    print('Europäische Länder (Name und Hauptstadt):', european_countries)

    # Länder mit mehr als 10 Millionen Einwohnern filtern und nach Name und Fläche transformieren
    large_population_countries = analyze_countries(countries_data, filter_large_population_countries,
                                                   transform_to_name_and_area)
    print('Länder mit mehr als 10 Millionen Einwohnern (Name und Fläche):', large_population_countries)
