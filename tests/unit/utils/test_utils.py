import pandas as pd
from Utils.data_types import map_dtypes, map_dtypes_names
from Utils.path_utils import create_data_path

data_path = create_data_path()


def test_data_types():
    number1 = map_dtypes_names('Age', 'int64')
    return_number = map_dtypes_names('Passenger', 'float64')

    assert number1 == 'number'
    assert return_number == 'number'


def test_map_dtypes():
    df = pd.read_csv(f'{data_path}/titanic.csv')
    types = map_dtypes(df)
    print(types)
    assert types['number'] == ['PassengerId', 'Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
    assert types['str_or_mixed'] == ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']


def test_create_data_path():
    path = create_data_path('titanic.csv')
    assert 'feature-engineerer/sample_data/titanic.csv' in path



