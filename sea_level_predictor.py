import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.figure(figsize=(12,6))
    plt.scatter(x, y)
   
    # Create first line of best fit
    regress1 = linregress(x, y)
    last_year = df["Year"].max()
    df = df.append([{"Year": y} for y in range(last_year + 1, 2051)])
    line1 = df['Year'] * regress1.slope + regress1.intercept
    plt.plot(df["Year"], line1, label="First Line of Best Fit", color='red')

    # Create second line of best fit
    df_recent = df.loc[(df["Year"] >= 2000) & (df["Year"] <= last_year)]
    regress2 = linregress(df_recent["Year"], df_recent["CSIRO Adjusted Sea Level"])
    df_recent = df_recent.append([{"Year": y} for y in range(last_year + 1, 2051)])
    line2 = df_recent["Year"] * regress2.slope + regress2.intercept
    plt.plot(df_recent["Year"], line2, label="Second Line of Best Fit", color="orange")
    plt.legend()

    # Add labels and title
    plt.xlabel('Year', fontsize='15')
    plt.ylabel('Sea Level (inches)', fontsize='15')
    plt.title('Rise in Sea Level', fontsize='20')
    
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()