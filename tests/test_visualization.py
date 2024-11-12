import matplotlib.pyplot as plt
import os
import sys

# Add the parent directory of the current file to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from my_scripts.visualization import plot_new_cases

def plot_new_cases():
    data = {
        'date': ['2020-01-01', '2020-01-02'],
        'total_cases': [100, 200]
    }
    plot =  plot_new_cases(data)
    assert isinstance(plot, plt.Figure), "Plotting function did not return a Figure object"

if __name__ == "__main__":
     plot_new_cases()