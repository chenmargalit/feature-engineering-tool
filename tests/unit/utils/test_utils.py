from Utils.data_types import map_dtypes_names
# from test import test

def test_data_types():
    returned_dtype = map_dtypes_names('PassengerId', 'int64')
    assert returned_dtype == 'int64'
    # test()
