from Utils.general_utils import remove_from_dict


def test_remove_from_dict():
    d = {'keep1': 1, 'remove': 2, 'keep2': 3}
    remove_from_dict(d, ['remove'])
    assert d == {'keep1': 1, 'keep2': 3}