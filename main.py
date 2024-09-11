def filter_european_countries(country):
    """
    Filtert europäische Länder aus der Liste.

    Args:
    - country: Ein Dictionary, das ein Land repräsentiert

    Returns:
    - True, wenn das Land in Europa liegt, sonst False
    """
    # TODO: Implementiere die Funktion hier
    pass


def filter_large_population_countries(country):
    """
    Filtert Länder mit einer Bevölkerung von mehr als 10 Millionen.

    Args:
    - country: Ein Dictionary, das ein Land repräsentiert

    Returns:
    - True, wenn das Land eine Bevölkerung von mehr als 10 Millionen hat, sonst False
    """
    # TODO: Implementiere die Funktion hier
    pass


def transform_to_name_and_capital(country):
    """
    Transformiert das Länder-Dictionary, sodass nur der Name und die Hauptstadt zurückgegeben werden.

    Args:
    - country: Ein Dictionary, das ein Land repräsentiert

    Returns:
    - Ein Dictionary mit dem Namen und der Hauptstadt des Landes
    """
    # TODO: Implementiere die Funktion hier
    pass


def transform_to_name_and_area(country):
    """
    Transformiert das Länder-Dictionary, sodass nur der Name und die Fläche zurückgegeben werden.

    Args:
    - country: Ein Dictionary, das ein Land repräsentiert

    Returns:
    - Ein Dictionary mit dem Namen und der Fläche des Landes
    """
    # TODO: Implementiere die Funktion hier
    pass


def analyze_countries(data, filter_func, transform_func):
    """ 
    Analysiert eine Liste von Länderdaten. Verwendet 'filter_func' zum Filtern und 'transform_func' zum Transformieren der Länderdaten.
    Diese Funktion wendet transform_func auf jedes Element von Data das den kriterien in filter_func entspricht und gibt diese Liste dann zurück.
    
    Args:
    - data: Liste von Ländern als Dictionaries
    - filter_func: Funktion zum Filtern der Länder
    - transform_func: Funktion zum Transformieren der Länderdaten

    Returns:
    - Liste von transformierten Länderdaten
    """
    # TODO: Implementiere die Funktion hier
    pass


if __name__ == '__main__':
    """ Hauptfunktion zum Ausführen des Programms """
    # TODO: JSON-Datei (countries_data.json) öffnen und Daten laden
    countries_data = None

    # Europäische Länder filtern und nach Name und Hauptstadt transformieren
    european_countries = analyze_countries(countries_data, filter_european_countries, transform_to_name_and_capital)
    print('Europäische Länder (Name und Hauptstadt):', european_countries)

    # Länder mit mehr als 10 Millionen Einwohnern filtern und nach Name und Fläche transformieren
    large_population_countries = analyze_countries(countries_data, filter_large_population_countries,
                                                   transform_to_name_and_area)
    print('Länder mit mehr als 10 Millionen Einwohnern (Name und Fläche):', large_population_countries)
