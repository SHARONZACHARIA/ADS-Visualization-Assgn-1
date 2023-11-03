import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


nobel_prize = pd.read_csv('DataSet/nobel_final.csv')

male_laureates = nobel_prize[nobel_prize["gender"] == "male"]
male_laureates_count = male_laureates.groupby("year").size()

female_laureates = nobel_prize[nobel_prize["gender"] == "female"]
female_laureates_count = female_laureates.groupby("year").size()

lauretes_by_country = nobel_prize["born_country_code"].value_counts()
plt.pie(lauretes_by_country)
plt.show()

plt.plot(male_laureates_count,color='#5865f2')
plt.plot(female_laureates_count,color='#a60096')
plt.xlabel('Year')
plt.ylabel('Number of Laurets ')
plt.legend(['Male','Female'])
# plt.xticks(np.arange(1903,2020,15))
plt.show()