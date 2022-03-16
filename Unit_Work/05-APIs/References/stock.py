from alpaca_trade_api.rest import REST,TimeFrame
import pandas as pd
alpaca = REST()

def get_stock(
    stocks,
    freq= TimeFrame.Day,
    start= "30 days",
    end= "1 day",
        ):
    # print(start, end)

    # handle if stock a string or a list of stocks
    if (type(stocks) == str):
        stocks = [stocks]
    # handle freq entries

    try:
        # handle start being a string
        if (type(start) == str):
            start = (pd.Timestamp.today(tz="UTC") - pd.Timedelta(start)).isoformat()
        # handle end being a string
        if (type(end) == str):
            end = (pd.Timestamp.today(tz="UTC") - pd.Timedelta(end)).isoformat()
    except:
        print("timestamps didn't work, using defaults of 30 days and 1 day")
        start = (pd.Timestamp.today(tz="UTC") - pd.Timedelta("30 days")).isoformat()
        end = (pd.Timestamp.today(tz="UTC") - pd.Timedelta("1 day")).isoformat()

    result = {}
    for stock in stocks:
        result[stock] = alpaca.get_bars(stock, freq ,start=start, end=end).df

    return pd.concat(result,axis="columns")

