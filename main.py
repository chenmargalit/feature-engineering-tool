from data_loader.csv_handler import CsvHandler
from data_manipulations.statistics_calculations import StatisticsCalculations
from Utils.data_types import map_dtypes


csv_handler = CsvHandler('./sample_data/titanic_data.csv')
df = csv_handler.load_csv()
statistics_calculator = StatisticsCalculations(df)
means = statistics_calculator.calculate_measurement('std')
print(means)





