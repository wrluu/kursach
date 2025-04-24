
import pandas as pd
import requests


def load_transactions(file_path: str) -> pd.DataFrame:
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception:
        return pd.DataFrame()


def get_currency_rates(currencies):
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    rates = response.json().get("rates", {})
    return [{"currency": cur, "rate": rates.get(cur, 0)} for cur in currencies]


def get_stock_prices(stocks):
    return [{"stock": stock, "price": 100} for stock in stocks]  # Заглушка
