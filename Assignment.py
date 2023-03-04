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
import pandas as pd
import matplotlib.pyplot as plt 





def load_data():
    """
    Load India economic data, including growth, per capita income, and GDP.

    Returns
    -------
    A data frame containing India's economic data from 2011 to 2021

    """
    
    # Load data in as a pandas DataFrame
    df = pd.read_csv('India_GDP_1960-2022.csv', skiprows=1, index_col=0)
    df= df.iloc[:11]
    
    return df

print (load_data())

india_df = load_data()

def indicators_line_plot():
    """
    A function that plots India's economic indicators from 2011 to 2021.

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
    The function displays a bar chart comparing GDP over the previous five years.

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
    The function displays a scatter plot of GDP and per capita income in rupees.

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
                              

          

