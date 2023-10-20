import pandas as pd
import datetime
from binance import Client
from dotenv import dotenv_values

config = dotenv_values(".env")
client = Client(config.get("KEY"), config.get("SECRET_KEY"))
def get_data(days: int, ticker: str, ts: str) -> pd.DataFrame:
    end = datetime.datetime.now()

    end = end - datetime.timedelta(days=0)
    start = end - datetime.timedelta(days=days)
    end = end.strftime("%d %b, %Y")
    start = start.strftime("%d %b, %Y")

    ts_list = ["1d", "4h", "1h", "5m"]
    if ts not in ts_list:
        print("Input Error!")

    if ts == "1d":
        klines = client.get_historical_klines(
            ticker, client.KLINE_INTERVAL_1DAY, start
        )

    elif ts == "1h":
        klines = client.get_historical_klines(
            ticker, client.KLINE_INTERVAL_1HOUR, start
        )

    elif ts == "4h":
        klines = client.get_historical_klines(
            ticker, client.KLINE_INTERVAL_4HOUR, start
        )

    elif ts == "5m":
        klines = client.get_historical_klines(
            ticker, client.KLINE_INTERVAL_5MINUTE, start
        )

    data = pd.DataFrame(
        data=[row[1:7] for row in klines],
        columns=["open", "high", "low", "close", "volume", "closetime"],
    ).set_index("closetime")
    data.index = pd.to_datetime(data.index + 1, unit="ms")
    data = data.apply(pd.to_numeric, axis=1)
    data = data.sort_index()
    return data