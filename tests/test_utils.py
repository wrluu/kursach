import pytest
import pandas as pd
from src.utils import load_transactions, get_currency_rates, get_stock_prices

def test_load_transactions():
    df = load_transactions("data/operations.xlsx")
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

def test_get_currency_rates(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"rates": {"USD": 1.0, "EUR": 1.1}}
    mocker.patch("requests.get", return_value=mock_response)

    rates = get_currency_rates(["USD", "EUR"])
    assert rates == [{"currency": "USD", "rate": 1.0}, {"currency": "EUR", "rate": 1.1}]

def test_get_stock_prices(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"price": 100}
    mocker.patch("requests.get", return_value=mock_response)

    stocks = get_stock_prices(["AAPL"])
    assert stocks == [{"stock": "AAPL", "price": 100}]
