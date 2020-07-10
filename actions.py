import yfinance as yf
from data import *
import matplotlib.pyplot as plt






""""  builder """""


def company(ticker, First_year, Second_year):
    ticker = yf.Ticker(ticker)
    tickerinfo = ticker.info
    investment = tickerinfo['shortName'] #getting the name of the stock
    print('investment:' + investment)
    divdend = dict(ticker.get_dividends())
    history = dict(ticker.history(period="max")) # get the whole history of the stock
    closes = history['Open'] # get all the Opening of the stocks in each day
    divedendlist = []  # the data of the divdends in this years
    closelist = []  # the data of the prices of the stock

    for key, value in closes.items():
        if (
                key.day == date_of_month_buying or key.day == date_of_month_buying + 3) and Second_year >= key.year and key.year >= First_year:  # I took the 2 days after the day of the month buying beacuse they stocks dont work 7 days a week
            temp = [key.year, key.month, key.day, value]
            closelist.append(temp)
    onelist(closelist)  # remove double's
    for key, value in divdend.items():
        if Second_year >= key.year and key.year >= First_year:  # taking all of the data from the years that i set
            temp = [key.year, key.month, key.day, value]
            divedendlist.append(temp)

    amount_of_stocks = OnceMoney // (closelist[0][3])
    Results = buying(closelist, divedendlist)

    return Results


def onelist(list):
    for i in range(len(list) - 1):
        if i > len(list) - 2:
            break
        if list[i][1] == list[i + 1][1]:
            list.remove(list[i + 1])


""" Sum of divdends """


def buying(list1, list2):  # list 1 will be closelist  and list 2 will be divdend
    global amount_of_stocks
    global amount_of_money
    global amount_of_divdend

    j = 0
    index = 0
    while j < len(list2) and j< len(list1) and index< len(list1):
        amount_of_money = amount_of_money + amount_of_money4month
        if list1[index][1] < list2[j][1]:
            amount_of_stocks = amount_of_stocks + amount_of_money4month // list1[index][3]
        else:
            if list1[index][2] < list2[j][2]:
                amount_of_stocks = amount_of_stocks + amount_of_money4month // list1[index][3]
                amount_of_divdend = amount_of_divdend + amount_of_stocks * list2[j][3]

            else:
                amount_of_divdend = amount_of_divdend + amount_of_stocks * list2[j][3]
                amount_of_stocks = amount_of_stocks + amount_of_money4month // list1[index][3]
            j += 1
        index += 1
    while index < len(list1) - 1:
        amount_of_money = amount_of_money + amount_of_money4month
        amount_of_stocks = amount_of_stocks + amount_of_money4month // list1[index][3]
        index += 1


    amount_of_money_afterSell = amount_of_stocks * list1[len(list1) - 1][3]
    total_money_earn = amount_of_money_afterSell + amount_of_divdend
    Total = total_money_earn - amount_of_money
    return_value = 100 * (Total / amount_of_money)
    return [amount_of_stocks, amount_of_divdend, amount_of_money_afterSell, amount_of_money, total_money_earn, Total,
            return_value]
def number(X,Y):
    for x, y in zip(X, Y):
        label = "{:.2f}".format(y)

        plt.annotate(label,  # this is the text
                     (x, y),  # this is the point to label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 10),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

"""
Research

"""
import etfStocks
import Best_Stock_In_A_Sector
import avarage_of_Sectors
import Amount_of__Years
etfStocks
Best_Stock_In_A_Sector
avarage_of_Sectors
Amount_of__Years

"""
-----------
"""
