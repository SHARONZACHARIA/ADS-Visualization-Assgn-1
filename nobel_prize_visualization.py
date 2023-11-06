"Importing required python packages"
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"Reading data set using pandas"
nobel_prize = pd.read_csv('DataSet/nobel_final.csv')

"Calculating number of male noble lauretes each year"
male_laureates = nobel_prize[nobel_prize["gender"] == "male"]
male_laureates_count = male_laureates.groupby("year").size()

"Calculating number of female noble lauretes each year"
female_laureates = nobel_prize[nobel_prize["gender"] == "female"]
female_laureates_count = female_laureates.groupby("year").size()

"Filtering Top 5 countrues in which where laurates are born"
lauretes_by_country = nobel_prize["born_country_code"].value_counts()
top_5_countries = lauretes_by_country.head(5)

"Adding the rest of countries to a single item in top_5_countries list"
other_count = lauretes_by_country[5:].sum()
top_5_countries['Other'] = other_count



def PlotLineGraph(male_count , female_count):
    plt.plot(male_count,color='#5865f2')
    plt.plot(female_count,color='#a60096')
    plt.xlabel('Year')
    plt.ylabel('Number of Laurets ')
    plt.legend(['Male','Female'])
    plt.show()


def PlotPie(xyaxis):
    plt.pie(xyaxis, labels=xyaxis.index, autopct='%1.1f%%')
    plt.show()

PlotPie(top_5_countries)
PlotLineGraph(male_laureates_count,female_laureates_count)