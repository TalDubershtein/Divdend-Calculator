"""
This python program shows the average return value in each sector .
"""

from actions import *
from data import *
import matplotlib.pyplot as plt

X = ['Basic_materials', 'Communication_services', 'Consumer_cyclical', 'Counsumer_Defensive', 'Energy', 'Financial',
     'Healthcare', 'Indusreials', 'Real_estate', 'Tech', 'Utilites']
avaragelist = []


def avarage(list1):
    sum = 0
    if len(list1) == 0:
        return 0
    for i in range(len(list1)):
        sum = sum + company(list1[i], First_year, Second_year)[6]
    return sum / len(list1)

#Graph creation
for i in range(len(List_of_sectors)):
    avaragelist.append(avarage(List_of_sectors[i]))
plt.bar(X, avaragelist)
plt.tick_params(axis='x', rotation=70)
plt.xlabel('X - Sectors')
plt.ylabel('Y - Avarage return of stocks in the Sector')
plt.title('Avarage return of stocks in each Sector')
plt.legend()
number(X,avaragelist)
plt.show()