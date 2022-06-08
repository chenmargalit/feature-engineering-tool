import pandas as pd
from Utils.data_types import map_dtypes
from Utils.path_utils import create_data_path

p = create_data_path('titanic.csv')


df = pd.read_csv(p)
types = map_dtypes(df)
print(types)





