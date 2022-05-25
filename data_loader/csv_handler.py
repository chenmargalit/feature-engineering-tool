import pandas as pd


class CsvHandler:

    def __init__(self, path: str):
        self.path = path
        self.df = None

    def load_csv(self):
        try:
            self.df = pd.read_csv(self.path, low_memory=False)
            return self.df
        except FileNotFoundError:
            print('File has not been found, please check the path')

    def present_table(self, num_of_rows=5):
        if self.df:
            self.df.head(num_of_rows)
        else:
            self.load_csv()
            print(self.df.head(num_of_rows))
