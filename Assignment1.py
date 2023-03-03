# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""

Created on Mon Feb 28 16:25:08 2023

@author: Awofisayo Victoria oladipo

"""

#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 



data_url='https://storage.googleapis.com/kaggle-data-sets/2626334/4488794/bundle/archive.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20230302%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20230302T153025Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=7ba2cd427211238aed1cc8925611b7242a66d1485ca7aaaaa3d81b1acd18b47c3f401980ab9fb5ff1fba9387cdf09e226265b60708abd0eae0b43060c7f7652fd58e223e8cd9d456a062e436804329b419f68f7d726ef3717add901586865345643b681b903f73d1e47f22afda3c47c0cafcbb21c4c57169e4bf049a46409249dabab1bac9a62dd99c10d709d2a31e930fdd2af6da16abbc23b9c607507fefb2ab05a9db1ac06def61bb04625d2c8f96de58a96686d16adfc2b8c6b89c403845c5729b087a34ef4f51d81ddf4e19d2c5062343412b4867bdcedb45220302a3b5a65488928469c8484b7d3b286d3617e9e933363ea94fc1fe90e2dce2668a77ca'

def load_data():
    """
    load India economic data showing its growth, per capital income and GDP.

    Returns
    -------
    A data frame of india economic data between 2011 to 2021

    """
    
    # Load data in as a pandas DataFrame
    df = pd.read_csv('India_GDP_1960-2022.csv', skiprows=1, index_col=0)
    df= df.iloc[:11]
    
    return df

print (load_data())

india_df = load_data()

def indicators_line_plot():
    """
    A function showing the plot of india's economic indicators
    between 2011 to 2021

    Returns
    -------
    """
    
    plt.figure()
    plt.plot(india_df['Year'], india_df['GDP in (Billion) $'], label= 'GDP')
    plt.plot(india_df['Year'], india_df['Growth %'], label= 'Growth')
    plt.plot(india_df['Year'], india_df['Per Capita in rupees'],label= 'Per_capita')
    
    #Add title, labels and legend
    plt.title("METRICS FOR INDIA", color='r')
    plt.xlabel('Year')
    plt.ylabel('Indicators')
    plt.legend()
    
    plt.savefig('LINE_PLOT.PNG')
    return plt.show()

print(indicators_line_plot())


def bar_chart_gdp(years):
    """
    The function shows a bar chart comparing gdp for the last five years

    Returns
    -------
    """    

    bar_data = india_df.iloc[:5] 
    print(bar_data)
    
    plt.figure()
    plt.bar(bar_data['Year'], bar_data['GDP in (Billion) $'], width=0.5)
    
    #Add title and label
    plt.title("GDP OF INDIA FOR THE LAST FIVE YEARS", color='r')
    plt.xlabel("Year")
    plt.ylabel("GDP in (Billion) $")
    
    plt.savefig('BAR_CHART1.PNG')
    plt.show()
    
years = [2017,2018,2019,2020,2021]

print(bar_chart_gdp(years))


india_df['GDP in(billion) rupees'] = india_df["GDP in (Billion) $"] * 0.012
print(india_df)

def scatter_plot_gdp(years):
    """
    The function shows a scatter plot comparing gdp and per capita in rupees

    Returns
    -------
    """  

    x = india_df.iloc[:, 1]
    y = india_df.iloc[:, 4]

    plt.figure()
    plt.scatter(x,y)
    
    #Add title,label and legend
    plt.title("A SCATTER PLOT COMPARING GDP AND PER CAPITA IN RUPEES", color='r')
    plt.xlabel("GDP in (Billion) rupees") 
    plt.ylabel("Per Capita in rupees")
    plt.legend(['Data Point'], loc='lower right')
    
    plt.savefig('SCATTERPLOT.PNG')
    plt.show()
    
print(scatter_plot_gdp(years))
                              

          

