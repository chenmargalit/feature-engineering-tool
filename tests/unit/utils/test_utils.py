import pandas as pd
from Utils.data_types import map_dtypes, map_dtypes_names


def test_data_types():
    number1 = map_dtypes_names('Age', 'int64')
    return_number = map_dtypes_names('Passenger', 'float64')

    assert number1 == 'number'
    assert return_number == 'number'


def test_map_dtypes():
    df = pd.read_csv('sample_roseman_data.csv')
    types = map_dtypes(df)
    print(types)
    assert types['number'] == ['Store', 'DayOfWeek', 'Sales', 'Customers', 'Open', 'Promo', 'StateHoliday', 'SchoolHoliday']
    assert types['str_or_mixed'] == ['Date']


