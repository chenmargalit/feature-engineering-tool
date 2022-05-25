from Utils.data_types import map_dtypes


class StatisticsCalculations:

    def __init__(self, df):
        self.df = df
        self.data = {}
        self.dtypes = map_dtypes(df)

    def calculate_measurement(self, measurement_type):
        for col_name in self.dtypes['number']:
            match measurement_type:
                case 'mean':
                    self.data[col_name] = self.df[col_name].mean()
                case 'median':
                    self.data[col_name] = self.df[col_name].median()
                case 'std':
                    self.data[col_name] = self.df[col_name].std()
        return self.data
