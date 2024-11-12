# summary_statistics.py
import pandas as pd

def save_summary_statistics(data):
    summary_stats = data.describe()
    summary_stats.to_csv('reports/summary_statistics.csv')

def main():
    data = pd.read_csv('D:/DataScienceProject/Data/processed_covid19_data.csv')
    save_summary_statistics(data)

if __name__ == '__main__':
    main()
