import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


nobel_prize = pd.read_csv('DataSet/nobel_final.csv')

male_laureates = nobel_prize[nobel_prize["gender"] == "male"]
male_laureates_count = male_laureates.groupby("year").size()

female_laureates = nobel_prize[nobel_prize["gender"] == "female"]
female_laureates_count = female_laureates.groupby("year").size()

lauretes_by_country = nobel_prize["born_country_code"].value_counts()
top_5_countries = lauretes_by_country.head(5)
other_count = lauretes_by_country[5:].sum()
top_5_countries['Other'] = other_count

plt.pie(top_5_countries, labels=top_5_countries.index, autopct='%1.1f%%')
plt.show()

plt.plot(male_laureates_count,color='#5865f2')
plt.plot(female_laureates_count,color='#a60096')
plt.xlabel('Year')
plt.ylabel('Number of Laurets ')
plt.legend(['Male','Female'])
plt.show()


