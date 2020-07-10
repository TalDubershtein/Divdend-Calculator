"""
This python program shows how many percentage of all the stocks and etf's get over a certain return value.
And shows that percentage during 10 years and present it in a graph.
(uses the Best_etf_dividend and Best_dividend_stock as well as return_profit
 (the parameter that  we want our stocks return profit be above))
"""

from actions import *
from data import *
import matplotlib.pyplot as plt

Best = Best_dividend_stock + Best_etf_divdend
data = []
for i in range(0, amount_of_years):

    notgood = []
    good = []
    for j in range(0, len(Best)):
        if company(Best[j], current_year - i, current_year)[6] >= return_profit:
            good.append(Best[j])
    data.append(100 * (len(good) / len(Best)))

#Graph creation
plt.bar(range(0, amount_of_years), data)
plt.xlabel('X- Number of years')
plt.ylabel('Y- The number of stocks above the return value')
plt.title('The number of stocks that are above the return value during 10 years')
number(range(0,amount_of_years),data)
plt.show()