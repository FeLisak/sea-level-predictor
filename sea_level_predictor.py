import pandas as pd  # Imports library for data manipulation
import matplotlib.pyplot as plt  # Imports library for plotting
from scipy.stats import linregress  # Imports function for linear regression

def draw_plot():  # Main function to generate the plot
    # Reads data from CSV file
    df = pd.read_csv('epa-sea-level.csv')  # Loads sea level data

    # Creates the scatter plot
    plt.figure(figsize=(12, 6))  # Sets plot size
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10)  # Plots data points

    # Creates the first trend line using all data
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])  # Calculates linear regression (1880-2050)
    x_pred_all = range(1880, 2051)  # Generates years for prediction
    y_pred_all = res_all.slope * pd.Series(x_pred_all) + res_all.intercept  # Calculates predicted values
    plt.plot(x_pred_all, y_pred_all, 'r', label='Best fit line (1880-2050)')  # Plots trend line (red)

    # Creates the second trend line using data from 2000
    df_2000 = df[df['Year'] >= 2000]  # Filters data from 2000 onwards
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])  # Linear regression (2000-2050)
    x_pred_2000 = range(2000, 2051)  # Generates years for prediction (2000-2050)
    y_pred_2000 = res_2000.slope * pd.Series(x_pred_2000) + res_2000.intercept  # Calculates predicted values
    plt.plot(x_pred_2000, y_pred_2000, 'g', label='Best fit line (2000-2050)')  # Plots trend line (green)

    # Adds labels and title to the plot
    plt.xlabel('Year')  # X-axis label
    plt.ylabel('Sea Level (inches)')  # Y-axis label
    plt.title('Rise in Sea Level')  # Plot title
    plt.legend()  # Shows legend

    # Saves the plot as an image and returns the plot object
    plt.savefig('sea_level_plot.png')  # Saves plot as PNG file
    return plt.gca()  # Returns plot object for testing