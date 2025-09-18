import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10)

    # Create first line of best fit (all data)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred_all = range(1880, 2051)
    y_pred_all = res_all.slope * pd.Series(x_pred_all) + res_all.intercept
    plt.plot(x_pred_all, y_pred_all, 'r', label='Best fit line (1880-2050)')

    # Create second line of best fit (from 2000)
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    x_pred_2000 = range(2000, 2051)
    y_pred_2000 = res_2000.slope * pd.Series(x_pred_2000) + res_2000.intercept
    plt.plot(x_pred_2000, y_pred_2000, 'g', label='Best fit line (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()