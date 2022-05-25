import matplotlib.pyplot as plt
import numpy as np


class PresentCharts:

    @staticmethod
    def show_bars(measurement, labels, data):
        fig, ax = plt.subplots()
        ax.barh(labels, data)
