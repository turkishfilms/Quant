# %%
import pandas as pd
import numpy as np
import json
import requests
from api_keys import stockorg_key 

# %%
base_url = r"https://api.stockdata.org/v1/data/eod?"
symbols = ["AAPL"]
url = base_url + f"symbols={symbols[0]}&api_token={stockorg_key}&date_from=2000"

# %%
req = requests.get(url)


# %%
res = json.loads(req.content)

# %%
stock_data = pd.DataFrame(res["data"])

# %%
stock_data.plot(kind="scatter", x="date", y="close")

# %%
indicators = ["MACD","RSI","VWAP","12EMA","26EMA","50EMA","200EMA","12SMA","26SMA","50SMA","200SMA"]

# %%
# stock_data["MACD"] = ""
more_stock_data = pd.concat([stock_data,pd.DataFrame(columns=list(indicators))])
more_stock_data["date"] = more_stock_data["date"].str[:10] 
more_stock_data.head()


# %%
# end = date
def ema(df,period, end,mult):
    closingprice = df[] end[closing]#here
    multiplier =  mult/(1+period) 
    return closing * multiplier + ema(df,period,end-1,mult) * (1-multiplier)

more_stock_data["12EMA"] = 


