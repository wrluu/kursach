import pytest
import pandas as pd
from src.views import homepage, events

@pytest.fixture
def sample_transactions():
    data = {
        "Дата операции": ["2023-10-01", "2023-10-02"],
        "Сумма платежа": [100, 200],
        "Категория": ["Супермаркеты", "Кафе"],
        "Описание": ["Описание 1", "Описание 2"],
        "Номер карты": ["1234", "5678"],
    }
    return pd.DataFrame(data)

def test_homepage(sample_transactions):
    result = homepage("2023-10-01 12:00:00", sample_transactions)
    assert "greeting" in result
    assert "cards" in result
    assert "top_transactions" in result
    assert "currency_rates" in result
    assert "stock_prices" in result

def test_events(sample_transactions):
    result = events("2023-10-01", sample_transactions)
    assert "expenses" in result
    assert "income" in result
    assert "currency_rates" in result
    assert "stock_prices" in result
