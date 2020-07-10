"""
This python program return the best sotck in each sector and puts the results in a graph.
"""

from actions import *
from data import *
import matplotlib.pyplot as plt

d=[]
X = ['Basic_materials', 'Communication_services', 'Consumer_cyclical', 'Counsumer_Defensive', 'Energy', 'Financial',
         'Healthcare', 'Indusreials', 'Real_estate', 'Tech', 'Utilites']
def Best_Out_Of_Sectors(Sector):
    BestSector = Sector[0]
    value = company(BestSector,current_year-amount_of_years, current_year)[6]
    for i in range(1,len(Sector)):
        temp=company(Sector[i], current_year - amount_of_years, current_year)[6]
        if temp > value:
            BestSector = Sector[i]
            value=company(BestSector,current_year-amount_of_years, current_year)[6]

    return BestSector
for i in range(len(List_of_sectors)):
    if len(List_of_sectors[i])==0:
        d.append([str(X[i]), '0'])
    else:
        d.append([str(X[i]),( Best_Out_Of_Sectors(List_of_sectors[i]))])

#Graph creation
fig=plt.figure(dpi=80)
ax=fig.add_subplot(1,1,1)
table= ax.table(cellText=d , loc='center')
table.set_fontsize(14)
table.scale(1,4)
ax.axis('off')
plt.show()