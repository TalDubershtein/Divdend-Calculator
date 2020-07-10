"""
This is the data used in this code .
all the data set right now is an example based on article that recommanded this stocks and etf's
"""



amount_of_money4month = 250 #amount of money you invest in each month
OnceMoney = 0 #The money you invest first time
amount_of_money = 0 #DONT CHANGE
amount_of_stocks = 0 #DONT CHANGE
date_of_month_buying = 15 # in what day in the month  you want to buy the stock
amount_of_divdend = 0 #DONT CHANGE
Best_dividend_stock = ["LOW", "JNJ", "SWM", "ANH", "EPR", "OLN", "MTSC", "IBM", "UVV", "T"]
Best_etf_divdend = ["ONEQ", "DNL", "SPHQ"]
Basic_materials = ["BHP","CMP","KRO","MSB","OLN","PKX","SWM","TX"]
Communication_services=["AHC","BBGI","DLX","EVC","IPG","NCMI","PHI","T","TEO"]
Consumer_cyclical=["BBBY","CRWS","GEF","GPS","IGT","IP","RCL","WYND"]
Counsumer_Defensive=["BGS","BTI","CCEP","CHSCP","MO","PM","UVV"]
Energy=["AM","BP","BPT","BTU","CEO","CQP","CRT","CVI","DCP","DKL","DMLP","E","EC","ENB","EPD","GEL","GLNG","GLP","HP","MARPS","MMLP","MMP","MVO","NRT","NS","PAA","PBT","RES","SBR","SGU","SNP","SUN","RGS","TOT","TRP","WES","WMB"]
Financial=[]
Healthcare=["PDCO"]
Indusreials=["BGG","CODI","CYD","EBF","HEES","NAT","PAC","PBI","R","SFL"]
Real_estate=["ABR","ACC","AGNC","AKR","ALX","ANH","CTT","CXW","GOOD","IRM","IVR","KW","LTC","MPW","NHI","NLY","OHI","OLP","PEI","RC","REG","RVI","RWT","STWD","UMH","WPC","WRE"]
Tech=["CAJ","CAMT","DSWL","IBM","ITRN","MNDO","RELL","TAIT","TSM","XRX"]
Utilites=["ELP","OGE","SPH"]
List_of_sectors=[Basic_materials,Communication_services,Consumer_cyclical,Counsumer_Defensive,Energy,Financial,Healthcare,Indusreials,Real_estate,Tech,Utilites]
current_year = 2020
return_profit = 100 # what return profit you want (uses for the Amount_of_Years.py)
amount_of_years = 10 #the amount of years you want the data to check or you can set the years in spacific
First_year = 2019
Second_year = 2020

if current_year<=0 or return_profit <=0 or amount_of_years <=0 or First_year <=0 or Second_year<=0 or First_year> Second_year or date_of_month_buying<=0:
    raise ValueError(" One of the parameters in the data are incorrect ")