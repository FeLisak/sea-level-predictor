# Sea Level Predictor

This project aims to **analyze and visualize the rise in sea level** over the years using historical data provided by CSIRO and EPA. The main logic is implemented in the [`sea_level_predictor.py`](./sea_level_predictor.py) file.

## Overview

The process begins by reading sea level data from the CSV file [`epa-sea-level.csv`](./epa-sea-level.csv), which contains annual records of adjusted measurements. The data is loaded and prepared for analysis using the `pandas` library.

## Data Visualization & Analysis

The code then uses `matplotlib` to create a **scatter plot**, visually representing the relationship between year and sea level. To understand the trends, two linear regressions are applied:

- **First regression:** Considers all available data, generating a trend line that predicts sea level behavior from 1880 to 2050.
- **Second regression:** Focuses on data from the year 2000 onwards, allowing observation of any acceleration or significant change in the recent trend, also projecting to 2050.

These trend lines are calculated using the `linregress` function from the `scipy` library and are displayed on the plot with distinct colors for easy visual comparison. The plot includes axis labels, a title, and a legend for clear interpretation.

## Output

Finally, the generated plot is saved as an image file ([`sea_level_plot.png`](./sea_level_plot.png)), enabling easy sharing and analysis of the results. The code returns the plot object for possible automated testing.
