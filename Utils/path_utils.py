import sys


def create_data_path(fname=''):
    root_path = sys.path[1]
    data_folder_path = f'{root_path}/sample_data'
    data_path = f'{data_folder_path}/{fname}'
    return data_path
