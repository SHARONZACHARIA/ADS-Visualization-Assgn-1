"""Importing required python packages"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

country_code_to_name={
    'US':'United States',
    'DE':'Germany',
    'FR':'France',
    'GB':'United Kingdom',
    'SE':'Sweden',
    'Other': 'Other Countries'
}

""" 
Reading data set using pandas  
"""
nobel_prize = pd.read_csv('DataSet/nobel_final.csv')

""""
Calculating number of male and female noble nobel laureates each year
Filtering out data set using gender and grouping it by year
"""
male_laureates = nobel_prize[nobel_prize["gender"] == "male"]
male_laureates_count = male_laureates.groupby("year").size()
female_laureates = nobel_prize[nobel_prize["gender"] == "female"]
female_laureates_count = female_laureates.groupby("year").size()


""" Filtering Top 5 countrues in which  laureates are born"""
lauretes_by_country = nobel_prize["born_country_code"].value_counts()

""" 
Filtering out top 5 countries 
Adding the rest of countries to a single item in top_5_countries list 
"""
top_5_countries = lauretes_by_country.head(5)
other_count = lauretes_by_country[5:].sum()
top_5_countries['Other'] = other_count

""" Fetching the number of nobel prize  lauretes by age """
age_counts = nobel_prize['age_get_prize'].value_counts().sort_index()

""" function to plot Bar chart """
def PlotBar(age_counts):
    plt.bar(age_counts.index.to_list(),age_counts.to_list())
    plt.title("Number of Nobel Prize Laureates by Age")
    plt.xlabel("Age")
    plt.ylabel("Number of Laureates")
    plt.show()


""" function to plot line graph """
def PlotLineGraph(male_count, female_count):
    plt.plot(male_count, color='#5865f2')
    plt.plot(female_count, color='#a60096')
    plt.xlabel('Year')
    plt.ylabel('Number of Laurets ')
    plt.legend(['Male', 'Female'])
    plt.show()


""" Setting index of top_5_countries """
top_5_countries.index = top_5_countries.index.map(country_code_to_name)

""" function to plot pie chart """
def PlotPie(xyaxis):
    plt.pie(xyaxis, labels=top_5_countries.index, autopct='%1.1f%%')
    # plt.legend(xyaxis.index, loc='lower right')
    plt.show()

""" Function calls """
PlotPie(top_5_countries)
PlotLineGraph(male_laureates_count, female_laureates_count)
PlotBar(age_counts)

